# HashSnake
HashSnake is a lightweight hash recovery tool designed to recover the plain-text value of a hash using a wordlist-based comparison approach.
It works by hashing each candidate word from a provided wordlist and comparing it against the target hash until a match is found.

# Description

HashSnake performs dictionary-based hash recovery (also known as wordlist-based cracking).

# The process is simple:
  ## The user is required to provide:
   1. A hash (using the -t option) // -t 717d3e7b9278e122e65d6240c7ea9b81 (which plain-text value of that hash is 'clarus')
   2. As well as a worldist (using the -w option) // -w rockyou.txt
   3. And an algorithm (using the -a option) // -a md5.

  Example usage: <br>
    <img width="811" height="35" alt="image" src="https://github.com/user-attachments/assets/a0426cf0-3178-4d39-b4cb-23d2457ba8fe" />

  <img width="604" height="288" alt="image" src="https://github.com/user-attachments/assets/de3e8ae6-7902-4e1b-8c06-31e9243e7182" />

  
  ## GUI (Graphical User Interface)

  To use the GUI, the user must provide the `--gui` argument when running `main.py`.

  ```bash
  python main.py --gui
  ```

  In the GUI environment the user is required to provide a Hash (Supported hash algorithms are - MD5, SHA1, SHA224, SHA256, SHA512, BCrypt), a wordlist, and salt which is optional.
# Installation:
  1. The repository can be clonned using - git clone https://github.com/RuslanVe0/HashSnake.git
  2. Important libraries are required to be installed such as BCrypt.



  
