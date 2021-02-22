configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": "<applicationid>",
  "fs.azure.account.oauth2.client.secret": "<app-secret>",
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenent_id>/oauth2/token",
  "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

dbutils.fs.mount(
  source = "abfss://<container_name>@<storage_account_name>.dfs.corewindows.net/<folder_where_files_are_uploaded>",
  mount_point = "/mnt/on_time",
  extra_configs = configs
)
