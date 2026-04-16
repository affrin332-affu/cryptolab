import random

def power(base, exp, mod):
    """Efficient modular exponentiation: (base^exp) % mod"""
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def miller_rabin():
    val = input("\nEnter number to test: ")
    try:
        n = int(val)
    except ValueError:
        print("Invalid Number.")
        return

    if n < 2: print("RESULT: Composite"); return
    if n in (2, 3): print("RESULT: Prime"); return
    if n % 2 == 0: print("RESULT: Composite"); return

    # Write n-1 as 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    print(f"PREPARATION: n - 1 = {n-1} = 2^{s} * {d}")

    for i in range(1, 4):
        print(f"\n--- Iteration {i} ---")
        a = random.randint(2, n - 2)
        print(f"Picking random base a = {a}")
        
        x = power(a, d, n)
        print(f"Initial test: {a}^{d} mod {n} = {x}")

        if x == 1 or x == n - 1:
            print(f"Success: Passes Fermat's Little Theorem.")
            continue

        composite = True
        for r in range(1, s):
            x = (x * x) % n
            print(f"Squaring (step {r}): Result = {x}")
            if x == n - 1:
                print(f"Success: Found {n-1} after squaring.")
                composite = False
                break
        
        if composite:
            print(f"\nRESULT: {n} is DEFINITELY COMPOSITE.")
            return

    print(f"\nRESULT: {n} is PROBABLY PRIME.")

def basic_gcd():
    try:
        a_val = input("Value A: ")
        b_val = input("Value B: ")
        a, b = int(a_val), int(b_val)
    except ValueError: 
        print("Invalid input.")
        return
    
    limit = min(abs(a), abs(b))
    common = [i for i in range(1, limit + 1) if a % i == 0 and b % i == 0]
    
    if not common:
        print("GCD = 0 (or undefined for these inputs)")
    else:
        print(f"Common Divisors: {', '.join(map(str, common))}")
        print(f"GCD = {common[-1]}")

def euclidean_gcd():
    try:
        a_val = input("Value A: ")
        b_val = input("Value B: ")
        a, b = int(a_val), int(b_val)
    except ValueError:
        print("Invalid input.")
        return

    a, b = abs(a), abs(b)
    if a < b: a, b = b, a
    
    print("\nHand-calculated steps:\n")
    while b != 0:
        q = a // b
        r = a % b
        # Used '*' instead of the special multiply character to avoid encoding errors
        print(f"{a} = ({b} * {q}) + {r}")
        a, b = b, r
    print(f"\nGCD = {a}")

def main():
    while True:
        print("\n" + "="*20)
        print("   SELECT A TOOL")
        print("="*20)
        print("1. Miller-Rabin Test")
        print("2. Euclidean Algorithm")
        print("3. Basic GCD")
        print("4. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1': miller_rabin()
        elif choice == '2': euclidean_gcd()
        elif choice == '3': basic_gcd()
        elif choice == '4': 
            print("Exiting...")
            break
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    main()
