x = int(input())
y = int(input())
print(f'{x} + {y} = {x + y}')

 ##### 수정했음~~~~~~~~~~!!!!!!!!!!!!!!
#우렐렐레레레레레레레레레레레레


#num = input('정수 홋은 소수를 입력하세요: ')

#float_num = float(num)
#print(f'입력한 숫자의 소수형: {float_num}')

#int_num = int(float(num))
#print(f'입력한 숫자의 정수형: {int_num}')


#string = input('영어로 아무거나 입력하세요 (5자 이상): ')

#print(f'str.upper(): {string.upper()}')
#print(f'str.lower(): {string.lower()}')
#print(f'str[2:4]: {string[2:4]}')


#l = list()

#l.append(4)
#print(l)

#l.append('String')
#print(l)

#l.append(10.44)
#print(l)

#l.remove('String')
#print(l)


#y = set()
#for n in range(0, 20):
#    y.add(n)
#print(y)


#d = dict()

#d['Key'] = 'Value'
#print(d)

#d[4] = 'String'
#print(d)

#d[20.2] = 99.4
#print(d)

#d.pop(4)
#print(d)


fruits = {
    '사과': 1000,
    '바나나': 2000,
    '자두': 500,
    '복숭아': 4000,
}

def find_fruits():
    fruit = input("어서옵쇼~ 어떤 과일을 찾으시죠? ")
    if fruit in fruits:
        print(f"아! {fruit}는 {fruits[fruit]}원입죠~")
    else:
        print(f"아이고~ {fruit}는 매장에 업네요.")

find_fruits()


