def kilometre_1(km):
    conversion_ratio_1 = 0.621371
    miles_1 = km * conversion_ratio_1
    print("The speed value of car in Miles: ", miles_1)


if __name__ == '__main__':
    km = float(input("Please enter the speed of car in Kilometre as a unit: "))
    kilometre_1(km)
