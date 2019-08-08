
class Fan():
    from math import pi
    def __init__(self, balance_grade,impeller_mass, fan_speed, backplate_dia):
       self.balance_grade = balance_grade
       self.impeller_mass = impeller_mass
       self.fan_speed = fan_speed
       self.backplate_dia = backplate_dia

    def pru(self):
        angular_velosity = self.fan_speed * Fan.pi/(30)
        per_res_unb=round(1000*self.balance_grade*self.impeller_mass/angular_velosity,2)
        return per_res_unb

    def patch_area(self):
        a1=0.012*(self.backplate_dia/10)**2
        area = round(min(1000,a1),1)
        return area




