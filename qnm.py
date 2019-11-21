import numpy as np
import numpy.matlib as ml
from fdom_2d_common import *

def inner_product(vec1, vec2):
    if ((vec1.shape[0] == 1) and (vec2.shape[0] == 1)) or ((vec1.shape[1] == 1) and (vec2.shape[1] == 1)): 
        return np.dot(np.ravel(vec1), np.ravel(vec2))
    return None

def quasi_newton_method(function, x, epsilon):
    if epsilon <= 0:
        return None

    k = 0
    H_k = ml.identity(n = 2, dtype = float)
    x_k = x
    
    while True:
        grad_f_xk = gradient1(function, x_k)
        if grad_f_xk == (0, 0):
            return x_k

        grad_vec = np.asmatrix(([grad_f_xk[0]], [grad_f_xk[1]]))
        p_k_vec = -H_k @ grad_vec
        p_k = (p_k_vec.item(0),p_k_vec.item(1))

        alpha_k = find_min(function, x_k, p_k, epsilon, sign = True)
        x_k1 = manipulate_points(x_k, p_k, mult2 = alpha_k)
        
        grad_f_xk1 = gradient1(function, x_k1)
        y_k = manipulate_points(grad_f_xk1, grad_f_xk, mult2 = -1)

        if max([length(x_k1, x_k), abs(function(x_k1)-function(x_k)), length(grad_f_xk1, (0,0))]) <= epsilon:
            print("Stopping on iteration #{}".format(k))
            return x_k1

        y_k_vec = np.asmatrix(([y_k[0]], [y_k[1]]))

        #BFGS formula        
        beta_k = alpha_k + inner_product(H_k @ y_k_vec, y_k_vec) / inner_product(y_k_vec, p_k_vec)
        H_k = H_k + (beta_k * p_k_vec * ml.transpose(p_k_vec) - p_k_vec * ml.transpose(y_k_vec) * H_k - H_k * y_k_vec * ml.transpose(p_k_vec)) / inner_product(y_k_vec, p_k_vec) 

        k += 1
        x_k = x_k1


def main():
    error = 0.00001
    solve_rosenbrock(quasi_newton_method, error)  
    solve_himmelblau(quasi_newton_method, error)  

if __name__ == "__main__":
    main()
