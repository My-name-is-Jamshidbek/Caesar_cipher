# ✨ Caesar Cipher 🔐🔤

Welcome to your classic **Caesar Cipher implementation**! With a sprinkle of Python magic, this tool effortlessly shifts your text letters by any number of positions—perfect for encoding and decoding secret messages! 🪄

## 🛠️ Features & Spells

- 🔒 **Two-Way Encryption**  
  - **Encode** your plaintext messages  
  - **Decode** your encrypted messages

- 🔄 **Flexible Shift Values**  
  Choose any shift value from 1-25 for your encryption needs!

- 🧩 **Case Preservation**  
  Maintains uppercase and lowercase letters exactly as you wrote them.

- 🔤 **Non-Alphabetic Character Preservation**  
  Numbers, spaces, and punctuation stay untouched—only letters get the cipher treatment!

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/My-name-is-Jamshidbek/Caesar_cipher.git
cd Caesar_cipher
```

### 2. Run the Caesar Cipher
```bash
python3 main.py
```

---

## ▶️ Usage

### Basic Example

```python
from main import Ceaser_cipher

# Create a Caesar cipher with shift value of 3
cipher = Ceaser_cipher(3)

# Encode a message
original_text = "Hello World!"
encoded_text = cipher.encod(original_text)
print(f"Original: {original_text}")
print(f"Encoded: {encoded_text}")  # Output: "Ebiil Tloia!"

# Decode the message back
decoded_text = cipher.decod(encoded_text)
print(f"Decoded: {decoded_text}")  # Output: "Hello World!"
```

### Advanced Usage

```python
# Try different shift values
cipher_5 = Ceaser_cipher(5)
cipher_13 = Ceaser_cipher(13)  # ROT13

# Encode with different shifts
message = "Secret Message"
encoded_5 = cipher_5.encod(message)
encoded_13 = cipher_13.encod(message)

print(f"Shift 5: {encoded_5}")
print(f"Shift 13 (ROT13): {encoded_13}")
```

---

## 📁 Project Structure

```
.
├── main.py              # 🔐 Caesar cipher implementation
└── README.md            # 📖 This documentation
```

---

## 🔍 How It Works

The Caesar cipher shifts each letter in the alphabet by a fixed number of positions:

- **Encoding**: Shifts letters forward in the alphabet
- **Decoding**: Shifts letters backward in the alphabet
- **Wrap-around**: 'z' + 1 = 'a', 'a' - 1 = 'z'

### Algorithm Details

1. **Alphabet Mapping**: Creates a shifted alphabet based on the shift value
2. **Character Processing**: 
   - Alphabetic characters get shifted according to the mapping
   - Case is preserved (uppercase stays uppercase)
   - Non-alphabetic characters remain unchanged
3. **Bidirectional**: Same cipher instance can both encode and decode

---

## 🎯 Class Methods

### `Ceaser_cipher(n)`
- **Parameter**: `n` - Shift value (integer)
- **Description**: Initialize cipher with shift value

### `encod(text)`
- **Parameter**: `text` - String to encode
- **Returns**: Encoded string
- **Description**: Encode plaintext using Caesar cipher

### `decod(text)`
- **Parameter**: `text` - String to decode  
- **Returns**: Decoded string
- **Description**: Decode ciphertext using Caesar cipher

---

## 🤝 Contributing

We love new contributors! 🎉 Please open an issue or PR to:

- Add command-line interface 💻  
- Implement batch file processing 📁  
- Add support for other alphabets 🌏  
- Enhance error handling 🛡️  

---

## 📚 Educational Use

Perfect for:
- Learning cryptography basics 🎓
- Understanding classical ciphers 📜
- Teaching alphabet manipulation 🔤
- Demonstrating Python programming concepts 🐍

Happy encoding! ✨🔐