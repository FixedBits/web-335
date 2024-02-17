/**
	Title: soto-aggregate-queries.js
    Author: Victor Soto
    Date: 02/17/2024
    Description: Creating and executing MongoDB queries and experimenting with aggregate queries.
 */

// Load 'houses.js' file.
load('houses.js')

// Display all houses.
db.houses.find()

// Display all students.
db.students.find()

// Add a new student 'Johnny Bravo'.
db.students.insertOne({'firstName':'Johnny', 'lastName':'Bravo', 'studentId':'s1019', 'houseId':'h1009'})

// Display 'Johnny Bravo's' details.
db.students.find({ 'studentId': 's1019'})

// Delete 'Johnny Bravo'.
db.students.deleteOne({ 'studentId': 's1019' })

// Try to find 'Johnny Bravo' again.
db.students.find({ 'studentId': 's1019'})

// List students with their house details.
db.students.aggregate([{ $lookup: { from: "houses", localField: "houseId", foreignField: "houseId", as: "house_info" } }])

// List students for house 'Gryffindor'.
db.students.aggregate([{ $lookup: { from: "houses", localField: "houseId", foreignField: "houseId", as: "house_info" } }, { $match: { "house_info.founder": "Godric Gryffindor" } }])

// List students from the house with the 'Eagle' mascot.
db.students.aggregate([{ $lookup: { from: "houses", localField: "houseId", foreignField: "houseId", as: "house_info" } }, { $match: { "house_info.mascot": "Eagle" } } ])