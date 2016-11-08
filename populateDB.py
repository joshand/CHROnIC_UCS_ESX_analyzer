import requests
from tinydb import TinyDB, where, Query
from colorama import init, Fore, Back, Style

db = TinyDB('testdb.json')
item = Query()
init(autoreset=True)

def checkThenInsert(i):
    if (db.search(item.T_ID == i['T_ID'])):
        print("T_ID {} already in DB".format(i['T_ID']))
    else:
        db.insert(i)
        print(Fore.YELLOW + "Inserted T_ID {} into DB".format(i['T_ID']))
    return

def getAdapterType():
    url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadAdapterTypes"
    response = requests.request("POST", url).json()
    return response

def buildAdapterType():
    adapters = getAdapterType()
    for i in adapters:
        i['otype'] = 'adaptertype'
        checkThenInsert(i)
    return


def buildAdapterModel(treeIdAdapterType):
    url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadAdapterModels"
    payload = "treeIdAdapterType={}".format(treeIdAdapterType)
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers).json()
    for i in response:
        i['otype'] = 'adapter'
        i['pid'] = 'unknown'
        checkThenInsert(i)
    return

def buildAdapterModelTable():
    adapter_types = db.search(item.otype == 'adaptertype')
    for adapter in adapter_types:
        buildAdapterModel(adapter['T_ID'])
        #print(adapter['T_ID'])


def getOSVender():
    url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadOsVendors"

    payload = "treeIdProcessor=6012"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers).json()
    return response

def buildOSVenderTable():
    OSVenders = getOSVender()
    for i in OSVenders:
        i['otype'] = 'osvender'
        checkThenInsert(i)
    return


def buildOSVersion(treeIdVendor):
    url = "http://ucshcltool.cloudapps.cisco.com/public/rest/controller/loadOsVersions"

    payload = "treeIdVendor={}".format(treeIdVendor)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers).json()
    for i in response:
        i['otype'] = 'osversion'
        checkThenInsert(i)
    return

def buildOSVersionTable():
    OSVenders = db.search(item.otype == 'osvender')
    for os in OSVenders:
        buildOSVersion(os['T_ID'])
    return

buildAdapterType()
buildAdapterModelTable()
buildOSVenderTable()
buildOSVersionTable()