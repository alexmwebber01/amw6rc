import pytest
import Staff
import System

def test_create_assignment(grading_system):
    #login as a TA
    grading_system.login('cmhbf5', 'bestTA')
    #create an assignment
    grading_system.usr.create_assignment('assignment3', '2/29/20', 'comp_sci')
    #check that the assignment is in the correct course with correct due date
    assertion = False
    course = grading_system.courses['comp_sci']
    for key in course:
        if course[key] == "assignment3":
            assertion = True
    if assertion == True:
        if course['assignment3']['due_date'] != "2/29/20":
            assertion = False
    return assertion
    #restore data
    grading_system.load_data()


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
