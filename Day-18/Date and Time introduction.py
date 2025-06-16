# Displaying date and time is very important part of all software applications.
# In almost every business application date is involved in various from like system date, date of birth, date of sale/purchase, date of manufacturing, date of expiry, date of registration, transaction date, date of issue/return, date/time before and after specific time etc. 
# Python suppports datetime module to handle date and time.
# Most commanly used classes of datetime module are:
# 1. date class
# 2. time class
# 3. datetime class
# 4. timedelta class
# Python provides different date formatting options for representing date in required format.
# The strftime() method is defined under classes date, datetime and time.
# The strftime() used to formart date and it creates a formatted string.
# The strftime() method creates a datetime object from a given string. It hsa two arguments, first is a string representing date and time, and another is format code.

# Commanly used formats are:
# 1. %a : Current location's weekday abbreviation
# 2. %A : Current location's full weekday name
# 3. %b : Current location's abbreviated month
# 4. %B : Current location's full month name
# 5. %c : Current location's date and time representation
# 6. %d : The day of the month as a deci,al number [01, 31]
# 7. %B : The hour (24-hour clock) as a decimal number [0, 23]
# 8. %I : The hour (12-hour clock) as a decimal number[01, 12]
# 9. %j : The day of the year as a decimal number [001, 366]
# 10. %m : The month as a decimal number [01, 12]
# 11. %M : The minute as a decimal number [00, 59]
# 12. %p : Current location's AM or PM
# 13. %S : The second as a decimal number [00, 59]
# 14. %U : The week number of a year (Begins with Sunday as the first day of the week) as a decimal number [00, 53]. Note that, all days in a new year before the first Sunday is considered as week 0.
# 15. %w : The weekday as a decimal number [0(Sunday), 6]
# 16. %W : The week number of a year (Begins with Monday as the first day of the week) as a decimal number [00, 53]. Note that, all days in a new year before the first Monday is considered as week 0
# 17. %x : Current location's date representation
# 18. %X : Current location's time representation
# 19. %y : A year without century as a decimal number [0001, 9999]
# 20. %Y : A year with century as a decimal number
# 21. %z : The time zone name (no characters when there is no time zone)