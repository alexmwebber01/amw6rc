import pytest
import System

def test_view_assignments(grading_system):
    #login as a student
    grading_system.login('akend3', '123454321')
    #get assignments for this user from a course which they are not in
    #this should return False
    assert grading_system.usr.view_assignments('cloud_computing') == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
