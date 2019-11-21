import math
import numpy as np
from fdom_2d_common import * 

def mean_point(points):
    return (np.mean([p[0][0] for p in points]), np.mean([p[0][1] for p in points]))

def nelder_mead_method(function, simplex, epsilon):
    ALPHA = 1
    BETA = 2.9
    GAMMA = 0.5
    n = 2 #Dimensions

    if epsilon <= 0:
        return None

    k = 0
    PERIOD = 30

    x = []
    for point in simplex:
        x.append((point, function(point)))
    x = sorted(x, key = lambda p: p[1])

    while True: 
        m = mean_point(x[:n])
        x_k = manipulate_points(m, manipulate_points(m, x[n][0], mult2 = -1), mult2 = ALPHA)
        fx_k = function(x_k)
        
        #Reflection.
        if fx_k >= x[0][1] and fx_k <= x[n-1][1]:
            x[n] = (x_k, fx_k)
            x = sorted(x, key = lambda p: p[1])

        #Expansion.
        elif fx_k <= x[0][1]:
            x_p = manipulate_points(m, manipulate_points(x_k, m, mult2 = -1), mult2 = BETA)
            fx_p = function(x_p)
            if fx_p < fx_k:
                x[n] = (x_p, fx_p)
            else:
                x[n] = (x_k, fx_k)
            x = sorted(x, key = lambda p: p[1])

        #Compression.
        elif fx_k > x[n-1][1]:
            if fx_k >= x[n][1]:
                x_m = manipulate_points(m, manipulate_points(x[n][0], m, mult2 = -1), mult2 = GAMMA)
            else:
                x_m = manipulate_points(m, manipulate_points(x_k, m, mult2 = -1), mult2 = GAMMA)
            
            fx_m = function(x_m)
            if fx_m < min([fx_k, x[n][1]]):
                x[n] = (x_m, fx_m)
                x = sorted(x, key = lambda p: p[1])
         
            stop = math.sqrt(sum([(x[i][1] - fx_m) ** 2 for i in range(n + 1)]) / (n + 1) )
            if stop <= epsilon:
                print("Criteria is {}, stop on iter #{}".format(stop, k))
                return x[0][0]

        if k % PERIOD == 0:
            center = x[0][0]
            end = x[n][0]
            l = length(center, end)
            r = l * (math.sqrt(n + 1) - 1 + n) / (math.sqrt(2) * n)
            s = l * (math.sqrt(n + 1) - 1) / (math.sqrt(2) * n)

            affines = [(0,0), (r, s), (s, r)]
            for i in range(0, n+1):
                x_i_s = manipulate_points(x[i][0], affines[i])
                x[i] = (x_i_s, function(x_i_s))

        k += 1

def solve_rosenbrock(error):
    rosenbrock_simplex =  [(0.05, 0.00), (2, 1), (1, 2)]
    result = nelder_mead_method(function = rosenbrock_func, simplex = rosenbrock_simplex,
                                     epsilon = error)
    print("Res: {}; f(result): {}".format(result, rosenbrock_func(result)))
    print("Min: {}\n".format(ROSENBROCK_MIN))

    return 0

def solve_himmelblau(error):
    himmelblau_simplexes = [ [(0, 0), (2, 0), (1, 2)],
                             [(-3, 3.5), (-4, 5), (-5, 3.5)],
                             [(-6, -3), (-4, -6), (-4, -5)],
                             [(2, -4), (4, -4), (5, -2)]]

    for i, s in enumerate(himmelblau_simplexes):
        result = nelder_mead_method(function = himmelblau_func, simplex = s,
                                     epsilon = error)
        print("Res: {}; f(result): {}".format(result, himmelblau_func(result)))
        print("Min: {}\n".format(HIMMELBLAU_MINS[i]))

    return 0


def main():
    error = 0.0001

    solve_rosenbrock(error)
    solve_himmelblau(error)
    
if __name__ == "__main__":
    main()
