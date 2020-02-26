import pytest
import System

def test_drop_student(grading_system):
    #login as a professor
    grading_system.login('goggins', 'augurrox')
    #drop student 'akend3' from course 'comp_sci'
    grading_system.usr.drop_student('akend3', 'comp_sci')

    #check that the course is not listed for that student
    assertion = True
    courses = grading_system.users['akend3']['courses']
    for key in courses:
        if courses[key] == "comp_sci":
            assertion = False
    assert assertion
    #restore data
    grading_system.load_data()
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
