def ex1():
    # EX1
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    product = x * y
    print(product)

    if product > 1000:
        print(x + y)


def ex2():
    # EX2
    last_number = None
    for i in range(0, 10):
        if last_number != None:
            sum = last_number + i
            print(sum)
        last_number = i


def ex3():
    # EX3
    list = [1, 2, 3, 4, 5, 7, 84, 6, 1]
    if list[0] == list[-1]:
        print("nice")
    else:
        print("wrong")


def ex4():
    # EX 4
    list2 = [0, 5, 6, 7, 8, 10, 23, 46]
    for i in list2:
        if int(i) % 5 == 0:
            print(i)


def ex5():
    # EX 5
    string1 = 'Emma is a good developer. Emma is also a writer'
    word = 'Emma'
    count = int(0)
    eos = False
    while not eos:
        tmp = string1.find(word)
        if tmp == -1:
            eos = True
        else:
            count += 1
            string1=string1[tmp+len(word):]

    print("String: " + word + " , " + str(count) + " times")


def ex6() :
    # EX6
    list1=[1,2,4,5,3,54,3,23,43,34,33]
    list2=[0,1,2,3,4,5,6,7,8,9]
    list3=[]
    for i in list1:
        if not i%2==0:
            list3.append(i)
    for a in list2:
        if a%2 ==0:
            list3.append(a)
    print(list3)

def ex7() :
    # EX 7
    str1 = '1111111111'
    str2 = '2222'

    str3 = str1[:(len(str1))//2] +str2 +str1[(len(str1))//2:]
    print(str3)
ex7()
