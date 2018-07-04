class PrimeGenerator: 
    def __init__(self):
        self.Sieve(10000)
    
    def get(self):
        return self.primes[self.index]
 
    def next(self):
        self.index += 1
 
    def Sieve(self, rng):
        sieve = [True for _ in range(rng+1)]
        sieve[0:1] = [False, False]
        for start in range(2, rng+1):
            if sieve[start]:
                for i in range(2 * start, rng + 1, start):
                    sieve[i] = False
        primes = []
        for i in range(2, rng+1):
            if sieve[i]:
                primes.append(i)
        self.primes = primes
        self.index = 0
 
t = PrimeGenerator()
print(t.get())
t.next()
print(t.get())
t.next()
print(t.get())
 