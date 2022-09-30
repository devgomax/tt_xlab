import os

from dotenv import load_dotenv

load_dotenv()

DADATA_TOKEN = os.getenv('DADATA_TOKEN')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
