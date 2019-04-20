# EzCryptSolver

This tool is to solve CTF decoding baby first Problem.
Give me your cipher, and i will decrypt/decode it！

Inspiration from [kaibro's EasyWebSolver](https://github.com/w181496/EasySolver)

# Feature

- Brute force all possible encode
- Specifie FLAG header
- If find the FLAG, automatic copy to your clipboard
- Brute force Classical cipher supported
- Specifie FLAG header as your custom list

# Requisites

python2.7 & pip2

# Install

1. Clone this repo

```Shell
git clone https://github.com/finn79426/EzCryptSolver.git
```

2. Using pip to get essential libraries

```shell
cd EzCryptSolver
pip2 install -r requirements.txt --user
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

If not find any compare FLAG, just no output.

One thing you should know, if your ciphertext has white space, use quotation marks, otherwise you will get an Error.

```Shell
python2 EzSolve.py "46 4c 41 47 7b 68 30 77 70 77 6e 5f 62 69 67 5f 67 67 7d"
```

By the way, **only specified FLAG header can get Brute Force output**, like this：
![](https://i.imgur.com/H8OweEh.png)


2018/7/26 Update:
You can preparatory CTFs FLAG header, so you don't have to use `--key` in CTF anymore!

Add `-l` to enable longlist support

![](https://i.imgur.com/rkz2NFw.png)


# Algorithm completed

- Encode transform
  - [x] Hex
  - [x] Binary
  - [x] Decimal
  - [x] Base64
  - [x] Base58
  - [x] Base32
  - [x] Base16
  - [x] URLencoded
  - [x] HTML Entity
- Brute force (Enable when using `-l` or `--key`)
  - [x] Transposition Cipher
  - [x] Caesar cipher

# Contact

My Email：finn79426@gmail.com

如果你找到 Bug 或 Error msg，發給我一個 issues <br>
或者如果你有更好的想法，歡迎 Fork、PR

# How to remove

Just remove the clone Folder.

```Shell
pip2 uninstall -r requirements.txt --yes
cd ../
rm EzCryptSolve -r
```

# ToDo

- [x] Specified FLAG header
- [x] Decode algorithm Modularization
- [x] Key_Checking Function
- [x] Usage add
- [x] Customize your FLAG header list
