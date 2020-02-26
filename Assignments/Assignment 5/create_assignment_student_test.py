import pytest
import System

def test_create_assignment(grading_system):
    #login as a student
    grading_system.login('akend3', '123454321')
    #try to create an assignment, should return False since we are a student
    assert grading_system.usr.create_assignment('student_assignment', '1/1/1', 'comp_sci') == False
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
