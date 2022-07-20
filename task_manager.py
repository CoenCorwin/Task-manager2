# ===========================================================================
# ====== Register new users ======
from datetime import date
from datetime import datetime
from itertools import count


def reg_user(count):
    # set while to True
    while True:
      # open text file called 'user.txt' second argument make read-only
      with open('user.txt', 'r') as f:
        
        # print out title
        print("Create new user:")
        
        # create input for new username and password 
        new_username = input("Please enter new username\n")
        new_pw = input("Please enter new password\n")
        confirm_pw = input("Please confirm password\n")
        
        # if new username in the file
        if new_username in f:
          # print out this message
          print("The username already exits")

        # if new password is not equal to confirm password 
        elif new_pw != confirm_pw:
          # print out this message
          print("Passwords doesn't match")

        # if new password is equal to confirm password 
        else:
          # open file 'user.txt' second argument make append-only
          new_user = open('user.txt', 'a')

          # count register user
          count += 1

          # write the new username and password to text file
          new_user.write(f"\n{new_username}, {new_pw}")

          # close the text file after add new user text file
          new_user.close()

          # print out this message
          print("You have successful create new user")

          # break loop if the password is eqaul to confirm password
          break

    print(" ")
count = 0
# ===========================================================================
# ====== Add new task ======
def add_task(count):
   
    with open( 'user.txt' ) as f:    
        usernames = [i.split(',')[0] for i in f.readlines() if len(i) > 3]
        task = input ("Please enter the username of the person the task is assigned to.\n")
    while task not in usernames :
        task = input("Username not registered. Please enter a valid username.\n")

    else:
        task_title = input("Please enter the title of the task.\n")
        task_description = input("Please enter the task description.\n")
        curr_date = str(date.today().strftime('%d-%m-%Y'))
        task_due = input("Please input the due date of the task. (dd-mm-yyyy)\n")
        task_completed = "No"

        with open('tasks.txt', 'a') as task1:
            count += 1
            task1.write(f"\n{task}, {task_title}, {task_description}, {curr_date}, {task_due}, {task_completed}")
            print("The new assigned task has been saved")
count = 0
# ===========================================================================
# ====== View all tasks ======
def view_all():

   # print out title
    print("View of all the task:")

    # open text file called 'user.txt' second argument make read-only
    with open('tasks.txt', 'r') as f:

      # loop thought in the file
      for line in f:
        # break down the string in the file where the are comma and white space is
        user, title, descr, curr_date, due_date, task_comp = line.split(", ")
        
        # print out the text file in user-friendly manner
        print(f'''
        Task:                 {title}
        Assigned to:          {user}
        Date assigned:        {curr_date}
        Due date:             {due_date}
        Task Complete?        {task_comp}
        Task description:
        {descr}
        ''')
        print(" ")
        
    print(" ")

# ===========================================================================
# ====== View all my tasks ======
def view_mine():
  print("All my task:")
  # create empty list 
  tasks = []
  # count the tasks
  i = 0

  # open the file 'tasks.txt'
  with open('tasks.txt') as f:
    # read the file and split lines
    lines = f.read().splitlines() 
    # loop though in enumrate count the line
    for row, line in enumerate(lines):
      # break down the string in the file where the are comma and white space is
      user, title, descr, curr_date, due_date, task_comp = line.split(", ")

      # if the user input is equal to whom the task is assigned to
      if username_input == user:
        # create a dictionary loop in dic and zip the dic to easy access the dic
        data = {k:v for k,v in zip((
          'number', 'row', 'user', 'title', 'description', 'current date', 'due date', 'completed'),
          (i + 1, row, user, title, descr, curr_date, due_date, task_comp)
        )} 
        # add data to tasks list
        tasks.append(data)
        # add 1 to task number
        i += 1

        # print out the text file in user-friendly manner
        print(f'''
        Task number:          {data['number']}
        Task:                 {data['title']}
        Assigned to:          {data['user']}
        Date assigned:        {data['current date']}
        Due date:             {data['due date']}
        Task Complete?        {data['completed']}
        Task description:
        {data['description']}
        ''')
        print(" ")

  # ask the user which task number to edit
  task_num = int(input("Please select the Task number you like to edit: "))
  # stay in the index range
  task = tasks[task_num - 1]

  while True:
    # print out this message
    edit_option = input('''Would you like to:
    e - edit the task
    c - mark the task complete
    -1 - return to main menu
    : ''').lower()

    # if user choice 'e' and task completed equal to 'No'
    if edit_option == 'e' and task['completed'] == 'No':
      # print out this message
      edit = input('''Would you like to:
      u - change the username the task assigned
      d - change the due date of the task
      : ''').lower()

      # if user choice 'u'
      if edit == 'u':
        # open the file 'tasks.txt'
        with open('tasks.txt', 'a') as f:
          # ask user name to assigned to the task
          task['user'] = input("Enter new user\n")

          # add to the text file
          f.write(f"\n{task['user']}, {task['title']}, {task['description']}, {task['current date']}, {task['due date']}, {task['completed']}")

      # if user choice 'd'
      elif edit == 'd':
        # open the file 'tasks.txt'
        with open('tasks.txt', 'a') as f:
          # ask user name to assigned to the task
          task['due date'] = input("Enter new due date\n")

          # add to the text file
          f.write(f"\n{task['user']}, {task['title']}, {task['description']}, {task['current date']}, {task['due date']}, {task['completed']}")
      
      # if user choice none
      else:
        # print out this message
        print("Invalid please select option")

    # if user choice 'c' and task completed equal to 'No'
    elif edit_option == 'c' and task['completed'] == 'No':
      # open the file 'tasks.txt'
        with open('tasks.txt', 'a') as f:
          # ask user name to assigned to the task
          task['completed'] = input("Enter yes or no if task is completed\n")

          # add to the text file
          f.write(f"\n{task['user']}, {task['title']}, {task['description']}, {task['current date']}, {task['due date']}, {task['completed']}")

    # if choice '-1' return to main menu
    elif edit_option == '-1':
      break

    # if user choice none
    else:
      # print out this message
      print("Invalid please select option")

# ===========================================================================
# ====== Generate task overview ======
def task_overview():
  
  # declare variables and use later in the code
  completed_tasks = 0
  uncompleted_tasks = 0
  overdue_tasks = 0
  i = 0

  # open the file 'tasks.txt'
  with open('tasks.txt') as f:
    # read the file and split lines
    lines = f.read().splitlines() 
    # loop though in enumrate count the line
    for row, line in enumerate(lines):
      # break down the string in the file where the are comma and white space is
      user, title, descr, curr_date, due_date, task_comp = line.split(", ")

      # create a dictionary loop in dic and zip the dic to easy access the dic
      data = {k:v for k,v in zip((
        'number', 'row', 'user', 'title', 'description', 'current date', 'due date', 'completed'),
        (i + 1, row, user, title, descr, curr_date, due_date, task_comp)
      )} 
      # number of task
      i += 1

      # completed is equal to 'No'
      if data['completed'] == 'No':
        # add 1
        uncompleted_tasks += 1

      # completed is equal to 'Yes'
      elif data['completed'] == 'Yes':
        # add 1
        completed_tasks += 1

      # Comparing the dates to check if the task is overdue.
      if data['due date'] < str(date.today()):
        overdue_tasks += 1


    # calc the percentage
    percentage_incomplete = (uncompleted_tasks * 100)/ (i)
    percentage_overdue = (overdue_tasks * 100)/ (i)

    # create new text file called 'task_overview'
    with open('task_overview.txt', 'w') as task_overview:
      task_overview.write(f"Total number of tasks generated using Task Manager: {i}\n")
      task_overview.write(f"Number of completed tasks: {completed_tasks}\n")
      task_overview.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
      task_overview.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
      task_overview.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
      task_overview.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")
        
# ===========================================================================
# ====== Generate user overview ======
def user_overview():
  # declare variables and use later in the code
  i = 0
  j = 0
  completed = 0
  incompleted = 0
  overdue = 0

  # open the file 'user.txt'
  with open('user.txt', 'r') as f:
    # loop though f
    for users in f:
      # add 1 for each line
      i += 1
  
  # open the file 'tasks.txt'
  with open('tasks.txt') as f:
    # read the file and split lines
    lines = f.read().splitlines() 
    # loop though in enumrate count the line
    for row, line in enumerate(lines):
      # break down the string in the file where the are comma and white space is
      user, title, descr, curr_date, due_date, task_comp = line.split(", ")

      # create a dictionary loop in dic and zip the dic to easy access the dic
      data = {k:v for k,v in zip((
        'number', 'row', 'user', 'title', 'description', 'current date', 'due date', 'completed'),
        (j + 1, row, user, title, descr, curr_date, due_date, task_comp)
      )} 
      # number of task
      j += 1

      # completed is equal to 'Yes'
      if data['completed'] == "Yes":
        # add 1
        completed += 1
      
       # completed is equal to 'No'
      elif data['completed'] == "No":
        # add 1
        incompleted += 1

      # Comparing the dates to check if the task is overdue.
      if data['due date'] < str(date.today()) and data['completed'] == 'No':
        # add 1
        overdue += 1

  # calc the percentage
  percentage_assigned = (j * 100)/ (i)
  percentage_completed = (completed * 100)/ (i)
  percentage_incompleted = (incompleted * 100)/ (i)
  percentage_overdue = (overdue * 100)/ (j)

  # check if username equal to user
  if username_input == user:
    # create new text file called 'task_overview'
    with open('user_overview.txt', 'w') as user_overview:
     user_overview.write(f"Total number of users registered using Task Manager: {i}\n")
     user_overview.write(f"Total number of tasks generated using Task Manager: {j}\n")
     user_overview.write(f"Total number of tasks assigned to user: {j}\n")
     user_overview.write(f"Percentage of the total number of tasks have been assigned to that user: {percentage_assigned}\n")
     user_overview.write(f"Percentage of the tasks assigned to that user have been completed: {percentage_completed:.0f}\n")
     user_overview.write(f"Percentage of the tasks assigned to that user must still be completed: {percentage_incompleted:.0f}%\n")
     user_overview.write(f"percentage of the tasks assigned to that user have not yet been completed and are overdue: {percentage_overdue:.0f}%\n")

# ===========================================================================
# ====== Generate reports ======
def generate_reports():
  task_overview()

  user_overview()
 
# ===========================================================================
# ====== Display statistics ======
def display_statistics():
  
  # if file exits
  try:
    # display the stats in user-friendly
    with open('task_overview.txt', 'r') as task:
      print('\nTASK OVERVIEW STATS:\n')
      for line in task:
        print(line.strip())
    
    with open('user_overview.txt', 'r') as user:
     print('\nUSER OVERVIEW STATS:\n')
     for line in user:
        print(line.strip())

  # if not display this message
  except Exception:
    print("Need to generate report first before display the stats")
 
# ===========================================================================
# ====== Login ======
# create empty list
user = []
pw = []

# open text file 'user.txt'
with open('user.txt', 'r') as f:
  
  # loop though file  
  for line in f:
   # break the text file in tiny piece get the username and password
    username, password = line.split(", ")
    
    # remove the white space end 
    password = password.strip()
    
    # add username to the list called 'user'
    user.append(username)
    # add password to the list called 'pw'
    pw.append(password)

# count i and login
i = 0
login = 0

# print out a title
print("Please login:")
# create a input to login 
username_input = input("Please enter your username\n") 
password_input = input("Please enter your password\n") 


# set while loop to True
while True:
      
  # if useename is in user list and password is in pw list and username is equal to admin
  if username_input in user and password_input in pw and username_input == 'admin':
    login = 1

    # print out this message
    print(" ")
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - genenrate reports
d  - Display statistics
e - Exit
: ''').lower()
    
  # if username is in user list and password is in pw list and username is not equal to admin
  elif username_input in user and password_input in pw and username_input != 'admin':
    # print out this message
    print(" ")
    
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

  # if username is in user list and password is not in pw list 
  elif username_input in user and password_input not in pw:
    # print out this message
    print("Incorrect password")

  # if user input is not in the user list
  else:
    # print out this message
    print("Does this username exits")

  print(" ")

# ===========================================================================
# ====== Menu options ======
   # if the user input is equal to 'r'
  if menu == 'r':
    reg_user(count)


  # if the user input is equal to 'a'
  elif menu == 'a':
    add_task(count)


  # if the user input is equal to 'va'
  elif menu == 'va':
    view_all()


  # if the user input is equal to 'vm'
  elif menu == 'vm':
    view_mine()

  # if the user input is equal to 'gr' 
  elif menu == 'gr':
    generate_reports()

  # if the user input is equal to 'd' 
  elif menu == 'd':
    display_statistics()

# ===========================================================================
# ====== Exit ======  
# if the user input is equal to 'e' 
  elif menu == 'e':
    # print out this message
      print(f"Goodbye!!! {username_input}")
      exit()
  
  # if the user enter empty string
  else:
    # print out this message
      print("You have made a wrong choice, Please Try again")
