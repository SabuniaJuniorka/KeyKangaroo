import pytest
import source.my_functions as my_functions

def test_generate_password():
    result = my_functions.generate_password(12)
    assert len(result) == 12