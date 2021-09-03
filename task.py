a = 'mnbadsbnamnbanmbamnbanmbadddsssabns'
for i in list(set(list(a))):
    print(i,a.count(i))
list (a)

c = {i:a.count(i) for i in a}
print (c)
d = list((c.values()))
print (d)
result = d.count(d[0]) == len(d)
result = d.count(d[0]) == len(d)-1
if (result):
    print("my string")
else:
    print("not mine")
    
