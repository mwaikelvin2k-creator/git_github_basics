from datetime import datetime
import re
# Import validation functions
import validation
from validation import validate_due_date as dd
from validation import validate_task_description as td
from validation import validate_task_title as tt





# Define tasks list
tasks = [
 {"title": "Stationery",
 "description": "Buy stationery", 
 "due_date": "2026-06-29",
 "completed": True
 },
 {"title": "Shopping",
 "description": "Shop at Market for food", 
 "due_date": "2026-06-30",
 "completed": False
 },
 {}
]


# Implement add_task function
def add_task(title,description,due_date):
    title = tt(title)
    description = td(description)
    due_date = dd(due_date)
    
    if title == True:
        print('Title added successfully!')
    
    if description == True:
        print('Description added successfully!')
    
    try:
        datetime.strptime(due_date, '%Y/%m/%d')
    except:
        print('please enter correct format (YYYY/MM/DD)')

    
    
    
# Implement mark_task_as_complete function
def mark_task_as_complete(tasks):
    for task in tasks:
        for key, value in task.items():
            if key == 'completed':
                if value == True:
                    print('Task marked as complete!')
                else:
                    print('Task marked as incomplete!')
            
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks):
    for task in tasks:
        for key, value in task.items():
            if key == 'completed':
                if value == False:
                    print('Task marked as incomplete!')
                else:
                    print('Task marked as completed!')
        
    

# Implement calculate_progress function
def calculate_progress(tasks):
    print('progress is ' ,tasks)

