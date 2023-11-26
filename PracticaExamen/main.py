from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QTabWidget, QPushButton, QLabel, QLineEdit, QCheckBox, QRadioButton, QComboBox, QFrame
import sys

def main():
    app = QApplication(sys.argv)

    # Ventana principal
    mainWindow = QMainWindow()
    centralWidget = QWidget(mainWindow)
    mainWindow.setCentralWidget(centralWidget)

    # Diseño principal
    mainLayout = QVBoxLayout(centralWidget)

    # Pestañas
    tabWidget = QTabWidget()
    mainLayout.addWidget(tabWidget)

    # Pestaña 1 - QHBoxLayout
    tab1Widget = QWidget()
    hBoxLayout = QHBoxLayout(tab1Widget)
    hBoxLayout.addWidget(QPushButton("Botón 1"))
    hBoxLayout.addWidget(QLabel("Etiqueta 1"))
    hBoxLayout.addWidget(QLineEdit("Texto inicial"))
    tabWidget.addTab(tab1Widget, "Tab 1")

    # Pestaña 2 - QGridLayout y QStackedLayout
    tab2Widget = QWidget()
    gridLayout = QGridLayout(tab2Widget)
    gridLayout.addWidget(QCheckBox("Casilla de verificación"), 0, 0)
    gridLayout.addWidget(QRadioButton("Botón de radio"), 0, 1)

    stackedLayout = QStackedLayout()
    stackedLayout.addWidget(QLabel("Página 1"))
    stackedLayout.addWidget(QLabel("Página 2"))
    gridLayout.addLayout(stackedLayout, 1, 0, 1, 2)

    tabWidget.addTab(tab2Widget, "Tab 2")

    # Agregar ComboBox y QFrame
    comboBox = QComboBox()
    comboBox.addItem("Opción 1")
    comboBox.addItem("Opción 2")
    mainLayout.addWidget(comboBox)

    frame = QFrame()
    frame.setFrameShape(QFrame.Shape.Box)
    frame.setLineWidth(2)
    mainLayout.addWidget(frame)

    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
