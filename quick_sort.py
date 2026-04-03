A=[12,-5,3,6,3,2,7,3,18,3,5]
def quick_sort(arr):
    #always write the base case when writing recursive alogirthm
    if len(arr)<=1:
        return arr
    p=arr[-1]
    L=[x for x in arr[:-1] if x<=p]#List Comprehension
    R=[x for x in arr[:-1] if x>p]

    L=quick_sort(L)
    R=quick_sort(R)#recursion
    return L+[p]+R
A=quick_sort(A)
print(A)
