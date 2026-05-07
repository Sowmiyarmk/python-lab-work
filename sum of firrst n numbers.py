num=int(input("enter the number n :"))
sum=0
i=0
#while loop
while i<=num:
    sum=sum+i
    i=i+1
print("The sum of n number is:",sum)
    
# for loop
for i in range (1,num+1):
    sum=sum+i
print("The sum of n number is:",sum)