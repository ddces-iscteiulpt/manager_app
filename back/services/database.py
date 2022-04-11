import os
from dotenv import load_dotenv
import motor.motor_asyncio
from bson.objectid import ObjectId

from database_helpers import items_helper

load_dotenv()

database_url = os.getenv('MONGO_DB')
client = motor.motor_asyncio.AsyncIOMotorClient(database_url)
database = client['SECClasS-DB']
print(f'Database == {database}')
items_collection = database.get_collection('items_test')

# Retrieve all items present in the database
async def retrieve_items():
    items = []
    async for items in items_collection.find():
        items.append(items_helper(items))
    return items

# # Add a new items into to the database
# async def add_items(items_data: dict) -> dict:
#     items = await items_collection.insert_one(items_data)
#     new_items = await items_collection.find_one({"_id": items.inserted_id})
#     return student_helper(new_student)
#
#
# # Retrieve a student with a matching ID
# async def retrieve_student(id: str) -> dict:
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         return student_helper(student)
#
#
# # Update a student with a matching ID
# async def update_student(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         updated_student = await student_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_student:
#             return True
#         return False
#
#
# # Delete a student from the database
# async def delete_student(id: str):
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         await student_collection.delete_one({"_id": ObjectId(id)})
#         return True
