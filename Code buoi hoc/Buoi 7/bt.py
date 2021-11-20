#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif 20 < n:
            print("Not weird")
        