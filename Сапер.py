import random
menu = 0
while menu != '2':
    print('          САПЁР\n\n          АВТОР (1)\n       НАЧАТЬ ИГРУ (2)\n       КАК ИГРАТЬ? (3)\n')
    AA = [str(i) for i in range(1, 4)]
    menu = str(input())
    if menu in AA:
        if menu == '2':
            print('Удачной игры!\n\n\n')
        elif menu == '1':
            print('     Автор игры:\n     inst:@enicks_on_youtube\n     YouTube:https://www.youtube.com/channel/UCqBeqR0pk-T949vaPO7-Edg\n     Либо просто набрать в поисковой строке "Enicks"\n\n\n')
            menu = 0            
        elif menu == '3':
            print('     Правила игры не отличаются от стандартного сапера. (Загугли)\n     Чтобы открыть клетку, введи два числа через пробел.\n     Первое - номер строки, второе - номер столбца.')
            print('     Чтобы отметить бомбу, укажи клетку и через пробел поставь "!"\n     Снять пометку можно проделав те же действия.\n\n\n')
            menu = 0
s = 1
XY = [str(i) for i in input('Введите размер поля через пробел (*Ширина(от 1 до 20)* *Высота(от 1 до 20)*)').split()] #Считывание размеров поля
D = [str(i) for i in range(1, 21)]
if len(XY) == 2 and XY[0] in D and XY[1] in D:
    X = int(XY[0])
    Y = int(XY[1])
else:
    print('Вы ввели некорректные данные. Параметры сброшены к настройкам по умолчанию.')
    X = 6
    Y = 6
a = [['# '] * X for i in range(Y)]#Генерация видимого поля
print('    ', end='')
for i in range(1, X + 1):
    if len(str(i)) == 1:
        print('  ', end='')
    else:
        print(str(i)[0], ' ', sep='', end='')
print()
print('    ', end='')
for i in range(1, X + 1):
    if len(str(i)) == 1:
        print(i, end=' ')
    else:
        print(str(i)[1], end=' ')
print('\n\n', end='')
for i in range(Y):
    if len(str(i + 1)) == 1:
        print(' ', i + 1, sep='', end='  ')
    else:
        print(i + 1, end='  ')
    for j in range(X):
        print(a[i][j], end='')
    print()
b = [[random.randint(0,6) for i in range(X)] for j in range(Y)]#Генерация мин и определение соседства клеток с минами
for v in range(Y):
  for w in range(X):
    if b[v][w] == 0:
      b[v][w] = 'X'
    else:
      b[v][w] = 0
for i in range(Y):
  for j in range(X):
    if b[i][j] == 0:
      for xi in range(-1,2):
        for yj in range(-1,2):
          x = i + xi
          y = j + yj
          if 0 <= x < Y and 0 <= y < X:
            if b[x][y] == 'X':
              b[i][j] += 1
'''for i in range(Y):''' #Вывод "внутреннего" поля для проверки (для активации убать четыре(!) тройки кавычек)
'''  for j in range(X):
    print(b[i][j], end=' ')
  print()'''
c = []
d = [str(i) for i in range(1,21)]
while s == 1: #Проверка наличия неразминированных игроком полей
  s = 0
  xy = [str(i) for i in input().split()] #Ввод координат хода
  if xy not in c or len(xy) == 3:
      if len(xy) == 2 and xy[0] in d and xy[1] in d:
          c.append(list(xy))
          x = int(xy[0]) - 1
          y = int(xy[1]) - 1
          if b[x][y] == 'X':#Проверка наличия бомбы в введенных координатах
              print('Вы нашли бомбу. Игра окончена.')
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print('  ', end='')
                  else:
                      print(str(i)[0], ' ', sep='', end='')
              print()
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print(i, end=' ')
                  else:
                      print(str(i)[1], end=' ')
              print('\n\n', end='')
              for i in range(Y):
                  if len(str(i + 1)) == 1:
                      print(' ', i + 1, sep='', end='  ')
                  else:
                      print(i + 1, end='  ')
                  for j in range(X):
                      print(b[i][j], end=' ')
                  print()
              break
          elif b[x][y] == 0:
              a[x][y] = '0 '
              for __ in range(X + Y):
                  for i0 in range(Y):
                      for j0 in range(X):
                          if a[i0][j0] == '0 ':
                              for ii in range(-1,2):
                                  for jj in range(-1,2):
                                      if (0 <= i0 + ii < X and 0 <= j0 + jj < Y) and a[i0 + ii][j0 + jj] != '! ':
                                          a[i0 + ii][j0 + jj] = str(b[i0 + ii][j0 + jj]) + ' '
                                          if [i0 + ii + 1, j0 + jj + 1] not in c:
                                              c.append([i0 + ii + 1, j0 + jj + 1])
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print('  ', end='')
                  else:
                      print(str(i)[0], ' ', sep='', end='')
              print()
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print(i, end=' ')
                  else:
                      print(str(i)[1], end=' ')
              print('\n\n', end='')
              for i in range(Y):
                  if len(str(i + 1)) == 1:
                      print(' ', i + 1, sep='', end='  ')
                  else:
                      print(i + 1, end='  ')
                  for j in range(X):
                      print(a[i][j], end='')
                  print()
          else: #Если в введенных координатах бомбы нет
              a[x][y] = str(b[x][y]) + ' '
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print('  ', end='')
                  else:
                      print(str(i)[0], ' ', sep='', end='')
              print()
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print(i, end=' ')
                  else:
                      print(str(i)[1], end=' ')
              print('\n\n', end='')
              for i in range(Y):
                  if len(str(i + 1)) == 1:
                      print(' ', i + 1, sep='', end='  ')
                  else:
                      print(i + 1, end='  ')
                  for j in range(X):
                      print(a[i][j], end='')
                  print()
      elif len(xy) == 3 and xy[0] in d and xy[1] in d and xy[2] == '!':#Установка пометки бомбы
          x = int(xy[0]) - 1
          y = int(xy[1]) - 1
          if a[x][y] == '! ':
              a[x][y] = '# '
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print('  ', end='')
                  else:
                      print(str(i)[0], ' ', sep='', end='')
              print()
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print(i, end=' ')
                  else:
                      print(str(i)[1], end=' ')
              print('\n\n', end='')
              for i in range(Y):
                  if len(str(i + 1)) == 1:
                      print(' ', i + 1, sep='', end='  ')
                  else:
                      print(i + 1, end='  ')
                  for j in range(X):
                      print(a[i][j], end='')
                  print()
          elif a[x][y] == '# ':
              a[x][y] = '! '
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print('  ', end='')
                  else:
                      print(str(i)[0], ' ', sep='', end='')
              print()
              print('    ', end='')
              for i in range(1, X + 1):
                  if len(str(i)) == 1:
                      print(i, end=' ')
                  else:
                      print(str(i)[1], end=' ')
              print('\n\n', end='')
              for i in range(Y):
                  if len(str(i + 1)) == 1:
                      print(' ', i + 1, sep='', end='  ')
                  else:
                      print(i + 1, end='  ')
                  for j in range(X):
                      print(a[i][j], end='')
                  print()
          else:
              print('Поле уже разминированно. Тут нельзя установить пометку')
      else:#Если ввод был некорректным
          print('Вы ввели некорректные данные')
  else:
      print('Это поле уже разминированно')
  for i in range(Y):#Проверка незанятых полей
    for j in range(X):
        if not((a[i][j] == str(b[i][j]) + ' ') or (a[i][j] == '! ' and b[i][j] == 'X') or (a[i][j] == '# ' and b[i][j] == 'X')):
            s = 1
else:#Если цикл не был завершен оператором break
    print('Вы победили! Игра окончена.')



