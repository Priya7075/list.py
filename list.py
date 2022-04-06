# a=[]
# # print(a,type(a))#list
# p=["ampeeret",55]
# print(p,type(p))#list
# print(p[0],type(p[0]))#ampeeret str
# print(p[1],type(p[1]))#55 int
# a=None
# print(type(a)) #NoneType
# b=[2,7,9,"hi",None,True]
# print(b[0],type(b[0]))# 2 int
# print(b[1],type(b[1]))#7 int
# print(b[2],type(b[2]))#9 int
# print(b[3],type(b[3]))#hi str
# print(b[3],type(b[4]))#NoneTpye
# print(b[3],type(b[5]))#Indexerror:list index out of range
# # print(b[3],type(b[,]))#SyntaxEror:Invalid syntax
# s=("vamsy")
# s[0]='v'#TypeError:'str' object does not support item assignment
# r=[4,3.1,"indu"]
# r[0]=89.23
# r[-1]='vI'
# print(r)#[89.23,3.1,'vI']
# n=[1,3.7,"mama",[10,22]]
# print(n,type(n))#list
# print(n[0],type(n[0]))#1 int
# print(n[1],type(n[1]))#3.7 float
# print(n[2],type(n[2]))#mama str
# print(n[3],type(n[3]))#list
# print(n[3][0],type(n[3][0]))#10
# print(n[3][1],type(n[3][1]))#22
# n=[1,3.7,"indu",[10,11]]
# n.appened('josh')
# print(n)#AttributeError:'list' object has no attribute
# n=[1,3.7,"indu",[10,11]]
# n.clear()
# print(n)#list
# n=[5,10,15,20]
# print(n)#[5,10,15,20]
# b=n.copy()
# print(b)#[5,10,15,20]
# n=[5,10,'vamsi',10,'']
# print(n.count(' '))#0
# print(n.count(6))#0
# print(n.count(10))#2
# print(n.count("vamsi"))#1
# print(n.count(8))#0
# a=[5,10,15]
# b=[1,3,5,7]
# a.extend(b)
# print(a)#[5,10,15,1,3,5,7]
# b.extend(a)
# print(b)#[1,3,5,7,5,10,15]
# n=[2,24,6,8,'mama',4.5,[56]
# print(n.index(14.5))#valueError:14.5 is not in list
# print(n.index(4.5))#5
# print(n.index(8))#3
# print(n.index(56))#6
# print(n.rindex[2])#AttributeError
# n=[1,3,5,7,11,13,15]
# n.insert(6,9)
# n.insert(2,4)
# n.insert(-1,8)
# n.insert(-2,10)
# print(n)#[1,3,4,5,7,11,13,9,10,8,15]
# n=[10,20,30,40]
# n.pop()
# print(n)#[10,20,30]
# n.pop(0)#[20,30,40]
# n.pop(4)#indexerror
# print(n)
# n=[10,20,'vamsi',30,40]
# n.remove('vamsi')
# n.index(100)#valueeror
# print(n)#[10,20,30,40]
# n=[1,2,3,4,5]
# print(n[::-1])#[5,4,3,2,1]
# n.reverse()
# print(n)#[5,4,3,2,1]
# n=[1,5,4,3,2]
# n.sort()
# print(n)#[1,2,3,4,5]
# n.sort(reverse=False)#[1,2,3,4,5]
# print(n)
# n.sort(reverse=True)
# print(n)#[5,4,3,2,1]
# j=[2.8,3.5,6.8,1.4,2.6]
# j.sort()
# print(j)#[1.4,2.6,2.8,3.5,6.8]
# k=['va','ms','in','du','pr','iy','av']
# k.sort()
# print(k)#['av','du','in','ms','pr','iy','va']




