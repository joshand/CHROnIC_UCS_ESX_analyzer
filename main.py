__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

from tinydb import TinyDB, Query
from HCL import getServerType_PID, getServerType, getServerModel, getProcessor, getOSVendor, getOSVersion, getFirmware
from HCL import hclSearch, lookupByPID
import pprint
from flask_api import FlaskAPI
from flask import request
import requests
import json
import ast

app = FlaskAPI(__name__)


piddb = TinyDB('piddb.json')
item = Query()




def server_merge(ucs_list, esx_list):
    servers = []
    count = 0
    for esx in esx_list:
        esx_ident_list = esx['otherIdentifyingInfo/identifierValue/~']
        for id in esx_ident_list:
            for ucs in ucs_list:
                ucs_serial = ucs['@serial'][0]
                if id == ucs_serial:
                    print("Building merged server object.  Matched on esx", id, "ucs", ucs_serial)
                    server = {}
                    server['ucs'] = ucs
                    server['id'] = count
                    server['esx'] = esx
                    count = count + 1
                    servers.append(server)
    pprint.pprint(servers)
    return servers




def buildHCL_os_version(fullName):
    formatedName = ""
    for i in fullName.split():
        if i == "ESXi":
            formatedName = formatedName + "vSphere "
        elif i.split(".")[-1] == "0":
            formatedName = formatedName + i.split(".")[0] + "." + i.split(".")[1]
        #TODO build a check for U1 U2 type verisons

    return formatedName

def buildHCL_processor_name(processorFull):
    #example     "PROCESSOR": "Intel Xeon E5-2600 Series processors"
    print(processorFull)
    if "E5-26" in processorFull:
        if "v2" in processorFull:
            print(processorFull, "is a Intel Xeon E5-2600 v2 Series processors")
            return "Intel Xeon E5-2600 v2 Series processors"
        else:
            print(processorFull, "is a Intel Xeon E5-2600 Series processors")
            return "Intel Xeon E5-2600 Series processors"
    else:
        print("unsupported processor")
        return "UNSUPPORTED"


def buildHCL_firmware_name(firmware):
    print("Formating firmware name from, " + firmware + " to " + firmware[:5] + ")")
    return (firmware[:5] + ")")

def buildHCL_enic_number(enic):
    print("Reformatting " + enic + "to " + enic.split()[-1])
    return enic.split()[-1]

def buildHCL_fnic_number(fnic):
    fnic_long = (fnic.split()[2])
    fnic_version = fnic_long.split("-")[0]
    print("Formating FNIC " + fnic + " to " + fnic_version)
    return fnic_version




#for server in servers:
#    osvendor_name = (server['fullName/~'][0].split()[0])
#    print(buildHCL_os_version(server['fullName/~'][0]))


def hclCheck(servers):

    for server in servers:
        #TODO write a check to make sure server PID in DB

        base_server_type = getServerType_PID(server['ucs']['@model'][0])
        #print(base_server_type)
        serverType = getServerType(base_server_type['server_type'])
        #print(serverType)
        serverModel = getServerModel(serverType['T_ID'], base_server_type['ID'])
        #print(serverModel)

        processor_hcl_name = buildHCL_processor_name(server['ucs']['computeBoard/processorUnit/@model'][0])
        processor = getProcessor(serverModel['T_ID'], processor_hcl_name)
        #print(processor)

        osvendor_name = (server['esx']['fullName/~'][0].split()[0])
        #TODO if not VMware execption

        osVendor = getOSVendor(processor['T_ID'], osvendor_name)
        #print(osVendor)

        osversion_name = buildHCL_os_version(server['esx']['fullName/~'][0])
        osVersion = getOSVersion(osVendor['T_ID'], osversion_name)
        #print(osVersion)
        firmware_hcl_name = buildHCL_firmware_name(server['ucs']['mgmtController/firmwareRunning/@version'][0])
        firmwareVersion = getFirmware(osVersion['T_ID'], firmware_hcl_name)
        #print(firmwareVersion)
        manageType = 'UCSM'
        adapterinfo = lookupByPID(server['ucs']['adaptorUnit/@model'][0])

        if firmwareVersion != "UNSUPPORTED":
            results = hclSearch(serverType['ID'], serverModel['ID'], processor['ID'], osVendor['ID'], osVersion['ID'],
                                firmwareVersion['ID'], manageType)
            #print(results[0]['HardwareTypes']['Adapters']['CNA'])
            CNAs = results[0]['HardwareTypes']['Adapters']['CNA']
            CNA_Table = {}
            for CNA in CNAs:
                if CNA['Model'] == adapterinfo['adapter']:
                    print("Found adapter " + adapterinfo['adapter'])
                    if CNA['Model'] not in CNA_Table:
                        CNA_Table[CNA['Model']] = {}

                    if "Ethernet" in CNA['DriverVersion']:
                        ENIC = CNA['DriverVersion'].split(" ")[0]
                        CNA_Table[CNA['Model']].update({'ENIC':ENIC})

                    if "Fibre Channel" in CNA['DriverVersion']:
                        FNIC = CNA['DriverVersion'].split(" ")[0]
                        CNA_Table[CNA['Model']].update({'FNIC':FNIC})
            print(CNA_Table)
            #print(CNA_Table)
            server['supported_enic'] = CNA_Table[adapterinfo['adapter']]['ENIC']
            server['supported_fnic'] = CNA_Table[adapterinfo['adapter']]['FNIC']
            server['firmware_status'] = "SUPPORTED"
        else:
            server['supported_enic'] = "UNSUPPORTED FIRMWARE"
            server['supported_fnic'] = "UNSUPPORTED FIRMWARE"
            server['firmware_status'] = "UNSUPPORTED"

        print(server['supported_enic'])
        print(server['supported_fnic'])


        enic = buildHCL_enic_number(server['esx']['driverinfo'][3])
        fnic = buildHCL_fnic_number(server['esx']['driverinfo'][1])
        if enic == server['supported_enic']:
            server['enic_status'] = "Supported"
        else:
            server['enic_status'] = "Unupported"

        if fnic == server['supported_enic']:
            server['fnic_status'] = "Supported"
        else:
            server['fnic_status'] = "Unsupported"

        #print("Updated Server to " + server)
    return servers

def collectServerInfo(channelid):
    ##TODO
    url = "http://imapex-chronic-bus.green.browndogtech.com/api/get/{}/2".format(channelid)

    headers = {
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, headers=headers).json()


    for item in response:
        msgresp = item['msgresp']
        msgresp = ast.literal_eval(msgresp)
        if 'ucs' in msgresp.keys():
            ucs_servers = msgresp['ucs']
        elif 'vcenter' in msgresp.keys():
            esx_servers = msgresp['vcenter']

    return({'ucs_servers':ucs_servers, 'esx_servers':esx_servers})


def writeToBus(checked_servers, channelid):
    newchannelid_base = channelid + "-report"
    url = "http://imapex-chronic-bus.green.browndogtech.com/api/get"
    response = requests.request("GET", url).json()

    count = 0
    for channel in response.keys():
        if channelid in channel:
            count = count + 1



    url = "http://imapex-chronic-bus.green.browndogtech.com/api/send/{0}-{1}".format(newchannelid_base, str(count))

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    payload = {
        "msgdata": checked_servers,
        "desc": "finished HCL report",
        "status": "2"}

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response)
    return

@app.route("/")
def hc():
    return("Healthy")

@app.route("/api/", methods=['POST'])
def main():
    channelid = request.data['channelid']
    formatted_servers = collectServerInfo(channelid)
    servers = server_merge(formatted_servers['ucs_servers'], formatted_servers['esx_servers'])
    checked_servers = hclCheck(servers)
    pprint.pprint(checked_servers)
    writeToBus(checked_servers, channelid)


    return (checked_servers)


#main('h86eK4Ds')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


