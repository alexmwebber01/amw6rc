import pytest
import System

def test_submit_assignment(grading_system):
    #login as a studnet
    grading_system.login('hdjsr7', 'pass1234')
    #submit an assignment for a course that doesn't exist, this should return False
    assert grading_system.usr.submit_assignment('fake_course', 'assignment1', 'test', '02/20/20') == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
