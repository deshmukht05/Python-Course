# Display current date
from datetime import datetime
print("1. Current Date: ", datetime.now())

# Print hour-min-sec
print("2. Print hour-min-sec: ", datetime.now().strftime("%I:%M:%S %p"))

# Print date and time
print("3. Print date and time: ", datetime.now().strftime("%d/%m/%Y, %I:%M:%S %p"))

# Print day, date and time
print("4. Print day, date and time: ", datetime.now().strftime("%A %d/%m/%Y, %I:%M:%S %p"))