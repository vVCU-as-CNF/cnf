import requests

BASE_URL = "https://10.255.28.79:9999/osm/"

VNF_NAME = "vvcu-as-cnf"
VIM_ACCOUNT_NAME = "5gasp-k8s-1"
# example
# https://10.255.28.79:9999/osm/vnfpkgm/v1/vnf_packages/1c7c0ecd-13f9-4b6d-b831-1b6381dec701

session = requests.Session()
session.verify = False

#
# MAIN
#

def main():
    getToken()
    
    # allTokens()
    # packages = listVNFPackages()
    # getVNFPackageInfo(packages[VNF_NAME])
    # accounts = listVIMAccounts()
    # getVIMAccountInfo(accounts[VIM_ACCOUNT_NAME])




    deleteToken()

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
    
    token = r.text.split("\n")[1].split(": ")[1]

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

    lines = r.text.split("\n")
    print(r.text)
    tokens = [l.replace("-   _id: ", "") for l in lines if l.startswith("-   _id: ")]

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

    lines = r.text.split("\n")
    vim_accounts = [l.replace("    name: ", "") for l in lines if l.startswith("    name: ")]
    vim_accounts_ids = [l.replace("    _id: ", "") for l in lines if l.startswith("    _id: ")]

    print("--------------------")
    print("All VIM Accounts: ")
    for i in range(len(vim_accounts)):
        print("  " + vim_accounts[i])
        print("  id - " + vim_accounts_ids[i])
    print("--------------------")

    return {k: v for k, v in zip(vim_accounts, vim_accounts_ids)}

def getVIMAccountInfo(account_id):
    """Gets VIM account info from OSM"""
    url = BASE_URL + "admin/v1/vim_accounts/" + account_id
    r = session.get(url)

    print(r.text)

#
# NS PACKAGES
#

def listNSPackages():
    """Lists all NS packages from OSM"""
    url = BASE_URL + "nsd/v1/ns_descriptors"
    r = session.get(url)

    lines = r.text.split("\n")

    ns_packages = [l.replace("    name: ", "") for l in lines if l.startswith("    name: ")]
    ns_packages_ids = [l.replace("    _id: ", "") for l in lines if l.startswith("    _id: ")]

    print("--------------------")   
    print("All NS packages: ")
    for i in range(len(ns_packages)):
        print("  " + ns_packages[i])
        print("  id - " + ns_packages_ids[i])
    print("--------------------")

    return {k: v for k, v in zip(ns_packages, ns_packages_ids)}

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

def getVNFPackageInfo(token):
    """Gets VNF package info from OSM"""
    url = BASE_URL + "vnfpkgm/v1/vnf_packages/" + token
    r = session.get(url)

    print(r.text)

#
# NS INSTANCES
#

def createNSInstance():
    """Creates NS instance on OSM"""
    url = BASE_URL + "nslcm/v1/ns_instances"
    payload = {
        

if __name__ == "__main__":
    main()