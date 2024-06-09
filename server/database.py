import os
import motor.motor_asyncio
from bson.objectid import ObjectId

from . import models

MONGODB_URL = os.environ['MONGODB_URL']

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.get_database("graphvisual_prod")
adjacency_collection = db.get_collection("adjacency_lists")


def transform_keys_to_strings(data: dict) -> dict:
    return {str(k): v for k, v in data.items()}


async def create_adjacency_list(item: models.AdjacencyList):
    item_dict = item.dict()
    item_dict['edges'] = transform_keys_to_strings(item_dict['edges'])
    if item_dict.get('labels'):
        item_dict['labels'] = transform_keys_to_strings(item_dict['labels'])
    if item_dict.get('colors'):
        item_dict['colors'] = transform_keys_to_strings(item_dict['colors'])

    result = await adjacency_collection.insert_one(item_dict)
    item_dict["_id"] = str(result.inserted_id)
    return item_dict


async def read_adjacency_list(item_id: str):
    item = await adjacency_collection.find_one({"_id": ObjectId(item_id)})
    return models.AdjacencyList.parse_obj(item)
