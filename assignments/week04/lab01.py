"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Coconut", 33, "London", "United Kingdom")  # name, age, city, country
    hobbies = [Listening Thai Remix Song]
    
    # Your code here
    while true:

        print("1 Display into ,2 Add hobby, 3 Remmove hobby, 4 edit age, 5 Exit")   
        choice = input("What do you want to do?: ")

    if choice == "1":
        print("Name:", person[0])
        print("Age:", person[1])
        print("City:", person[2])
        print("Country:", person[3])
        print("Hobbies:", hobbies)

    if else == "2":
        hobby = input("Insert new hobby: ")
        hobbies.append(hobby)

    if else == "3":
        del hobbies[0]

    if else == "4":
        age = int(input("Insert new age: ")
        person list = list(person)
        person_list[1]  = age
        person = tuple(person_list)

if __name__ == "__main__":
    personal_info_manager()
