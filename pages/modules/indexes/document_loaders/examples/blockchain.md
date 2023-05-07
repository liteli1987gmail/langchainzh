
区块链
 [#](#blockchain "Permalink to this headline")
===========================================================




 概述
 [#](#overview "Permalink to this headline")
-------------------------------------------------------



 这篇笔记的目的是为Langchain文档加载程序提供一个测试功能的手段，用于区块链。
 



 最初，这个加载程序支持：
 


* 从NFT智能合约（ERC721和ERC1155)加载NFT作为文档
* Ethereum Maninnet，Ethereum Testnet，Polgyon Mainnet，Polygon Testnet（默认为eth-mainnet)
* Alchemy的getNFTsForCollection API



 如果社区发现该加载程序有价值，它可以扩展。具体而言：
 


* 可以添加其他API（例如交易相关的API)



 这个文档加载器需要：
 


* 免费的 [Alchemy API Key](https://www.alchemy.com/)



 输出采用以下格式：
 


* pageContent=个体NFT
* metadata={'source': '0x1a92f7381b9f03921564a437210bb9396471050c'，'blockchain': 'eth-mainnet'，'tokenId': '0x15'})





 将NFT加载到文档加载器中
 [#](#load-nfts-into-document-loader "Permalink to this headline")
---------------------------------------------------------------------------------------------------






```
alchemyApiKey = "get from https://www.alchemy.com/ and set in environment variable ALCHEMY_API_KEY"

```






### 
 Option 1: Ethereum Mainnet (default BlockchainType)
 [#](#option-1-ethereum-mainnet-default-blockchaintype "Permalink to this headline")







```
contractAddress = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d" # Bored Ape Yacht Club contract address

blockchainType = BlockchainType.ETH_MAINNET  #default value, optional parameter

blockchainLoader = BlockchainDocumentLoader(contract_address=contractAddress,
                                            api_key=alchemyApiKey)

nfts = blockchainLoader.load()

nfts[:2]

```







### 
 Option 2: Polygon Mainnet
 [#](#option-2-polygon-mainnet "Permalink to this headline")







```
contractAddress = "0x448676ffCd0aDf2D85C1f0565e8dde6924A9A7D9" # Polygon Mainnet contract address

blockchainType = BlockchainType.POLYGON_MAINNET 

blockchainLoader = BlockchainDocumentLoader(contract_address=contractAddress, 
                                            blockchainType=blockchainType, 
                                            api_key=alchemyApiKey)

nfts = blockchainLoader.load()

nfts[:2]

```









