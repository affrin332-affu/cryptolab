# NOTE: Educational simplified AES-CMAC (not production secure)

BLOCK_SIZE = 16

# Simple XOR
def xor_bytes(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

# Pad message
def pad(message):
    padding_len = BLOCK_SIZE - len(message)
    return message + bytes([padding_len] * padding_len)

# Fake AES block encryption (for demonstration)
def simple_aes_encrypt(block, key):
    # NOT real AES — simplified mixing
    result = bytearray(block)
    for i in range(len(result)):
        result[i] ^= key[i % len(key)]
        result[i] = (result[i] * 7) % 256
    return bytes(result)

# Generate subkeys (simplified)
def generate_subkeys(key):
    zero_block = bytes([0]*BLOCK_SIZE)
    L = simple_aes_encrypt(zero_block, key)
    K1 = bytes([(b << 1) & 0xFF for b in L])
    K2 = bytes([(b << 1) & 0xFF for b in K1])
    return K1, K2

# CMAC function
def cmac(message, key):
    print("\n=== CMAC PROCESS ===")

    message = message.encode()
    key = key.encode()

    # Pad message
    if len(message) % BLOCK_SIZE != 0:
        message = pad(message)

    blocks = [message[i:i+BLOCK_SIZE] for i in range(0, len(message), BLOCK_SIZE)]

    print("Blocks:", blocks)

    K1, K2 = generate_subkeys(key)

    print("Subkey K1:", K1)
    print("Subkey K2:", K2)

    prev = bytes([0]*BLOCK_SIZE)

    for i, block in enumerate(blocks):
        print(f"\nBlock {i+1}: {block}")

        temp = xor_bytes(block, prev)
        print("After XOR:", temp)

        prev = simple_aes_encrypt(temp, key)
        print("After Encryption:", prev)

    tag = prev.hex()
    print("\nFinal CMAC:", tag)

    return tag


# -------- USER INPUT --------
msg = input("Enter message: ")
key = input("Enter key: ")

tag = cmac(msg, key)

verify_msg = input("\nEnter message to verify: ")
new_tag = cmac(verify_msg, key)

print("\n=== VERIFICATION ===")
print("Original Tag:", tag)
print("New Tag:", new_tag)

if tag == new_tag:
    print("✅ Authentic")
else:
    print("❌ Tampered")
