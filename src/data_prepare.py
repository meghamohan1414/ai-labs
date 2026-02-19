from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

RAW_FILE = Path("data/raw/sms_spam_collection.tsv")
OUT_DIR = Path("data/processed")


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw data file not found at {RAW_FILE}. Please run data_download.py first."
        )

    df = pd.read_csv(RAW_FILE, sep="\t", header=None, names=["label", "text"])
    df["label"] = df["label"].str.strip().str.lower()
    df["text"] = df["text"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    df = df[df["label"].isin(["ham", "spam"])]
    df = df[df["text"].str.len() > 0]

    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(OUT_DIR / "train.csv", index=False)
    test_df.to_csv(OUT_DIR / "test.csv", index=False)

    print(f"Saved train rows={len(train_df)} to data/processed/train.csv")
    print(f"Saved test  rows={len(test_df)} to data/processed/test.csv")


if __name__ == "__main__":
    main()
