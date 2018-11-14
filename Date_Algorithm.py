def datefunc(date, situation):

    year = date[:4]
    month = date[5:6]
    day = date[6:8]

    condition = 0
    secondcondition = 0

    day = int(day)
    month = int(month)

    thirtyone = [1,3,5,7,8,10,12] #months that have 31 days
    thirty = [4,6,9,11] #months that have 30 days

    if situation == 'a':
        day+=15
    if situation == 'b':
        day+=10
    if situation == 'c':
        day+=5

    if day < 28:

        if month < 10:
            condition = 1
        if day < 10:
            secondcondition = 1

        day = str(day)
        month = str(month)

        if condition==1:
            month = "0" + month
        if secondcondition==1:
            day = "0" + day

        c = year + month + day
        return(c)


    if month in thirty:

        month+=1
        day = day - 30

        if month < 10:
            condition = 1
        if day < 10:
            secondcondition = 1

        day = str(day)
        month = str(month)

        if condition==1:
            month = "0" + month
        if secondcondition==1:
            day = "0" + day

        c = year + month + day
        return(c)


    if month in thirtyone:

        month+=1
        day = day - 31

        if month < 10:
            condition = 1
        if day < 10:
            secondcondition = 1

        day = str(day)
        month = str(month)

        if condition==1:
            month = "0" + month
        if secondcondition==1:
            day = "0" + day

        c = year + month + day
        return(c)

    if month == 2 and day > 28:

        month = 3
        day = day - 28

        if day < 10:
            secondcondition = 1

        day = str(day)
        month = str(month)

        if secondcondition==1:
            day = "0" + day
        month = "0" + month

        c = year + month + day
        return(c)


date = input("Enter date: ")
situation = input("Situation: ")

print(datefunc(date,situation))

k=input("Press any key to exit ")
