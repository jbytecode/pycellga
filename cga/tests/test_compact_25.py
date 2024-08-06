from cga.neighborhoods.compact_25 import Compact25

def test_compact_25():
    """
    Test the Compact25 class for calculating neighbor positions in a grid.

    This test verifies that the Compact25 class correctly calculates the positions
    of the 24 neighbors surrounding a given position in a grid. It ensures that:
    1. The number of neighbors is always 24 for positions not on the boundary of the grid.
    2. Positions on the boundary of the grid still correctly return 24 neighbors.

    The test uses three different positions within the grid to validate the functionality
    of the Compact25 neighborhood calculation.

    Notes
    -----
    The Compact25 neighborhood considers all 24 surrounding cells in a 5x5 grid centered
    on a given position, excluding the cell itself. The grid is assumed to be toroidal,
    meaning that positions on the edges wrap around to the opposite edge.

    The following assertions are made:
    - The number of calculated neighbor positions is 24 for various positions in the grid.

    Raises
    ------
    AssertionError
        If the number of calculated neighbor positions is not 24.
    """
    n_rows = 5
    n_cols = 5

    # Test for a central position in the grid
    position = (3, 3)
    the_neighbors_positions = Compact25(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24, "The number of neighbors for a central position is not 24."

    # Test for a position near the bottom-left corner of the grid
    position = (5, 1)
    the_neighbors_positions = Compact25(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24, "The number of neighbors for a bottom-left corner position is not 24."

    # Test for a position near the top-center of the grid
    position = (1, 3)
    the_neighbors_positions = Compact25(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24, "The number of neighbors for a top-center position is not 24."
