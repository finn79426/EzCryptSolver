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

python2.7 & pip

# Install

1. Clone this repo

```Shell
git clone https://github.com/finn79426/EzCryptSolver.git
```

2. Using pip to get essential libraries

```shell
cd EzCryptSolver
pip install -r requirements.txt
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


# Algorithm completed

- [x] Hex
- [x] Binary
- [x] Decimal
- [x] Base64
- [x] Base32
- [x] Brute force：Transposition Cipher (only specified FLAG header)
- [x] Brute force：Caesar cipher (only specified FLAG header)
- [ ] ~~URLencode~~
- [ ] ~~jsfuck~~
- [ ] ~~aaencode~~

# Contact

My Email：finn79426@gmail.com

如果你找到 Bug 或 Error msg，發給我一個 issues <br>
或者如果你有更好的想法，歡迎 Fork、PR

# How to remove

Just remove the clone Folder.

```Shell
cd ../
rm EzCryptSolve -r
```

# ToDo

- [x] Specified FLAG header
- [x] Decode algorithm Modularization
- [x] Key_Checking Function
- [ ] Find more encode type！
- [x] Usage add
- [ ] ~~Import verbose mode~~
- [ ] ~~Double Encoding support~~
- [x] Customize your FLAG header list
