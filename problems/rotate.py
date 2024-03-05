# n=input("enter the value:")
# print("oringinal string:",n)
# start=n[3:]
# end=n[:-3]
# print("after rotate string:",start+end)
string=input("enter the string:")
n=int(input("enter the number:"))
m=[string[i:i+n] for i in range(0,len(string),n)]
arr=[]
for  i in m[::-1]:
    arr.append(i)
    print("".join(arr))
