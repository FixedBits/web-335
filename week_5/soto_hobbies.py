#---------------------------
#Title: soto_hobbies.py
#Author: Victor Soto
#Date: 02/11/2024
#Description: Exercise 5.3 – Python Conditionals, Lists, and Loops
#---------------------------

# List of hobbies
hobbies = ["lifting", "carpentry", "fishing", "biking", "hiking"]

# Loop through the hobbies & Print each hobby
for hobby in hobbies:
  print(hobby)

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Loop through the days. If it’s Saturday or Sunday print  "Day off! Time for hobbies!". 
# For the rest of the week, print ‘Work day.’”Print day status
for day in days:
  if day == "Saturday" or day == "Sunday":
    print(day + ": Day off! Time for hobbies!")
  else:
    print(day + ": Work day.")