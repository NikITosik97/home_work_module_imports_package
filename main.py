from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from colorama import Fore, Back, Style

if __name__ == '__main__':
    print(Fore.GREEN)
    print(date.today())