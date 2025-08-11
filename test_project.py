from project import validateBudget, validateIngredients, validateMood, validateRestrictions, validateTime
import pytest

def test_validateBudget():
    with pytest.raises(ValueError):
        validateBudget("Very high")

def test_validateMood():
    with pytest.raises(ValueError):
        validateMood("sad")

def test_validateIngredients():
    assert validateIngredients("")==[]
    assert validateIngredients("sauce , tomato")==["sauce","tomato"]

def test_validateTime():
    with pytest.raises(ValueError):
        validateTime(0)
    with pytest.raises(ValueError):
        validateTime(-10)

def test_validateRestrictions():
    with pytest.raises(ValueError):
        validateRestrictions(6)
    with pytest.raises(ValueError):
        validateRestrictions(-6)
