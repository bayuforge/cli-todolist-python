from datetime import datetime

task_list = []
task_date_list = []
task_status = []

def home():
    print("\n=================================================================")
    print("                            TO DO LIST                            \n")
    print("================================================================= \n")

    print("Please select an option below: \n")
    print("1. Add a Task \n")
    print("2. View All Task \n")
    print("3. Delete a Task \n")
    print("4. Mark a Task as Completed \n")
    print("5. Exit App \n")
    print("================================================================= \n")

    get_user_option()


def get_option_choice(option):
    match option:
          
        case 1:
            option_one()
        case 2:
            option_two()
        case 3:
            option_three()
        case 4:
            option_four()
        case 5:
            option_five()
        case _:
            print("Invalid option. \n")
            home()
          
            
def get_user_option():
    try:
        print("Your Choice")
        user_input = int(input("> "))
    
    except ValueError: 
        print("Your Input Must Be a String. \n")
        home()

    print(get_option_choice(user_input))


def is_valid_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")

        if date.year >= 2025:
            return True
        else:
            return False
        
    except ValueError:
        return False


def option_one():    
    print("Please Enter Task Description")
    task_desc = str(input("> "))
    #task_list.append(task_desc)

    while True:    
        print("Please Enter the Due Date (DD-MM-YYYY):")
        task_TND = str(input("> "))
        
        if is_valid_date(task_TND):
            task_date_list.append(task_TND)
            break
        else:
            print("Please Insert a Valid Date Where \n" +
                  "DD (1-31), MM (1-12), YYYY (2025 or Greater)")

    task_list.append(task_desc)
    task_status.append("Incomplete")
    print("[Task Successfully Added!]")

    while True:
        try:
            print("Type /home to navigate back to home.")
            user_input = str(input("> "))

            if user_input == "/home":
                home()
                break
            else:
                print("Input is Invalid.")

        except ValueError:
            print("Invalid Option.")


def option_two():
    tlistlen = len(task_list)

    print("Task List:")

    if tlistlen < 1:
        print("No Task is Available.")

    for listnumber, task in enumerate(task_list):
        print(f"{listnumber + 1}. {task} - Due: {task_date_list[listnumber]} - {task_status[listnumber]} \n")

    while True:
        try:
            print("Type /home to navigate back to home.")
            user_input = str(input("> "))

            if user_input == "/home":
                home()
                break
            else:
                print("Input is Invalid.")

        except ValueError:
            print("Invalid Option.")


def option_three():
    tlistlen = len(task_list)
    
    if tlistlen < 1:
        print("\n" + "Request Rejected. Reason: No task available.")
        print("To delete a task, you must first add a task.")
        home()

    print("\n" + "Request Granted.")

    while True:
        print("To delete a task, enter its task number")
        user_input = input("> ")

        if user_input == "/help":
                help_three()
                break

        try:
            task_number = int(user_input)
            if 1 <= task_number <= tlistlen:
                del task_list[task_number - 1]
                del task_date_list[task_number - 1]
                del task_status[task_number - 1]
                print(f"[Task number {task_number} has successfully deleted from existence!] \n")
                break
            else:
                print("Task number is out of range.")
                print("Type /help to see error details.")
        
        except ValueError:
            print("Input is invalid. Type a valid task number.")
    

    option_two()


def help_three():
    print("\n" + "Reference code: I301")
    print("To delete a task, Please refers to the correct task number.")
    print("Navigate back to home, and select '2' to view all task.")
    print("then, See all the list of task with the number associated with it. \n")

    while True:
        try:
            print("Type /home to navigate back to home.")
            user_input = str(input("> "))

            if user_input == "/home":
                home()
                break
            else:
                print("Input is Invalid.")

        except ValueError:
            print("Invalid Option.")


def option_four():
    tlistlen = len(task_status)

    if tlistlen < 1:
        print("\n" + "Option invalid. Please add a task first to mark a task as completed.")
        home()

    while True:
        print("Enter task number to mark as completed")
        user_input = input("> ")

        if user_input == "/help":
            help_four()
            break

        try:
            task_number = int(user_input)

            if 1 <= task_number <= tlistlen:
                task_status[task_number - 1] = "Completed"
                print(f"task value number {task_number}:", task_status[task_number - 1])
                print(f"[Task number {task_number} status: Completed!] \n")
                break
            else:
                print("Task number is out of range.")
                print("Type /help to see error details.")
        
        
        except ValueError:
            print("Input is invalid. Type a valid task number.")
    

    option_two()


def help_four():
    print("\n" + "Reference code: I401")
    print("To mark a task as completed, First you need to have a task added")
    print("In order to get the following task number attached to it.")
    print("if you dont have a task, add task by selecting '1' in home. \n")

    while True:
        try:
            print("Type /home to navigate back to home.")
            user_input = str(input("> "))

            if user_input == "/home":
                home()
                break
            else:
                print("Input is Invalid.")

        except ValueError:
            print("Invalid Option.")


def option_five():
    print("[Thanks for using this application. Have a good day!]")
    print("Freeing memory...")
    exit()


def exit():
    print("Closing the applications...")


home()
