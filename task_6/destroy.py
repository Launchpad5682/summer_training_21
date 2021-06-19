import os

def destroyInfra():
    os.chdir("terraformScript")
    os.system("terraform destroy -auto-approve")