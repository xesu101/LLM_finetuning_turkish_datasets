import pandas as pd

# Parquet dosyasını oku
combined_df = pd.read_parquet("crypto_ml_turkish.parquet")

# CSV'ye dönüştür
combined_df.to_csv("crypto_ml_turkish.csv", index=False)