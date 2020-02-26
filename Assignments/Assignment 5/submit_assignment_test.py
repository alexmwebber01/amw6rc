import pytest
import System

def test_submit_assignment(grading_system):
    #login as a studnet
    grading_system.login('hdjsr7', 'pass1234')
    #submit an assignment
    grading_system.usr.submit_assignment('databases', 'assignment1', 'test', '04/20/20')
    #test
    courses = grading_system.users['hdjsr7']['courses']
    assert courses['databases']['assignment1']['submission'] == "test"
    assert courses['databases']['assignment1']['submission_date'] == "04/20/20"
    #make sure it is submitted ontime, this assignment was late, so it should be false
    assert courses['databases']['assignment1']['ontime'] == False
    #restore data
    grading_system.load_data()
    
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
