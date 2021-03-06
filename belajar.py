# print("this line will be printed.")

# x = 5
# if x ==1:
# 	print("x is 1.")
# else:
# 	print("x is not 1")

# str1 = '"geraldi"'
# print(str1)
# print(str1[2:6])
# print(str1[2:6:2])
# print(str1[::-1])

# nihfloat = 1.55
# print(nihfloat)

# var1 = 1.1
# if isinstance(var1,float):
# 	print('betul ini float')

# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append('aldi')
# print(mylist)
# print(mylist[0])
# print('list length %s' %len(mylist))

# if 'aldi' in mylist:
# 	print('ada aldi nih..')

# cubed = 6 ** 3
# print(cubed)

# hellos = 'hello' * 10
# print(hellos)

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%.3f."

# print(format_string % data)

# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)


# def sum_two_numbers(a, b):
#     return a + b

# print(sum_two_numbers(5,41))

# class Bola:
# 	bentuk = 'bulat'
# 	jenis = 'bola sepak'
# 	warna = 'putih'

# 	def getBentuk(self,a):
# 		return self.bentuk+' '+a

# 	def sumNumbers(self,a,b):
# 		return a + b

# bolaku = Bola()
# print(bolaku.bentuk)
# print(bolaku.getBentuk('ayam'))
# print(bolaku.sumNumbers(1,2))

# phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
# for name, number in phonebook.items():
#     print("Phone number of %s is %d" % (name, number))

#     # Create 2 new lists height and weight
# height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# # Import the numpy package as np
import numpy as np

# # Create 2 numpy arrays from height and weight
# np_height = np.array(height)
# np_weight = np.array(weight)
# print(np_height)
# print(type(np_height))
# print(np_weight)

# numarr = [1,2,3,4]
# print(numarr[-2])
# print(numarr[1:])
# print(numarr[:-1])

# numberList = [1,2,3]
# strList = ['one', 'two', 'three']

# # No iterables are passed
# result = zip()

# # Converting itertor to list
# # resultList = list(result)
# # print(resultList)

# # Two iterables are passed
# # result = zip(numberList, strList)
# result = zip(numarr[:-1],numarr[1:])

# # Converting itertor to set
# resultSet = set(result)
# print(resultSet)

# for x, y in zip(numarr[:-1],numarr[1:]):
# 	print('%f,%f'%(x,y))

# weights = [np.random.randn(y, x) for x, y in zip(numarr[:-1],numarr[1:])]
# print(weights)
# print(np.random.randn(2,1))

# lista =[1,2]
# listb = [3,4]
# print(lista+listb)

# import matplotlib.pyplot as plt
# # plot a line, implicitly creating a subplot(111)
# plt.plot([1,2,3])
# # now create a subplot which represents the top plot of a grid
# # with 2 rows and 1 column. Since this subplot will overlap the
# # first, the plot
#  #(and its axes) previously created, will be removed
# plt.subplot(441)
# plt.plot([1,2,3],[4,5,6])
# plt.grid(False)
# plt.subplot(5,5,20)
# plt.plot([1,2,3],[4,5,6])
# plt.show()

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential()
model.add(keras.layers.Embedding(1000, 64, input_length=10))
# the model will take as input an integer matrix of size (batch, input_length).
# the largest integer (i.e. word index) in the input should be
# no larger than 999 (vocabulary size).
# now model.output_shape == (None, 10, 64), where None is the batch dimension.

input_array = np.random.randint(1000, size=(32, 10))

model.compile('rmsprop', 'mse')
output_array = model.predict(input_array)
# assert output_array.shape == (32, 10, 64)