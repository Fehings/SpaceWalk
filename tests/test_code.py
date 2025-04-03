import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size


def test_text_to_duration_integer():
   assert text_to_duration("10:00") == 10 

def test_text_to_duration_float():
    """
    Test that text_to_duration function with a float returns expected result.
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.3333333
    assert actual_result == pytest.approx(expected_result)

def test_calculate_crew_size():
    """
    Test case for the calculate_crew_size function.
    """
    
    crew = 'bob jones;'
    actual_result = calculate_crew_size(crew)
    expected_result = 1
    assert actual_result == expected_result


def test_calculate_crew_size_edge_cases():
    """
    Test case for the calculate_crew_size function.
    """
    
    crew = ""
    actual_result = calculate_crew_size(crew)
    expected_result = None
    assert actual_result == expected_result


test_text_to_duration_float()
test_text_to_duration_integer()