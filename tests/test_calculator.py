import pytest 
from src.calculator import add,substract,multiply,divide


#create test case
def test_add():
    assert add(2, 3) == 5
    

def test_substract():
    assert substract(4, 3) == 1
    
def test_multiply():
    assert multiply(3, 3) == 9
    
def test_divide():
    assert divide(4, 2) == 2
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
         
    