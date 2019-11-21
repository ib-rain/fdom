import math

#https://www.derivative-calculator.net/
def function(A, B, x):
    return A * x +  B / math.e**x

def bisect(func, const1, const2, a, b, epsilon, delta):
    if epsilon <= 0 or delta <=0:
        return None

    if (a > b):
        extra = a
        a = b
        b = extra

    #Step 1
    x_k = (a + b) / 2 - delta
    y_k = (a + b) / 2 + delta

    k = 0

    (a_k, b_k) = (a, b)

    while True:
        #Step k
        k = k + 1

        f_x_k = func(const1, const2, x_k)
        f_y_k = func(const1, const2, y_k)

        if f_x_k <= f_y_k:
            # a_k = a
            b_k = y_k
        elif f_x_k >= f_y_k:
            a_k = x_k
            # b_k = b
    
        delta_k = (b - a) / 2**k + (2**k - 1) / (2**(k - 1)) * delta

        # print("k={}\tdelta_k={}\tx_k={}\ty_k={}\t(y_k-x_k)={}".format(k, delta_k, x_k, y_k, y_k-x_k))

        if delta_k < epsilon:
            return (x_k + y_k) / 2

        x_k = (a_k + b_k) / 2 - delta
        y_k = (a_k + b_k) / 2 + delta


def main():
    result = bisect(func = function, const1 = 1, const2 = 1,
                    a = -10, b = 100, epsilon = 0.1, delta = 0.025)
    print(result)

if __name__ == "__main__":
    main()
