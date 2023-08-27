# import complex math module
import cmath
'''Let's take an example to solve the quadratic equation 8x2 + 16x + 8 = 0'''
if __name__ == '__main__':
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))
