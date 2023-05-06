import yaml
import requests

#
# STATIC VARIABLES
#

BASE_URL = "https://10.255.28.79:9999/osm/"

# creating a new NS instance
NAME = "nbi-test"
NSD_ID = "8ead4781-8830-4be6-a5e1-68ade6c21edb" # vvcu-as-cnf
VIM_ACCOUNT_ID = "a5571fea-254f-402a-8eec-ed4dc3424911" # 5gasp-k8s-1
#VIM_ACCOUNT_ID = "83216c56-70be-4955-9120-386aad3862b6" # 5gasp-k8s-2

session = requests.Session()
session.verify = False

#
# TOKENS
#

def getToken():
    """Get token from OSM"""
    url = BASE_URL + "admin/v1/tokens"
    payload = {
        "username": "admin",
        "password": "admin"
    }
    r = session.post(url, data=payload)

    token = yaml.safe_load(r.text)["id"]
    
    print("--------------------")
    print("Got token: " + token)
    print("--------------------")

    return token

def deleteToken():
    """Deletes token from OSM"""
    url = BASE_URL + "admin/v1/tokens"
    r = session.delete(url)

    token = r.text.split(" ")[2].replace("\'", "")

    print("--------------------")
    print("Deleted token: " + token)
    print("--------------------")

def allTokens():
    """Lists all tokens from OSM"""
    url = BASE_URL + "admin/v1/tokens"
    r = session.get(url)

    tokens = yaml.safe_load(r.text)
    tokens = [t["id"] for t in tokens]

    print("--------------------")
    print("All active tokens: ")
    for t in tokens:
        print("- " + t)
    print("--------------------")

    return tokens

#
# VIM ACCOUNTS
#

def listVIMAccounts():
    """Lists all VIM accounts from OSM"""
    url = BASE_URL + "admin/v1/vim_accounts"
    r = session.get(url)

    vim_accounts = yaml.safe_load(r.text)
    vim_accounts = {a["name"]: a["_id"] for a in vim_accounts}

    print("--------------------")
    print("All VIM Accounts: ")
    for k in vim_accounts:
        print("  " + k)
        print("  id - " + vim_accounts[k])
    print("--------------------")

    return vim_accounts

def getVIMAccountInfo(account_id):
    """Gets VIM account info from OSM"""
    url = BASE_URL + "admin/v1/vim_accounts/" + account_id
    r = session.get(url)

    print(r.text)

#
# VNF PACKAGES
#

def listVNFPackages():
    """Lists all VNF packages on OSM"""
    url = BASE_URL + "vnfpkgm/v1/vnf_packages"
    r = session.get(url)

    lines = r.text.split("\n")

    vnf_packages = [l.replace("        name: ", "") for l in lines if l.startswith("        name: ")]
    vnf_packages_ids = [l.replace("    _id: ", "") for l in lines if l.startswith("    _id: ")]

    print("--------------------")   
    print("All VNF packages: ")
    for i in range(len(vnf_packages)):
        print("  " + vnf_packages[i])
        print("  id - " + vnf_packages_ids[i])
    print("--------------------")

    return {k: v for k, v in zip(vnf_packages, vnf_packages_ids)}

def getVNFPackageInfo(id):
    """Gets VNF package info from OSM"""
    url = BASE_URL + "vnfpkgm/v1/vnf_packages/" + id
    r = session.get(url)

    print(r.text)

#
# NS PACKAGES
#

def listNSPackages():
    """Lists all NS packages from OSM"""
    url = BASE_URL + "nsd/v1/ns_descriptors"
    r = session.get(url)

    ns_packages = yaml.safe_load(r.text)
    ns_packages = {a["name"]: a["_id"] for a in ns_packages}

    print("--------------------")   
    print("All NS packages: ")
    for k in ns_packages:
        print("  " + k)
        print("  id - " + ns_packages[k])
    print("--------------------")

    return ns_packages

def getNSPackageInfo(id):
    """Gets NS package info from OSM"""
    url = BASE_URL + "nsd/v1/ns_descriptors/" + id
    r = session.get(url)

    print(r.text)


#
# NS INSTANCES
#

def listNSInstances():
    """Lists all NS instances on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances"
    r = session.get(url)

    ns_instances = yaml.safe_load(r.text)
    ns_instances = {a["name"]: {"id": a["_id"], "state": a["nsState"]} for a in ns_instances}

    print("--------------------")
    print("All NS instances: ")
    for k in ns_instances:
        print("  " + k)
        print("  id    - " + ns_instances[k]["id"])
        print("  state - " + ns_instances[k]["state"])
    print("--------------------")

    return ns_instances

def getNSInstanceInfo(id):
    """Gets NS instance info from OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances/" + id
    r = session.get(url)

    print(r.text)

def createNSInstance():
    """Creates NS instance on OSM (does not instantiate it)"""
    url = BASE_URL + "nslcm/v1/ns_instances"
    payload = {
        "vimAccountId": VIM_ACCOUNT_ID,
        "nsdId": NSD_ID, 
        "nsName": NAME,
    }

    r = session.post(url, data=payload)

    instance = yaml.safe_load(r.text)
    instance_id = instance["id"]

    print("--------------------")
    print("Created NS instance: ")
    print("  name - " + NAME)
    print("  id - " + instance_id)
    print("--------------------")

    return instance_id

def instantiateNSInstance(id):
    """Instantiates a given NS instance on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances/" + id + "/instantiate"
    payload = {
        "vimAccountId": VIM_ACCOUNT_ID,
        "nsName": NAME,
        "nsdId": id,
    }

    r = session.post(url, data=payload)

    instance = yaml.safe_load(r.text)
    instance_id = instance["id"]

    print("--------------------")
    print("Instantiated NS instance: ")
    print("  name - " + NAME)
    print("  id - " + instance_id)
    print("--------------------")

def buildNSInstance():
    """Creates and instantiates NS instance on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances_content"
    payload = {
        "nsName": NAME,
        "nsdId": NSD_ID, 
        "vimAccountId": VIM_ACCOUNT_ID,
    }

    r = session.post(url, data=payload)
    print(r.text)
    instance = yaml.safe_load(r.text)
    instance_id = instance["id"]

    print("--------------------")
    print("Created and instantiated NS instance: ")
    print("  name - " + NAME)
    print("  id - " + instance_id)
    print("--------------------")

    return instance_id    

def terminateNSInstance(id):
    """Terminates a given NS instance on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances/" + id + "/terminate"

    r = session.post(url)

    print("--------------------")
    print("Terminated NS instance: ")
    print("  name - " + NAME)
    print("  id - " + id)
    print("--------------------")

def deleteNSInstance(id):
    """Deletes a given NS instance on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances/" + id
    r = session.delete(url)

    print(r.text)

    print("--------------------")
    print("Deleted NS instance: ")
    print("  id - " + id)
    print("--------------------")

