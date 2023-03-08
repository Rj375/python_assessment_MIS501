name = 'python'

print(name[0:5:3]) #slice the sting [start: stop+1: iteration/step over]

print(name[-1:-7:-1]) #reverse the string.


#list / array, it is mutable or editable
arr = [1, 2, 3, 4, 5, 6, 7,1,5,3,6,9] #array oF interger
arr1 = ['Ramesh', 'giri', 26, 20.5, True,'Giri'] #array oF multiple data types

for arrays in arr1: #loops through arr1
    print(arrays)

arr1[1] = 'Giri' #change the value in array.
print(arr1)

arr1.append(False) #adds the value at the end oF the array.
print(arr1) 

arr1.insert(2, 'Butwal') #adds the value at the speciFic place. (index, new value)
print(arr1)

arr1.pop(4) #removes value From speciFic index.
arr1.pop() #removes the value at the last
print(arr1)

arr1.remove(True) #removes the value
print(arr1)

print(arr1.index('Giri', 1)) #shows the index oF the value
print(arr1.index('Giri')) #shows the index oF the value

print(arr1.count('Giri')) # it check how many times the value is repeated in array or list.

arr1.extend('True')
print(arr1)

arr.sort() #sorts in ascending order.
print(arr)

arr.reverse() #reverses
print(arr)

arr.sort(reverse=True) #sorts in descending order
print(arr)

#Find the min and max oF list/array
arr.sort()
print(arr[0])
print(arr[-1])
#or
print(min(arr))
print(max(arr))


#ways to copy the list/array
arr3 = arr.copy()
arr4 = arr[0:13:1]
arr5 = arr[0:13]
print(arr3,arr4,arr5) 


#tuple, it is immutable or is not editable. 
tup = ('python', 'javascript', 26)
tup1 = 1,2 #by deFault it has become tupple aFter puting comma.

print(sum(arr)) #sums the array or list
print(sorted(arr)) #sorts the list.
