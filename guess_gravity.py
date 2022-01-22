import numpy as np
import pickle

"""serialize_unserialize"""


class Predict:
    def __init__(self) -> None:
        """init"""
        self.model = self.unserialize("trained_linear.sav")
        # array stocking accident infos
        self.accident_carac = []
        # range of correct answers
        self.answer_range = [
            range(1, 13),
            range(1, 32),
            range(1, 6),
            range(1, 3),
            range(1, 10),
            range(1, 10),
            range(0, 2000),
            [0, 15, 30, 45],
            range(0, 25),
            [1, 2, 3, 4, 5, 6, 9],
            range(1, 5),
            range(0, 11),
            range(1, 5),
            range(1, 10),
        ]
        # list of questions about the accident
        self.question_array = [
            "entrez le mois:\n",
            "entrez le jour:\n",
            "quel était la visibilité?\n1:plein jour\n2:le crépuscule ou la"
            " nuit\n3:la nuit sans éclairage public\n4:la nuit avec éclairage"
            " public éteind\n5:la nuit avec éclairage public allumé\n",
            "était-ce hors agglomération? \n1:oui\n2:non\n",
            "ou était-ce?\n1:en dehors d'une intersection\n2:Dans une"
            " intersection en X\n3:Dans une intersection en T\n4:Dans une"
            " intersection en Y\n5:Dans une intersection avec 4"
            " branches\n6:Dans un giratoire\n7:Dans une route sans voie de"
            " passage\n8:Dans un passage à niveaux\n9:Une intersection"
            " différente\n",
            "quel était la condition atmosphérique?\n1:beau temps\n2:faible"
            " pluie\n3:forte pluie\n4:neige\n5:brouillard\n6:fort"
            " vent\n7:temps orageux\n8:temps nuageux\n9:autre\n",
            "Numéro du département:\n",
            "à quel quart d'heure l'accident s'est t'il"
            " passé?\n0\n15\n30\n45\n",
            "à quel heure de la journée l'accident s'est t'il passé?\n",
            "sur quel route l'accident s'est passé?\n1:autoroute\n2:route"
            " nationale\n3:route départementale\n4:route communale\n5:route en"
            " dehors du service public\n6:parking\n9:autre\n",
            "quel était le type de route?\n1:une unique"
            " voie\n2:bidirectionel\n3:bidirectionel séparées par un"
            " obstacle\n4:autre\n",
            "Combien y'a t'il de voie supplémentaire?\n",
            "Quel est le profile de la route?\n1:plat\n2:pente\n3:haut d'une"
            " colline\n4:bas d'une colline\n",
            "condition de la route?\n1:normal\n2:mouillée\n3:flaque"
            " d'eau\n4:inondée\n5:enneigée\n6:boueuse\n7:verglas\n8:flaque"
            " d'huile\n9:autre\n",
        ]

    def unserialize(self, path):
        """load the saved model"""
        with open(path, "rb") as file:
            return pickle.load(file)

    def get_answers(self):
        """ask every question about the accident"""
        for i in range(len(self.question_array)):
            self.ask(i)

    def ask(self, question_number):
        """ask a question"""
        answer = int(input(self.question_array[question_number]))
        while answer not in self.answer_range[question_number]:
            answer = int(input(self.question_array[question_number]))

    def get_gravity(self):
        """with the answer given predict the gravity of the accident"""
        labels = ["sain et sauf", "blessé", "gravement blessé"]
        precision = [0.51, 0.32, 0.51]
        grav = self.model.predict(np.array([self.accident_carac]))[0] - 1
        return (
            "\n\nl'accidenté est "
            + labels[grav]
            + "\nprécision de : "
            + str(precision[grav])
        )


if __name__ == "__main__":
    accident_predict = Predict()
    accident_predict.get_answers()
    print(accident_predict.get_gravity())
