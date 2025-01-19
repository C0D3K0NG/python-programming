# Write a Python program that takes any two lists M and N of the same size and add their
# elements together to form a new list M and N whose elements are sums of the
# corresponding elements in L and M.
# For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13].


listm=[2,7,8]
listn=[1,6,9]
listc=[]
if len(listm)==len(listn):
    for x in range(0,len(listm)):
        listc.append(listm[x]+listn[x])
    print(listc)
else:
    print("Lists sizes are not of the same size")