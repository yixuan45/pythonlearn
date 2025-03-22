# var1 = 'hello world!'
# var2 = 'runoob'
#
# print('var1[0]:', var1[0])
# print("var2的第2-5个字母为:{}".format(var2[1:5]))
#

# var1 = 'Hello World!'
# print("已更新的字符串:", var1[:6] + 'Runoob!')

#
# import time
#
# for i in range(101):
#     print("\r{:3}%".format(i), end='')
#     time.sleep(0.05)


# print("line1\
# ....line2\
# ......line3")
#
# print("\\")


# print('\'')


# print("\"")

# print("Hello \b World!")

# print("\000")

# print("Hello \v World!")

# print("Hello \rWorld!")

# print('googrunoob taobao\r123456')

# print('\'Hello,World!\'')
# print("Hello,World!\nHow are you?")
# print("Hello,world!\tHow are you?")
# print("Hello,\b world!")
# print("Hello,\fworld!")
# print("A对应的ASCII值为：", ord('A'))
# print("\x41为A的ASCII的代码")

# decimal_number = -42
# binary_number = bin(decimal_number)
# octal_number = oct(decimal_number)
# hexadecimal_number = hex(decimal_number)
# print("{}转换为二进制为：\n{}".format(int(decimal_number), binary_number))
# print("{}转换为八进制为：\n{}".format(decimal_number, octal_number))
# print("{}转换为十六进制为：\n{}".format(decimal_number, hexadecimal_number))

# a = 'Hello'
# b = 'Python'
# print(a + b)
# print(a*2)
# print(a[1])
# print('H'in a)
# print('M'not in a)
# print(r'\n')
# print(R'\n')

# print("我叫%s今年%d岁！" % ('小明', 10))

# name = 'Runoob'
# print('Hello %s' %name)


list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print(list1[0], end=' ')
# print(list1[1], end='')
# print(list1[-1])
# print(list1[-2])
# print(list4[1:4])
# print("第三个元素为：{}".format(list1[2]))
# list1[2] = 2001
# print("更新后的第三个元素为：{}".format(list1[2]))

# list1.append('Baidu')
# print("更新后的列表为：", list1)

# print("原始列表：", list1)
# del list1[2]
# print("删除第三个元素后的列表为：", list1)

# index = 0
# for i in list1:
#     index += 1
#     print("第{}个元素为{}".format(index, i))

# seq = (1, 2, 3, 4, 5)
# print("list1的长度为{}".format(len(list1)))
# print("list2的最大值为{}".format(max(list2)))
# print("list2的最小值为{}".format(min(list2)))
# print("把seq转换为列表为{}".format(list(seq)))

# print("list1原列表为{}".format(list1))
# list1.append('杨逸轩')
# list1.append('杨逸轩')
# list1.append('杨逸轩')
# print("list1列表添加新元素过后的列表为{}".format(list1))
# print("list1列表添加新元素过后\'杨逸轩\'出现的次数为{}".format(list1.count('杨逸轩')))
# print("list2列表为{}".format(list2))
# print("list3列表为{}".format(list3))
# list2.extend(list3)
# print("list2列表扩展后的列表为{}".format(list2))
# print("list2中\'a\'所在的索引为{}".format(list2.index('a')))
# print("list2中\'a\'所在的位置为{}".format(list2.index('a')+1))
# list1.extend(list2)
# print("list1原列表为：{}".format(list1))
# index = 0
# index1 = 0
# for i in list2:
#     list1.insert(index, i)
#     print("插入元素后的list1列表为:{}".format(list1))
#     index1 += 1
#     index = 2 * index1
# print("插入list2全部元素的list1列表为:{}".format(list1))


# a = list1.pop(0)
# print("a的值为{}".format(a))
# print("list1的结果为：{}".format(list1))

# list5 = [5, 7, 9, 6, 4, 4, 5, 9, 7, 2, 1]
# list5.sort()
# print("list5排序过后的结果为：{}".format(list5))
