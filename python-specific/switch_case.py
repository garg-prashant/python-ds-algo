"""
This module provides a function to map arithmetic operators to their corresponding operation names.
"""


def switch_case_example(operator: str) -> str:
    """
    Maps an arithmetic operator to its corresponding operation name.

    Parameters:
    ----------
    operator : str
        A string representing an arithmetic operator ('+', '-', '*', '/').

    Returns:
    -------
    str
        The name of the operation corresponding to the given operator.

    Raises:
    ------
    ValueError
        If the 'operator' value is not provided.
    """
    if not operator:
        raise ValueError("'operator' value not provided")

    match operator:
        case "+":
            return "addition"
        case "-":
            return "subtraction"
        case "*":
            return "multiplication"
        case "/":
            return "division"
        case _:
            return "not supported"


if __name__ == "__main__":
    print(switch_case_example("+"))
    print(switch_case_example("%"))
