names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

#1 OK
names[1] = 'Steven'
print(names)

#2 OK
names[10] = 'Pepe'
print(names)

#3 OK
names[0] = names[2] + names[4]
print(names)

#4 
last_index = len(names) - 1

for i in reversed(range(len(names))):
    print(names[i])