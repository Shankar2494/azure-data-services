from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "kulkv"
keyVaultUri = f"https://kulkv.vault.azure.net"
secretName = "secret-1"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=keyVaultUri, credential=credential)
dbpwd = client.get_secret(secretName)

print(f"Secret Value is '{dbpwd.value}'")
