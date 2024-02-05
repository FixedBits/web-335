/**
	Title: soto-mongodb-shell.js
    Author: Victor Soto
    Date: 02/04/2024
    Description: MongoDB queries for the users collection
 */

// Query to display all documents in the users collection
db.users.find();

// Query to find the user with an email address of jbach@me.com
db.users.find({ "email": "jbach@me.com" });

// Query to find a user with the last name of Mozart
db.users.find({ "lastName": "Mozart" });

// Query to find a user with a first name of Richard
db.users.find({ "firstName": "Richard" });

// Query to find a user with an employeeId of 1010
db.users.find({ "employeeId": "1010" });