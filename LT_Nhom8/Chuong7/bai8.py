def air_quality(n):
    air = dict()
    for i in range(n):
        index_air = input("Enter air quality: " + str(i+1) + ": ")
        date = input("Enter date: " + str(i+1) + ": ")
        air.update({date:index_air})
    print("The air quality: ", air)


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    air_quality(n)