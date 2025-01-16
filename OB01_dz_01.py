class Tasks():
    def __init__(self):
        self.task = []

    def add_task(self, name, dt):
        self.task.append([name, dt, False])

    def mark_task(self, name):
        pass

    def info_task(self):
        # print(self.task)
        for i in range(len(self.task)):
            print(i)
            print(self.task[i][0])
            
            # print(i[0]) # print(i[1]) # print(i[2])


tb = Tasks()
tb.add_task('Задача-1', '21-01-2025')
tb.add_task('Задача-2', '21-01-2025')
tb.info_task()
