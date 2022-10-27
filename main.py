# ############ Python Beta ############
#
# ########## variable name #########
#
# namesAllah = 99
#
# print(namesAllah)
#
# names_Allah = 99 ### valid
#
# _namesAllah = 99 ### valid
#
# _99namesAllah = 99 ### valid
#
# prophet_names = ['Muhammad', 'Ahmed']
#
# print(prophet_names)
#
# num = 10
# num = num + num
# print(num)
#
# print(num*num)
#
# ########## variable types ############
#
# numInt = 2
# type(numInt)
#
# numFloat = 2.2
# type(num)
#
# total = numInt + numFloat
# print(total)
# type(total)
#
# ####### commas working #########
#
# learn = "I'm learning the ropes with AlNafi"
# print(learn)
#
# ######## multi line string ########
#
# learn = "I'm learning the ropes with AlNafi"
# comma = ", "
# what = "Learning python"
# show = learn+ comma + what
# print(show)
#
# ########### string's length ##########
#
# print(len(show))
#
# islam = "Islam"
#
# print(islam[0:5])
#
# print(islam[-1])
#
# print(islam[-2])
#
# print(islam[0:-1])
#
# print(islam[-5:-1])
#
# name = 'Zulqarnain'
#
# print(name[2:10])
#
# print(name[::])
#
# print(name[1::])
#
# print(name[:2:])
#
# print(name[::2])
#
# print(name[::])
#
# ########### Reverse String ############
#
# print(name[::-1])
#
# ######### Immutability #########
#
# name = "Sadam"
#
# print(name)
#
# # name[0] = s  ############ ------------- throws error ------------#########
#
# a = 'salam'
#
# a + ' means peace'   ##### just concates but not stores in variable a
#
# print(a)
#
# a = a + ' means peace'   ########### concates and stores in variable a so variable a changes
#
# a
#
# ####### strings can be multiplied ###########
#
# word = 'hi'
# print(word)
#
# print(word*5)
#
# ########## string functions ###########
#
# program = 'Al Nafi'
#
# print(program.upper())
#
# print(program.lower())
#
# print(program.capitalize())
#
# print(program.split())
#
# x = 'Islam is the religion of peace'
#
# print(x.split('s'))     ######## breaks at given input ##########
#
# ############### Strings interpolation #################
#
# print("Al Nafi is a good {}".format('Institute'))
#
# print('{} {} {} {}'.format('Allah', 'is', 'the', 'greatest'))  ## auto index
#
# print('{0} {0} {0} {0}'.format('Allah', 'is', 'the', 'greatest'))  ## indexing matters
#
# print('{0} {1} {2} {3}'.format('Allah', 'is', 'the', 'greatest'))  ## proper indexing
#
# result = 'A grade'
#
# print('The result was {}'.format(result))
#
# ######## rounding off ############
#
# result = 22/321
#
# print(result)
#
# print("The result was {r:1.3f}".format(r = result))
#
# ### r for formate variable, 1 is for whitespace .3f means the precision of decimal
#
# name = 'Sadam'
#
# print('Salam, my name is {n}'.format(n = name))
#
# print(f'Salam, my name is {name}')  ###### f-string method is convenient
#
########################################

########### Lists ##################
#
# myList = [1,4,2,5,10,8]
#
# myList.sort()  ## it sorts the given object but does not return data to assign to a new variable.
#
# print(sorted(myList))
#
# print(myList)
#
# print(len(myList))
#
# names = ['hamza', 'asad', 'ahad']
#
# print(names[0])
#
# print(names)
#
# print(names[0:])
#
# print(names[0:2])
#
# print(names[1:3])
#
# print(names[::-1])
#
# list1 = ['hamza', 'asad']
#
# list2 = ['ahad', 'zainab']
#
# list3 = list1+list2
#
# print(list3)
#
# a = list3
#
# a.reverse() ## it reverses the given object but does not return data to assign to a new variable.
#
# print(a)
#
# names = ['hamza', 'asad', 'ahad']
#
# print(names)
#
# names[0] = 'Zainab'
#
# print(names)
#
# names.append('Hamza')
#
# print(names)
#
# names.pop()
#
# print(names)
#
# names.append('Hamza')
#
# print(names)
#
# print(names)
#
# poppedItem = names.pop()
#
# print(poppedItem)
#
# print(names)
#
# names.pop(0)  ###### index helps removing particular index value
#
# print(names)
#
# names.append('Hamza')
#
# print(names)

##########################################

######### Dictionary ###################
#
# wordDict = {
#     'name' : 'Hamza',
#     'class' : 9,
#     'age' : 15,
#     'school' : 'iiui',
# }
#
# print(wordDict)
#
# print(wordDict['name'])
#
# print(wordDict['age'])
#
# mangoDictionary = {
#     'name' : 'mango',
#     'types' : ['sindhri','rathore','chunsa','white chunsa'],
#     'price' : 200,
#     'exports' : {
#         'usa' : '200 tons',
#         'uk' : '500 tons'
#     }
# }
#
# print(mangoDictionary)
#
# print(mangoDictionary['types'])
#
# print(mangoDictionary['types'][0])
#
# print(mangoDictionary['types'][2])
#
# print(mangoDictionary['exports']['usa'])
#
# print(mangoDictionary['exports']['uk'])
#
# students = {
#     's1' : 'daud',
#     's2' : 'saud',
# }
#
# print(students)
#
# students['s3'] = 'fatima'
#
# print(students)
#
# students['s1'] = 'saad'
#
# print(students)
#
# print(students.keys()) ####### for keys only
#
# print(students.values()) ####### for values only
#
# print(students.items())

###################################

######## Tuples ############### immutable

# t = (1,2,3)

# print(t)

# ## t[0] = 2   ------- can't be performed --------

# print(len(t))

# t2 = (1,2,'apple',4,'apple')

# print(t2)

# print(t2[(1)])

# print(t2[(2)])

# print(t2.count('apple'))

# print(t2.index('apple'))

# print(t2.index(2))

# t3 = t+t2

# print(t3)

# ############ Tuple to List #############

# tupToList = list(t2)

# print(tupToList)

# x = tupToList

# print(x)

# listToTuple = tuple(x)

# print(listToTuple)

# ###### tuples are immutable but deletable #######

# myTuple = (1,2,3,4)

# print(type(myTuple))

# del myTuple      #### delete - so won't be printed now

# ######################################

# ################ Sets ###################

# mySet = set()

# mySet.add(1)

# print(mySet)

# mySet.add(2)

# mySet.add(4)

# mySet.add(3)

# print(mySet)

# mySet.add(4)    ########## no repetation - because it is SET

# print(mySet)

# setNumbers = {1,2,2,3,4,4}

# print(setNumbers)

# print(type(setNumbers))

# setToList = list(setNumbers)

# print(setToList)

# print(setNumbers.pop())

# print(setNumbers)

# setNumbers.pop()

# print(setNumbers)

# ##########################

# ###### Booleans ##############

# True

# print(type(True))

# print( 1 < 2)

# a = None

# print(type(a))

# 1 == 1

# print(1==1)

###################################

######### write file - type this part in jupyter #############
#
# %%writefile fileName.txt
# Asalam alaikum
# this is my alnafi write practice
#
# myfile = open("fileName.txt",)
#
# print(myfile.read())
#
# print(myfile.read())
#
# myfile.seek(0)
#
# print(myfile.read())
#
# ######################
#
# ###### Operators ##########
#
# print(1==1)
#
# print(1==2)
#
# print(1!=2)
#
# print(1>2)
#
# print(1<2)
#
# print(1>=2)
#
# print(1<=2)
#
# print(1<2<3)
#
# print(1<2>3)
#
# print(1<2 and 2>1)
#
# print('sadam' == 'sadam')
#
# num = 2
#
# if num < 2 or num ==2:
#     print("Correct")
#
# num = 2
#
# if num < 2 and num ==2:
#     print("Correct")
# else:
#     print("Not true for both cases")
#
# #########################
#
# ####### List and Loops ##############
#
# numList = [5,10,15,20,25,30,35,40,45,50]
#
# for li in numList:
#
#     print(li)
#
# for li in numList:
#     if li % 2 == 0:
#         print(li)
#
# for li in numList:
#     if li % 2 == 1:
#         print(li)
#
# sum = 0
#
# sumList = [5,10,15,20,25,30,35,40,45,50]
#
# for li in sumList:
#     sum += li
# print(sum)
#
# evenSum = 0
#
# evenSumList = [5,10,15,20,25,30,35,40,45,50]
#
# for li in evenSumList:
#     if li % 2 == 0:
#         evenSum += li
# print(evenSum)
#
# islam = 'Islam is the religion of peace'
#
# for i in islam:
#     print(i)
#
# ##### tuple & list #####
#
# tuple2list = [(1,2), (2,3), (3,4),(4,5)]
# print(len(tuple2list))
#
# for i in tuple2list:
#     print(i)
#
# for (a,b) in tuple2list:
#     print(a)
#     print(b)
#
# ######### dictionary + loops ##########
#
# priceDictionary = {'mango' : 200, 'apple':150, 'banana':300}
#
# for i in priceDictionary:
#     print(i)
#
#
# for i in priceDictionary.values():
#     print(i)
#
#
# for i in priceDictionary.keys():
#     print(i)
#
#
# for i in priceDictionary.items():
#     print(i)
#
# ##############################
#
# ###### While Loop ###########
#
# x = 0
#
# while x < 10:
#     print(x)
#     x += 1
#
# ###############
#
# ##### string to list ###########
#
# myString = 'Islam'
#
# myList = []
#
# for letters in myString:
#     myList.append(letters)
#
# print(myList)
#
# myString = 'Islam'
#
# myList = [letters for letters in myString]
#
# print(myList)
#
# nums = [num for num in range(1,10)]
# print(nums)
#
# nums = [num for num in range(1,10) if num % 2 == 0]
# print(nums)
#
# #############################
#
# ######### Methods #############
#
# myList = [1,2,3,4,5,6]
#
# myList.append(7)
#
# print(myList)
#
# myList.pop()
#
# print(myList)
#
# print(help(myList.pop))
