import pytest
from main import connectdb

def test_connectdb():
    cur, con = connectdb()
    assert cur is not None
    assert con is not None
    # Add more assertions if needed
