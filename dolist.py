import time
import collections

START = 1542057513.2037964

#TaskDays = collections.namedtuple("TaskDays", ['task', 'days'])


class TaskDays:
    def __init__(self, task):
        self.task = task
        self.start = START

    def __str__(self):
        return "1"

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


task_list = list()


def add_task(task: str, days=None):
    task = TaskDays(task)
    task_list.append(task)
    with open("data.txt", "a+") as f:
        f.write("{};{}\n".format(task.task, task.days))


add_task("Do German Quizlet.")
add_task("BMO1 prep.")
add_task("Clarinet practice.")
add_task("Brilliant.")
add_task("Finance.")
add_task("Anime.")
add_task("Minecraft.")

print(task_list)
task_list[0].reset()
print(task_list)
