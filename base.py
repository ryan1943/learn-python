#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 'ABC中'.encode('ascii',errors='ignore')
print(len(x))
y = x.decode("utf-8")
print(len(y))
print('%2d-%02d' % (3, 1))
print('percent:%s%%' % (25))

#list 类型
classmate = ['Lily', 'Bob', 50, True, ['asp', 'php']]
classmate.append('admin')
classmate.pop()
classmate.insert(1, 'jack')
classmate.pop(1)
print(classmate[-4])
classmate[-1][0] = 'java'
print(len(classmate))
a = ['c', 'b', 'a']
a.sort()
a.reverse()

#list和tuple 是Python内置的有序集合,是可变对象
#tuple 类型 初始化就不能修改
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('lily', 'bob', 20, False, ['php', 'java'])
t[4][0] = 'c++'
t2 = (1,)

age = 3
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

#x是非零数值、非空字符串、非空list等，就判断为True
if t:
    print('true')

#输入数字没问题，输入其他字符串报错
# s = input("birth input: ")
# birth = int(s)
# print(birth)

sum = 0
for x in [1,2,3,4,5]:
    sum = sum + x
print(sum)

sum = 0
#range生成[0,1,2,3,4]
for x in range(5):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    if n < 10:
        break
    sum = sum + n
    n = n - 1
    if n % 2 == 0:
        continue
print(sum)

#dict,其他语言中也称为map,是无序的，速度快，空间换时间
#dict的key必须是不可变对象,比如字符串，整数
d = {'lily': 20, 'bob': 78, 'tom': 54}
d['bob'] = 99
d['jim'] = 80
print(d['bob'])
print(d.get('bob')) #key不存在，可以返回None
print(d.get('Lina', -1)) #或者自己设定返回值
if 'bob' in d:
    print('has bob key')
d.pop('bob')  #删除key

#set 集合，重复会被自动过滤,不可以放入可变对象
s1 = set([1, 2, 4, 4, 3])
s1.add(4)

s1.remove(4)
s2 = set([2, 3, 6])
s3 = s1 & s2 #交集
for x in s3:
    print(x)

#元素中没有list的tuple可以作为dict的key和放入set中，是不可变对象
#素中有list的tuple不可以作为dict的key和放入set，因为tuple的不可以变性是指tuple的每个元素，但是指向的这个list本身是可变的
#s1.add(t) 报错
s1.add(t2)

#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
#相反，这些方法会创建新的对象并返回
a = 'abc'
b = a.replace('a', 'A') #a还是abc

