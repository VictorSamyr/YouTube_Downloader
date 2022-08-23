import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import *
from pytube import YouTube

class Video():
    def __init__(self, url):
        self.url = url
        self.video = YouTube(url)
        
    def get_Thumb(self):
        thumb = self.video.thumbnail_url
        return thumb
    
    def get_Title(self):
        title = self.video.title
        return title
    
class Tela(QWidget):
    def __init__(self):
        super().__init__()

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()
        
        self.setWindowTitle("Youtube Video Downloader")
        self.setFixedSize(400,200)
        self.setStyleSheet("background-color: white;")

        linkLabel=QLabel("Video Link")
        linkLabel.setStyleSheet("font-weight: 600;font-family: Arial;border:0px;")

        link = QLineEdit()
        
        layout1.addWidget(linkLabel)
        layout1.addWidget(link)
        layout1.addLayout(layout2)

        layout2.addLayout(layout3)
        
        v1 = Video('https://www.youtube.com/watch?v=QdVFvsCWXrA')
        img = QImage()
        img.loadFromData(requests.get(v1.get_Thumb()).content)
        thumb_place = QLabel(self)
        thumb_img = QPixmap(img)
        thumb_place.setPixmap(thumb_img.scaled(200,90))
        video_title = QLabel(v1.get_Title())
        video_title.setStyleSheet("font-weight: 600;font-family: Arial;color:")
        l2 = QLabel("Direita")
        
        layout3.addWidget(thumb_place)
        layout3.addWidget(video_title)

        layout2.addWidget(l2)
        
        
        self.setLayout(layout1)
        self.show()
       




if __name__ == "__main__":
        app = QApplication([])
        app.setStyle('Fusion')
        tela = Tela()
        app.exec()
