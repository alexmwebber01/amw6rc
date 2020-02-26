import pytest
import System

def test_check_grades(grading_system):
    #login as a student
    grading_system.login('akend3', '123454321')
    #get grades for a course that this user is not in
    #this should return False
    assert grading_system.usr.check_grades('cloud_computing') == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
