import pytest
import source.my_functions as my_functions

def test_generate_password():
    password = my_functions.generate_password(17)
    assert (len(password) >= 12 and len(password) <= 32)