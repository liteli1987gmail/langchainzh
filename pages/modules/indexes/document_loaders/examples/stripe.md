


 Stripe
 [#](#stripe "Permalink to this headline")
===================================================



 This notebook covers how to load data from the Stripe REST API into a format that can be ingested into LangChain, along with example usage for vectorization.
 







```
import os


from langchain.document_loaders import StripeLoader
from langchain.indexes import VectorstoreIndexCreator

```






 The Stripe API requires an access token, which can be found inside of the Stripe dashboard.
 



 This document loader also requires a
 `resource`
 option which defines what data you want to load.
 



 Following resources are available:
 



`balance_transations`
[Documentation](https://stripe.com/docs/api/balance_transactions/list) 




`charges`
[Documentation](https://stripe.com/docs/api/charges/list) 




`customers`
[Documentation](https://stripe.com/docs/api/customers/list) 




`events`
[Documentation](https://stripe.com/docs/api/events/list) 




`refunds`
[Documentation](https://stripe.com/docs/api/refunds/list) 




`disputes`
[Documentation](https://stripe.com/docs/api/disputes/list) 








```
stripe_loader = StripeLoader(os.environ["STRIPE_ACCESS_TOKEN"], "charges")

```










```
# Create a vectorstore retriver from the loader
# see https://python.langchain.com/en/latest/modules/indexes/getting_started for more details

index = VectorstoreIndexCreator().from_loaders([stripe_loader])
stripe_doc_retriever = index.vectorstore.as_retriever()

```







