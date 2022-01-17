import pickle
import numpy as np


class Predict:
    def __init__(self) -> None:
        self.model = self.unserialize('trained_linear.sav')
        self.accident_carac = []

    def unserialize(self, path):
        with open(path, 'rb') as file:
            return pickle.load(file)

    def ask_carac(self):
        self.accident_carac.append(input("entrez le mois:\n"))
        self.accident_carac.append(input("entrez le jour:\n"))
        self.accident_carac.append(input(
            "quel était la visibilité?\n1:plein jour\n2:le crépuscule ou la nuit\n3:la nuit sans éclairage public\n4:la nuit avec éclairage public éteind\n5:la nuit avec éclairage public allumé\n"))
        self.accident_carac.append(input(
            "était-ce hors agglomération? \n1:oui\n2:non\n"))
        self.accident_carac.append(input(
            "ou était-ce?\n1:en dehors d'une intersection\n2:Dans une intersection en X\n3:Dans une intersection en T\n4:Dans une intersection en Y\n5:Dans une intersection avec 4 branches\n6:Dans un giratoire\n7:Dans une route sans voie de passage\n8:Dans un passage à niveaux\n9:Une intersection différente\n"))
        self.accident_carac.append(input(
            "quel était la condition atmosphérique?\n1:beau temps\n2:faible pluie\n3:forte pluie\n4:neige\n5:brouillard\n6:fort vent\n7:temps orageux\n8:temps nuageux\n9:autre\n"))
        self.accident_carac.append(input("Numéro du département:\n"))
        self.accident_carac.append(input(
            "à quel quart d'heure était-ce?\n1:0\n2:15\n3:30\n4:45\n"))
        self.accident_carac.append(input(
            "à quel heure de la journée l'accident s'est t'il passé?\n"))
        self.accident_carac.append(input(
            "sur quel route l'accident s'est passé?\n1:autoroute\n2:route nationale\n3:route départementale\n4:route communale\n5:route en dehors du service public\n6:parking\n9:autre\n"))
        self.accident_carac.append(input(
            "quel était le type de route?\n1:upip ne unique voie\n2:bidirectionel\n3:bidirectionel séparées par un obstacle\n4:autre\n"))
        self.accident_carac.append(input(
            "Combien y'a t'il de voie supplémentaire?\n"))
        self.accident_carac.append(input(
            "Quel est le profile de la route?\n1:plat\n2:pente\n3:haut d'une colline\n4:bas d'une colline\n"))
        self.accident_carac.append(input(
            "condition de la route?\n1:normal\n2:mouillée\n3:flaque d'eau\n4:inondée\n5:enneigée\n6:boueuse\n7:verglas\n8:flaque d'huile\n9:autre\n"))
        self.accident_carac = [int(x) for x in self.accident_carac]

    def set_carac(self, array):
        self.accident_carac = [array]

    def get_gravity(self):
        labels = ['mort', 'gravement blessé', 'blessé', 'sauf']
        precision = [0.12, 0.42, 0.32, 0.51]
        grav = self.model.predict(np.array([self.accident_carac]))[0]-1
        return "\n\nl'accidenté est " + labels[grav] + "\nprécision de : " + str(precision[grav])


if __name__ == '__main__':
    p = Predict()
    p.ask_carac()
    print(p.get_gravity())
