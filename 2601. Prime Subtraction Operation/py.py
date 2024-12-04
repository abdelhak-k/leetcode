
class Solution:
    def max_prime_below_index(self):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        res = [0] * 1001
        max_prime = 0

        for i in range(2, 1001):
            res[i] = max_prime
            if is_prime(i):
                max_prime = i

        return res

    def primeSubOperation(self, nums: List[int]) -> bool:
        max_primes_below = self.max_prime_below_index()
        n= len(nums)
        prv=0
        for i in range(n-1):
            nums[i]-=  max_primes_below[nums[i]-prv]
            if nums[i]>=nums[i+1]:
                return False
            prv= nums[i]
        return True