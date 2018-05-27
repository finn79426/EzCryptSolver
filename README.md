# EzCryptSolver

This tool is to solve CTF decoding baby first Problem.
Give me the cipher, and i will decrypt/decode it！

Inspiration from [kaibro's EasyWebSolver](https://github.com/w181496/EasySolver)

# Feature

- Brute force all possible encoding
- Specifie FLAG header
- If find the FLAG, automatic copy to your clipboard
- Brute force Classical cipher is supported

# Requisites

python2.7 & pip

# Install

1. Clone this repo

```Shell
git clone https://github.com/finn79426/EzCryptSolver.git
```

2. Run setup.sh to get library 

```Shell
cd EzCryptSolver
chmod +x setup.sh && ./setup.sh
```

If you have problems with the installation, you can use this commands to install.

```Shell
pip2 install pyperclip
pip2 install termcolor
```

# Usage

For example (Base64)：

```Shell
python2 EzSolve.py RkxBR3toMHdwd25fYmlnX2dnfQ==
```

Now, you will get output like this：
![](https://i.imgur.com/N3DfWgv.png)

And also, you can specifie CTF FLAG header, just add `--key` argument.

```Shell
python2 EzSolve.py RkxBR3toMHdwd25fYmlnX2dnfQ== --key FLAG
```

Now, you will get output like this：
![](https://i.imgur.com/l8ukYqt.png)

If not find any pair Header, just no output.

One thing you should know, if your ciphertext has white space, use quotation marks, otherwise you will get an Error.

```Shell
python2 EzSolve.py "46 4c 41 47 7b 68 30 77 70 77 6e 5f 62 69 67 5f 67 67 7d"
```

By the way, **only specifie FLAG header can get Brute Force output**, like this：
![](https://i.imgur.com/H8OweEh.png)


# Algorithm completed

- [x] Hex
- [x] Binary
- [x] Decimal
- [x] Base64
- [x] Base32
- [x] Brute force：Transposition Cipher (only specified FLAG header)
- [x] Brute force：Caesar cipher (only specified FLAG header)
- [ ] URLencode
- [ ] ~~jsfuck~~
- [ ] ~~aaencode~~

# How to remove



# ToDo

- [x] Specified FLAG header
- [x] Decode algorithm Modularization
- [x] Key_Checking Function
- [ ] Find more encode type！
- [ ] Usage add
- [ ] ~~Import verbose mode~~
- [ ] ~~Double Encoding support~~
