a = abs(-20)
a = max(1, 4, -5, 0)
a = hex(16)
print(a)

a = int('123')
a = int(12.34)
a = float('12.1234567890123456789')  #得到15位小数

b = str(1.23)
b = str(100)

c = bool(1)  #True
c = bool('') #False

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量,相当于别名
a = abs
b = a(-1)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise  TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

# c = my_abs('-10')
# print(c)

#空函数,pass可以用来作为占位符,以后想好再写
def nop():
    pass
#多值返回
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 30, math.pi / 6)
print(x, y)
# 实际返回是一个值，是个tuple
r = move(100, 100, 30, math.pi / 6)
print(r)

#默认参数一般放后面,默认参数必须指向不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print('power(5,2)= %s' % (power(5, 2)))
print('power(5)= %s' % (power(5)))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
l = add_end()
l = add_end()
print(l)

#可变参数,参数 numbers 接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
d = calc(1, 2, 3)

#list或tuple的元素变成可变参数,前面加*
nums = [1, 2, 3]
d = calc(*nums)
print(d)

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('lily', 30, city='Beijing')
extra = {'city':"Beijing", 'job': 'Engineer'}
person('jack', 24, city=extra['city'], job=extra['job'])
person('jack', 24, **extra) #获取extra的一份拷贝

#命名关键字参数,*后面只接收city和job作为关键字参数,如果有默认值则可以不传入city参数
def person2(name, age, *, city='Shanghai', job):
    print(name, age, city, job)

person2('jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

person3('jack', 24, 'man', '168', city='Beijing', job='Engineer')

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
#这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

#递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

#尾递归，在函数返回的时候，调用自身本身，每一步的乘积传入到递归函数中
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
def fact2(n):
    return fact2_iter(n, 1)
    
def fact2_iter(num, product):
    if num == 1:
        return product
    return fact2_iter(num - 1, num * product)
