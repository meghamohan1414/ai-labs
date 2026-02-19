import urllib.request
import zipfile
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_FILE = RAW_DIR / "sms_spam_collection.tsv"
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = RAW_DIR / "smsspamcollection.zip"

    if not zip_path.exists():
        print(f"Downloading data to {zip_path}...")
        urllib.request.urlretrieve(URL, zip_path)
        print("Download complete.")

    if not RAW_FILE.exists():
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            with zip_ref.open("SMSSpamCollection") as f:
                RAW_FILE.write_bytes(f.read())
        print(f"Extracted data to {RAW_FILE}.")

    else:
        print(f"Data already exists at {RAW_FILE}.")


if __name__ == "__main__":
    main()
