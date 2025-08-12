from project import validateIngredients, validateRestrictions, validateTime
import pytest

def test_validateIngredients():
    assert validateIngredients("")==""
    assert validateIngredients("sauce , tomato ")=="sauce,tomato"

def test_validateTime():
    with pytest.raises(ValueError):
        validateTime(-10)
    with pytest.raises(ValueError):
        validateTime(10)

def test_validateRestrictions():
    with pytest.raises(ValueError):
        validateRestrictions(4)
    with pytest.raises(ValueError):
        validateRestrictions(-4)
    assert validateRestrictions(0)==""
    assert validateRestrictions(1)=="vegetarian"
    assert validateRestrictions(2)=="vegan"
    assert validateRestrictions(3)=="gluten free"

