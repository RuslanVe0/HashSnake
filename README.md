# HashSnake
HashSnake is a lightweight hash recovery tool designed to recover the plain-text value of a hash using a wordlist-based comparison approach.
It works by hashing each candidate word from a provided wordlist and comparing it against the target hash until a match is found.

# Description

HashSnake performs dictionary-based hash recovery (also known as wordlist-based cracking).

# The process is simple:
  ## The user is required to provide:
   1. A hash (using the -t option) // -t 717d3e7b9278e122e65d6240c7ea9b81 (which plain-text value of that hash is 'clarus')
   2. As well as a worldist (using the -w option) // -w rockyou.txt
   3. And an algorithm (using the -a option) // -a MD5.

  Example usage: <img width="811" height="35" alt="image" src="https://github.com/user-attachments/assets/a0426cf0-3178-4d39-b4cb-23d2457ba8fe" />



  
