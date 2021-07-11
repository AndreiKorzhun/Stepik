class multifilter:
    ''' Позволяет проитерироваться только по таким элементам elem из
    последовательности iterable, что значение решающей функции judge
    равно True. '''

    def __iter__(self):
        ''' Возвращает итератор по результирующей последовательности. '''
        for elem in self.iterable:
            pos, neg = 0, 0
            # проводим элемент по всем допускающим функциям
            for func in self.funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield elem

    def judge_half(pos, neg):
        ''' Допускает элемент, если его допускает хотя бы половина фукнций. '''
        return pos >= neg

    def judge_any(pos, neg):
        ''' Допускает элемент, если его допускает хотя бы одна функция. '''
        return pos >= 1

    def judge_all(pos, neg):
        ''' Допускает элемент, если его допускают все функции. '''
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge
