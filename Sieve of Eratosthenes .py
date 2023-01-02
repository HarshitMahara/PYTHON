#Sieve Of Eratosthenes

# sieve of eratosthenes is a simple and ancient algo used to find prime numbers upto any given limit . 
#It is one of the most efficient ways to find small prime numbers for a given upper limit n , the algo. works by itratively marking the multiples of primes at composites.starting from 2 .
#Once all multilples of 2 have been marked composite, the multiples of next primes , the process continues untill p*p<=n, p=current prime number .
# Following is the algo of the sieve of eratosthenes to find the prime numbers
#1- To find out all primes under small n , generates the list of all integers from 2 to n .
#2- Start with smallest prime numbers i.e, p=2.
#3- Marked all the multiples of p which are less than n as composites, for this we will mark it as 0(do not mark p itself as composites)
#4- Asign the value of p to the next non zero number in the list which is greater than p.
#5- Repeat the untill p*p<=n.


# sieve of eratosthenes (code)

n=int(input("Enter a number : "))
prime=[]
for i in range(n+1):
    prime.append(i)
prime[0]=0
prime[1]=0
p=2
while(p*p<=n):
    if(p!=0):
        for i in range (p*2,n+1,p):
            prime[i]=0
    p+=1
print("ALL PRIME NUMBERS UPTO ",n," ARE :")
for i in range (len(prime)):
    if (prime[i]!=0):
        print (prime[i],end=" ")
print()

