class Person:
    def __init__(self, first_name, middle_name, last_name, phones):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private', None)

    def get_work_phone(self):
        return self.phones.get('work', None)

    def get_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_sms_text(self):
        return f"Уважаемый {self.first_name} {self.middle_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц"


class Company:
    def __init__(self, name, company_type, phones, *employees):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = employees

    def get_phone(self):
        # сначала ищем контактный телефон компании
        contact = self.phones.get('contact', None)
        if contact is not None:
            return contact
        # если нет, ищем телефон первого сотрудника с work
        for emp in self.employees:
            wp = emp.get_work_phone()
            if wp is not None:
                return wp
        # если нет ни одного
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}"


def send_sms(*recipients):
    for r in recipients:
        number = r.get_phone()
        text = r.get_sms_text()
        if number is not None:
            print(f"Отправлено СМС на номер {number} с текстом: {text}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {r.get_name()}")


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)

send_sms(person1, person2, person3, person4, company1, company2, company3)