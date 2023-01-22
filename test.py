import pytest
import k8s as cs
import crud_pb2 as cr

def test_run_delete():
    argv = ["k9s.py", "delete", "0"]
    result = cs.run_delete(argv)
    assert result == 0

def test_run_read():
    argv = ["k9s.py", "read", "1"]
    result = cs.run_read(argv)
    assert result == 0

def test_run_update():
    argv = ["k9s.py", "update", "1", "testConfig.txt"]
    result = cs.run_update(argv)
    assert result == 0

if __name__ == '__main__':
    pytest.main()