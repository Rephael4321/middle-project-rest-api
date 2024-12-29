import requests
from utils import getInt, getStudentSpecificUrl

# Core functions
def getStudentsList(student_full_url: str) -> None:
    studentsData = fetchStudentsData(student_full_url)
    print('--- Students List ---')
    for student in studentsData:
        printStudentInformation(student)


def getASpecificStudentInformation(student_full_url: str) -> None:
    student_id = getInt('Enter the student ID: ')
    student_specific_url = getStudentSpecificUrl(student_full_url, student_id)
    students_data = fetchSpecificStudent(student_specific_url)
    if students_data:
        print('--- Student Information ---')
        printStudentInformation(students_data)


def saveANewStudent(student_full_url: str) -> None:
    student_name = input('Enter student name: ')
    student_age = getInt('Enter student age: ')
    student_obj = {'name': student_name, 'age': student_age}
    response = requests.post(student_full_url, json=student_obj)
    if response.status_code == 201:
        print('Student created successfully:')
        student_data = response.json()
        printStudentInformation(student_data)
        return
    elif response.status_code == 400:
        print(f'Error: {response.json()["error"]}')
    else:
        print('Error: can\'t create student')
    print(f'Error code: {response.status_code}')


def changeStudentName(student_full_url: str) -> None:
    changeStudentData(student_full_url, 'name')


def changeStudentAge(student_specific_url: str) -> None:
    changeStudentData(student_specific_url, 'age')


def deleteStudent(student_full_url: str) -> None:
    student_id = getInt('Enter the student ID: ')
    student_specific_url = getStudentSpecificUrl(student_full_url, student_id)
    response = requests.delete(student_specific_url)
    if response.status_code == 200:
        print('Student deleted successfully')
    else:
        print('Error: can\'t delete student')
        print(f'Error code: {response.status_code}')


def exitFunc():
    exit(0)


# Helper functions
def fetchStudentsData(student_full_url: str) -> list:
    response = requests.get(student_full_url)
    if response.status_code == 200:
        return response.json()['students']
    else:
        print('Error: can\'t fetch students data')
        print(f'Error code: {response.status_code}')
        return []


def fetchSpecificStudent(student_specific_url: str) -> dict:
    response = requests.get(student_specific_url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f'Error: {response.json()["error"]}')
    else:
        print('Error: can\'t fetch student data')
    print(f'Error code: {response.status_code}')
    return {}


def printStudentInformation(student: dict) -> None:
    print(f'ID: {student['id']}')
    print(f'Name: {student['name']}')
    print(f'Age: {student['age']}')
    print('-' * 20)


def changeStudentData(student_full_url: str, key: str) -> None:
    student_id = getInt('Enter the student ID: ')
    if key == 'age':
        value = getInt('Enter the new age: ')
    else:
        value = input(f'Enter the new {key}: ')
    student_specific_url = getStudentSpecificUrl(student_full_url, student_id)
    student_data = fetchSpecificStudent(student_specific_url)
    if student_data:
        student_data[key] = value
        response = requests.put(student_specific_url, json=student_data)
        if response.status_code == 200:
            print(f'Student {key} updated successfully')
            return
        elif response.status_code == 400:
            print(f'Error: {response.json()["error"]}')
        else:
            print(f'Error: can\'t update student {key}')
        print(f'Error code: {response.status_code}')
