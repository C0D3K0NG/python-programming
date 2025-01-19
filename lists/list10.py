# Create the following lists using a for loop:
# The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
#a=97 (ascii code)

list1=[]
for i in range(97,97+26):
    value=chr(i)
    for j in range(1,i-96):
        value+=chr(i)
    list1.append(value)
print(list1)
