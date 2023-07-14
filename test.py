# salam="Tunzala"
# print(f'WElcome {salam}')

# a=7
# b='slama'
# print(type(a))
# print(type(b))

# a= int(input('num1: '))
# b= int(input('num2: '))
# print({a*b})

# a=100
# b=100
# if(a<b):print("ok")
# elif (a==b):print('no') 
# else: print("yes")

# a=5
# b=7
# c=9
# if a<b and b<c : print("OK")

# a=79
# if a>30:
#     print('okeokeokoek')
#     if a<100:
#         print("lalalalalla")
#     else : print("no")

# int = input("Enter a number: ")  
# digits = list(int)               
# output = " ".join(digits)          
# print(output) 

# a=int(input('num1: '))
# b=int(input("num2: "))
# if a<b: print (a), print (b)  
# else : print(b), print (a) 


# a,b=map(int,input("num:").split())
# for i in range (a,b+1):
#     if i % 2 != 0: print(i)

# x=int(input("num: "))
# count=(0)
# while x>0:
#     x//=10
#     count+=1
# print(count)

# n=int(input('num: '))
# for i in range (1,n+1):
#     print(f'{i} OK')

# n=int(input('nim: '))
# n1=n
# say=0
# while n1>0:
#     cem=0
#     while n>0:
#         son_reqem=n %10
#         cem +=son_reqem
#         n //=10
#     n1-=cem
#     say +=1
#     n=n1
# print(say)

# n=int(input())
# count= 0
# while n > 0:
#     digit = n % 10  
#     count += digit     
#     n //= 10       
# print(count)

# number = input() 
# cem = sum(map(int, str(number))) 
# print(cem)

# number = input()  
# digits = list(number)          
# output = " ".join(digits)   
# print(output) 

# n = int(input())
# a = (n // 100) % 10
# b = (n // 10) % 10
# c = n % 10
# i = b*100 + c*10 + a
# print(i)

# n=int(input())
# if n%2==0:
#     print(n-1)
# else: print(n-2)

# x=int(input())
# if x<5:
#     y=x**2-3*x+4
# else:
#     y=x+7
# print(y)

# a, b = map(int, input().split())
# if a<b:
#     print(a,b)
# else:
#     print(b,a)

# n=int(input())
# if 1<= n <=3: print("Initial")
# elif 4<= n <=6: print("Average")
# elif 7<= n <=9 : print("Sufficient")
# elif 10<= n <=12 :print("High")

# n, m, k = map(int, input().split())
# otaq_sayi = (n + k - 1) // k + (m + k - 1) // k
# print(otaq_sayi)

# n, m = map(int, input().split())
# if n % 2 == m % 2:
#     print(1)
# else:
#     print(0)

# num = input()
# if num.startswith('-'):
#     num = num[1:]
# for digit in num:
#     print(digit)

# n = int(input())
# def total(n):
#     i = 0
#     while n != 0:
#         i += n % 10
#         n //= 10
#     return i
# i = total(abs(n))
# print(i)

# n = input()
# max_digit = max(n)
# print(max_digit)

# n = int(input())
# for i in range(1, n, 2):
#     print(i, end=" ")

# a, b = map(int, input().split())
# for i in range(a, b+1):
#     if i % 2 == 1:
#         print(i, end=" ")

# n = input()
# reversed_n = n[::-1]
# print(reversed_n)

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 1:
#         result *= digit
#     n //= 10

# if result == 1:
#     result = -1
# print(result)

# def reqem_sayi(n):
#     return len(str(abs(n)))
# n = int(input())
# say = reqem_sayi(n)
# print(say)

# def qalxma_sayi(l, k):
#     qalxma_sayi = 0
#     while l > 1:
#         l /= k
#         qalxma_sayi += 1
#     return qalxma_sayi -1

# l, k = map(int, input().split())
# say = qalxma_sayi(l, k)

# print(say)


# def ikinci_reqem(n):
#     while n >= 10:
#         n_str = str(n)
#         ikinci_reqem = int(n_str[1])
#     return ikinci_reqem

# n = int(input())
# ikinci_reqem = ikinci_reqem(n)

# def hasillar_hesabla(eded):
#     hasil = 1
#     for reqem in str(eded):
#         hasil *= int(reqem)
#     return hasil//4

# verilen_eded = 234
# hasil = hasillar_hesabla(verilen_eded)
# print(hasil)

# def palindrome(number):
#     number = str(number) 
#     reverse_number = number[::-1] 
#     if number == reverse_number:
#         return "Yes"
#     else:
#         return "No"
# number = int(input())
# result = palindrome(number)
# print(result)

# def sil(number):
#     reqem = str(number)
#     yeni_reqem = ""
#     for digit in reqem:
#         if digit not in ["3", "9"]:
#             yeni_reqem += digit
#     return int(yeni_reqem)
# reqem = int(input())
# result = sil(reqem)
# print(result)

# n=int(input())
# l=list(map(int,input().split()))
# sum=0
# for i in range (n):
#     if l[i]!=max(l):
#         sum=sum+l[i]
# print(sum)

# def maxi(n, array):
#     maximum = max(array)
#     count=array.count(maximum)
#     return count
# n = int(input())
# array = list(map(int, input().split()))
# result = maxi(n, array)
# print(result)

# def calculate(n, array):
#     average = sum(array) / n
#     count = 0
#     total_sum = 0
#     for num in array:
#         if num > average:
#             count += 1
#             total_sum += num
#     return total_sum, count
# n = int(input())
# array = list(map(int, input().split()))
# sum_result, count_result = calculate(n, array)
# print(f'{sum_result} {count_result}')

# def calculate(n, array):
#     sorted_array = sorted(array, reverse=True)
#     cem = sorted_array[0] + sorted_array[1]
#     return cem
# n = int(input())
# array = list(map(int, input().split()))
# result = calculate(n, array)
# print(result)

# def x(n, array):
#     indeks = array[0:n:2]
#     return indeks
# n = int(input())
# array = list(map(int, input().split()))
# result = x(n, array)
# print(*result)

# def qonsu(n, array):
#     neighbors = []
#     for i in range(n - 1):
#         if array[i] * array[i+1] > 0:
#             neighbors.append((array[i], array[i+1]))
#     return neighbors
# n = int(input())
# array = list(map(int, input().split()))
# result = qonsu(n, array)
# for neighbor in result:
#     print(*neighbor)

def say(N, array):
    maximum = max(array)
    minimum = min(array)
    count= maximum! + minimum!
    return count
N = int(input())
array = list(map(int, input().split()))
result = say(N, array)
print(result)









