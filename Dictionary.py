monthConversions = {
    "jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions.get("Dec"))

for key in monthConversions.keys():
    print(f" The key : {key} and value :  {monthConversions[key]}")