from .tile_num import Numb_reader, print_tiles
import time
import os
import math

with open('5x3.txt', "r") as f:
    Nreader = Numb_reader(f.read())


def shift_num(num):
    ret = str(num)
    if len(ret) == 1:
        return "0" + ret
    return ret


def padding_val(w, h):
    ww = os.get_terminal_size().columns
    wh = os.get_terminal_size().lines

    top = wh / 2 - math.ceil(h / 2) - 1
    top = 0 if top < 0 else top

    left = ww / 2 - math.ceil(w / 2) - 1
    left = 0 if left < 0 else left
    return math.floor(top), math.floor(left)


class Clock(object):
    def __init__(self, color=8):
        self.color = color

    def display(self):
        print("\33[?25l")
        # hiddin cursor
        while True:
            top, left = padding_val((3 + 2) * 8, 3)

            now = time.localtime(time.time())
            os.system("clear")
            spaces = math.floor(left / 4)
            print("\n" * (top - 1))
            print_tiles(Nreader["~" * spaces + shift_num(now.tm_hour) + ":" +
                                shift_num(now.tm_min) + ":" + shift_num(now.tm_sec)], self.color)
            time.sleep(1)


if __name__ == '__main__':

    c = Clock(4)
    c.display()
