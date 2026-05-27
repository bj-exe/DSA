import math

class PrimeCheckAlgorithms:

    # Algorithm 1 (n-1)
    @staticmethod
    def is_prime_n_minus_1(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # Algorithm 2 (n/2)
    @staticmethod
    def is_prime_half(n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    # Algorithm 3 (sqrt)
    @staticmethod
    def is_prime_sqrt(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def main():
    while True:
        try:
            number = int(input("\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check with all algorithms
        algorithm1 = PrimeCheckAlgorithms.is_prime_n_minus_1(number)
        algorithm2 = PrimeCheckAlgorithms.is_prime_half(number)
        algorithm3 = PrimeCheckAlgorithms.is_prime_sqrt(number)

        print(f"\nResults for {number}:")
        print(f"Algorithm 1 (2 to n-1): {'Prime' if algorithm1 else 'Not Prime'}")
        print(f"Algorithm 2 (2 to n/2): {'Prime' if algorithm2 else 'Not Prime'}")
        print(f"Algorithm 3 (2 to √n): {'Prime' if algorithm3 else 'Not Prime'}")

        if algorithm1 == algorithm2 == algorithm3:
            print(f"All algorithms agree: {'Prime' if algorithm1 else 'Not Prime'}")
        else:
            print("Algorithms do not agree. Check implementation.")

        choice = input("\nWant to try again? (Y/N): ").strip().lower()
        if choice != 'y':
            break

    print("\nProgram ended.")

if __name__ == "__main__":
    main()
