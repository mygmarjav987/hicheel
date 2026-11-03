#1 Үнэлгээ эерэг сөрөг тэгш

# n = int(input("too"))
# if n == 0:
#     print (0)
# elif n >= 0:
#     print ("eyreg")
# else:
#     print("surug")

#2 Үнэлгээ

# n = int(input("onoo"))
# if n >= 90:
#     print("a")
# elif n <= 89:
#     print("b")
# elif n <= 79:
#     print("c")
# elif n <= 69:
#     print("d")
# else:
#     print("f")

#3 Өндөр жил

# year = int(input("jil: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Өндөр жил")
# else:
#     print("Энгийн жил")

#4 Гурвалжны төрөл

# a, b, c = map(int, input().split())
# if a + b <= c or b + c <= a or c + a <= b:
#     print("vvsehgvi")
# elif a == b == c:
#     print("tegsh tal")
# elif a == b or b == c or a == c:
#     print("adil")
# else:
#     print("engiin")

#5 Таксины төлбөр

# km = int(input("km:"))
# hurd = int(input("tak:"))
# if 

#6 Тэгш тоонуудын нийлбэр

# n = int(input("toogoo oruul !"))
# sum = 0
# for i in range(2, n + 1, 2):
#     sum += i
# print(sum)

#7 Цифрүүдийн нийлбэр

# n = int(input())
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n = n // 10
# print(total)

#8 Тоог урвуулах

# too = int(input("toogoo oruul"))
# while n > 0:
#     too = n % 10
#     total = total * 10 + too
#     n = n // 10
# print(total)

#9 ФизБазз

# n = int(input("toogoo oruul"))
# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print("ФизБазз", end=" ")
#     elif i % 3 == 0:
#         print("Физ", end=" ")
#     elif i % 5 == 0:
#         print("Базз", end=" ")
#     else:
#         print(i, end=" ")

#10 Нууц тоо таах

# secret = 37
# count = 0
# while True:
#     guess = int(input("toogoo oruul"))
#     count += 1
#     if guess > secret:
#         print("ih baina")
#     elif guess < secret:
#         print("baga baina")
#     else:
#         print("zuw", count, "oroldlogoor")
#         break

#11 Үржүүлэх хүснэгт

n = int(input("too"))
