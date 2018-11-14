import time
import collections

START = 1542057513.2037964

#TaskDays = collections.namedtuple("TaskDays", ['task', 'days'])


class TaskDays:
    def __init__(self, task, start=None):
        self.task = task
        if start is None:
            start = START
        self.start = start

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "{}(task={}, days={})".format(
            __class__.__name__, self.task, self.days
        )

    def seconds_to_days(self, seconds):
        return (seconds - self.start) / 60 / 60 / 24

    def reset(self):
        self.start = time.time()

    @property
    def days(self):
        return self.seconds_to_days(time.time())


class TaskList:
    def __init__(self, file):
        self.lst = list()
        with open(file) as f:
            for line in f:
                task, start = line.split(";")
                self.lst.append(TaskDays(task, float(start)))
        self.file = file

    def __repr__(self):
        return str(self.lst)

    def __str__(self):
        return repr(self)

    def __getitem__(self, index):
        return self.lst[index]

    def update_file(self):
        with open(self.file, mode="w") as f:
            for task in self.lst:
                f.write("{};{}\n".format(task.task, task.start))


task_list = TaskList("data.txt")


def add_task(task: str, days=None):
    task = TaskDays(task)
    task_list.append(task)
    with open("data.txt", "a+") as f:
        f.write("{};{}\n".format(task.task, task.start))


# print(task_list)
# task_list[0].reset()
print(task_list)
