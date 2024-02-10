/**
	Title: soto-projections.js
    Author: Victor Soto
    Date: 02/10/2024
    Description: Building and executing queries in MongoDB (CLI Commands)
 */

// Adding a new user to the 'users' collection.
db.users.insertOne({
    // The first name of the new user is set here.
    "firstName": "Antonio", 
    // The last name of the new user is set here.
    "lastName": "Vivaldi", 
    // The employment ID of the new user is set here.
    "employeeId": "1013", 
    // The email of the new user is set here.
    "email": "antonio.vivaldi@example.com",
    // The date and time when the user is added are set here.
    "dateCreated": new Date() 
});

// This query is for updating Mozart's email address in the 'users' collection.
db.users.updateOne({ firstName: "Wolfgang", lastName: "Mozart" }, { $set: { email: "mozart@me.com" } });

// This query is for retrieving the document of the user named 'Wolfgang Mozart' to verify the email update.
db.users.findOne({ firstName: "Wolfgang", lastName: "Mozart" }, { email: 1, _id: 0 });

// This query is for listing all users in the 'users' collection, displaying only the firstName, lastName, and email fields.
db.users.aggregate([{ $project: { "_id": 0, "firstName": 1, "lastName": 1, "email": 1 } }]);