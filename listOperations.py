cars=['lexus','totyota','bugatti','volvo']
cars[1]='ferrari'
print(cars)
#to add new items to the end of the list
cars.append('tesla')
print(cars)
#We can use insert() to add taling as parameters the indices and the item
cars.insert(3,'lamboorghini')
print(cars)
#we use the del when we know the position of the element we want to delete
del cars[0]
print(cars)
#pop() removes the last item from the list and we can use it and can also take indexes
car_popped=cars.pop(3)
print(cars)
print(car_popped)
#we use the remove() to remove by value
cars.remove('tesla')#gonna remove the tesla
print(cars)


