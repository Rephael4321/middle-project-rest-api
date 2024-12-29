from enum import Enum, auto

class Options(Enum):
    GET_STUDENTS_LIST = auto()
    GET_A_SPECIFIC_STUDENT_INFORMATION = auto()
    SAVE_A_NEW_STUDENT = auto()
    CHANGE_STUDENT_NAME = auto()
    CHANGE_STUDENT_AGE = auto()
    DELETE_STUDENT = auto()
    EXIT = auto()
