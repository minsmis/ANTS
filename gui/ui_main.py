import sys
import time
import PySide6 as pys
import numpy as np
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QTextEdit, QMainWindow, \
    QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import core.ants as ants


class AntsBatch:
    def __init__(self):
        self.batch_ants = np.ndarray
        self.storage = str


class ChatBrowser(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setWidget(widget)
        self.setWidgetResizable(True)

    def showText(self, text, user_f):
        chatLbl = QLabel(text)
        chatLbl.setWordWrap(True)
        chatLbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        if user_f:
            chatLbl.setStyleSheet('QLabel { padding: 1em }')
            chatLbl.setAlignment(Qt.AlignRight)
        else:
            chatLbl.setStyleSheet('QLabel { background-color: #DDD; padding: 1em }')
            chatLbl.setAlignment(Qt.AlignLeft)
        self.widget().layout().addWidget(chatLbl)

    def showFigure(self, figure, user_f):
        canvasWidget = FigureCanvasQTAgg(figure)
        if user_f:
            canvasWidget.setStyleSheet('FigureCanvasQTAgg { padding: 1em }')
            canvasWidget.setAlignment(Qt.AlignRight)
        else:
            canvasWidget.setStyleSheet('FigureCanvasQTAgg { background-color: #DDD; padding: 1em }')
            canvasWidget.setAlignment(Qt.AlignLeft)
        self.widget().layout().addWidget(canvasWidget)

    def event(self, e):
        if e.type() == 43:
            self.verticalScrollBar().setSliderPosition(self.verticalScrollBar().maximum())
        return super().event(e)


class TextEditPrompt(QTextEdit):
    returnPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.setStyleSheet('QTextEdit { border: 1px solid #AAA; } ')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            if e.modifiers() == Qt.ShiftModifier:
                return super().keyPressEvent(e)
            else:
                self.returnPressed.emit()
        else:
            return super().keyPressEvent(e)


class Prompt(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__textEdit = TextEditPrompt()
        self.__textEdit.textChanged.connect(self.updateHeight)
        lay = QHBoxLayout()
        lay.addWidget(self.__textEdit)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)
        self.updateHeight()

    def updateHeight(self):
        document = self.__textEdit.document()
        height = document.size().height()
        self.setMaximumHeight(int(height + document.documentMargin()))

    def getTextEdit(self):
        return self.__textEdit


class MainWindow(QMainWindow, AntsBatch):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt Chat Widget Example')
        self.__prompt = Prompt()
        self.__textEdit = self.__prompt.getTextEdit()
        self.__textEdit.setPlaceholderText('Write some text...')
        self.__textEdit.returnPressed.connect(self.__chat)
        self.__browser = ChatBrowser()
        lay = QVBoxLayout()
        lay.addWidget(self.__browser)
        lay.addWidget(self.__prompt)
        lay.setSpacing(0)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)
        self.resize(1000, 500)

        self.__browser.showText('Hello!', True)
        self.__browser.showText('Hello! How may i help you?', False)

    def __chat(self):
        self.__browser.showText(self.__textEdit.toPlainText(), True)
        self.__operation_classifier(self.__textEdit.toPlainText())
        self.__textEdit.clear()

    def __operation_classifier(self, input):

        if input.startswith('import'):  # example: import > /home/user/.../file.mat
            try:
                operation, path = self.__process_query(query=input)

                path_list = ants.dirprep.DirPrep.get_data_directory(superior_path=path,
                                                                    expander='mat')  # get data directories
                self.batch_ants = ants.Ants.make(batch_size=len(path_list))  # make 'ants' as worker
                [self.batch_ants[i].call_neuralynx(path=str(path_list[i])) for i, _ in
                 enumerate(self.batch_ants)]  # import neuralynx

                self.__response(response_content=str(operation) + 'succeeded')  # report result
                self.__response(response_content=str(self.batch_ants[0].samples[0:10]))
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('downsample'):  # example: downsample > 2000
            try:
                operation, target_fs = self.__process_query(query=input)

                # downsample
                [self.batch_ants[i].downsampling(target_fs=int(target_fs)) for i, _ in enumerate(self.batch_ants)]

                self.__response(response_content=str(operation) + 'succeeded')  # report result
                self.__response(response_content=str(self.batch_ants[0].sample_frequency))
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('normalize'):  # example: normalize > rms
            try:
                operation, method = self.__process_query(query=input)

                # normalization
                [self.batch_ants[i].normalization(method=str(method)) for i, _ in enumerate(self.batch_ants)]

                self.__response(response_content=str(operation) + 'succeeded')  # report result
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('butter'):  # example: butter > [40, 100]
            try:
                operation, band = self.__process_query(query=input)

                # bandpass filter
                [self.batch_ants[i].bandpass_butter(target_band=eval(band)) for i, _ in enumerate(self.batch_ants)]

                self.__response(response_content=str(operation) + 'succeeded')  # report result
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('spectrogram'):  # example: spectrogram > duration=[0, 10]; nperseg=1000; pscale=log
            try:
                operation, parameters = self.__process_query(query=input)
                sub_params = self.__process_subparam(parameter=parameters)

                # calc multitaper spectrogram
                [self.batch_ants[i].spectrogram(**sub_params) for i, _ in enumerate(self.batch_ants)]

                self.__response(response_content=str(operation) + 'succeeded')  # report result
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('spectrum'):  # example: spectrum > xscope=[0, 200]
            try:
                operation, parameters = self.__process_query(query=input)
                sub_params = self.__process_subparam(parameter=parameters)

                f, m, sem = ants.Ants.sem(batch=self.batch_ants)  # calculate sem
                # draw power spectrum with sem
                self.storage = ants.Ants().power_spectrum(freqs=f, mean=m, sem=sem, **sub_params)

                self.__response(response_content=str('operation') + 'succeeded')  # report result
                # self.__fig_response(figure=fig)  # report figure
                # try:
                #     self.__fig_response(figure=fig)  # report figure
                # except:
                #     self.__response(response_content=str(operation) + ': Cannot plot figure')  # report figure error
                # self.__response(response_content=str('operation') + ': Stored in, ' + storage)  # report storage
            except:
                self.__response(response_content='Failed: ' + input)  # report result
        elif input.startswith('test'):
            operation, parameters = self.__process_query(query=input)
            sub_params = self.__process_subparam(parameter=parameters)
            self.__response(response_content=str(type(operation)))  # report result
            self.__response(response_content=str(type(sub_params)))  # report result

    def __response(self, response_content):
        self.__browser.showText(response_content, False)

    def __fig_response(self, figure):
        self.__browser.showFigure(figure, False)

    def __process_query(self, query):
        component = query.split('>')
        component = [component[i].strip() for i, _ in enumerate(component)]  # strip all
        operation = component[0]  # operation type
        # last value must be parameter
        parameter = component[-1]
        return operation, parameter

    def __process_subparam(self, parameter):
        dict_sub_params = {}

        sub_parameters = parameter.split(';')
        sub_parameters = [sub_parameters[i].strip() for i, _ in enumerate(sub_parameters)]  # strip all
        sub_parameters = [sub_parameters[i].split('=') for i, _ in enumerate(sub_parameters)
                          if '=' in sub_parameters[i]]  # split sub_parameter and sub_param value
        # [dict_sub_params.update({component[0].strip(): eval(component[-1])}) for component in
        #  sub_parameters]  # make sub_param dict
        for component in sub_parameters:  # make sub_param dict
            try:
                dict_sub_params.update({component[0].strip(): eval(component[-1])})
            except:
                dict_sub_params.update({component[0].strip(): component[-1]})

        return dict_sub_params


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
