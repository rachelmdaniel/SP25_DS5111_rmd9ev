import sys

def test_python_version(): # head's up that this will need to change when you update validations.yml for github actions
    assert sys.version_info[:2] in [(3,10),(3,11),(3,12)], "Python version not 3.10 or 3.11"

if __name__ == "__main__":  # This is interesting, are you running your tests with python?  the common idiom is to just run `pytest <target dir or files>` so you don't need that...
    pytest.main()
