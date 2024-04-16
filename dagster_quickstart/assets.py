from geojson import Point
import numpy as np
import pandas as pd

from dagster import (
    MaterializeResult,
    MetadataValue,
    asset,
)
from dagster_quickstart.configurations import NaptanConfig

def MaterializeResultMetaData(df):
    return {
            "num_records": len(df),
            "preview": MetadataValue.md(str(df.fillna('').head(10).to_markdown()))
        }

@asset
def naptan_raw(config: NaptanConfig):
    """Raw National Public Transport Access Nodes from NaPTAN endpoint."""
    naptan_url = "https://naptan.api.dft.gov.uk/v1/access-nodes?dataFormat=csv"
    naptan_raw_df = pd.read_csv(naptan_url)
    naptan_raw_df.columns = (naptan_raw_df.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )
    naptan_raw_df.to_csv(config.naptan_raw_path, index=False)

    return MaterializeResult(
        metadata=MaterializeResultMetaData(naptan_raw_df)
    )

@asset(deps=[naptan_raw])
def naptan_clean(config: NaptanConfig):
    """National Public Transport Access Nodes with geojson"""
    naptan_clean_df = pd.read_csv(config.naptan_raw_path,
                            dtype={'naptan_code':'string',
                                   'plate_code':'string',
                                   'short_common_name':'string',
                                   'town':'string',
                                   'town_lang':'string',
                                   'suburb':'string',
                                   'suburb_lang':'string',
                                   'locality_centre':'string',
                                   'longitude':'float',
                                   'latitude':'float'
                                   })
    zipped_point = zip(naptan_clean_df['longitude'].replace(np.nan,None), naptan_clean_df['latitude'].replace(np.nan,None))
    naptan_clean_df['geom'] = [Point(x) if all(x) else None for x in zipped_point]
    naptan_clean_df.to_csv(config.naptan_clean_path,index=False)

    return MaterializeResult(
        metadata=MaterializeResultMetaData(naptan_clean_df)
    )