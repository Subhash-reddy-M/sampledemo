#indexing numbers
#positive index
my_list=[10,20,30,40,50,60,70,80,90]
print (my_list[2:8:2])
#
my_list=[10,20,30,"subhash reddy",90]
print(my_list[0:4:2])

#negitive index
my_list=[10,20,30,40,50,60,70,80]
print (my_list[0:-9:-1])

my_list=[10,20,30,40,50]
print(my_list[-1])

#slicing
#forword direction
my_list=[10,20,30,40,50]
print(my_list[-1])

#backword drection
my_list=[50,40,30,20,10]
print(my_list[-5])

#LISTS METHODS
#append
numbers=[1,2,3,4,5,6,7]
numbers.append ("subhash")
print(numbers)

numbers=[9,4,5,3,4,5,9]
numbers.append("reddy")
print(numbers)
#extend
numbers=[30,40,50,70,80]
numbers.extend("subhashreddy")
print(numbers)
#copy
numbers=[1,2,3,4,5,6]
numbers.copy()
print(numbers)
#clear
numbers=[1,2,3,70,80]
numbers.clear()
print(numbers)
#count
numbers=[3,1,4,5,9]
numbers.count(1)
print (numbers)
#index
numbers=[1,8,9,5]
print (numbers.index(8))
#remove
numbers=[3,8,9,7,6]
numbers.remove(8)
print(numbers)
#insert
numbers=[1,2,3]
numbers.insert(3,"subhash reddy")
print(numbers)
#reverse
numbers=[1,2,3,4,8]
numbers.reverse()
print(numbers)
#sort
numbers=[4,5,6,9,8]
numbers.sort(reverse=True)
print(numbers)
#length
print(len('1,2,3,4,5,8,8'))
print(len)
#nested list

