# -*- coding: utf-8 -*-

from PyQt5 import QtGui
import sys
import tela  ## nome do módulo da tela
 
class Calc(QtGui.QMainWindow, tela.Ui_Janela):
    def __init__(self, parent=None):
        super(Calc, self).__init__(parent)
        self.setupUi(self)
        
        self.termo = ""
        self.expressao = []
        self.resultado = False
        
        self.btLimpar.clicked.connect(self.evtLimparTela)
        self.btResultado.clicked.connect(self.evtResultado)
        
        # Conexão de eventos dos botões numéricos
        for bt in self.__dict__:
            if bt.startswith("btNum"):
                getattr(self, bt).clicked.connect(self.evtNumeros)
        
        # Conexão dos eventos dos botões das operações
        self.btDiv.clicked.connect(lambda: self.evtOperacao("/"))
        self.btMult.clicked.connect(lambda: self.evtOperacao("*"))
        self.btSoma.clicked.connect(lambda: self.evtOperacao("+"))
        self.btSubtr.clicked.connect(lambda: self.evtOperacao("-"))
            
    def evtNumeros(self):
        if self.resultado:
            self.expressao = []
            self.termo = self.sender().objectName()[-1]
            self.resultado = False
        else:
            self.termo += self.sender().objectName()[-1]
        self.lcd.display(int(self.termo))
     
    def evtOperacao(self, operacao):
        if self.termo:
            if not self.resultado:
                self.expressao.append(int(self.termo))
                if len(self.expressao) > 1:
                    self.calcular()
            else:
                self.resultado = False
            self.expressao.append(operacao)
            self.termo = ""
     
    def evtLimparTela(self):
        self.termo = ""
        self.expressao = []
        self.lcd.display(0)
         
    def evtResultado(self):
        if self.termo and not self.resultado:
            self.expressao.append(int(self.termo))
            self.calcular()
            self.resultado = True
     
    def calcular(self):
        self.termo = str(int(eval("".join(map(str,self.expressao)))))
        self.expressao = [self.termo]
        self.lcd.display(self.termo)
 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = Calc()
    main_window.show()
    app.exec_()