class Person:
  pass

diusval = Person()
mateus = Person()

print(diusval)
print(mateus)

del mateus

print(diusval)
# Doi deletado o programa irá da erro
# print(mateus)