#!/usr/bin/python3

import random

l1 = set(random.randint(0, x) for x in range(random.randint(0, 50)))
l2 = set(random.randint(0, x) for x in range(random.randint(0, 50)))
print(f"Первое множество\n{l1}\nВторое множество\n{l2}")
print(f"Входят одновременно в оба множества\n{l1&l2}")
print(f"Входят только в первое множество, но не входят во второе\n{l1-l2}")
print(f"Входят только во второе множество, но не входят в первое\n{l2-l1}")
print(f"Входят в первое или во второе множество, но не в оба одновременно\n{l1^l2}")