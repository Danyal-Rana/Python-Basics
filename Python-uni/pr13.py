min = int(input("Enter the minutes: "))

dayS = min/1440

years = dayS//365

days = dayS%365

print ("The entered minutes are equal to",years,"years and almost",days,"days")