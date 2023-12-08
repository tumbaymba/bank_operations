class Operation:
    '''
    Создаёт экземпляр банковской операции,
    который содержит в себе всю информацию
    '''

    def __init__(self, _id, state, date, description, from_, to, amount, currency):
        self._id = _id
        self.state = state
        self.date = date
        self.description = description
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.currency = currency

    def get_id(self):
        '''
        возвращает id операции
        '''
        return self._id

    def get_state(self):
        '''
        возвращает статус перевода
        '''
        return self.state

    def get_date(self):
        '''
        возвращает дату проведения операции
        '''
        return self.date

    def get_information(self):
        '''
        Выводит информацию о переводе
        в читабельном виде
        '''
        return (f"{self.date} {self.description}\n"
               f"{self.from_} -> {self.to}\n"
               f"{self.amount} {self.currency}\n\n"
                )

    def __repr__(self):
        return f"операция {self._id}"
