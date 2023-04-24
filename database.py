from pymongo import MongoClient

db_connection = MongoClient("mongo uri here")

db = db_connection.management

user_collection = db["user"]
org_collection = db["organization"]
perm_collection = db["permission"]