
def celsius_to_fahrenheit(temp_c: float) -> float:
    """
    Converts teperature from Celsius to Fahrenheit

    Parameters
    ----------
    temp_c: Celsius Temperature as a floating point number

    Returns
    -------
    Temperature in Fahrenheit as a floating point number
    """

    conversion_factor = (9/5) 
    offset = 32 # Offset as 0 degrees C is 32 degrees F

    temp_f = (temp_c * conversion_factor) + offset

    return temp_f


def test_celsius_to_fahrenheit():
    """
    Tests the celsius to fahrenheit function. 
    """
    assert celsius_to_fahrenheit(0) == 32.0 # Freezing for water
    assert celsius_to_fahrenheit(100) == 212.0 # Boiling for water


if __name__=="__main__":
    test_celsius_to_fahrenheit()