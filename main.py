from options import Options
from functions import getStudentsList, getASpecificStudentInformation, changeStudentName, changeStudentAge, deleteStudent, saveANewStudent, exitFunc
from utils import getInt, getStudentsFullUrl


HOST_ADDRESS = input('Enter the host address: ')
PORT = getInt('Enter the port number: ')
STUDENT_API = 'students'
STUDENTS_FULL_URL = getStudentsFullUrl(HOST_ADDRESS, PORT, STUDENT_API)


def printMenu():
    print()
    print('What do you want to do?')
    for option in Options:
        print(f'{option.value}. {option.name.replace("_", " ").capitalize()}')
    choice = getInt('Enter your choice: ')
    if choice == 1:
        getStudentsList(STUDENTS_FULL_URL)
    elif choice == 2:
        getASpecificStudentInformation(STUDENTS_FULL_URL)
    elif choice == 3:
        saveANewStudent(STUDENTS_FULL_URL)
    elif choice == 4:
        changeStudentName(STUDENTS_FULL_URL)
    elif choice == 5:
        changeStudentAge(STUDENTS_FULL_URL)
    elif choice == 6:
        deleteStudent(STUDENTS_FULL_URL)
    elif choice == 7:
        exitFunc()
    else:
        print('\nInvalid choice. Please try again.\n')

while True:
    printMenu()
