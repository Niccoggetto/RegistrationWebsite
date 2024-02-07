class Cocktail:
    def __init__(self, nome, alcolici, quantita_alcolici, analcolici, quantita_analcolici):
        self.nome = nome
        self.alcohols = list(zip(alcolici[:2], quantita_alcolici[:2]))  # Coppia ogni alcolico con la quantità
        self.nonalcohols = list(zip(analcolici[:2], quantita_analcolici[:2]))  # Coppia ogni analcolico con la quantità

    '''def __str__(self):
        alcolici_str = ', '.join([f"{alcolico} ({quantita})" for alcolico, quantita in self.alcolici])
        analcolici_str = ', '.join([f"{analcolico} ({quantita})" for analcolico, quantita in self.analcolici])
        return f"{self.nome}: Alcolici - {alcolici_str}, Analcolici - {analcolici_str}"'''


vodka_lemon = Cocktail("vodka lemon", ["vodka"], [0.1], ["lemon"], [0.3])
gin_tonic = Cocktail("gin Tonic", ["gin"], [0.2], ["tonic"], [0.4])
gin_lemon = Cocktail("gin lemon", ["gin"], [0.2], ["lemon"], [0.3])
rum_cola = Cocktail("rum e cola", ["rum"], [0.15], ["cola"], [0.35])
spritz = Cocktail("spritz", ["prosecco", "aperol"], [0.2, 0.1], ["soda"], [0.3])
tequila = Cocktail("tequila", ["tequila"], [0.1], [], [])
prosecco = Cocktail("prosecco", ["prosecco"], [0.2], [], [])
montenegro = Cocktail("montenegro", ["montenegro"], [0.15], [], [])
amaro_del_capo = Cocktail("amaro del Capo", ["amarodelcapo"], [0.15], [], [])
jagermeister = Cocktail("jagermeister", ["jagermaister"], [0.1], [], [])

cocktails_list = [vodka_lemon, gin_tonic, gin_lemon, rum_cola, spritz, tequila, prosecco, montenegro, amaro_del_capo, jagermeister]

# Esempio di utilizzo
print(vodka_lemon)

