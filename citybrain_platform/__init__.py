import os as __os
from citybrain_platform.computing import Computing
from citybrain_platform.computing.data_types import ColumnType, Column, JobStatus

api_key = __os.getenv("CITYBRAIN_APIKEY")
api_baseurl = __os.getenv("CITYBRAIN_API_BASEURL", "https://citybrain.org/platform/")

__all__ = [
    "Computing", 
    "api_key", 
    "api_baseurl", 
    "ColumnType", 
    "Column", 
    "JobStatus"
]