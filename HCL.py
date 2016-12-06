import requests
from tinydb import TinyDB, Query
from colorama import init, Fore, Back
import os

db = TinyDB('testdb.json')
piddb = TinyDB('piddb.json')
item = Query()
init(autoreset=True)

hclbaseurl = os.environ['HCL']

def checkThenInsert(i):
    """
    This method checks to see if record that matches the item is already stored in the DB.  If it isn't it is added
    """
    if db.search((item.T_ID == i['T_ID']) & (item.ID == i['ID'])):
        print("{} already in DB".format(i))
    else:
        db.insert(i)
        print(Fore.GREEN + "Inserted {} into DB".format(i))
    return

def getAdapterType():
    '''
    This method is a base build method to populate all possible adapters.  This method returns the base adapter
    type to be fed into the buildAdapterType function.
    '''
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadAdapterTypes"
    url = hclbaseurl + "/controller/loadAdapterTypes"

    response = requests.request("POST", url).json()
    return response

def buildAdapterType():
    '''
    This function is likely unneeded.  This method adds the 'otype' field to the adapter items and stores them
    '''
    adapters = getAdapterType()
    for i in adapters:
        i['otype'] = 'adaptertype'
        checkThenInsert(i)
    return


def buildAdapterModel(treeIdAdapterType):
    '''
    This function queries the HCL for a given adapter type.  The return is a list of all adapter models.
    These are then stored in the db
    '''
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadAdapterModels"
    url = hclbaseurl + "/controller/loadAdapterModels"

    payload = "treeIdAdapterType={}".format(treeIdAdapterType)
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers).json()
    for i in response:
        i['otype'] = 'adapter'
        i['pid'] = 'unknown'
        checkThenInsert(i)
    return

def buildAdapterModelTable():
    '''
    This function is the base of what gathers and builds all the adapter info and stores it in the db
    '''
    adapter_types = db.search(item.otype == 'adaptertype')
    for adapter in adapter_types:
        buildAdapterModel(adapter['T_ID'])
        #print(adapter['T_ID'])


def buildOSVenderTable():
    '''
    This funciton returns back all OS vendor objects
    '''
    processors = db.search(item.otype == 'processor')
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadOsVendors"
    url = hclbaseurl + "/server/loadOsVendors"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }
    for processor in processors:
        payload = "treeIdProcessor={}".format(processor['T_ID'])
        oss = requests.request("POST", url, data=payload, headers=headers).json()
        for os in oss:
            os['otype'] = 'os'
            checkThenInsert(os)
    return

def getOSVendor(T_ID, reported_os_vendor):
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadOsVendors"
    url = hclbaseurl + "/server/loadOsVendors"

    payload = "treeIdProcessor={}".format(T_ID)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "25af9eaa-2d3d-0dda-92cc-632db98ec3b1"
    }

    vendors = requests.request("POST", url, data=payload, headers=headers).json()

    for vendor in vendors:
        if vendor['OSVENDOR'] == reported_os_vendor:
            return vendor
    ##TODO return error code
    return


def buildOSVersions(treeIdVendor):
    '''
    This funciton gets all OS Versions given an OS Vendor T_ID and stores them in the DB
    '''
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadOsVersions"
    url = hclbaseurl + "/controller/loadOsVersions"

    payload = "treeIdVendor={}".format(treeIdVendor)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers).json()
    for i in response:
        i['otype'] = 'osversion'
        checkThenInsert(i)
    return

def getOSVersion(T_ID, reported_version):
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadOsVersions"
    url = hclbaseurl + "/server/loadOsVersions"

    payload = "treeIdVendor={}".format(T_ID)
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }

    versions = requests.request("POST", url, data=payload, headers=headers).json()
    for version in versions:
        if version['OSVERSION'] == reported_version:
            return version

    ##TODO return error code
    return

def buildOSVersionTable():
    '''
    This funciton triggers the full build process for getting and storing all OS versions
    '''
    OSVenders = db.search(item.otype == 'osvender')
    for os in OSVenders:
        buildOSVersions(os['T_ID'])
    return

def getServerTypes():
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadServerTypes"
    url = hclbaseurl + "/server/loadServerTypes"

    response = requests.request("POST", url).json()
    return response

def getServerType(server_type):
    types = getServerTypes()
    for type in types:
        if type["TYPE"] == server_type:
            return type
    return

def buildServerTypesTable():
    server_types = getServerTypes()
    for i in server_types:
        i['otype'] = 'servertype'
        checkThenInsert(i)
    return

def getServerModels(treeIdRelease):
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadServerModels"
    url = hclbaseurl + "/server/loadServerModels"

    payload = "treeIdRelease={}".format(treeIdRelease)
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers).json()

    return response


def getServerModel(t_id, id):
    models = getServerModels(t_id)
    for model in models:
        if model['ID'] == id:
            return model
    return


def buildServerModel(treeIdRelease):
    server_models = getServerModels(treeIdRelease)
    for i in server_models:
        i['otype'] = 'servermodel'
        i['pid'] = 'unknown'
        checkThenInsert(i)
    return

def buildServerModelTable():
    server_models = db.search(item.otype == 'servertype')
    for server in server_models:
        buildServerModel(server['T_ID'])
    return

def buildProcessorsTable():
    server_models = db.search(item.otype == 'servermodel')
    #url = 'http://ucshcltool-dev.cloudapps.cisco.com/public/rest/server/loadProcessors'
    url = hclbaseurl + "/server/loadProcessors"

    headers = {'content-type': "application/x-www-form-urlencoded",}

    for server in server_models:
        payload = "treeIdServerModel={}".format(server['T_ID'])
        processors = requests.request("POST", url, data=payload, headers=headers).json()
        for processor in processors:
            processor['otype'] = 'processor'
            processor['pid'] = 'unknown'
            checkThenInsert(processor)
    return

def getProcessor(T_ID, PROCESSOR):
    #url = 'http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadProcessors'
    url = hclbaseurl + "/server/loadProcessors"

    headers = {'content-type': "application/x-www-form-urlencoded",}
    payload = "treeIdServerModel={}".format(T_ID)
    processors = requests.request("POST", url, data=payload, headers=headers).json()

    for processor in processors:
        if processor['PROCESSOR'] == PROCESSOR:
            return processor
    return

def getFirmware(T_ID, reported_firmware):
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadFirmwareVersions"
    url = hclbaseurl + "/server/loadFirmwareVersions"

    payload = "treeIdOSVersion={}".format(T_ID)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "dc4e4f4c-f156-78d8-a8e5-a8d872d627db"
    }

    firmwares = requests.request("POST", url, data=payload, headers=headers).json()
    for firmware in firmwares:
        if firmware['VERSION'] == reported_firmware:
            return firmware

    ##TODO return error code - running unsupported firmware
    return "UNSUPPORTED"


def getServerType_PID(pid):
    info = piddb.search(item.pid == pid)[0]
    return info


def hclSearch(serverType_ID, serverModel_ID, processor_ID, osVendor_ID, osVersion_ID,
                 firmwareVersion_ID, manageType):
    #url = "http://ucshcltool.cloudapps.cisco.com/public/rest/server/loadSearchResults"
    url = hclbaseurl + "/server/loadSearchResults"

    payload = "serverType_ID={0}&serverModel_ID={1}%2C31&processor_ID={2}&osVendor_ID={3}&osVersion_ID={4}&" \
              "firmwareVersion_ID={5}&manageType={6}".format(
        serverType_ID, serverModel_ID, processor_ID, osVendor_ID, osVersion_ID, firmwareVersion_ID, manageType
    )
    headers = {
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers).json()

    return response

def lookupByPID(adapter_pid):
    info = piddb.search(item.pid == adapter_pid)[0]
    return info

#DB Build Process
#buildServerTypesTable()
#buildServerModelTable()
#buildProcessorsTable()
#buildOSVenderTable()
