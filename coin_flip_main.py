import math


def bernoulli_equation(total_flips, number_of_successes):
    """
    Equation to find the probability of getting r successes (heads) out of n coin flips.
    """
    if number_of_successes > total_flips:
        return 0
    coef = get_bernoulli_coeffiecient(total_flips, number_of_successes)
    return coef * .5**number_of_successes * .5**(total_flips-number_of_successes) * 100


def get_bernoulli_coeffiecient(total_flips, number_of_successes):
    """
    Helper function to find the coeffiecient for the bernoulli equation.
    """
    return math.factorial(total_flips)/(math.factorial(number_of_successes)*(math.factorial(total_flips-number_of_successes)))


def get_probabilities_in_range(success, total):
    """
    Returns an array of probabilities of successes out of n where n increases to total.
    """
    result_array = []
    for x in range(1, total+1):
        result_array.append(bernoulli_equation(x, success))
    return result_array