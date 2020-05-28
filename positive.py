#positive no.s in a range
list_1=[]
terms=int(input('enter no. of terms: ')) #taking input from user
for x in range(0,terms):
    y=int(input())
    list_1.append(y)      #adding term at the end of list
print(list_1)             
print('positive no.s:')
for x in list_1:          #printing the positive no.s 
    if x>=0:
        print(x)
output:
enter no. of terms: 3
-1
-2
9
[-1, -2, 9]
positive no.s:
9
1
