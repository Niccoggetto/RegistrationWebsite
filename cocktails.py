class Cocktail:
    def __init__(self, nome, display_name, alcolici, quantita_alcolici, analcolici, quantita_analcolici, num):
        self.nome = nome
        self.display = display_name
        self.alcohols = list(zip(alcolici[:2], quantita_alcolici[:2]))  # Coppia ogni alcolico con la quantità
        self.nonalcohols = list(zip(analcolici[:2], quantita_analcolici[:2]))  # Coppia ogni analcolico con la quantità
        self.num = num

    '''def __str__(self):
        alcolici_str = ', '.join([f"{alcolico} ({quantita})" for alcolico, quantita in self.alcolici])
        analcolici_str = ', '.join([f"{analcolico} ({quantita})" for analcolico, quantita in self.analcolici])
        return f"{self.nome}: Alcolici - {alcolici_str}, Analcolici - {analcolici_str}"'''


vodka_lemon = Cocktail("vodkalemon", "vodka lemon", ["vodka"], [0.1], ["lemon"], [0.3], 0)
gin_tonic = Cocktail("gintonic", "gintonic", ["gin"], [0.2], ["tonic"], [0.4], 0)
gin_lemon = Cocktail("ginlemon", "gin lemon", ["gin"], [0.2], ["lemon"], [0.3], 0)
rum_cola = Cocktail("rumecola", "rum e cola", ["rum"], [0.15], ["cola"], [0.35], 0)
spritz = Cocktail("spritz", "spritz", ["prosecco", "aperol"], [0.2, 0.1], ["soda"], [0.3], 0)
tequila = Cocktail("tequila", "tequila", ["tequila"], [0.1], [], [], 0)
prosecco = Cocktail("prosecco", "prosecco", ["prosecco"], [0.2], [], [], 0)
montenegro = Cocktail("montenegro", "montenegro", ["montenegro"], [0.15], [], [], 0)
amaro_del_capo = Cocktail("amarodelcapo", "amaro del capo", ["amarodelcapo"], [0.15], [], [], 0)
jagermeister = Cocktail("jagermeister", "jagermeister", ["jagermaister"], [0.1], [], [], 0)

cocktails_list = [vodka_lemon, gin_tonic, gin_lemon, rum_cola, spritz, tequila, prosecco, montenegro, amaro_del_capo,
                  jagermeister]

