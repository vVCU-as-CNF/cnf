from nbi_interactions import *
from time import sleep

#
# STATIC VARIABLES
#

# testing getters
VIM_ACCOUNT_NAME = "5gasp-k8s-1"
VNF_NAME = "vvcu-as-cnf"
NS_NAME = "vvcu-as-cnf_ns"
NS_INSTANCE = "vvcu-as-acnf"

#
# MAIN
#
def main():
    getToken()
    
    # allTokens()

    vim_accounts = listVIMAccounts()
    # getVIMAccountInfo(vim_accounts[VIM_ACCOUNT_NAME])

    # vnf_packages = listVNFPackages()
    # getVNFPackageInfo(vnf_packages[VNF_NAME])

    # ns_packages = listNSPackages()
    # getNSPackageInfo(ns_packages[NS_NAME])

    ns_instances = listNSInstances()
    # getNSInstanceInfo(ns_instances[NS_INSTANCE]["id"])
    instance_id = createNSInstance()
    # instance_id = buildNSInstance()
    instantiateNSInstance(instance_id)
    # terminateNSInstance(instance_id)
    # deleteNSInstance(instance_id)

    deleteToken()

if __name__ == "__main__":
    main()