def wave(x, y, d, dd, step, b):
    step += 1
    if (0 <= x - 1 < d) and (0 <= y < dd) and (b[x - 1][y] == '-2' or int(b[x - 1][y]) > step):
        b[x - 1][y] = step
        b = wave(x - 1, y, d, dd, step, b)
    if (0 <= x < d) and (0 <= y - 1 < dd) and (b[x][y - 1] == '-2' or int(b[x][y - 1]) > step):
        b[x][y - 1] = step
        b = wave(x, y - 1, d, dd, step, b)
    if (0 <= x + 1 < d) and (0 <= y < dd) and (b[x + 1][y] == '-2' or int(b[x + 1][y]) > step):
        b[x + 1][y] = step
        b = wave(x + 1, y, d, dd, step, b)
    if (0 <= x < d) and (0 <= y + 1 < dd) and (b[x][y + 1] == '-2' or int(b[x][y + 1]) > step):
        b[x][y + 1] = step
        b = wave(x, y + 1, d, dd, step, b)
    return b


class LabirintTurtle:
    def __init__(self):
        self.a = []
        self.b = []
        self.d = 0
        self.dd = 0
        self.step = 0
        self.steps = 99999999
        self.x = 0
        self.y = 0
        self.f = []
        self.xv = 0
        self.yv = 0
        self.bb = True
        self.file = ''
        self.k = False
        self.k1 = 0
        self.napr = 'sever'

    def load_map(self, file):
        try:
            self.file = open(file, 'r')
        except FileNotFoundError:
            print('Файл не был найден.')
            raise SystemExit
        except TypeError:
            print('Вы не ввели имя файла.')
            raise SystemExit
        except OSError:
            print('Вы некорректно ввели имя файла.')
            raise SystemExit
        self.f = self.file.readlines()
        try:
            self.y = int(self.f[-1])
        except ValueError:
            print('Некорректный формат ввода данных.')
            raise SystemExit
        try:
            self.x = int(self.f[-2])
        except ValueError:
            print('Некорректный формат ввода данных.')
            raise SystemExit
        for i in self.f[0:-2]:
            a = []
            b = []
            for j in i:
                a.append(j)
                for _ in j:
                    if _ == '*':
                        b.append('-1')
                    elif _ == ' ':
                        b.append('-2')
                    elif _ != '\n':
                        self.bb = False
                        break
            a.pop(-1)
            self.a.append(a)
            if self.bb != 0:
                self.b.append(b)
        self.d = len(self.a)
        self.dd = len(self.a[0])
        if 0 <= self.x < self.d and 0 <= self.y < self.dd:
            self.x = self.x
        else:
            self.bb = False
        if self.bb != 0:
            if self.b[self.x][self.y] == '-2':
                self.b[self.x][self.y] = '0'
            else:
                self.bb = False
        if self.bb != 0:
            self.b = wave(self.x, self.y, self.d, self.dd, self.step, self.b)
            self.k = False
            for i in range(self.dd):
                if self.b[0][i] != '-1':
                    if -2 < int(self.b[0][i]) < self.steps:
                        self.steps = int(self.b[0][i])
                        self.xv = 0
                        self.yv = i
                    self.k = True
                    if i == 0:
                        if self.b[0][i + 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    elif i == self.dd - 1:
                        if self.b[0][i - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    else:
                        if self.b[0][i + 1] == '-1' and self.b[0][i - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                if self.b[self.d - 1][i] != '-1':
                    if -2 < int(self.b[self.d - 1][i]) < self.steps:
                        self.steps = int(self.b[self.d - 1][i])
                        self.xv = self.d - 1
                        self.yv = i
                    self.k = True
                    if i == 0:
                        if self.b[self.d - 1][i + 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    elif i == self.dd - 1:
                        if self.b[self.d - 1][i - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    else:
                        if self.b[self.d - 1][i + 1] == '-1' and self.b[self.d - 1][i - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
            for i in range(self.d):
                if self.b[i][0] != '-1':
                    if -2 < int(self.b[i][0]) < self.steps:
                        self.steps = int(self.b[i][0])
                        self.xv = i
                        self.yv = 0
                    self.k = True
                    if i == 0:
                        if self.b[i + 1][0] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    elif i == self.dd - 1:
                        if self.b[i - 1][0] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    else:
                        if self.b[i + 1][0] == '-1' and self.b[i - 1][0] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                if self.b[i][self.dd - 1] != '-1':
                    if -2 < int(self.b[i][self.dd - 1]) < self.steps:
                        self.steps = int(self.b[i][self.dd - 1])
                        self.xv = i
                        self.yv = self.dd - 1
                    self.k = True
                    if i == 0:
                        if self.b[i + 1][self.dd - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    elif i == self.dd - 1:
                        if self.b[i - 1][self.dd - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
                    else:
                        if self.b[i + 1][self.dd - 1] == '-1' and self.b[i - 1][self.dd - 1] == '-1':
                            self.k = True
                        else:
                            self.k1 += 1
        self.file.close()

    def show_map(self, aa='kamiladura', turtle=False):
        try:
            if turtle == 1:
                self.a[self.x][self.y] = '🐢'
        except IndexError:
            print('Некорректные значения ввода.')
            raise SystemExit
        if aa != 'kamiladura':
            print('Некорректный ввод. Функция show_map может принимать только аргументы True/False.')
            raise SystemExit
        for i in self.a:
            for j in i:
                print("\033[33m {}".format(j), end='\t')
            print('')

    def check_map(self, aa='kamiladura'):
        if aa != 'kamiladura':
            print('Некорректный ввод. Функция check_map не принимает аргументы.')
            raise SystemExit
        if self.bb == 0 or self.k == 0 or self.k1 > 0 or self.steps == 99999999:
            print("\033[34m {}".format('Карта невалидна. Загрузите, пожалуйста, другую карту.'))
            raise SystemExit
        else:
            print("\033[34m {}".format('Всё хорошо'))

    def exit_count_step(self):
        print("\033[34m {}".format(self.steps))

    def exit_show_step(self):
        if self.bb != 0:
            if self.k == 1:
                self.a[self.xv][self.yv] = '🐢'
                for i in range(1, self.steps + 1):
                    n = self.steps - i
                    g = 0
                    if (0 <= self.xv - 1 < self.d) and (0 <= self.yv < self.dd):
                        if int(self.b[self.xv - 1][self.yv]) == n:
                            self.xv, self.yv = self.xv - 1, self.yv
                            self.a[self.xv][self.yv] = '🐢'
                            g += 1
                    if (0 <= self.xv < self.d) and (0 <= self.yv - 1 < self.dd):
                        if int(self.b[self.xv][self.yv - 1]) == n and g == 0:
                            self.xv, self.yv = self.xv, self.yv - 1
                            self.a[self.xv][self.yv] = '🐢'
                            g += 1
                    if (0 <= self.xv + 1 < self.d) and (0 <= self.yv < self.dd):
                        if int(self.b[self.xv + 1][self.yv]) == n and g == 0:
                            self.xv, self.yv = self.xv + 1, self.yv
                            self.a[self.xv][self.yv] = '🐢'
                            g += 1
                    if (0 <= self.xv < self.d) and (0 <= self.yv + 1 < self.dd):
                        if int(self.b[self.xv][self.yv + 1]) == n and g == 0:
                            self.xv, self.yv = self.xv, self.yv + 1
                            self.a[self.xv][self.yv] = '🐢'
                            g += 1
        for i in self.a:
            for j in i:
                print("\033[33m {}".format(j), end='\t')
            print('')
        a = self.x
        b = self.y
        if a + 1 < self.d and 0 <= b < self.dd:
            if self.a[a + 1][b] == '🐢':
                a += 1
                if self.napr != 'ug':
                    print('на юг', 'шаг вперёд')
                    self.napr = 'ug'
                else:
                    print('шаг вперёд')
        for i in range(self.steps):
            if b + 1 < self.dd and 0 <= a <= self.d - 1:
                if self.a[a][b + 1] == '🐢' and self.napr != 'zapad':
                    b += 1
                    if self.napr != 'vostok':
                        print('на восток', 'шаг вперёд')
                        self.napr = 'vostok'
                    else:
                        print('шаг вперёд')
            if b - 1 >= 0 and 0 <= a <= self.d - 1:
                if self.a[a][b - 1] == '🐢' and self.napr != 'vostok':
                    b -= 1
                    if self.napr != 'zapad':
                        print('на запад', 'шаг вперёд')
                        self.napr = 'zapad'
                    else:
                        print('шаг вперёд')
            if a - 1 >= 0 and 0 <= b < self.dd:
                if self.a[a - 1][b] == '🐢' and self.napr != 'ug':
                    a -= 1
                    if self.napr != 'sever':
                        print('на север', 'шаг вперёд')
                        self.napr = 'sever'
                    else:
                        print('шаг вперёд')
            if a + 1 < self.d and 0 <= b < self.dd:
                if self.a[a + 1][b] == '🐢' and self.napr != 'sever':
                    a += 1
                    if self.napr != 'ug':
                        print('на юг', 'шаг вперёд')
                        self.napr = 'ug'
                    else:
                        print('шаг вперёд')
            if a == self.xv and b == self.yv:
                break
