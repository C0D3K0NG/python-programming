# Write a Python program that takes any two lists M and N of the same size and add their
# elements together to form a new list M and N whose elements are sums of the
# corresponding elements in L and M.
# For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13].

def add_lists(L, M):
    if len(L) != len(M):
        print("Error: The lists must be of the same length.")
        return None
    N = [L[i] + M[i] for i in range(len(L))]
    return N

L = [3, 1, 4]
M = [1, 5, 9]
N = add_lists(L, M)
if N:
    print("The resulting list N is:", N)
