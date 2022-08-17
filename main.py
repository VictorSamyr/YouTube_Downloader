from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QFormLayout,QLineEdit

class Tela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Video Downloader")
        self.setFixedSize(400,200)
        layout = QFormLayout()
        layout.addRow(QLabel("Link Do Vídeo"))
        layout.addRow(QLineEdit())
        self.setLayout(layout)
       




if __name__ == "__main__":
        app = QApplication([])
        tela = Tela()
        tela.show()
        app.exec()
