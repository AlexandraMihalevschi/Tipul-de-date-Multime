A = set(input('Dati o multime de caractere:'))
B = set(input('Dati o alta multime de caractere:'))
A.remove(' ')
A.remove(',')
B.remove(' ')
B.remove(',')
print('Reuniunea mulţimilor A şi B', A.union(B))
print('Intersecţia mulţimilor A şi B', A.intersection(B))
print('Diferenţa mulţimilor A şi B', A.difference(B))
print('Diferenţa mulţimilor B şi A', B.difference(A))