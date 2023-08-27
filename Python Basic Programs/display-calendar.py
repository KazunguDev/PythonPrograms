import calendar

if __name__ == '__main__':
    # Enter the month and year
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

    # display the calendar
    print(calendar.month(yy, mm))
