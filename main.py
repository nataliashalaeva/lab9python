import pandas as pd


def time_to_seconds(time_str):
    mas_time = []
    for time in time_str:
        if 'ч.' in time:  # Проверяем наличие символа "ч."
            hours, minutes, seconds = map(int,
                                          time.replace(' ч.', '').replace(' мин.', '').replace(' сек.', '').split())
            mas_time.append(hours * 3600 + minutes * 60 + seconds)  # Преобразуем часы в секунды
        else:
            minutes, seconds = map(int, time.replace(' мин.', '').replace(' сек.', '').split())
            mas_time.append(minutes * 60 + seconds)

    return pd.Series(mas_time)


data = pd.read_csv(".venv/Scripts/14 - 2.csv")
score = "90,00"
time_task = 540
result = data[(data.get("Оценка/100,00", "") == score)].reset_index()
result = result[time_to_seconds(result.get("Затраченное время", "")) > time_task]
print(len(result))
print(result)
