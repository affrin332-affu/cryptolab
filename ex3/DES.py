S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

P4_TABLE = [2, 4, 3, 1]


def permute(bits, table):
    return "".join(bits[i - 1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join('0' if a[i] == b[i] else '1' for i in range(len(a)))

def s_box_lookup(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], '02b')

def generate_keys(key, p10_table, p8_table):
    log = [f"Original Key: {key}"]
    
    p10 = permute(key, p10_table)
    log.append(f"After P10: {p10}")

    L, R = p10[:5], p10[5:]
    log.append(f"Split -> L={L}, R={R}")

    L, R = left_shift(L, 1), left_shift(R, 1)
    log.append(f"LS-1 -> L={L}, R={R}")
    k1 = permute(L + R, p8_table)
    log.append(f"Subkey K1: {k1}")

    L, R = left_shift(L, 2), left_shift(R, 2)
    log.append(f"LS-2 -> L={L}, R={R}")
    k2 = permute(L + R, p8_table)
    log.append(f"Subkey K2: {k2}")

    return k1, k2, log

def fk(bits, key, ep_table, round_num):
    log = []
    L, R = bits[:4], bits[4:]
    log.append(f"Round {round_num} Input: L={L}, R={R}")

    ep = permute(R, ep_table)
    log.append(f"EP(R): {ep}")

    x = xor(ep, key)
    log.append(f"XOR with K{round_num}: {x}")

    s0 = s_box_lookup(x[:4], S0)
    s1 = s_box_lookup(x[4:], S1)
    log.append(f"S0={s0}, S1={s1}")

    p4 = permute(s0 + s1, P4_TABLE)
    log.append(f"P4: {p4}")

    new_l = xor(L, p4)
    log.append(f"New L: {new_l}")

    return new_l + R, log

def run_sdes():
    pt = input("Enter 8-bit Plaintext: ").strip()
    key = input("Enter 10-bit Key: ").strip()
    
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]

    if len(pt) != 8 or len(key) != 10:
        print("Error: Plaintext must be 8 bits and Key must be 10 bits.")
        return

    k1, k2, key_log = generate_keys(key, P10, P8)
    print("\n--- Key Generation ---")
    print("\n".join(key_log))

    print("\n--- Encryption ---")
    ip_result = permute(pt, IP)
    print(f"After IP: {ip_result}")

    r1_result, r1_log = fk(ip_result, k1, EP, 1)
    print("\n".join(r1_log))

    swapped = r1_result[4:] + r1_result[:4]
    print(f"After Swap: {swapped}")

    r2_result, r2_log = fk(swapped, k2, EP, 2)
    print("\n".join(r2_log))

    cipher = permute(r2_result, IP_INV)
    print(f"\nFinal Ciphertext (After IP-1): {cipher}")

if __name__ == "__main__":
    run_sdes()

