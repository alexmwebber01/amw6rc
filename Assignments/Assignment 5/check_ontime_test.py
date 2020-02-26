import pytest
import System

def test_check_ontime(grading_system):
    #login as a student
    grading_system.login('yted91', 'imoutofpasswordnames')
    #check if assignments are ontime
    #check_ontime function takes submission_date and due_date as inputs
    #so I will just enter some test values
    #this is submitted on time, should return True
    assert grading_system.usr.check_ontime('2/1/20', '2/2/20') == True
    #this is submitted late, should return False
    assert grading_system.usr.check_ontime('2/2/20', '2/1/20') == False  


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
