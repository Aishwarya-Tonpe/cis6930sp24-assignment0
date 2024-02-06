import pytest
from assignment0.main import createdb, connectdb, deletedb
from assignment0.constants import strings

def test_createdb():
    deletedb()
    (cur, con) = connectdb()
    result = createdb()
    assert result is not None
    assert con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents'").fetchone() is not None