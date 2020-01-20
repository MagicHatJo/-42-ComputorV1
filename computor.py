#!/usr/bin/python

import sys

def perfect_square(n):
	i = 1
	while i * i < n:
		i += 1
	if i * i == n:
		return i
	return -1

def sqrt(n):
	num = perfect_square(n)
	if num != -1:
		return num

	x = n
	y = 1
	e = 0.000001
	while(x - y > e):
		x = (x + y) / 2
		y = n / x
	return x

def parser(input):
    input = input.split('+')
    output = {0 : 0, 1 : 0, 2 : 0}
    for arg in input:
        if arg == '':
            continue
        if ('X' in arg) and ('X' is not arg[-1]) and ((arg[-2] is not '^') or (int(arg[-1]) > 2 or int(arg[-1]) < 0)):
            raise Exception("Polynomial degree out of range")
        if ('X' in arg and '^' in arg):#handle poly
            if (arg.split('X')[0] is not ''):
                output[int(arg[-1])] = output[int(arg[-1])] + int(arg.split('X')[0])
            else:
                output[int(arg[-1])] = output[int(arg[-1])] + 1
        elif ('X' in arg):#handle linear
            if (arg.split('X')[0] is not ''):
                output[1] = output[1] + int(arg.split('X')[0])
            else:
                output[1] = output[1] + 1
        else:#handle constants
            output[0] = output[0] + int(arg)
    return output

def print_poly(left, right):
    if all(value == 0 for value in left.values()):
        print('0 ', end = '')
    else:
        if left[0] is not 0:
            print(str(left[0]) + ' ', end = '')
        if left[1] is not 0:
            if left[0] is not 0:
                print('+ ', end = '')
            if left[1] is not 1:
                print(left[1], end = '')
            print('X ', end = '')
        if left[2] is not 0:
            if left[0] is not 0 or left[1] is not 0:
                print('+ ', end = '')
            if left[2] is not 1:
                print(left[2], end = '')
            print('X^2 ', end = '')
    print('=', end = '')

    if all(value == 0 for value in right.values()):
        print(' 0', end = '')
    else:
        if right[0] is not 0:
            print(' ' + str(right[0]), end = '')
        if right[1] is not 0:
            if right[0] is not 0:
                print(' +', end = '')
            print(' ', end = '')
            if right[1] is not 1:
                print(right[1], end = '')
            print('X', end = '')
        if right[2] is not 0:
            if right[0] is not 0 or right[1] is not 0:
                print(' +', end = '')
            print(' ', end = '')
            if right[2] is not 1:
                print(right[2], end = '')
            print('X^2', end = '')
    print('')

def reduction(left, right):
    if (right[0] is 0 and right[1] is 0 and right[2] is 0):
        return left
    if right[0]:
        left[0] = left[0] - right[0]
        print_poly(left, {0:0, 1: right[1], 2: right[2]})
    
    if right[1]:
        left[1] = left[1] - right[1]
        print_poly(left, {0:0, 1:0, 2: right[2]})

    left[2] = left[2] - right[2]
    print_poly(left, {0: 0, 1: 0, 2: 0})
    return left

def solve_linear(coeff):
    print("Linear equation:")
    print('')

    right = {0:0, 1:0, 2:0}
    #print initial state
    print_poly(coeff, right)

    if coeff[0] is not 0:
        right[0] = 0 - coeff[0]
        coeff[0] = 0
        print_poly(coeff, right)

    if coeff[1] is not 0:
        right[0] = right[0] / coeff[1]
        coeff[1] = 1
        print_poly(coeff, right)
    
    print('')
    print("Solution:")
    print(right[0])

def solve_quadratic(coeff):
    discriminant = coeff[1] ** 2 - 4 * coeff[2] * coeff[0]
    bot = 2 * coeff[2]
    if discriminant > 0:#2 solutions
        print("There are two real solutions:")
        print('')

        #print initial state
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(coeff[1]) + " ^ 2 - 4 * " + str(coeff[2]) + " * " + str(coeff[0]) + "))) / 2 * " + str(coeff[2]))

        #first step (discriminant and bot)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(discriminant) + ")) / " + str(bot))
        
        #second step (sqrt)
        root = sqrt(discriminant)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + " + str(root) + ") / " + str(bot))

        #third step (top)
        top = (-1 * coeff[1]) + root
        print("x = " + str(top) + " / " + str(bot))

        #get plus answer
        solution_plus = top / bot
        print("x = " + str(solution_plus))

        print('')
        #print initial state
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" - sqrt(" + str(coeff[1]) + " ^ 2 - 4 * " + str(coeff[2]) + " * " + str(coeff[0]) + "))) / 2 * " + str(coeff[2]))

        #first step (discriminant and bot)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" - sqrt(" + str(discriminant) + ")) / " + str(bot))
        
        #second step (sqrt)
        root = sqrt(discriminant)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" - " + str(root) + ") / " + str(bot))

        #third step (top)
        top = (-1 * coeff[1]) - root
        print("x = " + str(top) + " / " + str(bot))

        #get minus answer
        solution_minus = top / bot
        print("x = " + str(solution_minus))
        print('')
        print("Solutions:")
        print(solution_plus)
        print(solution_minus)

    elif discriminant == 0:#one solution
        print("There is one solution:")
        print('')

        #print initial state
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(coeff[1]) + " ^ 2 - 4 * " + str(coeff[2]) + " * " + str(coeff[0]) + "))) / 2 * " + str(coeff[2]))

        #first step (discriminant and bot)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(discriminant) + ")) / " + str(bot))

        #second step (get answer)
        solution = (-1 * coeff[1]) / bot
        print("x = " + str(solution))
        print("Solution:")
        print(solution)

    else:#both solutions are imaginary
        print("There are no real solutions:")
        print('')

        #print initial state
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(coeff[1]) + " ^ 2 - 4 * " + str(coeff[2]) + " * " + str(coeff[0]) + "))) / 2 * " + str(coeff[2]))

        #first step (discriminant and bot)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + sqrt(" + str(discriminant) + ")) / " + str(bot))

        #second step (extract i)
        root = sqrt(-1 * discriminant)
        print("x = (", end = '')
        if coeff[1] >= 0:
            print("-" + str(coeff[1]), end = '')
        else:
            print(coeff[1] * -1, end = '')
        print(" + " + str(root) + "i) / " + str(bot))

        #print status
        print("x = ", end = '')
        if coeff[1] / bot is not 1:
            print(str(-1 * coeff[1] / bot) + " + ", end = '')
        if root % bot is 0 and int(root / bot) is not 1:
            print(root / bot, end = '')
        print('i')
        print('')

        #print status
        print("x = ", end = '')
        if coeff[1] / bot is not 1:
            print(str(-1 * coeff[1] / bot) + " - ", end = '')
        if root % bot is 0 and int(root / bot) is not 1:
            print(root / bot, end = '')
        print('i')
        print('')

        print("Solutions:")
        if coeff[1] / bot is not 1:
            print(str(-1 * coeff[1] / bot) + " + ", end = '')
        if root % bot is 0 and int(root / bot) is not 1:
            print(root / bot, end = '')
        print('i')

        if coeff[1] / bot is not 1:
            print(str(-1 * coeff[1] / bot) + " - ", end = '')
        if root % bot is 0 and int(root / bot) is not 1:
            print(root / bot, end = '')
        print('i')

def main():
    if len(sys.argv) is not 2:
        raise Exception("ComputorV1 takes 1 argument")

    input = sys.argv[1].replace('-', '+-').replace('*', '').replace('x', 'X').replace(' ', '').split('=')
    if len(input) is not 2:
        raise Exception("Not a valid polynomial")

    left = parser(input[0])
    right = parser(input[1])

    print_poly(left, right)
    reduced = reduction(left, right)

    print("Polynomial degree: " + (str(2) if left[2] else str(1) if left[1] else str(0)))

    if reduced[2] is 0:
        solve_linear(reduced)
    else:
        solve_quadratic(reduced)

main()
