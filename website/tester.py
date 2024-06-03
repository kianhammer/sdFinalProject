date = '2024-05-26 12:55:24.586449'
date = date[0:24]
point = 11
if point < 10:
    string = f"0{point}"
else:
    string = f"{point}"
date = date + string
print(date)