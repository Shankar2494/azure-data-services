### Installing Azure CLI on Ubuntu machine & Setting up login
```
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
$ az login # Open the link generate after running this command and add the code mentioned on the console, then login with your azure account
```
### Setting up permission for VM on Key Vault
```
$ az vm identity assign --name "vm-day-4" --resource-group "TechM-Feb" # Generate "systemAssignedIdentity"
$ az keyvault set-policy --name "<your-vault-name>" --object-id "use-<systemAssignedIdentity> generated in above command" --secret-permissions get list
```
