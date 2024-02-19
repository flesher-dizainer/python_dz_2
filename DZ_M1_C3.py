def zadanie_1():
    print(str(input("input a  "))+str(input("input b  "))+str(input("input c  ")))

def zadanie_2():
    a = str(input("input a "))
    ex_value = 1
    for i in range(len(a)):
        ex_value *= int(a[i])
    print (ex_value)

def zadanie_3():
    a = int(input("input a "))
    cm = a * 100
    dm = a * 10
    mm = a * 1000
    ml = a * 0.0006
    print ('sm = '+str(cm)+'\n'+'dm = '+str(dm)+'\n'+'mm = '+str(mm)+'\n'+'ml = '+str(ml))
 
def zadanie_4():
    a = float(input("a "))
    h = float(input("h "))
    s = 0.5 * a * h
    print ('S = '+str(s))

def zadanie_5():
    a = str(input("input a "))
    ex = ''
    for i in range(len(a)):
        ex += a[len(a)-i-1]
    print (ex)
    
def main():
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
    zadanie_5()
    
if	__name__	==	'__main__':
	main()
