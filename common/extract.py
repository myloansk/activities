
from abc import abstractmethod

from pandas import DataFrame

import pyspark.sql.functions as f
import pyspark.sql.types as t
import pandas as pd

from __future__ import annotations
from abc import ABC, abstractmethod
from pyspark.sql import DataFrame
from typing import Dict, List, NamedTuple,Optional

class Source(ABC):

    _config:SourceConfig

    @abstractmethod
    def prepare_data(self)->None:pass 

    def get_data(self)->DataFrame:
        return spark.sql(f"SELECT * FROM {dbName}.{tablaName}")



