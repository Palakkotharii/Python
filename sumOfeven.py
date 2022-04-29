# Given a number N, print sum of all even numbers from 1 to N.
n= int(input())
counter=2
sum =0
while counter <=n:
    sum+=counter
    counter+=2
print(sum)