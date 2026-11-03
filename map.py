# # task 1


# a, b, c= map(int, input("Too: ").split())
# if a > b and a > c and b > c:
#     print(a, b, c)
# elif b > a and b > c and a > c:
#     print(b, a, c)
# elif c > a and c > b and b > a:
#     print(c, b, a)
# elif a > b and a > c and c > b:
#     print(a, c, b)
# elif b > a and b > c and c > a:
#     print(b, c, a)
# elif c > a and c > b and a > b:
#     print(c, a, b)


# # task 2


# starth, startm = map(int, input("ehleh tsag: ").split())
# endh, endm = map(int, input("duusah tsag: ").split())
# start = starth * 60 + startm
# end = endh * 60 + endm
# if end < start:
#     end = end + 1440
# scc = end - start
# tsag = scc // 60
# minut = scc % 60
# print(tsag, minut)


# # task 3


# a, b, c = map(int, input("Urt: ").split())
# if a + b <= c or a + c <= b or b + c <= a:
#     print("NOT A TRIANGLE")
# if a * a + b * b == c * c:
#         print("right")
# elif a * a + b * b > c * c:
#         print("acute")
# elif a * a + b * b < c * c:
#         print("obtuse")     


# # task 4


# a, b, c = map(int, input("too: ").split())
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("INF")
#         else:
#             print("no roots")
#     else:
#         print("one roots")        
# else:
#     d = b*b - 4*a*c
# if d > 0:
#     print("two roots")
# elif d == 0:
#     print("one roots")
# elif d < 0:
#     print("no roots")


# # task 5


# day, mnth, yr = map(int, input("date: ").split())
# if mnth == 1 or mnth == 3 or mnth == 5 or mnth == 7 or mnth == 8 or mnth ==10 or mnth == 12:
#     odor = 31
# elif mnth == 4 or mnth == 6 or mnth == 9 or mnth == 11:
#     odor = 30
# else:
#     if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
#         odor = 29
#     else:
#         odor = 28
# if day < odor:
#     day=day + 1
# else:
#     day = 1
#     mnth = mnth + 1
#     if mnth > 12:
#         month = 1
#         yr= yr+ 1
#     print(day, mnth, yr)


# # task 6


# x1, y1, x2, y2 = map(int, input("Cm: ").split())
# x3, y3, x4, y4 = map(int, input("Cm: ").split())
# if x2 > x3 and x4 > x1 and y2 > y3 and y4 > y1:
#     print("yes")
# else:
#     print("no")


# # task 7


# uts, umin = map(int, input("tsag min: ").split())
# d = int(input("Tsagiin zoruu: "))
# newts = uts + d 
# if newts > 24:
#     print("tommorow", newts-24, umin )
# elif newts < 0:
#     print("yesterday", newts+24, umin)
# else:
#     print("today", newts, umin)


# # task 8


# a, b = map(int, input("Onoo: ").split())
# if a == 25 and b <= 23:
#     print("player 1")
# elif b == 25 and a<= 23:
#     print("player 2")
# elif a >= 26 and b >= 24 and a - b == 2:
#     print("player 1")
# elif b >= 26 and a >= 24 and b - a == 2:
#     print("player 2")
# elif a <= 24 and b <= 24:
#     print("not finished")
# elif a >= 24 and b >= 24 and a - b <= 1:
#     print("not finished")
# else:
#     print("invalid")


# # task 9


# ners = input("Ners: ")
# r1, c1, r2, c2 = map(int, input("nuudel: ").split())
# if r1 < 0 or r1 > 8 or c1 < 0 or c1 > 8 or r2 < 0 or r2 > 8 or c2 < 0 or c2 > 8:
#     print("invalid")
# elif r1 == r2 and c1 == c2:
#     print("NO")
# else:
#     dr = r2 - r1
#     if dr < 0:
#         dr = 0 - dr
#     dc =  c2 - c1
#     if dc < 0:
#         dc = 0 - dc
#     if ners == "king":
#         if dr <= 1 and dc <= 1:
#             print("YES")
#         else:
#             print("NO")
#     elif ners == "rook":
#         if dr == 0 or dc == 0:
#             print("yes")
#         else:
#             print("no")
#     elif ners == "bishop":
#         if dr == dc:
#             print("yes")
#         else:
#             print("no")
#     elif ners == "queen":
#         if dr == 0 or dc == 0 or dr == dc:
#             print("yes")
#         else:
#             print("no")
#     elif ners == "knight":
#         if (dr == 1 and dc == 2) or (dr == 2 and dc == 1):
#             print("YES")
#         else:
#             print("NO")

# # task 10

# a1, a2, a3 = input("utga: ").split()
# b1, b2, b3 = input("utga: ").split()
# c1, c2, c3 = input("utga: ").split()
# if ((a1 == "X" and a2 == "X" and a3 == "X") or
#     (b1 == "X" and b2 == "X" and b3 == "X") or
#     (c1 == "X" and c2 == "X" and c3 == "X") or
#     (a1 == "X" and b1 == "X" and c1 == "X") or
#     (a2 == "X" and b2 == "X" and c2 == "X") or
#     (a3 == "X" and b3 == "X" and c3 == "X") or
#     (a1 == "X" and b2 == "X" and c3 == "X") or
#     (a3 == "X" and b2 == "X" and c1 == "X")):
#     print("X wins")
# elif ((a1 == "0" and a2 == "0" and a3 == "0") or
#     (b1 == "0" and b2 == "0" and b3 == "0") or
#     (c1 == "0" and c2 == "0" and c3 == "0") or
#     (a1 == "0" and b1 == "0" and c1 == "0") or
#     (a2 == "0" and b2 == "0" and c2 == "0") or
#     (a3 == "0" and b3 == "0" and c3 == "0") or
#     (a1 == "0" and b2 == "0" and c3 == "0") or
#     (a3 == "0" and b2 == "0" and c1 == "0")):
#     print("0 wins")
# elif (a1 == "." or a2 == "." or a3 == "." or
#     b1 == "." or b2 == "." or b3 == "." or
#     c1 == "." or c2 == "." or c3 == "."):
#     print("Not finished")
# else:
#     print("draw")