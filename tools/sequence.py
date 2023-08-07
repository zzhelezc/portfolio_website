#!/usr/bin/python3

import sys, os
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox,
                             QApplication, QVBoxLayout,QAbstractItemView,QListWidgetItem,
                             QPushButton,QFileDialog,QHBoxLayout,QLabel, QListView,
                             QLineEdit, QRadioButton, QMainWindow)

from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QSize, Qt 
import json





class Sequencer(QWidget):

    def __init__(self):
        super().__init__()
        self.icon_size = 200
        
        self.current_dir = os.getcwd()
        self.init_ui()

    def load_image_item(self, fajl,folder=None):
        icon = QIcon()
        item = QListWidgetItem()
        
        if folder is not None:
            pot = os.path.join(folder,fajl)
        else:
            pot = fajl
            
        icon.addFile(pot,size=QSize(self.icon_size,self.icon_size))
        item.setData(Qt.UserRole, pot.split('/')[-1])
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignBottom)
        
        return item

    def load_items_from_current_dir(self):
        folder = self.current_dir
        files = os.listdir(folder)

        files = [f for f in files if (os.path.isfile(os.path.join(folder,f)) and
                                      f.lower().endswith(('.png', '.jpg', '.jpeg')))]

        for foo in files:
            self.list.addItem(self.load_image_item(foo,folder=folder))
            
    def load_items(self, d, files):
        for f in files:
            self.list.addItem(self.load_image_item(f,folder=d))
        
    def init_ui(self):

        vbox = QVBoxLayout(self)

        self.current_dir_label = QLabel(f'Directory: {self.current_dir}')
        vbox.addWidget(self.current_dir_label)

        listWidget = QListWidget()
        
        listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        listWidget.setFlow(QListView.LeftToRight)
        listWidget.setWrapping(True)
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setMovement(QListView.Snap)
        listWidget.setIconSize(QSize(200,200))
        listWidget.setFocusPolicy(Qt.NoFocus)

        # Make selection grey
        palette = QPalette()
        palette.setColor(QPalette.Highlight, listWidget.palette().color(QPalette.Base))
        palette.setColor(QPalette.HighlightedText, listWidget.palette().color(QPalette.Text))
        listWidget.setPalette(palette)
        
        self.list = listWidget
        self.load_items_from_current_dir()

        vbox.addWidget(listWidget)
        self.setLayout(vbox)
        self.setGeometry(10, 10, 1260, 820)
        self.setWindowTitle('Sequence Creator')


        hbox = QHBoxLayout()
        

        btn_load_dir = QPushButton()
        btn_load_dir.setText("Load Directory")
        hbox.addWidget(btn_load_dir)
        btn_load_dir.clicked.connect(self.load_dir_btn_clicked)

        btn_load_seq = QPushButton()
        btn_load_seq.setText("Load Sequence")
        hbox.addWidget(btn_load_seq)
        btn_load_seq.clicked.connect(self.load_seq_btn_clicked)

        
        btn_save = QPushButton()
        btn_save.setText("Save Sequence")
        hbox.addWidget(btn_save)
        btn_save.clicked.connect(self.save_btn_clicked)

        hbox2 = QHBoxLayout()

        self.title = QLineEdit()
        self.title.setPlaceholderText('Enter title')
        hbox2.addWidget(self.title)

        self.href = QLineEdit()
        self.href.setPlaceholderText('Enter href')
        hbox2.addWidget(self.href)

        self.unlist_btn = QRadioButton('Unlist')
        hbox2.addWidget(self.unlist_btn)

        vbox.addLayout(hbox2)
        vbox.addLayout(hbox)
        
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.list.takeItem(self.list.row(self.list.currentItem()))
            
        if event.key() == Qt.Key_S:
            self.list.clearSelection()

    def mousePressEvent(self, event):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()
        QMainWindow.mousePressEvent(self, event)        

    ####################################################################################
    # Misc
    ####################################################################################
    def image_sequence(self):
        return [self.list.item(n).data(Qt.UserRole) for n in range(self.list.count())]
            
    ####################################################################################
    # button handlers
    ####################################################################################

    def save_btn_clicked(self):
        if self.title.text() == '' or self.href.text() == '':
            msg = QMessageBox()
            msg.setText('Please fill all the fields.')
            msg.exec()
            return 

        filename = f'{self.current_dir}/sequence.json'
        with open(filename, 'w') as f:
            f.write(json.dumps({
                'title'     : self.title.text(),
                'href'      : self.href.text(),
                'unlist'    : self.unlist_btn.isChecked(),
                'sequence'  : self.image_sequence()
            }, indent=4))

        msg = QMessageBox()
        msg.setText(f'written: {filename}\ntitle:{self.title.text()}\nhref:{self.href.text()}\nunlist:{self.unlist_btn.isChecked()}')
        msg.exec()    

    def load_dir_btn_clicked(self):
        res = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        if res != "":
            self.current_dir = res 
            self.list.clear()
            self.load_items_from_current_dir()
            self.current_dir_label.setText(f'Directory: {self.current_dir}')

    def load_seq_btn_clicked(self):
        d = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        if not os.path.isfile(f'{d}/sequence.json'):
            msg = QMessageBox()
            msg.setText(f'Error: No sequence.json in {d}!')
            msg.exec()
            return

        with open(f'{d}/sequence.json', 'r') as f:
            cfg = json.load(f)
            self.list.clear()
            self.current_dir = d
            self.current_dir_label.setText(f'Directory: {self.current_dir}')
            self.load_items(d, cfg['sequence'])
            self.title.setText(cfg['title'])
            self.href.setText(cfg['href'])
            

def main():

    App = QApplication(sys.argv)
    ex = Sequencer()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
