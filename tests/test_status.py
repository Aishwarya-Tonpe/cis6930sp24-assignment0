import pytest
from assignment0.main import createdb, connectdb, deletedb, print_status
from assignment0.constants import strings

def test_populatedb():
    sorted_data = print_status()


