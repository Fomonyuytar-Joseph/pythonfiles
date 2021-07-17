guests=['Max','Christy','Jared','Mommy']
print('Hello ' + guests[0] +' ,you are highly invited for my dinner')
print('Hello ' + guests[1] +' ,you are highly invited for my dinner')
print('Hello ' + guests[2] +' ,you are highly invited for my dinner')
print('Hello ' + guests[3] +' ,you are highly invited for my dinner\n')

Not_coming=guests.pop(2)#removing a guest who cannot make it
print(Not_coming+ ' is not going to make it\n' )

new_guest=guests.insert(2, 'Chantal')#changing guest list
print('Hello ' + guests[0] +' ,you are highly invited for my dinner')
print('Hello ' + guests[1] +' ,you are highly invited for my dinner')
print('Hello ' + guests[2] +' ,you are highly invited for my dinner')
print('Hello ' + guests[3] +' ,you are highly invited for my dinner\n')

#printing a statement to invite guest to abigger table
print('Hi ' + guests[0] +' ,you are invited to the bigger dinner table')
print('Hi ' + guests[1] +' ,you are invited to the bigger dinner table')
print('Hi ' + guests[2] +' ,you are invited to the bigger dinner table')
print('Hi ' + guests[3] +' ,you are invited to the bigger dinner table\n')

#insert a new guest to the begiining of the list
guests.insert(0, 'Joseph')
#insert guest at the mddle of the list
guests.insert(2,'Ekema')
#to add a new guest to the end of the list
guests.append('Nazy')

#printing a new set of invitation messages
print('Hello ' + guests[0] +' ,you are highly invited for my dinner')
print('Hello ' + guests[1] +' ,you are highly invited for my dinner')
print('Hello ' + guests[2] +' ,you are highly invited for my dinner')
print('Hello ' + guests[3] +' ,you are highly invited for my dinner')
print('Hello ' + guests[4] +' ,you are highly invited for my dinner')
print('Hello ' + guests[5] +' ,you are highly invited for my dinner')
print('Hello ' + guests[6] +' ,you are highly invited for my dinner\n')

#printing a statement to invirte only two guesty
print('only two guests will be invited\n')

#removing 5 guests
guest1=guests.pop(4)
print('Sorry I cant invite you '+ guest1 +' for the dinner')
guest2=guests.pop(3)
print('Sorry I cant invite you '+ guest2 +' for the dinner')
guest3=guests.pop(2)
print('Sorry I cant invite you '+ guest3 +' for the dinner\n')
guests.remove('Mommy')
guests.remove('Nazy')


print(guests)
#inviting the remaining 2 guests
print(guests[0] + ' you are still invited for the dinner')
print(guests[1] + ' you are still invited for the dinner\n')


#deleting the guests who are to come
del guests[0]
del guests[0]


#printing the empty list
print(guests)





                       





