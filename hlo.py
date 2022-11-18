# a,b,x,y=map(int,input().split())
# print((a*x)+(b*y))

# a=int(input("enter the num:-"))
# if a%5==0 and a%11==0:
#     print("BOTH")
# elif a%5==0 or a%11==0:
#     print("ONE") 
# else:
#     print("NONE")       

# L,R=map(int, input().split())
# for i in range(L,R+1):
#     if i%2!=0:
#         print(i,end=" ")

# N=int(input())
# odd=0
# evn=0
# for i in range(N*2+1):
#     if i>0:
#         if i%2==0 and i>0:
#             evn=evn+i
#         else:
#             odd=odd+i
# print(odd," ",evn)            

# N=int(input())
# time=0
# strr=" "
# a=[]
# for i in range(1,N+1):
#     if N%i==0:
#         time+=1
#         strr=strr+" "+str(i)
# print(str(time),strr)   


# N=int(input())
# if N%5==0 or N%6==0:
#     print("YES")
# else:
#     print("NO")    

# N=int(input())
# def f():
#     sum=0
#     for i in range(N+1):
#         sum=sum+i
#     return sum
# print(f())


# T=int(input())
# for i in range(T):
#     def countWays(p, q, r, last):
#         if (p < 0 or q < 0 or r < 0):
#             return 0;
#         if (p == 1 and q == 0 and r == 0 and last == 0):
#              return 1; 
#         if (p == 0 and q == 1 and r == 0 and last == 1):
#             return 1;
         
#         if (p == 0 and q == 0 and r == 1 and last == 2):
#             return 1;
#         if (last == 0):
#             return (countWays(p - 1, q, r, 1) + countWays(p - 1, q, r, 2));
#         if (last == 1):
#             return (countWays(p, q - 1, r, 0) + countWays(p, q - 1, r, 2));
#         if (last == 2):
#             return (countWays(p, q, r - 1, 0) +countWays(p, q, r - 1, 1));
# def countUtil(p, q, r):
#             return (countWays(p, q, r, 0) +countWays(p, q, r, 1) +countWays(p, q, r, 2));
                 
#                 # Driver Code
# p = int(input())
# q = int(input())
# r = int(input())
# print(countUtil(p, q, r));    


# A,B,C=map(int, input().split())
# li=[]
# li.append(A)
# li.append(B)
# li.append(C)
# li.sort()
# print(li[-2])


# if A>B and A>C:
#     if B>C:
#         print(B)
#     else:
#         print(C)    
# elif B>A and B>C:
#     if A>C:
#         print(A)
#     else:
#         print(C)
# elif C>A and C>B:  
#     if A>B:
#         print(A)
#     else:
#         print(B)    

# a,b,c=map(int,input().split())
# if a+b>c and b+c>a and c+a>b:
#     print("YES")
# else:
#     print("NO")    


# rows=int(input())
# for i in range(0, rows+1):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end='')
#         else:
#             print("*", end=' ')
#             num += 1
#     # print("")

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j > (n-i) :
#             print('*',end ='')
#         else :
#             print(' ',end ='')
#     print()


# x,y,z=map(int,input().split())
# if x == y == z:
#         print("Equilateral Triangle")
 
#     # Check for isosceles triangle
# elif x == y or y == z or z == x:
#         print("Isosceles Triangle")
 
#     # Otherwise scalene triangle
# else:
#         print("Scalene Triangle")

# N,K=map(int,input().split())
# arr=[]
# for i in range(0,N):
#     arr.append(int(input()))
# if K in arr:
#     print(1)
# else:
#     print(-1)

# N,K=map(int,input().split())
# arr=[]
# for i in range(0,N):
#     a=int(input())
#     arr.append(a)
# if K in arr:
#     print(1)
# else:
#     print(-1)

# n = int(input())
# cnt = 1
# for i in range(n):
#     for j in range(5):
#         if i%2==0:
#             print(cnt,end=' ')
#             m = cnt 
#         else :
#             print(m+5-j,end =' ')
#         cnt+=1 
#     print()r̥

i=65
while i<=74:
    j=1
    while j<=4:
        print(chr(i),end="")
        j=j+1
    i=i+1