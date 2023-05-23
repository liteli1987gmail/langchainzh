

# Stripe

本教程介绍了如何从Stripe REST API中加载数据到可以摄取到LangChain的格式，以及矢量化的示例用法。
 







```
import os


from langchain.document_loaders import StripeLoader
from langchain.indexes import VectorstoreIndexCreator

```



Stripe API需要访问令牌，该令牌可以在Stripe控制面板中找到。

此文档加载器还需要一个`resource`选项，该选项定义要加载的数据。

以下资源可用：
 



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







