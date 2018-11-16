# -*- coding: UTF-8 -*-
from .tile_num import Numb_reader, print_tiles
from .clock import padding_val, shift_num
from .tomato import Tomato
import time
import os
import math
import random

__all__ = ("Scheduler",)

with open('5x3.txt', "r") as f:
    Nreader = Numb_reader(f.read())


def rest(rest_time=5):
    print("Rest,now ", end="")
    tomato = Tomato(rest_time)
    tomato.start()
    while True:
        min, sec = tomato.runtime_check()
        print(shift_num(min) + ":" + shift_num(sec), end='')
        for i in range(5):
            print(">", end='', flush=True)
            time.sleep(0.2)
        print("\b" * 10 + " " * 10 + "\b" * 10, end='')

        # end
        if tomato.state == "complete":
            break


class Scheduler(object):
    """Tomato manger"""

    def __init__(self, tasks=None, color=8, isRandom=False):
        self.tasks = tasks
        self.color = color
        self.cur_task = None
        self.random = isRandom

    def next(self):
        if len(self.tasks) != 0:
            if self.random:
                self.cur_task = random.choice(self.tasks)
                self.tasks.remove(self.cur_task)
                self.run()
            else:
                self.cur_task = self.tasks.pop(0)
                self.run()

    def run(self):
        os.system("clear")
        print("\33[?25l")
        # hiddin cursor
        self.cur_task.start()
        while True:
            # center layout
            top, left = padding_val((3 + 2) * 5, 3)
            spaces = math.floor(left / 4)
            # space with 2 gap-block = 4

            # mage display string
            min, sec = self.cur_task.runtime_check()
            disStr = f"{'~' * spaces}{shift_num(min)}:{shift_num(sec)}"

            # display
            print("\n" * (top - 1))
            print_tiles(Nreader[disStr], self.color)
            print(" " * left + self.cur_task.name)
            # >> content
            if self.cur_task.content:
                print(" " * left + self.cur_task.content)
            time.sleep(1)
            # cls
            os.system("clear")

            # tomato done.
            if self.cur_task.state == 'complete':
                self.cur_task.logger()
                rest(self.cur_task.rest_time)
                self.next()
                break
