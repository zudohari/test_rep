python  ='Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python','JAVA'))

print(python)
index = python.index("n")
print(index)
index =python.index("n",index+1)
print(index)

print(python.find("JAVA"))  #index는 찾는 문자가 없을시 에러남
print(python.find("A "))