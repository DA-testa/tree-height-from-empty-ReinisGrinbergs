import sys
import threading
import numpy


def compute_height(n, vecaki):
    h = [0] * n
    for i in range(n):
        if not h[i]:
            node = i
            augst = 1
            while vecaki[node] != -1:
                 if h[vecaki[node]]:
                      augst += h[vecaki[node]]
                      break
                 node = vecaki[node]
                 augst += 1
            h[i] = augst
    return max(h)
def main():
    inpt = input().upper()
    vecaki = None
    n = None
    if inpt == "I":
          n = int(input())
          vecaki = list(map(int, input().split()))
    elif inpt == "F":
        filen = input()
        if "a" in filen.lower():
              print("a not allowed")
              return
        try:
            with open(filen, mode="r") as f:
                x = f.readlines()
                n = int(x[0])
                vecaki = list(map(int, x[1].split()))
        except FileNotFoundError:
           print("File does not exist")
           return
    else:
        print("Incorrect input")
        return
    print(compute_height(n, vecaki))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
