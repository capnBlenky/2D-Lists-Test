contact1 = ["John", "123 Applewood Gate", "Calgary", "403-123-3432"]
contact2 = ["Aaron", "123 Applewood Gate", "Calgary", "403-123-1234"]
contact3 = ["Jason", "123 Applewood Gate", "Calgary", "403-123-4536"]
contact4 = ["Riu", "123 Applewood Gate", "Calgary", "403-123-3211"]
contact5 = ["Mo", "123 Applewood Gate", "Calgary", "403-123-1555"]

#Add into the addressbook all of my contacts.
addressBook = []
addressBook.append(contact1)
addressBook.append(contact2)
addressBook.append(contact3)
addressBook.append(contact4)
addressBook.append(contact5)


# for contact in addressBook:
#   print(contact[0])

# print(addressBook[1][3])

from random import randint

myGrid = []

randX =randint(10,15)
randY = randint(10,15)
for x in range(randX):
  myGrid.append([])
  for y in range(randY):
    myGrid[x].append(randint(1,100))

for row in myGrid:
  print(row)