class Treatment(object):
    def __init__(self, t_date, t_time, id, name, sickness, med, total, next_app, appointment, remarks):
        self.date = t_date
        self.time = t_time
        self.id = id
        self.name = name
        self.sick = sickness
        self.medicine = med
        self.total = total
        self.next = next_app
        self.appointment = appointment
        self.remark = remarks

    def __str__(self):
        return f'{self.date},{self.time},{self.id},{self.name},{self.sick}, {self.medicine}, ' \
               f'{self.total}, {self.next}, {self.appointment}, {self.remark}'
