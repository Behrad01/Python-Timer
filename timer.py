import time
import sys

def main():   # defining main function
    # CLI guide
    print('*' * 10, end='')
    print('  Timer  ', end='')
    print('*' * 10)

    try:
        i = int(input('Seconds: '))   # catching user input
    except ValueError:
        print('Please enter a valid input.')
        return

    if i > 0:   # validating user input
        # setting up timer
        for remaining in range(i, -1, -1):
            sys.stdout.write(f'\r{remaining:5d}')
            sys.stdout.flush()
            time.sleep(1)   # waiting 1 second for each iteration
    else:
        print('Please enter a positive number.')   # checking if input is negative
    
if __name__ == '__main__':
    main()   # running main function
