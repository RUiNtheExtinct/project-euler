MAX_SIZE = 2000001
isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * (MAX_SIZE)


def sieve(N):
    isprime[0] = isprime[1] = False
    for i in range(2, N):
        if isprime[i] == True:
            prime.append(i)
            SPF[i] = i
        j = 0
        while j < len(prime) and i * prime[j] < N and prime[j] <= SPF[i]:
            isprime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j]
            j += 1


N = int(input())
sieve(N)
print(prime)