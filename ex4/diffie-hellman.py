def run_diffie_hellman():
    p = int(input("Enter Prime (p): ") or 23)
    g = int(input("Enter Generator (g): ") or 5)
    a = int(input("Enter Alice Private (a): ") or 6)
    b = int(input("Enter Bob Private (b): ") or 15)

    alice_public = pow(g, a, p)
    bob_public = pow(g, b, p)

    alice_secret = pow(bob_public, a, p)
    bob_secret = pow(alice_public, b, p)

    print("\n=== DIFFIE-HELLMAN RESULT ===")
    print(f"Alice Public Key: {alice_public}")
    print(f"Bob Public Key:   {bob_public}")
    print(f"Alice Shared Secret: {alice_secret}")
    print(f"Bob Shared Secret:   {bob_secret}")
    
    if alice_secret == bob_secret:
        print("Keys Match!")

if __name__ == "__main__":
    run_diffie_hellman()
