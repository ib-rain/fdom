import math

ROSENBROCK_MIN = (1.0, 1.0)

def rosenbrock_func(point):
    (x, y) = point
    return (1 - x) ** 2 +  100 * (y - x ** 2) ** 2

HIMMELBLAU_MINS = [(3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848126)]

def himmelblau_func(point):
    (x, y) = point
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

def manipulate_points(p1, p2, mult1 = 1, mult2 = 1):
    return (mult1 * p1[0] + mult2 * p2[0], mult1 * p1[1] + mult2 *  p2[1])

def length(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

DEFAULT_H = 0.0000000001

#Numerical differential number 5.
def gradient1(f, point, h = DEFAULT_H):
    (x, y) = point
    return ((f((x+3*h,y))-6*f((x+2*h, y))+18*f((x+h, y))-10*f((x, y))-3*f((x-h,y))) / (12 * h),
        (f((x, y+3*h))-6*f((x, y+2*h))+18*f((x, y+h))-10*f((x, y))-3*f((x,y-h))) / (12 * h))

def golden_section_search(function, a, b, epsilon):
    if epsilon <= 0:
        return None

    if (a > b):
        extra = a
        a = b
        b = extra

    delta = []

    #Step 2
    delta.insert(0, b - a)
    delta.insert(1, delta[0] * (math.sqrt(5) - 1) / 2)
    delta.insert(2, delta[0] - delta[1])

    k = 1

    #Notation: S_k is k-th S, S_k1 is (k-1)-th S.
    (a_k1, b_k1) = (a, b)

    x_k1 = a + delta[2]
    y_k1 = b - delta[2]

    f_x_k1 = f_x_k = function(x_k1)
    f_y_k1 = f_y_k = function(y_k1)

    while True:

        #Step 3
        delta.insert(k+2, delta[k] - delta[k+1])

        if f_x_k1 <= f_y_k1:
            a_k = a_k1
            b_k = y_k1
            y_k = x_k1
            x_k = a_k + delta[k+1]
            f_y_k = f_x_k1
            if x_k < y_k:
                f_x_k = function(x_k)
        #The only possibility left is f_x_k1 > f_y_k1
        else:
            a_k = x_k1
            b_k = b_k1
            x_k = y_k1
            y_k = b_k - delta[k+1]
            f_x_k = f_y_k1
            if x_k < y_k:
                f_y_k = function(y_k)

        #Step 4
        if delta[k] <= epsilon:
            return (x_k + y_k) / 2

        k = k + 1

        #Reassignment after incrementing k according to notation.
        a_k1 = a_k
        b_k1 = b_k
        x_k1 = x_k
        y_k1 = y_k
        f_x_k1 = f_x_k
        f_y_k1 = f_y_k

#https://www.youtube.com/watch?v=V3RJGWaYqxQ
def new_func(func, point0, point1, sign):
    if sign:
        def F(step):
            return func((point0[0] + step * point1[0], point0[1] + step * point1[1]))
    else:
        def F(step):
            return func((point0[0] - step * point1[0], point0[1] - step * point1[1]))
    return F

def find_min(func, point0, point1, epsilon, sign = False):
    step_func = new_func(func, point0, point1, sign)
    LEFT = 0
    RIGHT = 100
    step = golden_section_search(step_func, LEFT, RIGHT, epsilon)

    return step

def solve_rosenbrock(method, error):
    result = method(function = rosenbrock_func, x = (-0.0, -10.0000001),
                                     epsilon = error)
    print("Res: {}; f(result): {}".format(result, rosenbrock_func(result)))
    print("Min: {}\n".format(ROSENBROCK_MIN))

    return 0

def solve_himmelblau(method, error):
    himmelblau_points = [(3, 3), (-4, 5), (-3.5, -3.5), (-3, 3)]

    # HIMMELBLAU_MINS = [(3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848126)]

    for i, point in enumerate(himmelblau_points):
        result = method(function = himmelblau_func, x = point,
                                     epsilon = error)
        print("Res: {}; f(result): {}".format(result, himmelblau_func(result)))
        print("Min: {}\n".format(HIMMELBLAU_MINS[i]))

    return 0