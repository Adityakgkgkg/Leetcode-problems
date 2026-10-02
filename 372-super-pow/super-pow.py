class Solution(object):
    def superPow(self, a, b):
        MOD = 1337
        def Pow(x, n):
            result = 1
            while n > 0:
                if n % 2 == 1:
                    result =(result * x) % MOD
                x = (x * x) % MOD
                n //=2
            return result

        result = 1  
        for num in b:
            result = (Pow(result,10) * Pow(a, num)) % MOD
        return result
        