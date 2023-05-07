from nbi_interactions import *
from time import sleep

#
# STATIC VARIABLES
#

VIM_ACCOUNT_NAME_1 = "5gasp-k8s-1"
VIM_ACCOUNT_NAME_2 = "5gasp-k8s-2"

VNF_PACKAGE_NAME = "vvcu-as-cnf"
NS_PACKAGE_NAME = "vvcu-as-cnf_ns"

# creating a new NS instance
INSTANCE_NAME = "nbi-test"
NSD_NAME = "vvcu-as-cnf_ns" # TODO CHANGE THIS WHEN WIFI AND REMOVE LINE BELOW
NSD_ID = "8ead4781-8830-4be6-a5e1-68ade6c21edb" # vvcu-as-cnf
#VIM_ACCOUNT_ID_1 = "a5571fea-254f-402a-8eec-ed4dc3424911" # 5gasp-k8s-1
#VIM_ACCOUNT_ID_2 = "83216c56-70be-4955-9120-386aad3862b6" # 5gasp-k8s-2

#
# MAIN
#
def main():
    getToken()
    
    vim_accounts = listVIMAccounts()
    ns_packages = listNSPackages()
    instance_id = createNSInstance(vim_accounts[VIM_ACCOUNT_NAME_1], ns_packages[NSD_NAME], INSTANCE_NAME)
    instantiateNSInstance(instance_id, vim_accounts[VIM_ACCOUNT_NAME_1], INSTANCE_NAME)
    listNSInstances()

    # terminateNSInstance(instance_id)
    # deleteNSInstance(instance_id)

    deleteToken()
    

if __name__ == "__main__":
    main()