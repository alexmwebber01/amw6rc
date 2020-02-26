import pytest
import System

def test_check_password(grading_system):
    #try a bunch of valid passwords
    assert grading_system.check_password('akend3', '123454321')
    assert grading_system.check_password('hdjsr7', 'pass1234')
    assert grading_system.check_password('yted91', 'imoutofpasswordnames')
    assert grading_system.check_password('calyam', '#yeet')
    assert grading_system.check_password('cmhbf5', 'bestTA')
                                         

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
