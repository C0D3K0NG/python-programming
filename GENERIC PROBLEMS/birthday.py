from datetime import datetime, date

d = int(input("Enter the day of your birth: "))
m = int(input("Enter the month of your birth: "))
y = int(input("Enter the year of your birth: "))
birthday = date(y, m, d)

# Calculate age in days
today = date.today()
age_in_days = (today - birthday).days

# Calculate age in years and months
years = today.year - birthday.year
months = today.month - birthday.month
days = today.day - birthday.day

if days < 0:
    months -= 1
    days += (birthday.replace(month=birthday.month + 1, day=1) - birthday).days

if months < 0:
    years -= 1
    months += 12

print(f"No of days: {age_in_days}")
print(f"No of months: {years * 12 + months}")
print(f"No of years: {years} and {months} months")
