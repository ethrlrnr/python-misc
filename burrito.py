class Burrito:
    meats = ["chicken", "pork", "steak", "tofu"]
    rices = ["brown", "white"]
    beanss = ["black", "pinto"]
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        if meat in self.__class__.meats:
            self.set_meat(meat)
        else:
            self.set_meat(False)
        if type(to_go) == bool:
            self.set_to_go(to_go)
        else:
            self.set_to_go(False)
        if rice in self.__class__.rices:
            self.set_rice(rice)
        else:
            self.set_rice(False)
        if beans in self.__class__.beanss:
            self.set_beans(beans)
        else:
            self.set_beans(False)
        if type(extra_meat) == bool:
            self.set_extra_meat(extra_meat)
        else:
            self.set_extra_meat(False)
        if type(guacamole) == bool:
            self.set_guacamole(guacamole)
        else:
            self.set_guacamole(False)
        if type(cheese) == bool:
            self.set_cheese(cheese)
        else:
            self.set_cheese(False)
        if type(pico) == bool:
            self.set_pico(False)
        else:
            self.set_pico(False)
        if type(corn) == bool:
            self.set_corn(corn)
        else:
            self.set_corn(False)

    def set_meat(self, meat):
        if meat in self.__class__.meats:
            self.meat = meat
        else:
            self.meat = False

    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False

    def set_rice(self, rice):
        if rice in self.__class__.rices:
            self.rice = rice
        else:
            self.rice = False

    def set_beans(self, beans):
        if beans in self.__class__.beanss:
            self.beans = beans
        else:
            self.beans = False

    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            self.guacamole = False

    def set_cheese(self, cheese):
        if type(cheese) == bool:
            self.cheese = cheese
        else:
            self.cheese = False

    def set_pico(self, pico):
        if type(pico) == bool:
            self.pico = pico
        else:
            self.pico = False

    def set_corn(self, corn):
        if type(corn) == bool:
            self.corn = corn
        else:
            self.corn = False
    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico
    def get_corn(self):
        return self.corn

    def get_cost(self):
        cost = 5
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            cost += 1
        if self.get_meat() == "steak":
            cost += 1.5
        if self.get_extra_meat() and self.get_meat():
            cost += 1
        if self.get_guacamole():
            cost += 0.75
        return cost
