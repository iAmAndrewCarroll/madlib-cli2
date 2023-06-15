import pytest
from madlib.py import crawl_blank, template_parsed, fulfill_template


def test_read_template_returns_stripped_string():
    actual = crawl_blank("madlib_cli/madlib_template.txt")
    expected = "Don't even brush your {noun} with a {adjective} {noun} brush."
    assert actual == expected


@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = template_parsed(
        "Don't even brush your {noun} with a {adjective} {noun} brush.."
    )
    expected_stripped = "Don't even brush your {} with a {} {} brush."
    expected_parts = ("noun", "adjective", "noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = fulfill_template("Don't even brush your {} with a {} {} brush.", ("teeth", "wet", "tooth"))
    expected = "Don't even brush your teeth with a wet tooth brush."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        crawl_blank(path)
