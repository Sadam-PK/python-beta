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

wordDict = {
    'name' : 'Hamza',
    'class' : 9,
    'age' : 15,
    'school' : 'iiui',
}

print(wordDict)

print(wordDict['name'])

print(wordDict['age'])

mangoDictionary = {
    'name' : 'mango',
    'types' : ['sindhri','rathore','chunsa','white chunsa'],
    'price' : 200,
    'exports' : {
        'usa' : '200 tons',
        'uk' : '500 tons'
    }
}

print(mangoDictionary)

print(mangoDictionary['types'])

print(mangoDictionary['types'][0])

print(mangoDictionary['types'][2])

print(mangoDictionary['exports']['usa'])

print(mangoDictionary['exports']['uk'])

students = {
    's1' : 'daud',
    's2' : 'saud',
}

print(students)

students['s3'] = 'fatima'

print(students)

students['s1'] = 'saad'

print(students)

print(students.keys()) ####### for keys only

print(students.values()) ####### for values only

print(students.items())