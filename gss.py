import math

#https://www.derivative-calculator.net/
def function(A, B, x):
    return A * x +  B / math.e ** x

def golden_section_search(func, const1, const2, a, b, epsilon):
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

    f_x_k1 = f_x_k = func(const1, const2, x_k1)
    f_y_k1 = f_y_k = func(const1, const2, y_k1)

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
                f_x_k = func(const1, const2, x_k)
        #The only possibility left is f_x_k1 > f_y_k1
        else:
            a_k = x_k1
            b_k = b_k1
            x_k = y_k1
            y_k = b_k - delta[k+1]
            f_x_k = f_y_k1
            if x_k < y_k:
                f_y_k = func(const1, const2, y_k)

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




def main():
    result = golden_section_search(func = function, const1 = 1, const2 = 1,
                                    a = -10, b = 100, epsilon = 0.001)
    print(result)

if __name__ == "__main__":
    main()
