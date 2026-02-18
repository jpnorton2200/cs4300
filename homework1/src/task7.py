import numpy as np

def vector_dot(a: list[float], b: list[float]) -> float:
    """
    Compute the dot product of two vectors using numpy.
    """
    va = np.array(a, dtype=float)
    vb = np.array(b, dtype=float)

    if va.shape != vb.shape:
        raise ValueError("Vectors must be the same length")

    return float(np.dot(va, vb))
