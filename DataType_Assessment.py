# Numbers
a = 4
b = 5
c = 6

print(a * (b + c))
print(a * c + b)
print(a + c * b)

d = 3
e = 1.5
f = 4
type(print(d + e + f))

# String
s = 'hello'
print(s[1])
print(s[::-1])

# print the o-method1
print(s[4])
# print the o-method2
print(s[-1])

# lists

My_List = [0,0,0]
print(My_List)


My_List1 = [1,2,[3,4,'hello']]
My_List1[2][2] = 'goodbye'
print(My_List1)


list_5 = [5,3,4,6,1]
list_4 = sorted(list_5)
print(list_4)

#dictionaries

d = {'simple_key':'hello'}
print(d['simple_key'])

d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])

d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])