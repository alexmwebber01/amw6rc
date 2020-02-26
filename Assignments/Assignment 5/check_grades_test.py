import pytest
import System

def test_check_grades(grading_system):
    #login as a student
    grading_system.login('akend3', '123454321')
    #get grades for this user, for comp_sci course
    grades = grading_system.usr.check_grades('comp_sci')
    #check that the grades are correct for the assignments in comp_sci course
    assert grades[0][0] == "assignment1" and grades[0][1] == 99
    assert grades[1][0] == "assignment2" and grades[1][1] == 66

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
