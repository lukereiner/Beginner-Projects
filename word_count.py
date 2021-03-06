# -*- coding: utf-8 -*-
"""Word Count

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bBAdZe2-RB3TPBWrn0oI5blDoBgWNObQ

Resources:
https://docs.python.org/2/library/collections.html#collections.Counter

https://docs.python.org/3/library/re.html

https://blog.usejournal.com/regular-expressions-a-complete-beginners-tutorial-c7327b9fd8eb

https://www.guru99.com/python-regular-expressions-complete-tutorial.html
"""

from google.colab import drive
import collections as co
import re
drive.mount('/content/drive/')

# Search for a word of your choice #
word_search = input("Search for word: ").lower()
words = re.findall(r'\b%s\b'%word_search, open('/content/drive/My Drive/Colab Notebooks/Beginner Projects/White Fang.txt').read().lower())
co.Counter(words)

# Search for most common words #
words = re.findall('\w+', open('/content/drive/My Drive/Colab Notebooks/Beginner Projects/White Fang.txt').read().lower())
co.Counter(words).most_common(10)