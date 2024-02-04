import pytest
from main import createdb, connectdb, deletedb

def test_createdb():
    deletedb()
    (cur, con) = connectdb()
    result = createdb()
    assert result is not None
    assert con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents'").fetchone() is not None