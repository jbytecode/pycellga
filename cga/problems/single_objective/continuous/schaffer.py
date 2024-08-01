from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

class Schaffer(AbstractProblem):
    """
    Modified Schaffer function #1 function implementation for optimization problems.

    The Modified Schaffer function #1  is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(X: list) -> float
        Calculates the Modified Schaffer function #1 value for a given list of variables.

    Notes
    -----
    -100 ≤ xi ≤ 100 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, X: list) -> float:
        """
        Calculate the Modified Schaffer function #1 value for a given list of variables.

        Parameters
        ----------
        X : list
            A list of float variables.

        Returns
        -------
        float
            The Modified Schaffer function #1 value.
        """
        fitness = 0.0
        for i in range(len(X) - 1):
            fitness += (0.5 + ((pw(np.sin(pw(X[i], 2) + pw(X[i + 1], 2)), 2) - 0.5) /
                               pw((1 + 0.001 * (pw(X[i], 2) + pw(X[i + 1], 2))), 2)))
        return round(fitness, 3)
