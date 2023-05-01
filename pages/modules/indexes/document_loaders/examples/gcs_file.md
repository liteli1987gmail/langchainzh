


 GCS File Storage
 [#](#gcs-file-storage "Permalink to this headline")
=======================================================================



 This covers how to load document objects from an Google Cloud Storage (GCS) file object.
 







```
from langchain.document_loaders import GCSFileLoader

```










```
# !pip install google-cloud-storage

```










```
loader = GCSFileLoader(project_name="aist", bucket="testing-hwc", blob="fake.docx")

```










```
loader.load()

```








```
/Users/harrisonchase/workplace/langchain/.venv/lib/python3.10/site-packages/google/auth/_default.py:83: UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. We recommend you rerun `gcloud auth application-default login` and make sure a quota project is added. Or you can use service accounts instead. For more information about service accounts, see https://cloud.google.com/docs/authentication/
  warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)

```






```
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmp3srlf8n8/fake.docx'}, lookup_index=0)]

```







