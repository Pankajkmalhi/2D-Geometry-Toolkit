import matplotlib.pyplot as plt
import numpy as np
import time
from memory_profiler import memory_usage
def intersect_ccw(line1, line2):
    A, B = line1
    C, D = line2
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def slope(A, B):
    return (B[1] - A[1]) / (B[0] - A[0]) if B[0] - A[0] != 0 else float('inf')
def y_intercept(A, slope):
    return A[1] - slope * A[0]
def intersect_slope(line1, line2):
    A, B = line1
    C, D = line2
    slope1 = slope(A, B)
    slope2 = slope(C, D)

    if slope1 == slope2:
        return False

    intercept1 = y_intercept(A, slope1)
    intercept2 = y_intercept(C, slope2)

    x_intersect = (intercept2 - intercept1) / (slope1 - slope2)
    #y_intersect = slope1 * x_intersect + intercept1

    return (min(A[0], B[0]) <= x_intersect <= max(A[0], B[0]) and
            min(C[0], D[0]) <= x_intersect <= max(C[0], D[0]))

def plot_lines(line1, line2, intersect):
    plt.figure()
    plt.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], 'b-o', label='Line 1')
    plt.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], 'r-o', label='Line 2')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Intersection: ' + ('Yes' if intersect else 'No'))
    plt.legend()
    plt.show()

def vector_cross_product(A, B):
    return A[0] * B[1] - A[1] * B[0]

def subtract_vectors(A, B):
    return (A[0] - B[0], A[1] - B[1])

def intersect_vector(line1, line2):
    A, B = line1
    C, D = line2

    AB = subtract_vectors(B, A)
    AC = subtract_vectors(C, A)
    AD = subtract_vectors(D, A)
    CA = subtract_vectors(A, C)
    CB = subtract_vectors(B, C)
    CD = subtract_vectors(D, C)

    return vector_cross_product(AB, AC) * vector_cross_product(AB, AD) < 0 and \
           vector_cross_product(CD, CA) * vector_cross_product(CD, CB) < 0

def main():

        print("Enter the coordinates for the first line segment (x1 y1 x2 y2): ")
        x1, y1, x2, y2 = map(float, input().split())
        line1 = ((x1, y1), (x2, y2))

        print("Enter the coordinates for the second line segment (x3 y3 x4 y4): ")
        x3, y3, x4, y4 = map(float, input().split())
        line2 = ((x3, y3), (x4, y4))

        method = input("Choose the method (CCW, Slope, or Vector): ").lower()
        if method == 'ccw':
            intersect = intersect_ccw(line1, line2)
        elif method == 'slope':
            intersect = intersect_slope(line1, line2)
        elif method == 'vector':
            intersect = intersect_vector(line1, line2)
        else:
            print("Invalid method. Please choose 'CCW', 'Slope', or 'Vector'.")
            return

        plot_lines(line1, line2, intersect)
        print("The lines intersect." if intersect else "The lines do not intersect.")
if __name__ == "__main__":
    main()
