import sys


def validate_input(value):
    return map(int, value.split(','))


def main(x, y):
    """
    Generate two dimensional array having x rows and y columns
    """
    return [list(range(i * y + 1, (i + 1) * y + 1)) for i in range(x)]


if __name__ == "__main__":
    """
    Write a program which takes 4 inputs, where each input consists of 2 numbers in the format x,y. 
    You are required to print a two dimensional array having x rows and y columns for each input. 
    The elements of the arrays should be whole numbers starting from 1 and incrementing by 1. 
    """
    results = []
    for i in range(1, 5):
        while True:
            try:
                x, y = validate_input(input('Enter {}st input: '.format(i)))
                results.append(main(x, y))
            except (ValueError, TypeError):
                sys.stdout.write('Please enter 2 numbers in the format x,y. \n')
                continue
            else:
                break

    [sys.stdout.write('{}\n'.format(res)) for res in results]
