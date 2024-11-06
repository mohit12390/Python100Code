
while True:
    x = input("Enter the Month name : \n")

    match x:
        case "Jan":
            print("Month is January")
        case "Feb":
            print("Month is February")
        case "Mar":
            print("Month is March")
        case "Apr":
            print("Month is April")
        case "May":
            print("Month is May")
        case "Jun":
            print("Month is June")
        case "Jul":
            print("Month is July ")
        case "Aug":
            print("Month is August")
        case "Sep":
            print("Month is September")
        case "Oct":
            print("Month is October")
        case "Nov":
            print("Month is November")
        case "Dec":
            print("Month is December")
        case _:
            print("Invalid Month Name ")