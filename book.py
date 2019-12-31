from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, random, sys


class Ui_Dialog(object):

    def setupUi(self, Dialog):

        self.where_sql = 'title'
        self.where_sql_text = ''
        self.find_setting = {'title': '0', 'autor': '1'}

        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 530, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)
        self.checkWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.checkWidget.setGeometry(QtCore.QRect(20, 50, 520, 450))
        self.checkWidget.setObjectName("checkWidget")
        self.checkWidget.setColumnCount(0)
        self.checkWidget.setRowCount(0)

        self.checkWidget.setMouseTracking(True)
        self.checkWidget.setTabKeyNavigation(True)

        # ------------------------------------------------------------
        # Этот сигнал испускается при каждом щелчке ячейки в таблице.
        self.checkWidget.cellClicked[int, int].connect(self.clickedRowColumn)

        # Этот сигнал испускается, когда ячейка, указанная в строке и столбце, активирована
        self.checkWidget.cellActivated[int, int].connect(self.activatedRowColumn)

        # Этот сигнал излучается всякий раз, когда данные элемента в ячейке изменяются.
        self.checkWidget.cellChanged[int, int].connect(self.changedRowColumn)

        # Этот сигнал испускается, когда курсор мыши входит в ячейку.
        self.checkWidget.cellEntered[int, int].connect(self.enteredRowColumn)
        # -------------------------------------------------------------

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 180, 30))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 10, 250, 30))
        self.textEdit.setObjectName("textEdit")
        self.add_combo_box()
        self.search()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 130, 180))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 210, 251, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(530, 240, 261, 31))
        self.label_title.setText("")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setGeometry(QtCore.QRect(530, 300, 261, 31))
        self.label_autor.setText("")
        self.label_autor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_autor.setObjectName("label_autor")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 270, 251, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(530, 360, 261, 31))
        self.label_year.setText("")
        self.label_year.setAlignment(QtCore.Qt.AlignCenter)
        self.label_year.setObjectName("label_year")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 330, 261, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 390, 261, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(530, 420, 261, 31))
        self.label_genre.setText("")
        self.label_genre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genre.setObjectName("label_genre")

        self.label.resize(120, 200)

        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Каталог библиотеки"))
        self.pushButton.setText(_translate("Dialog", "Найти"))
        self.comboBox.setItemText(0, _translate("Dialog", "Название"))
        self.comboBox.setItemText(1, _translate("Dialog", "Автор"))
        self.label_2.setText(_translate("Dialog", "Наименование"))
        self.label_3.setText(_translate("Dialog", "Автор"))
        self.label_4.setText(_translate("Dialog", "Год выпуска"))
        self.label_5.setText(_translate("Dialog", "Жанр"))

    def activatedRowColumn(self, r, c):
        self.update_image(r)
        self.update_text(r)

    def changedRowColumn(self, r, c):
        pass

    def clickedRowColumn(self, r, c):
        self.update_image(r)
        self.update_text(r)

    def enteredRowColumn(self, r, c):
        self.update_image(r)
        self.update_text(r)

    def add_combo_box(self):
        for n in self.find_setting.keys():
            self.comboBox.addItem(n)

    def selectionchange(self, i):
        self.where_sql = list(self.find_setting.keys())[
            self.comboBox.currentIndex()]

    def update_text(self, r):
        self.label_title.setText(self.checkWidget.model().index(r, 1).data())
        self.label_autor.setText(self.checkWidget.model().index(r, 2).data())
        self.label_year.setText(self.checkWidget.model().index(r, 3).data())
        self.label_genre.setText(self.checkWidget.model().index(r, 4).data())

    def update_image(self, r):
        con = sqlite3.connect('catalog_1.db')
        id = self.checkWidget.model().index(r, 0).data()
        text_sql_base = f'SELECT photo FROM book  WHERE id = {id}'
        for (img_data,) in con.execute(text_sql_base):
            print(type(bool(img_data)))
            self.pixmap = QtGui.QPixmap()
            self.pixmap.loadFromData(img_data)
            self.label.setPixmap(self.pixmap.scaledToHeight(150))
        self.label.resize(120, 200)

    def del_row(self):
        for d in range(self.checkWidget.rowCount()):
            self.checkWidget.removeRow(0)

    def create_base(self):
        try:
            books = [['Мойдодыр', 'Чуковский Корней', 2016, 'Стихи', 1],
                     ['Айболит', 'Чуковский Корней', 2015, 'Стихи', 2],
                     ['Дед Мороз', 'Степанов В.', 2017, 'Стихи', 3],
                     ['Краденое солнце', 'Жигарев Вячеслав Алексеевич', 2010, 'Стихи', 4],
                     ['Гарри Поттер', 'Роулинг Джоан Кэтлин', 2018, 'Фэнтези', 5],
                     ['Девочка с Земли', 'Кир Булычев', 2016, 'Фэнтези', 6],
                     ['Блейз', 'Кинг Стивен', 2018, 'Фэнтези', 7],
                     ['Оно. Тень прошлого', 'Кинг Стивен', 2018, 'Фэнтези', 8],
                     ['Девушка в тумане', 'Карризи Донато', 2018, 'Детективы', 9],
                     ['Убийства по алфавиту', 'Кристи Агата', 2019, 'Детективы', 10],
                     ['Мотылек', 'Шарьер Анри', 2015, 'Романы', 11],
                     ['Трезориум', 'Борис Акунин', 2019, 'Романы', 12]
                     ]

            # Открываем базу данных
            con = sqlite3.connect('catalog_1.db')
            cur = con.cursor()

            # Готовим текст запроса в базу
            text_sql_base = f'CREATE TABLE "book" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `title` ' \
                            f'text NOT NULL, `autor` TEXT, `year` INTEGER NOT NULL, `genre` TEXT NOT NULL,' \
                            f' `photo` blob NOT NULL)'
            cur.execute(text_sql_base)
            con.commit()
            text_sql_genres = f'INSERT INTO genres VALUES (?,?)'
            text_sql_book = f'INSERT INTO book VALUES (?,?,?,?,?,?)'
            cur.close()

        # В случаи ошибки выводим ее текст.
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            if con:
                # Закрываем подключение с базой данных
                con.close()
                print("The SQLite connection is closed")

    def search(self):
        self.del_row()
        z = ['<', '>', '=']
        con = sqlite3.connect("catalog_1.db")
        cur = con.cursor()
        self.where_sql_text = f'"{self.textEdit.toPlainText().strip()}"'
        if self.textEdit.toPlainText().strip() == "":
            text_sql = f'SELECT * FROM book'
        elif (self.textEdit.toPlainText().strip().upper().startswith('LIKE')) \
                or (self.textEdit.toPlainText().strip()[0] in z):
            self.where_sql_text = self.textEdit.toPlainText().replace("'", '"')
            text_sql = f'SELECT * FROM book  WHERE {self.where_sql} ' \
                       f'{self.where_sql_text}'
        else:
            text_sql = f'SELECT * FROM book  WHERE {self.where_sql} ' \
                       f'= {self.where_sql_text}'

        print(f'text_sql = {text_sql}')
        result = cur.execute(text_sql)
        names_title = [description[0] for description in result.description]
        self.checkWidget.setColumnCount(len(names_title))
        self.checkWidget.setHorizontalHeaderLabels(names_title)

        self.addrow(result)
        con.close()

    def addrow(self, result):
        for i, row in enumerate(result):
            self.checkWidget.setRowCount(self.checkWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.checkWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))
        self.checkWidget.resizeColumnsToContents()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
