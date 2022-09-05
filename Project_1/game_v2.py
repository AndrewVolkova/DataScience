"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0

    # Выбираем предполагаемое число в середине диапазона 1..100,
    # чтобы сразу уменьшить диапазон поиска вдвое,как predict_number = 50
    # также инициализируем переменную shift, она будет использоваться для следующих смещений
    predict_number = shift = 50

    while True:
        # каждую иттерацию уменьшаем смещение для поискового диапазона на 2
        shift = int(shift / 2)
        # если смещение уменьшилось до 0, возвращаем ему значение 1, чтобы не попасть
        # в бесконкечный цикл поиска в одном и том же не изменяемом диапазоне
        shift = 1 if shift == 0 else shift
        count += 1
        # Число найдено, выходим из цикла поиска
        if number == predict_number:
            break
        # если число меньше предполагаемого, уменьшаем диапазон поиска
        # путем уменьшения на расчитанную выше величину shift и наоборот в случае если больше
        predict_number = predict_number - shift if number < predict_number \
            else predict_number + shift
    return count


def score_game(func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    