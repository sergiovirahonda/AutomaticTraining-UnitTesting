import datetime
from google.cloud import storage
import pandas as pd
import numpy as np
import tensorflow as tf
import os
import cv2
import sys

def previous_model(bucket_name,model_filename):
    try:
        print('Checking if a previous model exists at GCS/testing.',flush=True)
        storage_client = storage.Client() #if running on GCP
        bucket = storage_client.bucket(bucket_name)
        status = storage.Blob(bucket=bucket, name='{}/{}'.format('testing',model_filename)).exists(storage_client)
        print('Model existance: '+str(status))
        return status,None
    except Exception as e:
        print('Something went wrong when trying to check if previous model exists GCS bucket. Exception: '+e,flush=True)
        return None,e

def load_model(bucket_name,model_filename):
    print('Loading previous model from GCS bucket. Downloading file.',flush=True)
    try:
        storage_client = storage.Client() #if running on GCP
        bucket = storage_client.bucket(bucket_name)
        blob1 = bucket.blob('{}/{}'.format('testing',model_filename))
        blob1.download_to_filename('/root/'+str(model_filename))
        print('Previous model loaded',flush=True)
        return True,None
    except Exception as e:
        print('Something went wrong when trying to load previous model from GCS bucket. Exception: '+e,flush=True)
        return False,e




    

