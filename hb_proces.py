"""
Homework 23.

Description:
    Моніторингова система клєнта надсилає сигнал кожні 30 сек.
    Засобами автоматизації проаналізуйте наданий нам лог
    в папці heartbeat/hblog.
    Змініть заготовку - файл hb_proces.py так? щоб там був
    аналіз правилності вимоги:
    для кожного випадку де hertbeat більше 30 сек але менше 32
    логувало варнінг в файл log_file.log
    для кожного випадку де hertbeat більше рівно 32
    логувало error в файлік log_file.log
    Необовязова частина, виклик для найтриваліших:
    (на оцінку не впливає, на самоцінку - впливає)
    Врахуйте, що завтра вам використовувати файл hb_proces.py
    для тестів багатьох файлів
    Здається через посилання на PR з змінами одного файлу (hb_proces.py),
    АЛЕ додатково приатачте у форму відповіді лог, що сворить ваша робота.
    ЛОГ в PR потрапити НЕ ПОВИНЕН.
"""

import logging
import re
from datetime import datetime, timedelta
from pathlib import Path

# Adding logger from the lesson
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('log_file.txt')
console_handler = logging.StreamHandler()
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_format)
console_handler.setFormatter(log_format)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def convert_time_from_log(time):
    """Convert time from input file to time."""
    time_out = datetime.strptime(time, '%H:%M:%S')
    return time_out


filename = Path(__file__).parent / 'hblog.txt'
print(filename)
with open(filename) as fh:
    text = str(fh.read())

pattern = r"""(?<=Timestamp )(.*)(?= Key TSTFEED0300)"""
find_timestamp = re.findall(pattern, text)
print(find_timestamp)

for i in range(len(find_timestamp)):
    time_first = convert_time_from_log(find_timestamp[i])
    if i < len(find_timestamp) - 1:
        time_next = convert_time_from_log(find_timestamp[i + 1])
        delta = time_first - time_next
        if delta >= timedelta(seconds=32):
            logger.error(f'ALARM between {time_first} and {time_next}')
        elif timedelta(seconds=30) < delta < timedelta(seconds=32):
            logger.warning(f'WARN between {time_first} and {time_next}')
    else:
        break
