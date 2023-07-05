class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age >= 20 and self.age < 65:
            return 1500
        elif self.age >= 65:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"
