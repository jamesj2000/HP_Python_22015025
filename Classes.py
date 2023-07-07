class MathSeries:
    @staticmethod
    def is_prime(number):
        """Checks if a number is prime."""
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_prime_numbers(self):
        """Generates prime numbers up to a given limit."""
        limit = int(input("Enter the limit: "))
        primes = []
        for num in range(2, limit + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes

    def fibonacci(self):
        """Generates Fibonacci series up to a given term."""
        num_terms = int(input("Enter the number of terms: "))
        fib = [0, 1]
        for i in range(num_terms - 2):
            fib.append(fib[-1] + fib[-2])
        return fib

    def geometric_progression(self):
        """Generates geometric progression with user-input values."""
        a = float(input("Enter the first term (a): "))
        r = float(input("Enter the common ratio (r): "))
        num_terms = int(input("Enter the number of terms: "))
        progression = [a]
        term = a
        for _ in range(num_terms - 1):
            term *= r
            progression.append(term)
        return progression

    def arithmetic_progression(self):
        """Generates arithmetic progression with user-input values."""
        a = float(input("Enter the first term (a): "))
        d = float(input("Enter the common difference (d): "))
        num_terms = int(input("Enter the number of terms: "))
        progression = [a]
        term = a
        for _ in range(num_terms - 1):
            term += d
            progression.append(term)
        return progression

    def permutation(self):
        """Generates all permutations of a given list."""
        lst = input("Enter a list of items (comma-separated): ").split(",")
        perms = self.permutation_helper(lst)
        return perms

    def permutation_helper(self, lst):
        """Helper function to generate all permutations."""
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        perms = []
        for i in range(len(lst)):
            m = lst[i]
            remaining_list = lst[:i] + lst[i+1:]
            for p in self.permutation_helper(remaining_list):
                perms.append([m] + p)
        return perms

# Example usage
ms = MathSeries()

# Check if a number is prime
number = int(input("Enter to test prime: "))
print(ms.is_prime(number))

# Generate prime numbers up to a given limit
primes = ms.get_prime_numbers()
print(primes)

# Generate the Fibonacci series up to a given term
fib = ms.fibonacci()
print(fib)

# Generate a geometric progression with user-input values
geometric = ms.geometric_progression()
print(geometric)

# Generate an arithmetic progression with user-input values
arithmetic = ms.arithmetic_progression()
print(arithmetic)

# Generate all permutations of a given list
perms = ms.permutation()
print(perms)
