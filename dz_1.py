duration = int(input('Введите количество секунд: '))
if duration <= 60:
    sek_1 = 60 - (60 - duration)
    print(sek_1, 'сек')
elif duration > 60 and duration <= 3600:
    min_2 = duration // 60
    sek_2 = duration % 60
    print(min_2, 'мин', sek_2, 'сек')
elif duration < 86400 and duration > 3600:
    hour_3 = duration // (60 * 60)
    min_3 = (duration - 60 * 60) // 60
    sek_3 = (duration - 60 * 60) % 60
    print(hour_3, 'час', min_3, 'мин', sek_3, 'сек')
else:
    print(duration // (24 * (60 * 60)), 'дня', (duration % (24 * (60 * 60))) // (60 * 60), 'часов',
          (duration % (24 * (60 * 60))) % (60 * 60) // 60, 'минут', (duration % (24 * (60 * 60))) % (60 * 60) % 60,
          'секунд')