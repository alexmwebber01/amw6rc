import pytest
import System

def test_add_student(grading_system):
    #login as a professor
    grading_system.login('goggins', 'augurrox')
    #add a student to a course
    grading_system.usr.add_student('akend3', 'cloud_computing')
    #check that there is a course called 'cloud_computing' for the student
    courses = grading_system.users['akend3']['courses']
    assertion = False
    for key in courses:
        if courses[key] == "cloud_computing":
            assertion = True
    assert assertion
    #restore data
    grading_system.load_data()
    
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
