


 Slack (Local Exported Zipfile)
 [#](#slack-local-exported-zipfile "Permalink to this headline")
=================================================================================================



 This notebook covers how to load documents from a Zipfile generated from a Slack export.
 



 In order to get this Slack export, follow these instructions:
 




 🧑 Instructions for ingesting your own dataset
 [#](#instructions-for-ingesting-your-own-dataset "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------



 Export your Slack data. You can do this by going to your Workspace Management page and clicking the Import/Export option ({your_slack_domain}.slack.com/services/export). Then, choose the right date range and click
 `Start
 

 export`
 . Slack will send you an email and a DM when the export is ready.
 



 The download will produce a
 `.zip`
 file in your Downloads folder (or wherever your downloads can be found, depending on your OS configuration).
 



 Copy the path to the
 `.zip`
 file, and assign it as
 `LOCAL_ZIPFILE`
 below.
 







```
from langchain.document_loaders import SlackDirectoryLoader 

```










```
# Optionally set your Slack URL. This will give you proper URLs in the docs sources.
SLACK_WORKSPACE_URL = "https://xxx.slack.com"
LOCAL_ZIPFILE = "" # Paste the local paty to your Slack zip file here.

loader = SlackDirectoryLoader(LOCAL_ZIPFILE, SLACK_WORKSPACE_URL)

```










```
docs = loader.load()
docs

```








