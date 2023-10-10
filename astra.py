import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QLineEdit, QWidget
from PyQt5.QtCore import QDir

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Дерево Файловой Системы")

#Домашняя директория текущего пользователя
home_dir = os.path.expanduser("~")

#Создаем модель для файловой системы
model = QFileSystemModel()
model.setRootPath(home_dir)
model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot | QDir.Hidden) # скрытые файлы

#Создаем виджеты
tree_view = QTreeView()
tree_view.setModel(model)
tree_view.setRootIndex(model.index(home_dir))

# Создаем окно для фильтра
filter_line_edit = QLineEdit()
filter_line_edit.setPlaceholderText("Фильтр")

#Функция фильтра
def filter_changed(text):
    filter_text = filter_line_edit.text()
    print(filter_text)
    if not filter_text:
        # Если фильтр пуст, сбрасываем фильтрацию
        model.setNameFilters([])
        model.setNameFilterDisables(True)
    else:
        # Если что то есть то добовляем *, чтобы видеть файлы начинающиеся с...
        name_filter = ("{}*").format(filter_text)
        model.setNameFilters([name_filter])
        model.setNameFilterDisables(False)

filter_line_edit.textChanged.connect(filter_changed)

#Создаем контейнерный виджет для размещения виджетов
widget = QWidget()
layout = QVBoxLayout() #вертикальный макет
layout.addWidget(filter_line_edit)
layout.addWidget(tree_view)
widget.setLayout(layout)
window.setCentralWidget(widget)
window.setGeometry(100, 100, 800, 600)
window.show()
sys.exit(app.exec())