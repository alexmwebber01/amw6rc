import pytest
import System

def test_add_student(grading_system):
    #login as a professor
    grading_system.login('saab', 'boomr345')
    #Try to add a student to Cloud Computing
    #This should return false since Saab is the professor of Comp_Sci,
    #not Cloud Computing
    assert grading_system.usr.add_student('akend3', 'cloud_computing') == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
