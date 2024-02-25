#---------------------------
#Title:  soto_usersp2.py
#Author: Victor Soto
#Date:   02/25/2024
#Description: Learning how to use Python to connect to MongoDB - Part 2
#---------------------------

# Import the MongoClient
from pymongo import MongoClient
from datetime import datetime

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.heixdsl.mongodb.net/web335DB?retryWrites=true&w=majority&appName=BellevueUniversity")

# Get a reference to the 'web335DB' database
db = client.web335DB

# Create a new user document
new_user = {
    "employeeId": "1012",
    "firstName": "Johnny",
    "lastName": "Bravo",
    "email": "jbravo@nomail.com",
    "dateCreated": datetime.now()
}
result = db.users.insert_one(new_user)
print(result.inserted_id)

# Display the newly created document
created_user = db.users.find_one({"_id": result.inserted_id})
print(created_user)

# Update the email address of the created document
db.users.update_one({"_id": result.inserted_id}, {"$set": {"email": "j_newbravo@yesmail.com"}})

# Display the updated document
updated_user = db.users.find_one({"_id": result.inserted_id})
print(updated_user)

# Delete the document
db.users.delete_one({"_id": result.inserted_id})

# Prove the document was deleted
deleted_user = db.users.find_one({"_id": result.inserted_id})
print(deleted_user)