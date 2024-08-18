name = "Michael Jackson"

print(name[-1])

print("AB\nc\nDE")
name = "holaMike".find("Mike")

print (name)


L = ["Michael Jackson".split(","), 10.1,1982,[1,2],('A',1)]

L.extend(["pop",10]) # aca agregamos 2 elementos mas a la lista
L.append(["music",12]) # aca agregamos una lista dentro de la lista

J = ["Michael Jackson", 10.1,1982,"MJ",1]

print(len (L))
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])

print(L[-5])
print(L[-4])
print(L[-3])
print(L[-2])
print(L[-1])

print(len (J))
print(J[0])
print(J[1])
print(J[2])
print(J[3])
print(J[4])
# print(J[3:5]:["MJ",1])
print(L)
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

a_list = [1,"hello",[1,2,3]]

print(a_list[1])
print(a_list[1:4])

A = [1, 'a'] 
B = [2, 1, 'd']
C = A + B
print(C)

shopping_list = []
shopping_list = ["Watch","Laptop","Shoes","Pen","Clothes"]
shopping_list.append(["Football"])

print(len (shopping_list))
print(shopping_list)
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[1:3])
shopping_list[3]="Notebook"
print(shopping_list)
del(shopping_list[4])
print(shopping_list)

decir_qué=('decir','qué','usted','será') 

print("say_what", decir_qué[-1])

A =[1,2,3,4,5]
print(A[1:4])

B = [1,3,[3,'a'],[4,'b']]
print(B[3][1])

C =[1,2,3]
D =[1,1,1]
E = C+D
print(E)

A.append([2,3,4,5])
print(A[1])