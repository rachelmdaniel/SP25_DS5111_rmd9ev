import sys

def test_OS_linux():
    assert sys.platform.startswith("linux"), "OS is not linux"

if __name__ == "__main__":
    pytest.main()
