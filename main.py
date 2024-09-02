def mean_square_error(observed_values, expected_values) -> float:
    """
    Calculates the mean square error between observed and expected values.

    Args:
    observed_values(list of int or float): list of observed values.
    expected_values(list of int or float): list of expected values.

    Return:
    float: mean square error.
    """
    squared_diff = []
    #for loop to store squared difference between each corresponding element of two lists
    for observed, expected in zip(observed_values, expected_values):
        squared_diff.append((abs(expected - observed))**2)

    #returns the mean square error
    return sum(squared_diff) / len(observed_values)
    

def main():
    print(mean_square_error([12, 12.4, 13.0], [14.0, 15.64, 15]))

if __name__=="__main__":
    main()