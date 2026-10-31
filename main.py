from operator import itemgetter

class Microprocessor:
    """Микропроцессор; computer_id реализует связь один-ко-многим."""
    def __init__(self, id, model, frequency, computer_id):
        self.id = id
        self.model = model
        self.frequency = frequency # количественный признак, ГГц
        self.computer_id = computer_id

class Computer:
    """Компьютер."""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProcessorComputer:
    """Связь многие-ко-многим между микропроцессором и компьютером."""
    def __init__(self, processor_id, computer_id):
        self.processor_id = processor_id
        self.computer_id = computer_id

computers = [
    Computer(1, 'Альтаир компьютер'),
    Computer(2, 'Беркут компьютер'),
    Computer(3, 'Кедр компьютер'),
    Computer(4, 'Орбита компьютер'),
]

processors = [
    Microprocessor(1, 'Альфа', 3.2, 1),
    Microprocessor(2, 'Бета', 4.0, 2),
    Microprocessor(3, 'Гамма', 3.6, 3),
    Microprocessor(4, 'Дельта', 2.8, 4),
    Microprocessor(5, 'Атом', 4.4, 3),
]

# В M:N-списке показаны совместимые комплектации; два процессора общие.
processor_computers = [
    ProcessorComputer(1, 1), ProcessorComputer(2, 2),
    ProcessorComputer(3, 3), ProcessorComputer(4, 4),
    ProcessorComputer(5, 3), ProcessorComputer(1, 4),
]

# Представления связей
one_to_many = [
    (p.model, p.frequency, c.name)
    for c in computers for p in processors if p.computer_id == c.id
]

m2m_temp = [
    (pc.processor_id, pc.computer_id)
    for pc in processor_computers
]

many_to_many = [
    (p.model, p.frequency, c.name)
    for pid, cid in m2m_temp
    for p in processors if p.id == pid
    for c in computers if c.id == cid
]

def run_queries():
    # Набор А
    print('Задание А1. Связанные микропроцессоры и компьютеры, сортировка по компьютерам')
    print(sorted(one_to_many, key=itemgetter(2)))
    print('\nЗадание А2. Суммарная частота микропроцессоров по компьютерам')
    sums = [(c.name, sum(row[1] for row in one_to_many if row[2] == c.name))
    for c in computers if any(row[2] == c.name for row in one_to_many)]
    print(sorted(sums, key=itemgetter(1)))
    print('\nЗадание А3. Компьютеры со словом «компьютер» в названии и их процессоры')
    print({c.name: [p.model for p in processors if p.computer_id == c.id]
    for c in computers if 'компьютер' in c.name.lower()})

    # Набор Б
    print('\nЗадание Б1. Связанные микропроцессоры и компьютеры, сортировка по процессорам')
    print(sorted(one_to_many, key=itemgetter(0)))
    print('\nЗадание Б2. Число микропроцессоров в компьютерах')
    counts = [(c.name, sum(1 for row in one_to_many if row[2] == c.name)) for c in computers]
    print(sorted(counts, key=itemgetter(1)))
    print('\nЗадание Б3. Процессоры с моделью, оканчивающейся на «а», и их компьютеры (M:N)')
    print([(model, name) for model, _, name in many_to_many if model.lower().endswith('а')])

    # Набор В
    print('\nЗадание В1. Процессоры, модель которых начинается с «А», и их компьютеры')
    print([(model, name) for model, _, name in one_to_many if model.startswith('А')])
    print('\nЗадание В2. Минимальная частота по компьютерам')
    mins = [(c.name, min(row[1] for row in one_to_many if row[2] == c.name))
    for c in computers if any(row[2] == c.name for row in one_to_many)]
    print(sorted(mins, key=itemgetter(1)))
    print('\nЗадание В3. Все связанные пары M:N, сортировка по процессорам')
    print(sorted(many_to_many, key=itemgetter(0)))

    # Набор Г
    print('\nЗадание Г1. Компьютеры, название которых начинается с «А», и их процессоры')
    print({c.name: [p.model for p in processors if p.computer_id == c.id]
    for c in computers if c.name.startswith('А')})
    print('\nЗадание Г2. Максимальная частота по компьютерам')
    maxs = [(c.name, max(row[1] for row in one_to_many if row[2] == c.name))
    for c in computers if any(row[2] == c.name for row in one_to_many)]
    print(sorted(maxs, key=itemgetter(1)))
    print('\nЗадание Г3. Все связанные пары M:N, сортировка по компьютерам')
    print(sorted(many_to_many, key=itemgetter(2)))

    # Набор Д
    print('\nЗадание Д1. Модели, оканчивающиеся на «а», и названия компьютеров')
    print([(model, name) for model, _, name in one_to_many if model.lower().endswith('а')])
    print('\nЗадание Д2. Средняя частота по компьютерам, округление до 2 знаков')
    avgs = [(c.name, round(sum(row[1] for row in one_to_many if row[2] == c.name) /
    sum(1 for row in one_to_many if row[2] == c.name), 2))
    for c in computers if any(row[2] == c.name for row in one_to_many)]
    print(sorted(avgs, key=itemgetter(1)))
    print('\nЗадание Д3. Компьютеры, название которых начинается с «А», и их процессоры (M:N)')
    print({c.name: [model for model, _, name in many_to_many if name == c.name]
    for c in computers if c.name.startswith('А')})

if __name__ == '__main__':
    run_queries()