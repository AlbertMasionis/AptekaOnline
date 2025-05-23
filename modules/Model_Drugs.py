class drug:
    def __init__(self, id, nazwa, cena, stan_magazynowy,):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena
        self.stan_magazynowy = stan_magazynowy

        def __str__(self):
            return f"{self.nazwa}-{self.cena}zł"