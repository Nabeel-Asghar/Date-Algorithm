def format(year,month,day):

    newMonth = ""
    newDay = ""
    newYear = str(year)

    if month < 10:
        month = str(month)
        newMonth = "0"+month

    elif month >= 10:
        newMonth = str(month)

    if day < 10:
        day = str(day)
        newDay = "0"+day

    elif day > 10:
        newDay = str(day)

    result = newYear + "/" + newMonth + "/" + newDay
    print(result)

def theDate(date,choice):

    if choice == 'A':
        choice = 10
    elif choice == 'B':
        choice = 15
    elif choice == 'C':
        choice = 5

    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])

    dict = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

    daysMonth = 0

    if month in dict:
        daysMonth = dict[month]

    day += choice

    if day > daysMonth:
        month += 1
        if month == 13:
            month = 1
            year += 1
        newDay = day - daysMonth
        format(year,month,newDay)

    elif day <= daysMonth:
        format(year,month,day)

x = input("Date: ")
y = input("A - 10 days, B - 15 days, C - 5 days: ")
theDate(x, y)
