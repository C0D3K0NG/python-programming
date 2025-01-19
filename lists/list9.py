# Write a program to compare two equal-sized lists and print the first index where they
# differ.

list1=[2,4,6,7]
list2=[2,5,6,7]

if len(list1)==len(list2):
    for x in range(0,len(list1)):
        if list1[x]!=list2[x]:
            print("They differ in index ",x) 
            break
        else:
            print("The lists are identical")

else:
    print("The lists do not have the same size")