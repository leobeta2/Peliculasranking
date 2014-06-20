#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ventana import Ui_MainWindow
import controller


class Movies(QtGui.QMainWindow):

    table_columns = (
        (u"Título", 200),
        (u"Año", 100),
        (u"Director", 200),
        (u"País", 100),
        (u"Ranking", 75))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_movies()
        self.signals()
        self.show()

    def signals(self):
		#toma miss señales
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)
        self.ui.table_movies.clicked.connect(self.select)

    def load_movies(self):
        #carga mi tabla movies a la ventana
        movies = controller.get_movies()
        rows = len(movies)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
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
            #Parametros ocultos
            model.item(i).mov = data
            model.item(i).pk = data[0]

    def up(self):
		#para subir la pelicula
        model = self.ui.table_movies.model()
        index = self.ui.table_movies.currentIndex()
        if index.row() == -1:  
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Seleccione fila!!!")
            return False
        else:
            id_movie = model.item(index.row()).pk
            if (controller.up(id_movie)):
                self.load_movies()
                return True
            else:
                return False

    def down(self):
		# lo baja en el ranking
        model = self.ui.table_movies.model()
        index = self.ui.table_movies.currentIndex()
        if index.row() == -1:  
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Seleccione fila!!!")
            return False
        else:
            id_movie = model.item(index.row()).pk
            if (controller.down(id_movie)):
                self.load_movies()
                return True
            else:
                return False

    def select(self):
		#recargo la informacion, para despues cargarla en la ventana
        model = self.ui.table_movies.model()
        index = self.ui.table_movies.currentIndex()
        id_movie = model.item(index.row()).pk
        rep = controller.get_reparto(id_movie)
        rep = str(rep[0][0])
        self.ui.lbl_stars.setText(rep)
        des = controller.get_descripcion(id_movie)
        des = str(des[0][0])
        self.ui.lbl_description.setText(des)
        im = controller.get_imagen(id_movie)#busco mi imagen
        im = str(im[0][0])
        self.ui.lbl_imagen.setPixmap(im)# cargo mi imagen



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())
