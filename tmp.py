# -*- coding:utf-8 -*-

from PyPDF2 import PdfFileReader
import re

with open('tmp.txt', 'r') as f:
    content = f.read()
    f.close()
print(repr(content))

res = re.search(rf"^1(([\s\S])*?)？$", content, flags=re.M | re.S)
print(res)