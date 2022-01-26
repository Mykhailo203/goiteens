from matplotlib.pyplot import title


class Human:
    name = ''
    id = 0
    sallary = 0
class WorkerHour(Human):
    tariff = 0
    hour = 0

    def set_tariff(self, tarrif):
        self.tariff = tarrif

    def set_hour(self, hour):
        self.hour = hour

    def calc_sallary(self):
        self.sallary = self.hour * self.tariff

class WorkerRate(Human):
    rate = 0
    bonus = 0

    def set_rate(self, money):
        self.rate = money

    def set_bonus(self, money):
        self.bonus = money

    def calc_sallary(self):
        self.sallary = self.rate + self.bonus

class Company():
    title = ''
    workers = list()

    def add_worker(self, worker):
        self.workers.append(worker)

    def calculate_total_sallary(self):
        total_sallary = 0
        for employer in self.workers:
            employer.calc_sallary()
            total_sallary += employer.sallary
            print("|{:^5}|{:<40}|{:>15}".format(employer.id, employer.name, employer.sallary))

        print("|{:<40}|{:>15}".format('Всього за місяць', total_sallary))



Ivanova = WorkerHour()
Ivanova.name = 'Ivanova Ivanna'
Ivanova.id = 48
Ivanova.set_hour(80)
Ivanova.set_tariff(300)

Petrova = WorkerHour()
Petrova.name = 'Petrova Antonina'
Petrova.id = 5
Petrova.set_hour(50)
Petrova.set_tariff(350)

Ivanov = WorkerRate()
Ivanov.name = 'Ivanov Ivan'
Ivanov.id = 1
Ivanov.set_rate(50000)
Ivanov.set_bonus(20000)

Sidorov = WorkerRate()
Sidorov.name = 'Sidorov'
Sidorov.id = 15
Sidorov.set_rate(25000)

company = Company()
company.title = 'GoIteens'
company.add_worker(Ivanova)
company.add_worker(Ivanov)
company.add_worker(Petrova)
company.add_worker(Sidorov)

company.calculate_total_sallary()   