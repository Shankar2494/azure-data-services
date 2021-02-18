### Installing Azure CLI on Ubuntu machine & Setting up login
```
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
$ az login # Open the link generate after running this command and add the code mentioned on the console, then login with your azure account
```
### Setting up permission for VM on Key Vault
```
$ az vm identity assign --name "vm-day-4" --resource-group "TechM-Feb" # Generate "systemAssignedIdentity"
$ az keyvault set-policy --name "<your-vault-name>" --object-id "use-<systemAssignedIdentity> generated in above command" --secret-permissions get list set
```

### Install Python3 and PIP3 on Ubuntu
```
$  python3 --version
$  sudo apt-get update
$  sudo apt-get -y upgrade
$  python3 --version
$  sudo apt-get install -y python3-pip
$  pip3 --version
$  sudo -H pip3 install --upgrade pip
$  pip3 --version
$  sudo apt-get install -y python3-setuptools

# Azure python module installed on machine using pip3

$  pip install azure-keyvault-secrets
$  pip install azure.identity

```

### Installing Dotnet Core 5.0 on Ubuntu
```
$ wget https://packages.microsoft.com/config/ubuntu/20.10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
$ sudo dpkg -i packages-microsoft-prod.deb
$ sudo apt-get update;
$ sudo apt-get install -y apt-transport-https &&   sudo apt-get update &&   sudo apt-get install -y dotnet-sdk-5.0
$ sudo apt-get update;
$ sudo apt-get install -y apt-transport-https &&   sudo apt-get update &&   sudo apt-get install -y aspnetcore-runtime-5.0
$ sudo apt-get install -y dotnet-runtime-5.0
```
