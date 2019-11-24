# Machine Learning Hack (IoT)

# Agenda
## Module 0 : 環境作成

#### Microsoft Azure ([link](https://portal.azure.com/?feature.customportal=false#home))

- Azure Machine Learning
    - Azure Blob Storage
    - Azure Container Registry
    - Azure KeyVault
- Azure Blob Storage
- Azure SQL Database
- Azure Databricks
- Azure DevOps ([link](https://dev.azure.com))
- Power BI Service ([link](powerbi.com))


#### ローカルPC

- Power BI Desktop ([link](https://aka.ms/pbidesktopstore))
- Visual Studio Code ([link](https://code.visualstudio.com/))
- Azure Storage Explorer ([link](https://azure.microsoft.com/en-us/features/storage-explorer/))
- Azure Data Studio ([link](https://github.com/microsoft/azuredatastudio))


## Module 1 : 実験的なモデル開発と推論環境作成
ここでは実験的に IoT データを用いた機械学習のライフサイクルを回していきます。

- データ前処理
- 時系列予測モデル開発
- 推論環境の作成とテスト

 
### データ前処理
- 利用するサービス
    - Azure Databricks
    - Azure SQL Database
- Azure Databricks が提供する Spark 環境を用いて、分散並列処理のデータの前処理プロセスを実行する。また結果を Azure SQL Database に格納する。
- Data : [AirPassengers.csv](data/AirPassengers.csv)
- Notebook : [databricks-blob-mount.ipynb](notebook/databricks-blob-mount.ipynb)
- 参考ドキュメント
    - [Mount Azure Blob storage containers to DBFS](https://docs.microsoft.com/ja-jp/azure/databricks/data/data-sources/azure/azure-storage?toc=https%3A%2F%2Fdocs.microsoft.com%2Fja-JP%2Fazure%2Fazure-databricks%2FTOC.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fja-jp%2Fazure%2Fbread%2Ftoc.json#--mount-azure-blob-storage-containers-to-dbfs--mount-azure-blob-storage-containers-to-dbfs)

### 機械学習モデル開発
- 利用するサービス
    - Azure Machine Learning
        - Notebook VM or ローカルPC Python環境
- 状態空間モデルを開発する
- Data : [AirPassengers.csv](data/AirPassengers.csv)
- Notebook : [SSM-local-trend-azureml.ipynb](notebook/SSM-local-trend-azureml.ipynb)

### 推論環境の作成とテスト
- 利用するサービス
    - Azure Machine Learning
    - Azure Kubernetes Service
- マニュアル操作で学習済みの状態空間モデルをデプロイする。また、テストデータに対して推論を実行する


## Module 2 : データの運用管理
- 利用するサービス
    - Azure Data Factory
    - Azure Databricks
    - Azure SQL Database
- データを運用に乗せていく作業を行います。データソースからのデータ抽出、前処理の処理を自動化します。
- 参考ドキュメント
    - [Azure Data Factory で Databricks Notebook アクティビティを使用して Databricks ノートブックを実行する](https://docs.microsoft.com/ja-JP/azure/data-factory/transform-data-using-databricks-notebook)

## Module 3 : モデルの運用管理
- 利用するサービス
    - Azure Machine Learning
    - Azure DevOps
- 機械学習モデルの再学習と再デプロイが自動で出来るようにパイプラインを構築します。



## Module 4 : 業務アプリケーションとの連携
Power BI や Microsoft Teams と連携して、より効率的に日々の開発・運用管理できる環境を作成します。
- レポートの作成
- Azure DevOps、Power BI の Teams 連携

<br>

#  Documents

- [Azure Machine Learning](https://docs.microsoft.com/ja-JP/azure/machine-learning/)
- [Azure Storage Account](https://docs.microsoft.com/ja-jp/azure/storage/blobs/)
- [Azure SQL Database](https://docs.microsoft.com/ja-jp/azure/sql-database/)
- [Azure Databricks](https://docs.microsoft.com/ja-JP/azure/azure-databricks/)
- [Azure DevOps](https://docs.microsoft.com/ja-jp/azure/devops/?view=azure-devops)
- [Power BI Service](https://docs.microsoft.com/ja-JP/power-bi/)