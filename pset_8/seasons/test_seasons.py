from pset_8.seasons.seasons import convert_time_in_words
import pytest


def test_one_year_ago():
    convert_time_in_words(
        "2023-02-10"
    ) == "Five hundred twenty-five thousand, six hundred minutes"


def test_two_years_ago():
    convert_time_in_words(
        "2022-02-10"
    ) == "One million, fifty-one thousand, two hundred minutes"


def test_different_format():
    """This function tests format for day rather then having 02, we test 2"""
    convert_time_in_words(
        "2023-2-10"
    ) == "Five hundred twenty-five thousand, six hundred minutes"
    convert_time_in_words(
        "2022-2-10"
    ) == "One million, fifty-one thousand, two hundred minutes"


def test_wrong_format():
    with pytest.raises(SystemExit) as sample:
        convert_time_in_words("2014, 1 January") == sys.exit("Invalid date")
    assert sample.type == SystemExit
