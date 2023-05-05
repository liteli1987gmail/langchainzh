提示模板连接到特征存储
===============

特征存储是传统机器学习中的一个概念，确保馈入模型的数据是最新和相关的。有关详细信息，请参见[此处](https://www.tecton.ai/blog/what-is-a-feature-store/)。

在考虑将 LLM 应用程序投入生产时，此概念非常相关。为了个性化 LLM 应用程序，您可能希望将 LLM 与特定用户的最新信息相结合。特征存储可以是保持数据新鲜的好方式，LangChain 提供了一种将该数据与 LLM 组合的简单方式。

在本笔记本中，我们将展示如何将提示模板连接到特征存储。基本思路是从提示模板内部调用特征存储以检索值，然后将其格式化到提示中。

Feast[#](#feast "此标题的永久链接")
---------------------------

首先，我们将使用流行的开源特征存储框架[Feast](https://github.com/feast-dev/feast)。

这假定您已经运行了有关入门的步骤。我们将在入门示例的基础上构建，创建 LLMChain，以向特定司机写入有关其最新统计数据的注释。

### 加载Feast存储[#](#load-feast-store "这个标题的永久链接")

同样，这应该按照Feast README中的说明设置

```
from feast import FeatureStore

# You may need to update the path depending on where you stored it
feast_repo_path = "../../../../../my_feature_repo/feature_repo/"
store = FeatureStore(repo_path=feast_repo_path)

```

### 提示[#](#prompts "这个标题的永久链接")

在这里，我们将设置一个自定义的FeastPromptTemplate。这个提示模板将接受一个驱动程序ID，查找他们的统计数据，并将这些统计数据格式化为提示。

请注意，这个提示模板的输入只是`driver_id`，因为这是唯一的用户定义部分（所有其他变量都在提示模板内查找）。

```
from langchain.prompts import PromptTemplate, StringPromptTemplate

```

```
template = """Given the driver's up to date stats, write them note relaying those stats to them.
If they have a conversation rate above .5, give them a compliment. Otherwise, make a silly joke about chickens at the end to make them feel better

Here are the drivers stats:
Conversation rate: {conv_rate}
Acceptance rate: {acc_rate}
Average Daily Trips: {avg_daily_trips}

Your response:"""
prompt = PromptTemplate.from_template(template)

```

```
class FeastPromptTemplate(StringPromptTemplate):

    def format(self, **kwargs) -> str:
        driver_id = kwargs.pop("driver_id")
        feature_vector = store.get_online_features(
            features=[
                'driver_hourly_stats:conv_rate',
                'driver_hourly_stats:acc_rate',
                'driver_hourly_stats:avg_daily_trips'
            ],
            entity_rows=[{"driver_id": driver_id}]
        ).to_dict()
        kwargs["conv_rate"] = feature_vector["conv_rate"][0]
        kwargs["acc_rate"] = feature_vector["acc_rate"][0]
        kwargs["avg_daily_trips"] = feature_vector["avg_daily_trips"][0]
        return prompt.format(**kwargs)

```

```
prompt_template = FeastPromptTemplate(input_variables=["driver_id"])

```

```
print(prompt_template.format(driver_id=1001))

```

```
Given the driver's up to date stats, write them note relaying those stats to them.
If they have a conversation rate above .5, give them a compliment. Otherwise, make a silly joke about chickens at the end to make them feel better

Here are the drivers stats:
Conversation rate: 0.4745151400566101
Acceptance rate: 0.055561766028404236
Average Daily Trips: 936

Your response:

```

### 在链中使用[#](#use-in-a-chain "这个标题的永久链接")

现在我们可以在链中使用这个，成功创建一个支持特征存储的个性化链

```
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

```

```
chain = LLMChain(llm=ChatOpenAI(), prompt=prompt_template)

```

```
chain.run(1001)

```

```
"Hi there! I wanted to update you on your current stats. Your acceptance rate is 0.055561766028404236 and your average daily trips are 936. While your conversation rate is currently 0.4745151400566101, I have no doubt that with a little extra effort, you'll be able to exceed that .5 mark! Keep up the great work! And remember, even chickens can't always cross the road, but they still give it their best shot."

```

Tecton[#](#tecton "这个标题的永久链接")
------------------------------

上面，我们展示了如何使用Feast，一个流行的开源和自管理特征存储，与LangChain一起使用。下面的示例将展示使用Tecton进行类似集成。Tecton是一个完全管理的特征平台，用于编排完整的ML特征生命周期，从转换到在线服务，具有企业级SLA。

### Prerequisites[#](#prerequisites "Permalink to this headline")

* Tecton Deployment (sign up at <https://tecton.ai>)
* `TECTON_API_KEY` environment variable set to a valid Service Account key

### Define and Load Features[#](#define-and-load-features "Permalink to this headline")

We will use the user_transaction_counts Feature View from the [Tecton tutorial](https://docs.tecton.ai/docs/tutorials/tecton-fundamentals) as part of a Feature Service. For simplicity, we are only using a single Feature View; however, more sophisticated applications may require more feature views to retrieve the features needed for its prompt.

```
user_transaction_metrics = FeatureService(
    name = "user_transaction_metrics",
    features = [user_transaction_counts]
)

```

The above Feature Service is expected to be [应用到实时工作区](https://docs.tecton.ai/docs/applying-feature-repository-changes-to-a-workspace). For this example, we will be using the “prod” workspace.

```
import tecton

workspace = tecton.get_workspace("prod")
feature_service = workspace.get_feature_service("user_transaction_metrics")

```

### 提示[#](#id1 "Permalink to this headline")

在这里，我们将设置一个自定义的TectonPromptTemplate。这个提示模板将接受一个user_id，查找他们的统计信息，并将这些统计信息格式化成一个提示。

请注意，此提示模板的输入只是`user_id`，因为这是唯一的用户定义部分（所有其他变量都在提示模板内查找）。

```
from langchain.prompts import PromptTemplate, StringPromptTemplate

```

```
template = """Given the vendor's up to date transaction stats, write them a note based on the following rules:

1. If they had a transaction in the last day, write a short congratulations message on their recent sales
2. If no transaction in the last day, but they had a transaction in the last 30 days, playfully encourage them to sell more.
3. Always add a silly joke about chickens at the end

Here are the vendor's stats:
Number of Transactions Last Day: {transaction_count_1d}
Number of Transactions Last 30 Days: {transaction_count_30d}

Your response:"""
prompt = PromptTemplate.from_template(template)

```

```
class TectonPromptTemplate(StringPromptTemplate):

    def format(self, **kwargs) -> str:
        user_id = kwargs.pop("user_id")
        feature_vector = feature_service.get_online_features(join_keys={"user_id": user_id}).to_dict()
        kwargs["transaction_count_1d"] = feature_vector["user_transaction_counts.transaction_count_1d_1d"]
        kwargs["transaction_count_30d"] = feature_vector["user_transaction_counts.transaction_count_30d_1d"]
        return prompt.format(**kwargs)

```

```
prompt_template = TectonPromptTemplate(input_variables=["user_id"])

```

```
print(prompt_template.format(user_id="user_469998441571"))

```

```
Given the vendor's up to date transaction stats, write them a note based on the following rules:

1. If they had a transaction in the last day, write a short congratulations message on their recent sales
2. If no transaction in the last day, but they had a transaction in the last 30 days, playfully encourage them to sell more.
3. Always add a silly joke about chickens at the end

Here are the vendor's stats:
Number of Transactions Last Day: 657
Number of Transactions Last 30 Days: 20326

Your response:

```

### 在链中使用[#](#id2 "Permalink to this headline")

现在，我们可以在一个链中使用它，成功创建一个由Tecton Feature Platform支持的个性化链。

```
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

```

```
chain = LLMChain(llm=ChatOpenAI(), prompt=prompt_template)

```

```
chain.run("user_469998441571")

```

```
'Wow, congratulations on your recent sales! Your business is really soaring like a chicken on a hot air balloon! Keep up the great work!'

```

