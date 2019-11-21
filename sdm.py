from fdom_2d_common import * 

#gradient method
def steepest_descent_method(function, x, epsilon):
    if epsilon <= 0:
        return None

    k = 0
    x_k = x
    alpha_k = 0.0000001

    while True:
        if gradient1(function, x_k) == (0, 0):
            return x_k

        grad_f_xk = gradient1(function, x_k)

        alpha_k = find_min(function, x_k, gradient1(function, x_k), epsilon)

        x_k1 = manipulate_points(x_k, grad_f_xk, mult2 = -alpha_k)

        if max([length(x_k1, x_k), abs(function(x_k1)-function(x_k)), length(gradient1(function, x_k1), (0,0))]) <= epsilon:
            print("Stopping on iteration #{}".format(k))
            return x_k1

        k += 1
        x_k = x_k1


def main():
    error = 0.00001
    solve_rosenbrock(steepest_descent_method, error)  
    solve_himmelblau(steepest_descent_method, error)  

if __name__ == "__main__":
    main()
