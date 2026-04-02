from datetime import datetime
import re

def validate_task_title(title):
    title = input('title:')
    pattern1 = r'^\w{0,12}$'
    if re.fullmatch(pattern1,title):
        return True
    else:
        print('Invalid, Kindly check above')
    
    
def validate_task_description(description):
    description  = input('description:')
    pattern2 = r'^\w{0,12}$'
    if re.fullmatch(pattern2,description):
        return True
    else:
        print('Invalid, Kindly check above')


def validate_due_date(due_date):
    due_date = input('due_date:')
    try:
        datetime.strptime(due_date,'%Y/%m/%d')
    except ValueError:
        print('please enter correct format (YYYY/MM/DD)')
