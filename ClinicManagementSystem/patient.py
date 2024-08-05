class Patient(object):
    def __init__(self, id, name, gender, age, full_add,
                 phone, emer_contact, emer_contact_no, allergic, history):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.address = full_add
        self.phone = phone
        self.emer_contact = emer_contact
        self.emer_contact_no = emer_contact_no
        self.allergic = allergic
        self.history = history

    def __str__(self):
        return f'{self.id},{self.name},{self.gender},{self.age},{self.address}, {self.phone}, ' \
               f'{self.emer_contact}, {self.emer_contact_no}, {self.allergic}, {self.history}'
