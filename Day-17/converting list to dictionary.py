# Converting list to dictionary
# Converting 2 lists of month containing list of month names and days containing number of days in months
# zip() function works like zipper that combines two lists and returns a zipped object. And list() constructor is used to construct a list from zipped object. As below -

print("Converting list to dictionary")
month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
num = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_num = zip(num, month) # Here we will use zip
m_n = list(month_num) # Then make it list
m = dict(m_n) #At last make it a dictionary
print("Months with numbers: ", m)