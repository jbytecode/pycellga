import pytest
from cga.problems.single_objective.discrete.binary.maxcut20_01 import Maxcut20_01

@pytest.fixture
def maxcut_instance():
    """
    Fixture for creating an instance of the Maxcut20_01 class.

    This fixture returns an instance of the Maxcut20_01 class to be used in tests.
    """
    return Maxcut20_01()

def test_maxcut20_01(maxcut_instance):
    """
    Test the MAXCUT function implementation.

    This test checks the calculation of the MAXCUT function value for a given list of binary variables.
    It uses predefined inputs and compares the outputs to expected values.
    """
    # Define sample input chromosomes (binary lists)
    sample_chromosome1 = [0, 1] * 10  # Example binary sequence
    sample_chromosome2 = [1] * 20  # All ones
    sample_chromosome3 = [0] * 20  # All zeros

    # Calculate the MAXCUT function value for the sample inputs
    fitness_value1 = maxcut_instance.f(sample_chromosome1)
    fitness_value2 = maxcut_instance.f(sample_chromosome2)
    fitness_value3 = maxcut_instance.f(sample_chromosome3)

    # Assertions to check correctness
    assert isinstance(fitness_value1, float)
    assert isinstance(fitness_value2, float)
    assert isinstance(fitness_value3, float)

    assert fitness_value1 > 0
    assert fitness_value2 == 0  # All ones should result in zero cut value
    assert fitness_value3 == 0  # All zeros should result in zero cut value

    # Additional checks with known values
    # Here we assume specific values and their known outputs for more thorough testing
    # You can add more specific test cases if you have known outputs for certain inputs

if __name__ == "__main__":
    pytest.main()
