import pytest
from eva_data_analysis import text_to_duration


def test_text_to_duration_integer():
   assert text_to_duration("10:00") == 10 

def test_text_to_duration_float():
    """
    Test that text_to_duration function with a float returns expected result.
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.3333333
    assert actual_result == pytest.approx(expected_result)

test_text_to_duration_float()
test_text_to_duration_integer()