from tabulate import tabulate

#This is to select the courses for the department of technology at the ABC College holiday pathway program
headers = ["Number", "Course", "Duration", "Cost", "Pre Requisite"]
courses = {  # list dictionary
    1: {
        "name": "Food Science",
        "duration": "16",
        "cost": 150,
        "pre_requisite": "Food technology in secondary school",
    },
    2: {
        "name": "Food Technology",
        "duration": "17",
        "cost": 280,
        "pre_requisite": "Food technology in secondary school",
    },
    3: {
        "name": "Material Science",
        "duration": "15",
        "cost": 250,
        "pre_requisite": "Materials Technology in Secondary School",
    },
    4: {
        "name": "Hard Materials",
        "duration": "16",
        "cost": 300,
        "pre_requisite": "Materials Technology in Secondary School",
    },
    5: {
        "name": "Digital Technologies",
        "duration": "18",
        "cost": 200,
        "pre_requisite": "Digital Technologies in Secondary Education",
    },
    6: {
        "name": "Robotics",
        "duration": "16",
        "cost": 280,
        "pre_requisite": "Digital Technologies in Secondary Education",
    },
}
values = [[name, *inner.values()] for name, inner in courses.items()]
table = tabulate(values, headers=headers, tablefmt="grid")

#this is to restart the selection if the user does not want to confirm
while True:
    print('\nWelcome to the department of technology, ABC College holiday pathway program')
    #basic details 
    while True:
        name = input("\n\nEnter your first name: ")
        if len (name) > 30:
            print('Error, 30 character limit.')
            continue 
        
        if name.isalpha():
            break
        print('Invalid, please use letters only.')
    #asking user for age
    while True:
        try:
            age = int(input('What is you age: '))
            if age < 15:
                print('You are too young to be enrolled into this course.')
                exit()
            elif age > 100:
                print("You probably shouldn't be here!")
                exit()
        except ValueError:
            print('Please enter a valid number.')
            continue
        break
    while True:
        email = input("Enter your school email address: ")
        if '@ac.school.nz' in email:
            break
        elif '@alfristoncollege.school.nz' in email:
            break
        else:
            print('Sorry, this is not a valid email.')
            continue
    print (f'\nwelcome {name}, here are your course options:')

    #display courses   
    print(table)

        # selecting courses
    while True:
        while True:
            try:
                course_select = int(input("\nSelect a course 1-6: "))
                if course_select > 6 or course_select == 0:
                    print("Invalid choice, please try again")
                    continue
            except ValueError:
                print('Please enter a valid number.')
                continue

                    # meeting pre requisite
            requisite = input(
                    f'Do you meet the pre-requisites for {courses[course_select]["pre_requisite"]}? (y/n): '
                )
            if requisite == "n":
                print("You cannot choose this course.")
                print(f"\n\n {table}")
                continue
            elif requisite == "y":
                print("You can pick this course!")
            else:
                print("invalid, please try again")
                continue
            while True:
                try:
                    course_select2 = int(input("\nSelect your second course 1-6: "))
                    if course_select2 == course_select:
                        print('This is the same course!')
                        continue
                    if course_select2 > 6 or course_select2 == 0:
                        print("Invalid choice, please try again")
                        continue
                except ValueError:
                    print('Please enter a valid number.')
                    continue
                requisite = input(
                    f'Do you meet the pre-requisites for {courses[course_select2]["pre_requisite"]}? (y/n): '
                )
                if requisite == "n":
                    print("You cannot choose this course.")
                    print(f"\n\n {table}")
                    continue
                elif requisite == "y":
                    print("You can pick this course!")
                else:
                    print("invalid, please try again")
                    continue
                while True:
                    try:
                        course_select3 = int(input("\nSelect your third course 1-6: "))
                        if course_select3 == course_select:
                            print('This is the same course!')
                            continue
                        elif course_select3 == course_select2:
                            print('This is the same course!')
                            continue
                        if course_select3 > 6 or course_select3 == 0:
                            print("Invalid choice, please try again")
                            continue
                    except ValueError:
                        print('Please enter a valid number.')
                        continue
                    requisite = input(
                        f'Do you meet the pre-requisites for {courses[course_select3]["pre_requisite"]}? (y/n): '
                    )
                    if requisite == "n":
                        print("You cannot choose this course.")
                        print(f"\n\n {table}")
                        continue
                    elif requisite == "y":
                        print("You can pick this course!")
                        break
                    else:
                        print("invalid, please try again")
                    continue
                break
            break
        break #breaking out of all loops if it reaches this point
    # asking if user needs transport
    while True:
        transport = input(
            "\nDo you need transport which is a shuttle bus for $80? (y/n): "
        )
        if transport == "y":
            break
        elif transport == "n":
            break
        else:
            print("invalid, please try again")
            continue
            #asking for meal preference
    while True:
        food = input('\nWhat is your meal preference? \n1 - standard\n2 - veg\n3 - vegan\n\nselect a meal 1-3: ')
        if food == '1':
            food = 'standard'
            break
        elif food == '2':
            food = 'veg'
            break
        elif food == '3':
            food = 'vegan'
            break
        else:
            print('invalid, please try again')
            continue
    # adding or removing cost of transport
    transport_cost = 80
    if transport == "n":
        transport_cost = 0
    price = (
        courses[course_select]["cost"]
        + transport_cost
        + courses[course_select2]["cost"]
        + courses[course_select3]["cost"]
    )
    #deciding which course is longer
    if courses[course_select]["duration"] > courses[course_select2]["duration"] and courses[course_select]["duration"] > courses[course_select3]["duration"]:
        duration = courses[course_select]["duration"]
    elif courses[course_select2]["duration"] > courses[course_select]["duration"] and courses[course_select2]["duration"] > courses[course_select3]["duration"]:
        duration = courses[course_select2]["duration"]
    elif courses[course_select3]["duration"] > courses[course_select]["duration"] and courses[course_select3]["duration"] > courses[course_select2]["duration"]:
        duration = courses[course_select3]["duration"]
    # display details
    print(f'\nHi {name}, you have chosen {courses[course_select]["name"]}, {courses[course_select2]["name"]} and {courses[course_select3]["name"]} the total time you will be going to course is {duration} weeks, and you will be recieving the {food} option of food.')
    print(f"Your total cost is - ${price}")
        
    #confirming if this is the wanted course
    confirm = input('\nwould you like to confirm? (y/n): ')
    if confirm =='n':
        print('\nYou are restarting the selection.')
        continue
    if confirm != 'y' and confirm != 'n':
        print('Invalid, restarting the selection.')
        continue
    if confirm == 'y':
        print (f'Congratulations! {name} you have been enrolled for these courses, your receipt will be emailed to you at {email}.')
    break
