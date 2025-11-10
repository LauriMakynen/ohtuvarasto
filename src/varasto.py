"""Varasto-luokka varaston hallintaan."""


class Varasto:
    """Kuvaa varastoa, johon voidaan lisätä ja josta voidaan ottaa tavaraa."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston annetulla tilavuudella ja aloitussaldolla."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa varaston jäljellä olevan vapaan tilan."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon annetun määrän, jos se on positiivinen ja mahtuu."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo += maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta annetun määrän ja palauttaa sen."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo -= maara
        return maara

    def __str__(self):
        """Palauttaa varaston tilan merkkijonona."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
