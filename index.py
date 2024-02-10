__author__ = 'YEHADJI Abilé Alexis-Honoré'
__license__ = 'BSD 3 Simplified'
__version__ = '0.1.0'
__email__ = 'yehadjialexis@gmail.com'


import numpy as np
import matplotlib.pyplot as plt

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def _f(self, x):
        return x**5

    def plot_curve(self):
        x_values = np.linspace(self.start, self.stop, self.nbr_points)
        y_values = self._f(x_values)
        plt.plot(x_values, y_values, label='f(x) = x^5', color='red')
        plt.title('Courbe de f(x) = x^5 avec points aléatoires')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)

    def point_position(self, x, y):
        y_curve = self._f(x)
        if y > y_curve:
            return "dessus"
        elif y < y_curve:
            return "dessous"
        else:
            return "on"

    def generer_points(self):
        self.plot_curve()
        
        
        plotted_above = False
        plotted_below = False

        for _ in range(self.nbr_points):
            x = np.random.uniform(self.start, self.stop)
            y = np.random.uniform(self.start, self._f(self.stop))

            if self.point_position(x, y) == "dessus":
                if not plotted_above:
                    plt.scatter(x, y, color='blue', marker='x', label='Au dessus')
                    plotted_above = True
                else:
                    plt.scatter(x, y, color='blue', marker='x')
            elif self.point_position(x, y) == "dessous":
                if not plotted_below:
                    plt.scatter(x, y, color='green', marker='o', label='En dessous')
                    plotted_below = True
                else:
                    plt.scatter(x, y, color='green', marker='o')

        plt.legend()
        plt.show()

# Création d'une instance de la classe Curve
curve = Curve(start=0, stop=1, nbr_points=50)
# Génération et affichage des points aléatoires sur le graphique
curve.generer_points()
