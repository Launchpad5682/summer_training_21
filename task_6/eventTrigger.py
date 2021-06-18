import os


def terraformLaunch():
    os.chdir("terraformScript")
    os.system("terraform init")
    print("Terraform initiated")
    os.system("terraform apply -auto-approve")
    print("Setup Launched Successfully")
    os.chdir("..")
