# Machine Learning Hack (IoT)

# Agenda
## 0. 環境作成

#### Microsoft Azure

- Azure Machine Learning
    - Azure Storage Account
    - Azure Container Registry
    - Azure KeyVault
- Azure Storage Account
- Azure SQL Database
- Azure Databricks
- Azure DevOps
- Power BI Service


#### ローカルPC

- Power BI Desktop
- Visual Studio Code
- Azure Storage Explorer


## 1. 実験的なモデル開発と推論環境作成
ここでは実験的に IoT データを用いた機械学習のライフサイクルを回していきます。

- データ前処理
- 時系列予測モデル開発
- 推論環境の作成とテスト

 
### データ前処理
- 利用するサービス
    - Azure Databricks
    - Azure SQL Database
- Azure Databricks が提供する Spark 環境を用いて、分散並列処理のデータの前処理プロセスを実行する。また結果を Azure SQL Database に格納する。

### 機械学習モデル開発
- 利用するサービス
    - Azure Machine Learning
        - Notebook VM or ローカルPC Python環境
- 状態空間モデルを開発する

### 推論環境の作成とテスト
- 利用するサービス
    - Azure Machine Learning
    - Azure kubernetes Service
- マニュアル操作で学習済みの状態空間モデルをデプロイする。また、テストデータに対して推論を実行する


## 2. システムの運用管理
前章で構築したものを運用に乗せていく作業を行います。
- データの前処理の自動化
- モデル運用管理  (再学習、際デプロイ)

## 3. 業務アプリケーションとの連携