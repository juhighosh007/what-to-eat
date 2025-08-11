from project import validateIngredients, length, validateRestrictions, validateTime
import pytest

def test_validateIngredients():
    assert validateIngredients("")==""
    assert validateIngredients("sauce , tomato ")=="sauce,tomato"

def test_validateTime():
    with pytest.raises(ValueError):
        validateTime(-10)
    with pytest.raises(ValueError):
        validateTime(10)

def test_length():
    assert length("sauce , tomato")==2

def test_validateRestrictions():
    with pytest.raises(ValueError):
        validateRestrictions(4)
    with pytest.raises(ValueError):
        validateRestrictions(-4)
    assert validateRestrictions(0)==""
