from dagster import Config
import os

class NaptanConfig(Config):
    naptan_raw_path: str = os.path.join("tmp", "naptan_raw.csv")
    naptan_clean_path: str = os.path.join("tmp", "naptan_clean.csv")