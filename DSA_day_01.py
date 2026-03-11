'''def multiply_numbers(n):
    return n*n

print(multiply_numbers(99))
'''

'''
def print_num(n):
    for i in range(n):
        print(i)

print_num(10)
'''

"""def print_numbers(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)"""

def prnt_num(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


prnt_num(10)