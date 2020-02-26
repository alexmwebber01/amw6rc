import pytest
import System

def test_change_grade(grading_system):
    #login as a TA
    grading_system.login('cmhbf5', 'bestTA')
    #change grade to 100 for an assignment
    grading_system.usr.change_grade('akend3', 'comp_sci', 'assignment1', 99)
    #check that grade is now 100
    assert grading_system.users['akend3']['courses']['comp_sci']['assignment1']['grade'] == 99
    #restore data
    grading_system.load_data()


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
