# 情報科学演習2025

## ✅ 概要
このリポジトリは，2025年度の情報科学演習で使用する教材とコンペティション課題を含んでいます．
時系列データ分析をテーマに，Pythonのデータサイエンスライブラリを用いた実践的なプログラミングスキルと分析手法の習得を目指します．

## 📁 ディレクトリ構成

```
情報科学演習2025/
├── README.md
├── 01_turorial/                # 基礎編：チュートリアル
│   ├── README.md               # 基礎編の詳細説明
│   ├── data/
│   │   ├── raw/
│   │   │   └── cafe_customers.csv
│   │   └── processed/
│   │       └── feature_engineered_data.csv
│   └── notebooks/
│       ├── 01_pandas_basics.ipynb          # 01.Pandasの基礎
│       ├── 02_visualization_basics.ipynb   # 02.データ可視化の基礎
│       ├── 03_time_series_features.ipynb   # 03.特徴量エンジニアリング
│       ├── 04_prediction_model.ipynb       # 04.予測モデルの構築
│       └── hint/
|
└── 02_competition/             # 実践編：コンペティション
    ├── README.md               # 実践編の詳細説明
    ├── data/
    │   └── raw/
    │       ├── attendance_data.csv
    │       └── calendar_data.csv
    ├── notebooks/
    │   ├── analysis_report.ipynb
    │   └── hint/
    └── submission/
        ├── submission.csv
        └── submission_advanced.csv
```

## 🚀 学習の進め方

### Step 1: 基礎編（01_tutorial）
詳細は [`01_turorial/README.md`](./01_turorial/README.md) を参照してください。

### Step 2: 実践編（02_competition）
詳細は [`02_competition/README.md`](./02_competition/README.md) を参照してください。

## 💻 環境構築

### 仮想環境の作成

```bash
python3 -m venv .venv
source .venv/bin/activate

# (.venv) hogehoge@dnnXX:~$のように表示されたら成功
```

### 必要なライブラリのインストール
注意：仮想環境をアクティベートした状態で実行してください！

```bash
pip install -r requirements.txt
```

### カーネルの登録

```bash
python3 -m ipykernel install --user --name=.venv --display-name ".venv"
```