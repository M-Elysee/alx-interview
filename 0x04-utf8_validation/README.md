<h1>0x04. UTF-8 Validation</h1>

<h2>Resources</h2>

[UTF-8](https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ)<br/>
[Characters, Symbols, and the Unicode Miracle](https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw)<br/>

<h2>Requirements</h2>
<h2>General</h2>
<ul>
    <li>Allowed editors: vi, vim, emacs</li>
    <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly #!/usr/bin/python3</li>
    <li>A README.md file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the PEP 8 style (version 1.7.x)</li>
    <li>All your files must be executable</li>
</ul>

<li>Tasks</li>

0. UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
```
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
Repo:

GitHub repository: alx-interview
Directory: 0x04-utf8_validation
File: 0-validate_utf8.py
```