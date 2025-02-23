import pandas as pd

# JSON dosyalarını oku
crypto_df = pd.read_json("crypto_money_turkish_dataset.json")
finance_df = pd.read_json("finance_turkish_dataset.json")
ml_df = pd.read_json("machine_learning_turkish_dataset.json") # Yeni eklenen veri seti

# Veri setlerini birleştir
combined_df = pd.concat([crypto_df, finance_df, ml_df])

# Parquet formatına dönüştür
combined_df.to_parquet("crypto_ml_turkish.parquet")