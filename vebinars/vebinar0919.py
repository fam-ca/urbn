tasks = []  # Инициализация пустого списка для хранения задач

# ANSI-коды — это последовательности символов, которые терминал может интерпретировать для изменения внешнего вида текста
GREEN = '\033[92m'  # Зеленый цвет для отображения завершенных задач
RED = '\033[91m'  # Красный цвет для отображения незавершенных задач
YELLOW = '\033[93m'  # Желтый цвет для выделения названий задач
BOLD = '\033[1m'  # Жирный шрифт для выделения текста
UNDERLINE = '\033[4m'  # Подчеркивание для выделения текста
RESET = '\033[0m'  # Сброс всех стилей (возвращение к обычному тексту)

def add_task(task_name, *args, priority='Normal', **kwargs):
    """
    Функция для добавления задачи в список задач.
    - task_name: строка, содержащая название задачи
    - *args: дополнительные параметры задачи, переданные как позиционные аргументы
    - priority: приоритет задачи (по умолчанию 'Normal')
    - **kwargs: дополнительные именованные параметры, переданные как словарь
    """
    task = {
        'name': task_name,  # Название задачи
        'priority': priority,  # Приоритет задачи
        'completed': False,  # Статус выполнения задачи (изначально False)
        'additional': args,  # Сохранение дополнительных параметров в виде кортежа
        'extra_info': kwargs  # Сохранение именованных параметров в виде словаря
    }
    tasks.append(task)  # Добавление задачи в список задач
    print(f'Task {BOLD}{YELLOW}{task_name}{RESET} added with priority {priority}. Extra info: {kwargs}')  # Вывод информации о добавленной задаче

def list_tasks(tasks, show_completed=False):
    """
    Функция для вывода всех задач.
    - show_completed: если True, отображаются также выполненные задачи
    """
    print(f'\n{BOLD}{UNDERLINE}List tasks:{RESET}')  # Заголовок списка задач с подчеркиванием
    for index, task in enumerate(tasks):  # Цикл по всем задачам
        # Определение статуса задачи в зависимости от того, завершена она или нет
        status = f'{GREEN}Completed{RESET}' if task['completed'] else f'{RED}In the process{RESET}'
        # Проверка: если задача не выполнена или включен флаг show_completed, она будет отображена
        if not task['completed'] or show_completed:
            extra_info = []  # Список для хранения дополнительной информации о задаче
            for k, v in task['extra_info'].items():  # Перебор всех дополнительных именованных параметров
                extra_info.append(f'{k}: {v}')  # Формирование строки для каждого параметра
            extra_info_str = ', '.join(extra_info)  # Преобразование списка параметров в одну строку
            print(f'{index + 1}. {task["name"]} [{task["priority"]}] - {status} | {extra_info_str}')  # Вывод информации о задаче

def complete_task(task_index):
    """
    Отмечает задачу как выполненную.
    - task_index: индекс задачи (начинается с 1 для удобства пользователя)
    """
    try:
        task = tasks[task_index - 1]  # Получение задачи по индексу (минус 1 для корректного доступа)
        task['completed'] = True  # Установка флага выполнения задачи в True
        print(f'\nTask {YELLOW}{task["name"]}{RESET} marked as complete')  # Сообщение о завершении задачи
    except IndexError:
        print(f'\nTask with index {task_index} not found.')  # Обработка ошибки, если индекс задачи некорректен

def remove_task(task_index):
    """
    Удаляет задачу по индексу.
    - task_index: индекс задачи
    """
    try:
        task = tasks.pop(task_index - 1)  # Удаление задачи из списка по индексу
        print(f'\nTask {BOLD}{UNDERLINE}{YELLOW}{task["name"]}{RESET} was removed')  # Сообщение о том, что задача удалена
    except IndexError:
        print(f'\nTask with index {task_index} not found.')  # Обработка ошибки, если индекс задачи некорректен

def search_task(keyword):
    """
    Ищет задачи по ключевому слову в названии.
    - keyword: ключевое слово для поиска
    """
    found = False  # Флаг, указывающий, найдены ли задачи
    print("\nTasks found:")  # Заголовок для вывода найденных задач
    for task in tasks:  # Перебор всех задач
        if keyword.lower() in task['name'].lower():  # Проверка, есть ли ключевое слово в названии задачи
            extra_info = []  # Список для хранения дополнительной информации
            for k, v in task['extra_info'].items():  # Перебор дополнительных параметров
                extra_info.append(f'{k}: {v}')  # Добавление параметра в список
            extra_info_str = ', '.join(extra_info)  # Формирование строки с дополнительными параметрами
            print(f'- {task["name"]} [{task["priority"]}] | {extra_info_str}\n')  # Вывод информации о найденной задаче
            found = True  # Установка флага в True, если задача найдена
    if not found:  # Если задачи не найдены
        print(f'No tasks with this keyword were found')  # Вывод сообщения о том, что задачи не найдены

def remove_completed_recursive(index=0):
    """
    Рекурсивно удаляет все выполненные задачи и возвращает количество удаленных задач.
    - index: текущий индекс для проверки, по умолчанию начинается с 0
    """
    if index >= len(tasks):  # Базовый случай: если индекс выходит за пределы списка, прекращаем рекурсию
        return 0  # Возвращаем 0, так как больше нечего удалять
    removed_count = 0  # Переменная для хранения количества удаленных задач
    if tasks[index]['completed']:  # Проверка, выполнена ли текущая задача
        print(f"{BOLD}{RED}Deleting a completed task:{RESET} {YELLOW}{tasks[index]['name']}{RESET}")  # Вывод сообщения об удалении задачи
        tasks.pop(index)  # Удаление выполненной задачи из списка
        removed_count = 1  # Увеличиваем счетчик удаленных задач
        removed_count += remove_completed_recursive(index)  # Рекурсивный вызов для проверки текущего индекса (так как после удаления список сдвигается)
    else:
        removed_count += remove_completed_recursive(index + 1)  # Если задача не выполнена, проверяем следующую задачу
    return removed_count  # Возвращаем общее количество удаленных задач

def remove_task(task_index):
    """
        Удаляет задачу по индексу.
        - task_index: индекс задачи
        """
    print(f"\n{BOLD}{RED}A task {RESET} {YELLOW} {tasks[task_index]['name']} {RESET} is removed!")
    tasks.pop(task_index)


def list_tasks_sorted_by_priority(show_completed=False):
    """
    Выводит список задач, отсортированных по приоритету.
    - show_completed: если True, показывает выполненные задачи
    """
    low_priority_task = [] 
    medium_priority_task = []
    high_priority_task = []
    for index, task in enumerate(tasks):
        if task['priority'].lower()=='low':
            low_priority_task.append(task)
        elif task['priority'].lower()=='medium':
            medium_priority_task.append(task)
        elif task['priority'].lower()=='high':
            high_priority_task.append(task)
    tasks_sorted = low_priority_task + medium_priority_task + high_priority_task
    return list_tasks(tasks_sorted)


# Добавление задач с произвольными параметрами
add_task("Buy food", 'Urgent', priority="High", location="Supermarket", due_date="2024-09-20")
add_task("Write a report", 'High priority', priority="Low", department="HR", project="Quarterly Review")
add_task("Prepare for the webinar", 'Important', priority="Medium", speaker="John Doe")
add_task("Call a coworker", 'Routine', priority="High", contact="Jane Smith")
add_task("Call a friends", 'Routine', priority="Low")



# # Вывод списка задач
# list_tasks(tasks)

# # Отметка задач как выполненных
# complete_task(1)
# complete_task(2)

# # Вывод списка задач, включая выполненные
# list_tasks(tasks, show_completed=True)

# # Поиск задач по ключевому слову
# search_task('call')

# # Удаление всех выполненных задач и получение количества удаленных задач
# removed_tasks = remove_completed_recursive()

# # Вывод списка задач после удаления выполненных
# list_tasks(tasks)

# # Вывод количества удаленных задач
# print(f"{BOLD}{UNDERLINE}Total removed tasks:{RESET} {removed_tasks}")

# remove_task(1)

# # list_tasks(tasks)

list_tasks_sorted_by_priority(show_completed=True)


