"""Yksikkötestit Varasto-luokalle."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testiluokka Varasto-luokan toiminnallisuuden testaamiseen."""

    def setUp(self):
        """Alustaa uuden Varasto-olion ennen jokaista testiä."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa, että varasto on aluksi tyhjä."""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa, että varaston tilavuus on oikein."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa, että lisääminen kasvattaa saldoa."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        """Testaa, että lisääminen pienentää vapaata tilaa oikein."""
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus - lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa, että ottaminen palauttaa oikean määrän."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa, että ottaminen lisää vapaata tilaa oikein."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
