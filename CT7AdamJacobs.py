#Adam Jacobs
#Critical Thinking 7
#Requirements:
    #Step 1: Data Specifications
    #Step 2: Program Logic

#Creating three dictionaries Rooms, Instructors, and Times
room_numbers ={
    "CSC101": "Room 3004",
    "CSC102": "Room 4501",
    "CSC103": "Room 6755", 
    "NET110": "Room 1244",  
    "COM241": "Room 1411"
}
instructors_names ={
    "CSC101": 'Haynes',
    "CSC102": 'Alvarado',
    "CSC103": 'Rich', 
    "NET110": 'Burke',  
    "COM241": 'Lee'
}
meeting_times = {
    "CSC101": "8:00 AM",
    "CSC102": "9:30 AM",
    "CSC103": "11:00 AM", 
    "NET110": "2:00 PM", 
    "COM241": "3:30 PM"
}

#Input: Prompting student for course number
course_number = input("Please Enter Course Number:")

#Retrieval: Look up Course Number with if
#Output: Display Room Number, Instructor and Meeting Time and error message
if course_number in room_numbers:
    print()
    print("COURSE INFORMATION")
    print (f"Your Room Number is: {room_numbers[course_number]}")
    print (f"Your Instructor is: {instructors_names[course_number]}")
    print (f"Class Time is: {meeting_times[course_number]}")
else:
    print("Double check course number and try again, course does not exsit")