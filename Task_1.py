class Tuning:
    """класс Tuning, описывает доп.оборудование"""
    def __init__(self, exgaust,turbo,injection):
        self.exgaust = exgaust
        self.turbo = turbo
        self.injection = injection
    def avg_tuning_engine(self):
        """метод рассчитывает общую стоимость для авто"""
        return(int(self.exgaust)+(self.turbo)+(self.injection))


class TuningAudi:
    """доп оборудование для ауди"""
    def __init__(self,name,year,exgaust,turbo,injection):
        self.year = year
        self.name = name
        self.obj_tuning = Tuning(exgaust,turbo,injection)
    def avg_tuning(self):
        return self.obj_tuning.avg_tuning_engine()
audi_t = TuningAudi('Audi RS6','2022',4000,5500,3000)
#print(audi_t.name,'\n',audi_t.year,'\n','цена дополнительного оборудования\n'+str(audi_t.avg_tuning()))

class TuningBMW:
    def __init__(self,name,year,exgaust,turbo,injection):
        self.year = year
        self.name = name
        self.obj_tuning = Tuning(exgaust,turbo,injection)
    def avg_tuning(self):
        return self.obj_tuning.avg_tuning_engine()
bmw_t = TuningBMW('BMW M5','2022',4500,3500,5500)
#print(bmw_t.name,'\n',bmw_t.year,'\n','цена дополнительного оборудования\n'+str(bmw_t.avg_tuning()))

class TuningMercedes:
    def __init__(self,name,year,exgaust,turbo,injection):
        self.year = year
        self.name = name
        self.obj_tuning = Tuning(exgaust,turbo,injection)
    def avg_tuning(self):
        return self.obj_tuning.avg_tuning_engine()
mercedes_t = TuningMercedes('Mercedes-Benz E63 AMG','2021',5500,1900,5200)
#print(mercedes_t.name,'\n',mercedes_t.year,'\n','цена дополнительного оборудования\n'+str(mercedes_t.avg_tuning()))


class Auto:
    """класс определяет характеристики автомобиля(любого)"""
    def __init__(self,year,max_speed,engine_type,price,):
        self.year = year
        self.max_speed = max_speed
        self.engine_type = engine_type
        self.price = price

    def info(self):
        """получаем информацию об автомобиле(любом)"""
        print('Цена: ' + str(self.price))
        print('Год выпуска: ' + str(self.year))
        print('Максимальная скорость: ' + str(self.max_speed))
        print('Тип двигателя: ' + str(self.engine_type))


class BMW (Auto):
    """наследуемый класс от класса Auto"""

    ruClassname = "Бизнес Спорт"

    def __init__(self,name,modification,year,max_speed,engine_type,
                 price,power,engine_volume,tYpe):
        super().__init__(year,max_speed,engine_type,price)#то что передаём от родительского класса
        self.name = name
        self.modification = modification
        self.power = power
        self.engine_volume = engine_volume
        self.tYpe = tYpe

    def info(self):
        """получаем инфо о конкретном автомобиле"""

        print('Класс: ' + BMW.ruClassname)
        print(self.name)
        print("Модификация: " + str(self.modification))
        super().info()
        print("Мощность: " + str(self.power))
        print("Обьём двигателя: " + str(self.engine_volume))
        print("Тип кузова: " + str(self.tYpe))
        print('стоимость доп оборудования: ' + str(bmw_t.avg_tuning()))
bmw_m5 = BMW('BMW M5','CS','2022','290 km/h','Gasoline','98 000 $','625 hp','4395cc','Sedan')
#bmw_m5.info()


class Mercedes (Auto) :

    ruClassname = "Luxary Sport"

    def __init__(self, name, modification, year, max_speed,
                 engine_type,price, power, engine_volume,tYpe):
        super().__init__(year, max_speed, engine_type,price)
        self.name = name
        self.modification = modification
        self.power = power
        self.engine_volume = engine_volume
        self.tYpe = tYpe

    def info(self):
        print('Класс: ' + Mercedes.ruClassname)
        print(self.name)
        print("Модификация: " + str(self.modification))
        super().info()
        print("Мощность: " + str(self.power))
        print("Обьём двигателя: " + str(self.engine_volume))
        print("Тип кузова: " + str(self.tYpe))
        print('стоимость доп оборудования: ' + str(mercedes_t.avg_tuning()))

mercedes_e63s = Mercedes('Mercedes-Benz E63 AMG', 'S', '2021', '280 km/h',
                         'Gasoline','104 000 $','612 hp','3982cc', 'Estate')
#mercedes_e63s.info()

class Audi (Auto) :

    ruClassname = "Intelegent Sport"

    def __init__(self, name, modification, year, max_speed,
                 engine_type,price, power, engine_volume,tYpe):
        super().__init__(year, max_speed, engine_type,price)
        self.name = name
        self.modification = modification
        self.power = power
        self.engine_volume = engine_volume
        self.tYpe = tYpe

    def info(self):
        print('Класс: ' + Audi.ruClassname)
        print(self.name)
        print("Модификация: " + str(self.modification))
        super().info()
        print("Мощность: " + str(self.power))
        print("Обьём двигателя: " + str(self.engine_volume))
        print("Тип кузова: " + str(self.tYpe))
        print('стоимость доп оборудования: ' + str(audi_t.avg_tuning()))

audi_RS6 = Audi('Audi RS6','Plus','2022','299 km/h','Gasoline','120 000 $',
                '605hp', '3993cc', 'Avant')
#audi_RS6.info()


print("Добрый День! Рады видеть Вас в нашем автосалоне! \n Какой автомобиль желаете?")
print(" 1. Audi\n 2. BMW\n 3. Mercedes")
model_avto = int(input('- '))


if model_avto == 1:
    print('Отлично, у нас в наличии есть прекрасная \n ' + str(audi_RS6.name) +
          '\nхотите посмотреть характеристики ?')
    print(' 1. да\n 2. нет')
    vibor_audi = int(input('- '))
    if vibor_audi == 1:
        print(audi_RS6.info())
        print('\nцена чуть выше чем у конкурентов но из плюсов тут\n'
              'максимальная скорость:\n'+str(audi_RS6.max_speed)+'\n'
              'и конфигурация кузова:\n'+str(audi_RS6.tYpe)+'\n'
              'и самая низкая стоимость доп оборудования: \n'+str(audi_t.avg_tuning()))
        print("***********************************")
        print('предлагаю оформить покупку'+" "+audi_RS6.name+" "+':-)')
    elif vibor_audi == 2:
        print('посмотрите другие наши модели')
        print('1. Mercedes ?\nили\n2. BMW ?')
        vibor_audi_1 = int(input('- '))
        if vibor_audi_1 == 1:print(mercedes_e63s.info())
        elif vibor_audi_1 == 2:print(bmw_m5.info())
        print("************************************")
        print("предлагаю оформить покупку понравившегося авто")



elif model_avto == 2:
    print('Отлично, у нас в наличии есть прекрасная \n ' + str(bmw_m5.name))
    print('хотите узнать максимальную скорость и мощность?')
    print('1. Да\n2. нет')
    vibor_bmw = int(input('- '))
    if vibor_bmw == 1:
        print('Максимальная скорость:\n'+bmw_m5.max_speed+'\n'+
              "Мощность:\n"+bmw_m5.power)
        print('глянем остальные характеристики?')
        print('1. да\n2. нет')
        vibor_bmw_1 = int(input('- '))
        if vibor_bmw_1 == 1:
            print(bmw_m5.info())
            print("*********************")
            print("предлагаю оформить покупку :-)")
        else:
            print('посмотрите на характеристики Audi или Mercedes\n'
                  '1. Audi\n2. Mercedes')
            vibor_bmw_2 = int(input('- '))
            if vibor_bmw_2 == 1:
                print(audi_RS6.info())
                print("***********************")
                print('предлагаю оформить покупку')
            else:
                print(mercedes_e63s.info())
                print("************************")
                print("предлагаю оформить покупку)")
    else:
        print('обратите внимание на другие наши модели')
        if input("хотите посмотреть"+" "+str(mercedes_e63s.name)+' & '+str(audi_RS6.name)+
            "? (audi/mercedes) \n:")== "audi":
            print(audi_RS6.info())
            print("***********************")
            print("предлагаю оформить покупку)")
        else:
            print(mercedes_e63s.info())
            print("**************************")
            print("предлагаю оформить покупку)")



elif model_avto == 3:
    print('Отлично, у нас в наличии есть прекрасный \n ' + str(mercedes_e63s.name))
    if input("что посмотрим первым? (мощность/скорость): ").lower()=="мощность":
        print(mercedes_e63s.power)
        print('хотите узнать цену конкурентов ?'+' '
              +bmw_m5.name +' '+'&'+' '+audi_RS6.name)
        if input('да/нет : ')=='да':
            print("цена" + " " + bmw_m5.name + '\n' + bmw_m5.price)
            print("VS")
            print("цена"+" "  +audi_RS6.name+'\n'+audi_RS6.price)
            if input("что будем оформлять для покупки ? (bmw/audi) :")== "bmw":
                print(" отличный выбор\n вот все характеристики" )
                print(bmw_m5.info())
            else:
                print("после просмотра характеристик, предлагаю перейти к оформлению)")
                print(audi_RS6.info())
        else:
            print("тогда предлагаю ознакомиться со всеми характеристиками и "
                  "оформить покупку"+" "+mercedes_e63s.name)
            print('****************************************')
            print(mercedes_e63s.info())
    else:
        print(mercedes_e63s.max_speed)
        if input("хотите узнать цену Mercedes? (да/нет): ") =='да':
            print(mercedes_e63s.price)
            print("после просмотра всех характеристик, предлагаю перейти к покупке")
            print("*********************")
            print(mercedes_e63s.info())

        else:
            print('ознакомьтесь с ценами на другие наши модели:\n')
            print("цена"+" "  +audi_RS6.name+'\n'+audi_RS6.price)
            print("цена"+" " +bmw_m5.name+'\n'+bmw_m5.price)
            print("какой автомобиль желаете к покупке:\n 1.audi\n 2.bmw\n 3.mercedes")
            vibor_avto_3 = int(input("- "))
            if vibor_avto_3 == 1:
                print("отличный выбор, вот полные характеристики: ")
                print("************************")
                print(audi_RS6.info())
            elif vibor_avto_3 ==2:
                print("отличный выбор, вот полные характеристики: ")
                print("************************")
                print(bmw_m5.info())
            elif vibor_avto_3 == 3:
                print("отличный выбор, вот полные характеристики: ")
                print("************************")
                print(mercedes_e63s.info())
            else:
                print("такого автомобиля нет в наличии")
else:
    print('помогу вам рассчитать годовую зарплату для одобрения кредита : \n')



"""    
#не знал куда приспособить агрегацию)), пусть будет отдельно для примера
#расчёт зарплаты за год
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class EmployeeOne:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.agg_salary = sal
    def total_sal(self):
        return self.agg_salary.annual_salary()


#salary = Salary(2300, 1500)
#emp = EmployeeOne('Иван',"34 года", salary)



#print(emp.name)
#print((emp.age))
#print(emp.total_sal())   """

