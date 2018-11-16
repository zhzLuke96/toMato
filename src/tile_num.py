# -*- coding: UTF-8 -*-
__all__ = ("Numb_reader", "print_tiles")


def buf_link(buf1, buf2, ext=""):
    height = max(len(buf1), len(buf2))
    ret = []
    for i in range(height):
        ret.append(buf1[i] + ext + buf2[i])
    return ret


class Numb_reader(object):
    def __init__(self, text):
        self.lib = {}
        self.read(text)

    def read(self, text):
        lines = text.split("\n")
        temp = ""
        for line in lines:
            if line == "":
                self.lib[temp[:1]] = temp[1:-1]
                temp = ""
            else:
                temp += line + "\n"

    def long_num(self, key, gap=2):
        bufs = [self.lib[str(index)].split() for index in key]
        ret = bufs[0]
        for buf in bufs[1:]:
            ret = buf_link(ret, buf, "0" * gap)
        return "\n".join(ret)

    def __getitem__(self, key):
        key = str(key)
        length = len(key)
        if length == 1:
            return self.lib[key]
        else:
            return self.long_num(key)


def print_tiles(tiles, fc=8, bgc=1):
    fc = fc + 39
    bgc = bgc + 39
    for token in tiles:
        if token == "1":
            print(f'\033[1;{fc-10};{fc}m \033[0m', end="")
        elif token == "0":
            print(f'\033[1;{bgc-10};{bgc}m \033[0m', end="")
        elif token == "\n":
            print("")
    print("")


def rinbow_tiles(tiles):
    from random import choice
    for token in tiles:
        mod = choice([0, 1, 4, 5, 7])
        fc = 40 + choice(range(1, 8))
        if token == "1":
            print(f'\033[{mod};{fc-10};{fc}m \033[0m', end="")
        elif token == "0":
            print(f'\033[0;{30};{40}m \033[0m', end="")
        elif token == "\n":
            print("")
    print("")


if __name__ == '__main__':
    import os
    import time
    with open('5x3.txt', "r") as f:
        text = f.read()
        T = Numb_reader(text)
        # print(T.lib)
        # print(T[0])
        # print(T[3])
        # print(T[4])
        # print()
        # count = 1
        # while True:
        #     count += 1
        #     rinbow_tiles(T[count])
        #     print_tiles(T[count])
        #     time.sleep(.1)
        #     os.system('clear')
        print_tiles(T["~+-*/!?%^&()|\"'"])
        print()
        # rinbow_tiles(T["99.99"])
        # print()
        # print_tiles(T["75:11"])
        # print()
        # print_tiles(T[f"45-68={45-68}"])
        print_tiles(T[f"8*(9-5)/32={8*(91-54)/32}"])
        print()
        print_tiles(T[f"15*8={15*8}"])
