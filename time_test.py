
## [Attribute error:](https://stackoverflow.com/questions/54781947/attributeerror-datetime-time-object-has-no-attribute-time)

# Figure out how to print out time differences in Python:

if __name__ == '__main__':
    print('in main')
    import math
    import time as t
    x = math.inf
    counter = 0
    start=t.time()

    while True:
        print('in-loop')
        print(f"start: {start} ")
        # not resetting
        if t.time() - start >= 59:
            counter = 0
        # get time
        start = t.time()
        counter +=1
        # see where its at
        print(f"counter: {counter}")

