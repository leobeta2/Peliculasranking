# _*_ coding: utf-8 -*-

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
        self.load_movies()
        self.signals()
		self.show()

	def signals(self):
        #todas señales
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)
        self.ui.table_movies.clicked.connect(self.select)

	def load_movies(self):
		#función que carga películas
		movies = controller.get_movies()
		rows = len(movies)
        model = QtGui.QStandardItemModel(rows, len(self.table_columns))
        self.ui.table_movies.setModel(model)
        self.ui.table_movies.horizontalHeader().setResizeMode(
        	0, self.ui.table_movies.horizontalHeader().Stretch)
        for col, h in enumerate(self.table_columns):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.table_movies.setColumnWidth(col, h[1])
        for i, data in enumerate(movies):
            row = [data[1], data[3], data[4], data[5], data[8]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index, field)
            #para hacerlo más sencillo
            model.item(i).mov = data
            model.item(i).pk = data[0]

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	main = Movies()
	sys.exit(app.exec_())
