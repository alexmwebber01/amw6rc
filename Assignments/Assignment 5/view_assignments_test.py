import pytest
import System

def test_view_assignments(grading_system):
    #login as a student
    grading_system.login('akend3', '123454321')
    #get assignments for this user, for databases course
    assignments = grading_system.usr.view_assignments('databases')
    #check that the assignment and due dates are correct
    assert assignments[0][0] == "assignment1" and assignments[0][1] == "1/6/20"
    assert assignments[1][0] == "assignment2" and assignments[1][1] == "2/6/20"
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
