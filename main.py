import random


class GenerateNewCoordinate:

    def __init__(self, accuracy):
        self.__accuracy = accuracy
        self.__x = random.randint(1, self.__accuracy) / self.__accuracy
        self.__y = random.randint(1, self.__accuracy) / self.__accuracy

    def check_coordinate(self):
        if self.__x**2 + self.__y**2 > 1:
            return 0
        else:
            return 1


if __name__ == "__main__":
    accuracy = 10**7
    counter = 0
    for i in range(1, accuracy):
        new_point = GenerateNewCoordinate(accuracy).check_coordinate()
        counter += new_point

    print(counter / accuracy * 4)
