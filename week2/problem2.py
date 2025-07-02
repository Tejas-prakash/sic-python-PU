N=int(input('Enter the number of requests: '))
lis=[]
server1=0
server2=0
for i in range(N):
    requests=input("enter value: ")
    lis.append(requests)
for i in range (len(lis)) :
    if i%2==0:
        server2+= server2+int(lis[i])
    else:
        server1+= server1+int(lis[i])
print('Server 1 = ',server1)
print('Server 2 = ',server2)

