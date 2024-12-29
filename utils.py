from options import Options


def choiceIs(choice: int, option: str) -> bool:
    return choice == Options[option].value


def getInt(msg: str) -> int:
    value = input(msg)
    while not value.isnumeric():
        value = input('Please enter a valid number: ')
    return int(value)


def getStudentsFullUrl(host_address: str, port: int, student_api: str) -> str:
    return host_address + str(port) + '/' + student_api


def getStudentSpecificUrl(student_full_url: str, student_id: int) -> str:
    return student_full_url + '/' + str(student_id)
