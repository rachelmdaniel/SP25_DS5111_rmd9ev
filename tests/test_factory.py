import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from bin.gainers.factory import GainerFactory
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

def test_factory_initialization():
    """
    Test that GainerFactory initializes correctly with valid choices.
    """

    factory_yahoo = GainerFactory("yahoo")
    assert factory_yahoo.choice == "yahoo"

    factory_wsj = GainerFactory("wsj")
    assert factory_wsj.choice == "wsj"

def test_factory_invalid_choice():
    """
    Test that GainerFactory raises an assertion error for invalid choice.
    """

    with pytest.raises(AssertionError, match="Unrecognized gainer type"):
        GainerFactory("invalid_source")

def test_get_downloader():
    """
    Test that the correct downloader is returned based on choice.
    """

    factory_yahoo = GainerFactory("yahoo")
    assert isinstance(factory_yahoo.get_downloader(), GainerDownloadYahoo)

    factory_wsj = GainerFactory("wsj")
    assert isinstance(factory_wsj.get_downloader(), GainerDownloadWSJ)

def test_get_processor():
    """
    Test that the correct processor is returned based on choice.
    """

    factory_yahoo = GainerFactory("yahoo")
    assert isinstance(factory_yahoo.get_processor(), GainerProcessYahoo)

    factory_wsj = GainerFactory("wsj")
    assert isinstance(factory_wsj.get_processor(), GainerProcessWSJ)


