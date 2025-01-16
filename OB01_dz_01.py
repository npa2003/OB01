class Tasks():
    def __init__(self):
        self.task = []

    def add_task(self, name, dt):
        self.task.append([name, dt, False])
        print(f'Задача с именем: {name}   Добавлена.')

    def mark_task(self, name):  # отмечаем задание по имени
        for i in range(len(self.task)):
            if self.task[i][0] == name:
                self.task[i][2] = True

    def info_task(self):  # вывод всех задач
        for i in range(len(self.task)):
            marked = 'НЕ выполнена'
            if self.task[i][2]:
                marked = 'Выполнена'
            print(f'{i + 1}.   {self.task[i][0]}   {self.task[i][1]}   {marked}')

    def info_task_marked(self):  # вывод отмеченных задач
        for i in range(len(self.task)):
            marked = 'НЕ выполнена'
            if self.task[i][2]:
                marked = 'Выполнена'
                print(f'{i + 1}.   {self.task[i][0]}   {self.task[i][1]}   {marked}')

    def info_task_unmarked(self):  # вывод НЕотмеченных задач
        for i in range(len(self.task)):
            marked = 'НЕ выполнена'
            if not self.task[i][2]:
                print(f'{i + 1}.   {self.task[i][0]}   {self.task[i][1]}   {marked}')


# __________________________________________________________________________________________

def com_list():
    print('\n/list - вывести список невыполненных задач')
    print('/listm - вывести выполненных список задач')
    print('/lista - вывести список ВСЕХ задач')
    print('/add NAME DATE - добавить задачу с именем NAME и сроком исполнения DATE')
    print('/mark NAME - отметить задачу с именем NAME как выполненную')
    print('/exit - звершить работу')
    print('ЛЮБОЙ другой набор сиволов - вывести список команд\n')


# __________________________________________________________________________________________
tb = Tasks()
tb.add_task('Задача-1', '21-01-2025')
tb.add_task('Задача-2', '21-01-2025')

com_list()

while True:
    c = input('\nВведите команду: ')
    split_c = c.rsplit()  # разделяем на команду и параметры
    com = split_c[0]  # вынимаем команду
    match com:
        case '/list':
            tb.info_task_unmarked()

        case '/listm':
            tb.info_task_marked()

        case '/lista':
            tb.info_task()

        case '/add':
            tb.add_task(split_c[1], split_c[2])  # print('Пока не обрабатываем')

        case '/mark':
            print('Пока не обрабатываем')

        case '/exit':
            print('До свидания!')
            exit(0)

        case _:
            com_list()

tb.info_task()
