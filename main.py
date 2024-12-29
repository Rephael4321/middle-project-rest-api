from options import Options
from functions import getStudentsList, getASpecificStudentInformation, changeStudentName, changeStudentAge, deleteStudent, saveANewStudent, exitFunc
from utils import getInt, getStudentsFullUrl, choiceIs


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

    if choiceIs(choice, 'GET_STUDENTS_LIST'):
        getStudentsList(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'GET_A_SPECIFIC_STUDENT_INFORMATION'):
        getASpecificStudentInformation(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'SAVE_A_NEW_STUDENT'):
        saveANewStudent(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'CHANGE_STUDENT_NAME'):
        changeStudentName(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'CHANGE_STUDENT_AGE'):
        changeStudentAge(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'DELETE_STUDENT'):
        deleteStudent(STUDENTS_FULL_URL)

    elif choiceIs(choice, 'EXIT'):
        exitFunc()

    else:
        print('\nInvalid choice. Please try again.\n')

while True:
    printMenu()
