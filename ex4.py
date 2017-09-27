# set the number of cars
cars = 100
# set the number of seats in the car
space_in_a_car = 4
# set the number of drivers available
drivers = 30
# set the amount of passengers for the day
passengers = 90
# work out the amount of free cars
cars_not_driven = cars - drivers
# 1 driver per car makes the amount of cars driven for the say
cars_driven = drivers
# find the carpool capacity based on the number of cars and the space in each car
carpool_capacity = cars_driven * space_in_a_car
# find the average number of people that need to be in the car to satisfy the demand
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
