import pytest
from assignment0.main import createdb, connectdb, deletedb, print_status

def test_print_status(capfd):
    print_status()
    captured = capfd.readouterr()
    # Add assertions based on your specific requirements
