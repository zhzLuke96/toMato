#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import configparser
from src.tomato import Tomato
from src.scheduler import Scheduler
import click


def get_tasks_conf(filename="./tasks.ini"):
    conf = configparser.ConfigParser()
    conf.read(filename, encoding="utf-8-sig")
    sections = conf.sections()
    ret_right = []
    for i in sections:
        ret_right.append(dict(conf.items(i)))
    return dict(zip(sections, ret_right))


def farm(orders):
    ret = []
    for key, val in orders.items():
        toma = Tomato(body=val["time"], rest=val["rest"],
                      task_name=key, content=val["content"])
        ret.append(toma)
    return ret

# entry point


@click.command()
@click.option('--name', default=None, help='Your task name.')
@click.option('--time', default=25, help='single task cast time.')
@click.option('--rest', default=5, help='single task rest time.')
@click.option('--mode', default="random", help='Scheduler policy. *Single task dont to set up.')
@click.option('--conf', default="tasks.ini", help='task config file name.')
@click.option('--color', default=4, help='display font color.')
def hello(name, time, rest, mode, conf, color):
    """The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks."""
    tasks = get_tasks_conf(conf)
    # default
    if not name and not time and not rest and not mode:
        tomatos = farm(tasks)
        manager = Scheduler(tomatos, color=color, isRandom=True)
    # single task
    if name is not None:
        if name in tasks:
            task = tasks[name]
            tom = Tomato(task["time"], task["rest"], name, task["content"])
        else:
            print("The task name is not in configuration file. Please input description and create temporary tasks for you.")
            description = input("task description:")
            tom = Tomato(time, rest, name, description)
        manager = Scheduler([tom], color=color, isRandom=False)
    # mode choice
    if name is None:
        tomatos = farm(tasks)
        isRandom = True if mode == "random" else False
        manager = Scheduler(tomatos, color=color, isRandom=isRandom)

    manager.next()


if __name__ == '__main__':
    hello()
