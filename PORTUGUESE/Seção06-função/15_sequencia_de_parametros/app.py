def soma_todos(*nums):
  soma = 0
  for num in nums:
    soma = soma + num
  return soma

s = soma_todos(1,2,3,4,5)
print(s)

s2 =soma_todos(1,2,3)
print(s2)
