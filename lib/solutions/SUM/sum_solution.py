# noinspection PyShadowingBuiltins,PyUnusedLocal

def compute(x, y):
    """Compute sum of passed in arguments

    :param x: Integer (operand 1)
    :param y: Integer (operand 2)

    :rtype: Integer
    """
    if x > 100 or x < 0 or y > 100 or y < 0:
        raise ValueError("Passed in value out of bounds")

    return x + y

