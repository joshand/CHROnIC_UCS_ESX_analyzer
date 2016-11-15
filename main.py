__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

from tinydb import TinyDB, Query
from HCL import getServerType_PID, getServerType, getServerModel, getProcessor, getOSVendor, getOSVersion, getFirmware
from HCL import hclSearch, lookupByPID

piddb = TinyDB('piddb.json')
item = Query()

#build way to pass in server objects
servers = [{'server_pid':'UCSB-B200-M3', 'processor_pid':'UCS-CPU-E5-2680',
               'osvendor': 'VMware', "osversion": "vSphere 5.5", 'firmware':"3.1(2)", 'adapter_pid':'UCSB-MLOM-40G-01',
               'manageType': "UCSM", 'fnic': '1.5.0.4-1', 'enic':'1.4.2.15c'
               }]

for server in servers:
    base_server_type = getServerType_PID(server['server_pid'])
    #print(base_server_type)
    serverType = getServerType(base_server_type['server_type'])
    #print(serverType)
    serverModel = getServerModel(serverType['T_ID'], base_server_type['ID'])
    #print(serverModel)
    processor = getProcessor(serverModel['T_ID'], server['processor_pid'])
    #print(processor)
    osVendor = getOSVendor(processor['T_ID'], server['osvendor'])
    #print(osVendor)
    osVersion = getOSVersion(osVendor['T_ID'], server['osversion'])
    #print(osVersion)
    firmwareVersion = getFirmware(osVersion['T_ID'], server['firmware'])
    #print(firmwareVersion)
    manageType = server['manageType']
    adapterinfo = lookupByPID(server['adapter_pid'])['adapter']


    if firmwareVersion != "UNSUPPORTED":
        results = hclSearch(serverType['ID'], serverModel['ID'], processor['ID'], osVendor['ID'], osVersion['ID'],
                            firmwareVersion['ID'], manageType)

        #print(results[0]['HardwareTypes']['Adapters']['CNA'])
        CNAs = results[0]['HardwareTypes']['Adapters']['CNA']
        CNA_Table = {}
        for CNA in CNAs:
            if CNA['Model'] == adapterinfo:
                if CNA['Model'] not in CNA_Table:
                    CNA_Table[CNA['Model']] = {}

                if "Ethernet" in CNA['DriverVersion']:
                    ENIC = CNA['DriverVersion'].split(" ")[0]
                    CNA_Table[CNA['Model']].update({'ENIC':ENIC})

                if "Fibre Channel" in CNA['DriverVersion']:
                    FNIC = CNA['DriverVersion'].split(" ")[0]
                    CNA_Table[CNA['Model']].update({'FNIC':FNIC})

        server['supported_enic'] = CNA_Table[adapterinfo]['ENIC']
        server['supported_fnic'] = CNA_Table[adapterinfo]['FNIC']
        server['firmware_status'] = "SUPPORTED"
    else:
        server['supported_enic'] = "UNSUPPORTED FIRMWARE"
        server['supported_fnic'] = "UNSUPPORTED FIRMWARE"
        server['firmware_status'] = "UNSUPPORTED"



    if server['enic'] == server['supported_enic']:
        server['enic_status'] = "Supported"
    else:
        server['enic_status'] = "Unupported"

    if server['fnic'] == server['supported_enic']:
        server['fnic_status'] = "Supported"
    else:
        server['fnic_status'] = "Unsupported"

    print(server)