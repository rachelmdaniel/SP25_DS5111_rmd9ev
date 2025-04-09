import sys

def test_python_version():
    assert sys.version_info[:2] in [(3,12),(3,13)], "Python version not 3.12 or 3.13"

if __name__ == "__main__":
    pytest.main()
