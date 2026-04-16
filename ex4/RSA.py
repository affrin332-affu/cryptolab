def run_rsa():
    p = int(input("Enter Prime p: ") or 3)
    q = int(input("Enter Prime q: ") or 11)
    e = int(input("Enter Public Exponent (e): ") or 3)
    msg = int(input("Enter Message (Number): ") or 7)

    n = p * q
    phi = (p - 1) * (q - 1)

    d = -1
    for i in range(1, phi):
        if (e * i) % phi == 1:
            d = i
            break

    if d == -1:
        print("Error: 'e' is not coprime with phi. Choose a different 'e'.")
        return

    cipher = pow(msg, e, n)
    decrypted = pow(cipher, d, n)

    print("\n=== RSA RESULT ===")
    print(f"n (p*q) = {n}")
    print(f"phi (p-1)(q-1) = {phi}")
    print(f"Private Key (d) = {d}")
    print(f"Encrypted Cipher = {cipher}")
    print(f"Decrypted Message = {decrypted}")
    
    if msg == decrypted:
        print("Success!")

if __name__ == "__main__":
    run_rsa()

