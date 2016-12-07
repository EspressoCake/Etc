#!/usr/bin/python
import sys
import numpy as np
import pylab as pl

def length():
    with open(sys.argv[1], 'r') as f:
        return sum(1 for _ in f)


if __name__ == '__main__':
    DATA = "abcdefghijklmnopqrstuvwxyz1234567890"
    dataset = dict.fromkeys(DATA, 0)

    with open(sys.argv[1], 'r') as file:
        for line in file.readlines():
            if line.strip() != "":
                try:
                    data = dict.fromkeys(line.strip(), 0)
                    for c in line.strip():
                        data[c] += 1
                    for k in dataset:
                        if k in data:
                            dataset[k] += data[k]
                except Exception,e:
                    pass
            else:
                pass

    X = np.arange(len(dataset))
    pl.bar(X, dataset.values(), align='center', width=0.5)
    pl.xticks(X, dataset.keys())
    ymax = max(dataset.values()) + 1
    pl.ylim(0, ymax)
    pl.ylabel("Frequency")
    pl.xlabel("Characters")
    pl.title("Distribution of Characters in Sample of {0} NETSESSION Cookies".format(length()))
    pl.show()
