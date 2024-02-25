#---------------------------
#Title:  soto_usersp1.py
#Author: Victor Soto
#Date:   02/18/2024
#Description: Learning how to use Python to connect to MongoDB
#---------------------------

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.heixdsl.mongodb.net/web335DB?retryWrites=true&w=majority&appName=BellevueUniversity")

# Get a reference to the 'web335DB' database
db = client.web335DB

# Display all documents in the 'users' collection
for user in db.users.find():
    print(user)

# Display a document where the employeeId is 1011
print(db.users.find_one({"employeeId": 1011}))

# Display a document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))