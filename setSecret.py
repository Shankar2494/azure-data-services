from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://kulkv.vault.azure.net/", credential=credential)
secret = secret_client.set_secret("Tera-github-ka-pwd-kya-hai", "MaiKyoBataunMeraPwd")

print(secret.name)
print(secret.value)
print(secret.properties.version)
