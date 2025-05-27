# Recognizes and prints dates (in the dd-mm-yyyy form) from the text copied to clipboard

import re
import pyperclip

dates_to_find = re.compile(r'''(
                       [0-3]\d)
                       (-|/|.)
                       ([0-1]\d)
                       (-|/|.)
                       ([1-2]?[09]?\d\d)
                       ''', re.VERBOSE)

clipboard = str(pyperclip.paste())
search_dates = dates_to_find.findall(clipboard)

dates = []

for date in search_dates:
    day_group = date[0]
    month_group = date[2]
    year_group = date[4]
    
    dates.append({"day":day_group, "month":month_group, "year":year_group})

months = ("January", "February", "March", "April",
          "May", "June", "July", "August", "September", "October", "November", "December")

for date in dates:
    try:
        if date["day"].endswith("1"):
            print("The {}st of {}, {}".format(date["day"],months[int(date["month"])-1],date["year"]))
        elif date["day"].endswith("2"):
            print("The {}nd of {}, {}".format(date["day"],months[int(date["month"])-1],date["year"]))
        else:
            print("The {}th of {}, {}".format(date["day"],months[int(date["month"])-1],date["year"]))
    except IndexError:
        continue
