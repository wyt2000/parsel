import sys
import time
import itertools
from itertools import accumulate, product, permutations, combinations
import collections
from collections import Counter, OrderedDict, deque, defaultdict, ChainMap
from functools import lru_cache
import math
from math import sqrt, sin, cos, tan, ceil, fabs, floor, gcd, exp, log, log2
import fractions
from typing import List, Tuple
import numpy as np
import random
import heapq
# Splits l on space, converts each element to int, and returns the result of converting the result to a list.

def main(l):
    return list(map(int, l.split()))


assert repr(str(main("10 1"))) == repr(str([10, 1])) or (main("10 1") == [10, 1])
