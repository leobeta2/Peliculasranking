

import sys
from Pyside import QtGui,QtCore
from ui_movies import Ui_MainWindow
import controller

class Movies(QtGui.QWidget):
	"""docstring for Movies"""

	table_columns = (
		(u"Titulo", 200),
		(u"Año",100),
		(u"Director", 150),
		(u"Pais", 100),
		(u"Rankink", 75),
		)

	def __init__(self, parent=None):
		QtGui.QMainWindow()
		self.ui.setupUi(self)
		self.show()

	def load_movies(self):
		movies = controller.get_movies()

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	main = Movies()
	sys.exit(app.exec_())
