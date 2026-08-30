import time


def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("პროგრამამ იმუშავა:", round(end - start, 2), "წამი")

    return wrapper


@timer
def study():
    seconds = int(input("რამდენი წამი გინდა ისწავლო? "))

    print("სწავლა დაიწყო!")

    time.sleep(seconds)

    print("დრო დასრულდა!")


study()