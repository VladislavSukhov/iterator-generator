import hashlib
import os

countries = 'wiki_countries.txt'
  
def hash_generator(file):
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        hash = hashlib.md5(line.encode()).hexdigest()
        yield hash

g = hash_generator(countries)        

print(next(g))
print(next(g))
print(next(g))