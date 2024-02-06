import pytest
from assignment0.main import createdb, connectdb, deletedb

def test_connectdb():
    cur, con = connectdb()
    assert cur is not None
    assert con is not None
