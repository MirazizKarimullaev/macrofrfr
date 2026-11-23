import random
import time
def loud_volume():
    loud = input("chose volume?\n")
    print(f"ok processing")
    x = random.randint(1000,10000)
    while True:
        time.sleep(1)
        y = random.randint(1,50)
        if y >= 0 and y <= 48:
            x = x-1
        elif y == 49:
            x = x*2
        elif y == 50:
            x - 100
            print("your estimated time left is 1 seconds")
            x = 3297412398479812347912374980123740912
        print(f"your estimated time left is {x} seconds")
        if x > 1:
            break
    print("your voluma is -10u0829y7829")
loud_volume()
