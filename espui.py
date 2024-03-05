import win32api
import serial_asyncio
import win32con  
import asyncio, nest_asyncio
import threading
from PySide6.QtWidgets import (QApplication, QWidget, QSystemTrayIcon,QMainWindow,QMenu,QMessageBox)
from PySide6.QtGui import QAction, QCloseEvent,QIcon
from esp_ui import Ui_Form
from serial.tools import list_ports

import ctypes


nest_asyncio.apply()



class keyboard(QWidget):
    def __init__(self, baudrate):
        super().__init__()
        self.port = "None"
        self.baudrate = baudrate
        self.MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
        self.key=[0x41,0x42,0x43,0x44]

        self.init_ui()
        
    def showsuccess(self):
        self.startbutton.setDisabled(True)
        self.success_sign.show()
        self.fail_sign.hide()
        self.portbox.setDisabled(True)



    def showfail(self):
        self.startbutton.setDisabled(False)
        self.fail_sign.show()
        self.success_sign.hide()
        self.portbox.setDisabled(False)

    def init_ui(self):
        # self.ui =Ui_MainWindow()
        self.ui= Ui_Form()
        self.ui.setupUi(self)

        self.portbox=self.ui.comboBox
        self.startbutton=self.ui.pushButton
        self.refreshbutton=self.ui.pushButton_2
        self.keycustombutton=self.ui.pushButton_3




        # 初始化系统托盘相关的对象和菜单项
        self._restore_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("kb.png"))  # 替换为你的图标路径
        self.create_actions()
        self.create_tray_icon()
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.tray_icon_activated)

        self.startbutton.clicked.connect(self.run_serial)
        self.refreshbutton.clicked.connect(self.refresh_serial)
        self.keycustombutton.clicked.connect(self.keycustom)

        self.keya=self.ui.lineEdit
        self.keyb=self.ui.lineEdit_2
        self.keyc=self.ui.lineEdit_3
        self.keyd=self.ui.lineEdit_4


        # # 提取要操作的控件
        self.success_sign = self.ui.label_3  # 运行提示
        self.fail_sign = self.ui.label_2  # 停止提示

        self.a_ok=self.ui.label_8
        self.b_ok=self.ui.label_9
        self.c_ok=self.ui.label_10
        self.d_ok=self.ui.label_11
        self.a_ok.hide()
        self.b_ok.hide()
        self.c_ok.hide()
        self.d_ok.hide()

        self.success_sign.hide()
        self.fail_sign.hide()

        self.refresh_serial()
        if self.port!='None':
            self.run_serial()
        else:
            self.showfail()  
        # self.focusInEvent()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '是否最小化到托盘',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.ignore()
            self.hide()
        else:
            event.accept()

    def hideEvent(self, event):
        self.hide()

    def minimize_to_tray(self):
        # 最小化窗口到系统托盘
        self.hide()
    def restore_from_tray(self):
        # 还原窗口
        if self.isMinimized():
            self.showNormal()
        elif self.isMaximized():
            self.showMaximized()
        else:
            self.show()

    def tray_icon_activated(self, reason):
        # 当系统托盘图标被点击时的处理
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # 如果点击的是触发事件（比如左键单击），则还原窗口
            self.restore_from_tray()

    def create_actions(self):
        # 创建菜单项
        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)  # "显示"菜单项触发还原窗口的操作
        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(QApplication.quit)  # "退出"菜单项触发退出应用程序的操作

    def create_tray_icon(self):
        # 创建系统托盘图标和上下文菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)
        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()


    def keydown(self, num):
        win32api.keybd_event(num, self.MapVirtualKey(num, 0), 0, 0)

    def keyup(self, num):
        win32api.keybd_event(
            num, self.MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0
        )

    async def read_from_serial(self):
        data = await self.reader.read(2)
        return data

    # 异步写入串口数据
    async def write_to_serial(self, data):
        self.writer.write(data)
        await self.writer.drain()

    async def _run_serial(self):
        # 连接串口
        while True:
            self.port = self.portbox.currentText()
            try:
                self.reader, self.writer = await serial_asyncio.open_serial_connection(
                    url=self.port, baudrate=self.baudrate
                )
                self.showsuccess()
                break
        
            except:
                self.showfail()
                break
    
    def refresh_serial(self):
        ser=list_ports.comports()
        serlist=[]
        for element in ser:
            serlist.append(element.device)
            if element.description[:16]== 'USB-SERIAL CH340':
                self.port=element.device        
        self.portbox.clear()
        self.portbox.addItems(serlist)
        self.portbox.setCurrentText(self.port)
    
    def keycustom(self):
        a=ord(self.keya.text())
        b=ord(self.keyb.text())
        c=ord(self.keyc.text())
        d=ord(self.keyd.text())
        key=[a,b,c,d]
        for i in range(4):
            if key[i]>0x61 and key[i]<0x7a:
                key[i]=key[i]-0x20

        self.key = key

    async def _run(self):
        status = [0, 0, 0, 0]

        while True:
            try:
                data = await self.read_from_serial()
                # print(data, "start")
            except:
                self.showfail()
                break

            # 处理数据
            # ...
            # 模拟按键
            if data == b"A1" and status[0] == 0:
                # print(data)
                self.keydown(self.key[0])
                status[0] = 1
                self.a_ok.show()
            if data == b"B1" and status[1] == 0:
                # print(data)
                self.keydown(self.key[1])
                status[1] = 1
                self.b_ok.show()
            if data == b"C1" and status[2] == 0:
                # print(data)
                self.keydown(self.key[2])
                status[2] = 1
                self.c_ok.show()
            if data == b"D1" and status[3] == 0:
                # print(data)
                self.keydown(self.key[3])
                status[3] = 1
                self.d_ok.show()

            if data == b"A0" and status[0] == 1:
                self.keyup(self.key[0])
                status[0] = 0
                self.a_ok.hide()
            if data == b"B0" and status[1] == 1:
                self.keyup(self.key[1])
                status[1] = 0
                self.b_ok.hide()
            if data == b"C0" and status[2] == 1:
                self.keyup(self.key[2])
                status[2] = 0
                self.c_ok.hide()
            if data == b"D0" and status[3] == 1:
                self.keyup(self.key[3])
                status[3] = 0
                self.d_ok.hide()

    def run(self):
        asyncio.run(self._run_serial())
        asyncio.run(self._run())

    def run_serial(self):
        # 在新线程中启动事件循环
        new_loop = asyncio.new_event_loop()
        self.loop = new_loop
        t = threading.Thread(target=self.start_loop, args=(new_loop,), daemon=True)
        t.start()
        # 将coroutine添加到新线程的事件循环中
        coro1 = self._run_serial()
        asyncio.run_coroutine_threadsafe(coro1, new_loop)
        coro2 = self._run()
        asyncio.run_coroutine_threadsafe(coro2, new_loop)
        

    def start_loop(self, loop):
        # 启动事件循环
        asyncio.set_event_loop(loop)
        loop.run_forever()



app= QApplication([])
kb = keyboard(115200)
kb.show()
app.exec()

