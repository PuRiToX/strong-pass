# 🔒 StrongPass - Password Strength Analyzer & Pwned Checker

A password checker in Python that analyzes password strength and checks for leaks in data breaches. StrongPass is a Python program made by [PuRiToX](https://github/puritox/) that allows you to check the strength of a password locally and remotely using the "[Have I Been Pwned](https://haveibeenpwned.com/)" API. This is done in a completely secure manner and without compromising the password.

## How does it work?
Run the program and enter your password. It will first check that it meets basic security rules and then see if your password is in the Rockyou dictionary locally. (For this, you must have the dictionary in the "strong_pass.py" folder.)

Finally, it will check that your password hasn't been leaked online using the HIBP API.

If you encounter any of these problems, the program will suggest a randomly generated, completely secure 16-character password.

## What is the HIBP API?

It's a free service from Have I Been Pwned that allows you to check if a password has been exposed in public data breaches.
Key Features:

-Uses k-anonymity to protect your privacy (you never send the full password).

-Contains over 800 million compromised passwords.

## Why Is It Secure?

Privacy:
The full password is never sent, only a fragment of the hash. Not even HIBP knows which password you're verifying.

Efficiency:
The API returns multiple hashes with the same prefix, reducing the risk of identification.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## ✨ Characteristics

- **Strength Analysis**:
  - Minimum length (8+ characters)
  - Requires uppercase, lowercase, numbers, and special characters
  - Detailed scoring system

- **Common Password Detection**:
  - Comparison with 14 million passwords (rockyou.txt)
  - Case-insensitive mode

- **Leak Check**:
  - Integration with [Have I Been Pwned](https://haveibeenpwned.com/)
  - Uses **k-anonymity** to protect your privacy

- **Extras**:
  - Secure password generator
  - Graphical user interface support (Tkinter) (Not Released!)

## 📦 Prerequisites

- Python 3.6+
- Modules: `requests`, `hashlib`
- (Optional but Recomended) File: [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) (1.4 GB)

## 🚀 Setup

1. Clone the repository:
```bash
git clone https://github.com/PuRiToX/strong-pass.git
cd strong-pass
```

2. Install dependencies:
```bash
pip install requests
```

3. If you want to check the passwords locally with a common dictionary you'll need to download `rockyou.txt` and place it in the sofware root directory.

```bash
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

🔍 **Notes to Know**:
  - The `hashlib`, `os`, and `pathlib` modules come preinstalled with Python.
  - You only need to install `requests` externally.
  - If you don't download the `rockyou.txt` the program will ignore the local verification and will let you know.
  - We recommend downloading `rockyou.txt` since there are passwords that are there and are not in the API.

## 🛠 Preview usage

### Password Checker
```bash
python strong_pass.py
```
**Example output**:
```
🔒 Password Strenght Validator 🔒
Enter you password: ha^&#764AdC
✅ Complies with basic safety rules

🔍 - Loading the common dictionary 'Rockyou'
Loaded passwords: 14343756
Examples: ['', 'fresastar', 'sexies#1', 'sharonlisa', 'sileluskin']
✅ The password isn't in the dictionary.

🔍 Checking with the I Been Pwned API
✅ Not found in known leaks.


🏆 Security Level: Very Strong
```

## 🤝 Contributions
All contributions are welcome! Follow these steps:
1. Fork the project
2. Create your branch (`git checkout -b feature/new-feature`)
3. Commit the changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.

## 🙏 Acknowledgments
- [Have I Been Pwned](https://haveibeenpwned.com/) for the Password API
- [rockyou.txt](https://wiki.skullsecurity.org/Passwords) Dataset (educational use)

---

**⚠️ Note**: This project is for educational purposes. We do not store or transmit passwords.