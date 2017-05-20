import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# Create the actions
# @pyqtSlot()


def emptyOptionsGrid():
    for i in reversed(range(options_grid.count())):
        options_grid.itemAt(i).widget().setParent(None)

def showCurrentLightSwitches():
    if(not options_grid.isEmpty()):
        emptyOptionsGrid()
        print(options_grid)
    else:
        None
    light_options=['yellow_cfl1','yellow_cfl2','yellow_bulb12', 'fan', 'yellow_tube1', 'yellow_tube2','white_tube1', 'white_tube2']
    for i in range(0,len(light_options)):
        options_grid.addWidget(QPushButton(light_options[i]),0, i)

def showCurtainSwitches():
    if(not options_grid.isEmpty()):
        emptyOptionsGrid()
        print(options_grid.count())
    else:
        None

def center(widget):
    qr = widget.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    widget.move(qr.topLeft())



# create our window
app = QApplication(sys.argv)
#main window
room_control=QWidget()
room_control.resize(500, 500)
center(room_control)
room_control.setWindowTitle("Abhinav's Room Control")

options_grid=QGridLayout()
room_control.setLayout(options_grid)

# Main Light Control Switches
light_switch_button = QPushButton('Lights', room_control)
# connect the signals to the slots
light_switch_button.clicked.connect(showCurrentLightSwitches)


# Curtains Switch
curtains_button=QPushButton('Curtains', room_control)
curtains_button.move(100, 0)
# connect the signals to the slots
curtains_button.clicked.connect(showCurtainSwitches)



room_control.show()
sys.exit(app.exec_())

