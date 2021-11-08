palind = input('Enter the object: ')
newList = []
newList.append(palind.upper())

for elem in newList:
  if elem[::-1] == elem: print(palind)
  else: print('It\'s not a palindrome!')