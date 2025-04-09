import sys

def test_python_version():
    assert sys.version_info[:2] in [(3,10),(3,11),(3,12)], "Python version not 3.10 or 3.11"

if __name__ == "__main__":
    pytest.main()
