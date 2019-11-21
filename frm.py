from fdom_2d_common import *

#conjugate gradient method
def fletcher_reeves_method(function, x, epsilon):
    if epsilon <= 0:
        return None

    k = 0
    x_k = x
    beta_k = 1
    g_k = manipulate_points(gradient1(function, x_k), (0,0), mult1 = -1)

    while True:
        grad_f_xk = gradient1(function, x)
        if grad_f_xk == (0, 0):
            return x_k

        alpha_k = find_min(function, x_k, g_k, epsilon, sign = True)

        x_k1 = manipulate_points(x_k, g_k, mult2 = alpha_k)

        grad_f_xk1 = gradient1(function, x_k1)
        g_k = manipulate_points(grad_f_xk1, g_k, mult1 = -1, mult2 = beta_k)

        if max([length(x_k1, x_k), abs(function(x_k1)-function(x_k)), length(grad_f_xk1, (0,0))]) <= epsilon:
            print("Stopping on iteration #{}".format(k))
            return x_k1

        beta_k = length(grad_f_xk1, (0,0)) ** 2 / length(grad_f_xk, (0,0)) ** 2

        k += 1
        x_k = x_k1

def main():
    error = 0.00001
    solve_rosenbrock(fletcher_reeves_method, error)  
    solve_himmelblau(fletcher_reeves_method, error)  

if __name__ == "__main__":
    main()
