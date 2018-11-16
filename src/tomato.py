# -*- coding: UTF-8 -*-
import time
import math

__all__ = ("Tomato",)


class Tomato(object):
    def __init__(self, body=35, rest=5, task_name="Simple Task", content=None):
        self.name, self.content = task_name, content
        self.body_time = int(body)
        self.rest_time = int(rest)
        self.start_time, self.end_time = None, None

    @property
    def state(self):
        if self.start_time is not None and self.end_time is None:
            return 'running'
        if self.start_time is None:
            return 'wait'
        if self.end_time is not None:
            return 'complete'

    def logger(self):
        content = f'# {self.name} b{self.body_time}r{self.rest_time}\n'
        content += f'state: {self.state}\n'
        content += f'content: {self.content}\n'
        print(content)

    def start(self):
        self.start_time = time.time()

    def runtime_check(self):
        min, sec = self.overtime(), self.overtime_sec()
        if self.state == "running" and sec <= 0:
            self.end_time = time.time()
        return min, int(sec) % 60

    def runtime(self):
        return math.floor(self.runtime_sec() / 60)

    def runtime_sec(self):
        return int(time.time() - self.start_time)

    def overtime(self):
        return self.body_time - math.ceil(self.runtime_sec() / 60)

    def overtime_sec(self):
        return self.body_time * 60 - self.runtime_sec()


if __name__ == '__main__':
    t1 = Tomato()
    t1.logger()
    t1.run()
    time.sleep(2)
    print(t1.runtime())
    print(t1.runtime_sec())
    t1.logger()
