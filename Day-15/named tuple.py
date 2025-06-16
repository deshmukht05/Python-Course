# Python allows named tuple where we can refer each item by name rather than its index.
# This increase readability and is easier to debug.

from collections import namedtuple
vehicle = namedtuple('type', 'state city series no')
print(type(vehicle))
car = vehicle(state='MH', city='31', series='AB', no='2023')
print(car)
print(car.state, car.city, car.series, car.no)