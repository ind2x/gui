from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os
from MyFileManager import FileManager
import magic

file_manager = FileManager()

if getattr(sys, 'frozen', False):
    # PyInstaller로 빌드된 경우
    script_directory = os.path.dirname(sys.executable) + '\\..'
else:
    # 일반적으로 실행되는 경우
    script_directory = os.path.dirname(os.path.realpath(__file__))

class kCheckFileExtension(object):
    def setupUi(self, MainWindow):
        # 디렉터리 경로 저장
        self.directory = ''

        # 메인 윈도우 설정
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 585)
        MainWindow.setStyleSheet("")

        # 아이콘 설정
        icon_path = os.path.join(script_directory, 'image', 'icon.png')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)

        # 중앙 위젯과 메인 레이아웃 설정
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # 버튼을 위한 수평 레이아웃
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # 홈 버튼
        self.Btn_home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Btn_home.setObjectName("Btn_home")
        self.Btn_home.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.horizontalLayout_2.addWidget(self.Btn_home)

        # 닫기 버튼
        self.Btn_close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Btn_close.setObjectName("Btn_close")
        self.Btn_close.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.horizontalLayout_2.addWidget(self.Btn_close)

        # 폴더 선택
        self.Btn_SetDirectoryPath = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Btn_SetDirectoryPath.setObjectName("Btn_SetDirectoryPath")
        self.Btn_SetDirectoryPath.setStyleSheet(
            "background-color: rgb(85, 170, 255);")
        self.horizontalLayout_2.addWidget(self.Btn_SetDirectoryPath)

        # 확장자 검사 버튼
        self.Btn_checkExtension = QtWidgets.QPushButton(
            parent=self.centralwidget)
        self.Btn_checkExtension.setObjectName("Btn_checkExtension")
        self.Btn_checkExtension.setStyleSheet(
            "background-color: rgb(85, 170, 255);")
        self.horizontalLayout_2.addWidget(self.Btn_checkExtension)

        # 새로고침 버튼
        self.Btn_refresh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Btn_refresh.setObjectName("Btn_refresh")
        self.Btn_refresh.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.horizontalLayout_2.addWidget(self.Btn_refresh)

        # 수평 레이아웃을 수직 레이아웃에 추가
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 입력 필드 및 콤보 박스를 위한 수평 레이아웃
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 검색 입력 필드
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        # 검색 기능을 위한 함수 정의
        def search_table():
            search_text = self.lineEdit.text().lower()  # 검색어를 소문자로 변환하여 비교
            for row_idx in range(self.tableWidget.rowCount()):
                row_hidden = True
                for col_idx in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row_idx, col_idx)
                    if item is not None:
                        cell_data = item.text().lower()
                        if search_text in cell_data:
                            row_hidden = False
                            break
                self.tableWidget.setRowHidden(row_idx, row_hidden)

        # 검색어가 변경될 때마다 검색 함수 호출
        self.lineEdit.textChanged.connect(search_table)

        # 검색 대상 콤보 박스
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 22))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("전체")
        self.comboBox.addItem("문서")
        self.comboBox.addItem("실행파일")
        self.horizontalLayout.addWidget(self.comboBox)

        # 수평 레이아웃을 수직 레이아웃에 추가
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 스크롤 가능한 영역
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        # 스크롤 가능한 영역의 내용 위젯
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 816, 482))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 테이블 위젯
        self.tableWidget = QtWidgets.QTableWidget(
            parent=self.scrollAreaWidgetContents_2)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1200, 1200))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(1200, 1200))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        # 테이블 열 헤더 설정
        self.tableWidget.setHorizontalHeaderLabels(
            ["이름", "경로", "확장자", "파일 크기"])
        header = self.tableWidget.horizontalHeader()

        # 더블 클릭 시 파일/폴더 열기
        self.tableWidget.itemDoubleClicked.connect(self.double_clicked)

        # 폴더 선택 후 출력
        self.setDirectoryPath()

        self.horizontalLayout_3.addWidget(self.tableWidget)

        # 스크롤 가능한 영역의 내용 위젯 설정
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # 수직 레이아웃에 스크롤 가능한 영역 추가
        self.verticalLayout.addWidget(self.scrollArea_2)

        # 메인 윈도우에 중앙 위젯 설정
        MainWindow.setCentralWidget(self.centralwidget)

        # 상태 표시줄 설정
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 버튼 동작 연결
        self.Btn_home.clicked.connect(self.goHome)
        self.Btn_close.clicked.connect(self.close_window)
        self.Btn_SetDirectoryPath.clicked.connect(self.setDirectoryPath)
        self.Btn_checkExtension.clicked.connect(self.check_extension)
        self.Btn_refresh.clicked.connect(self.refresh)

        # F5 단축키 설정
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key.Key_F5))
        self.actionRefresh.triggered.connect(self.refresh)
        MainWindow.addAction(self.actionRefresh)

        # UI 다시 설정
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 콤보 박스 선택에 따라 테이블 필터링
        self.comboBox.currentIndexChanged.connect(self.filter_table)

    # 더블 클릭 시 이벤트 함수
    def double_clicked(self, item):
        # 윈도우 파일탐색기로 선택된 파일 혹은 폴더 열기
        selected_row = item.row()

        # 현재 파일 이름 및 경로 가져오기
        current_file_name = self.tableWidget.item(selected_row, 0).text()
        current_file_path = self.tableWidget.item(selected_row, 1).text()
        name = os.path.join(current_file_path, current_file_name)

        try:
            if os.path.isdir(name):
                # subprocess.run(['explorer', '', name], shell=True)
                os.startfile(name)
            else:
                subprocess.run(['start', '', name], shell=True)
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self.centralwidget, "에러", f"파일 혹은 폴더가 없습니다.\n에러 메시지: {str(e)}", QtWidgets.QMessageBox.StandardButton.Ok)

    # table 설정
    def showTable(self):
        # 테이블 초기화
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        if file_manager.directory_path == '':
            pass
        else:
            # 데이터를 테이블에 추가
            files_info = file_manager.list_files_in_directory()
            for row_idx, row_data in enumerate(files_info):
                path = os.path.join(row_data["file_path"], row_data["file_name"])
                isfile = os.path.isfile(path)
                
                if isfile:
                    row_idx = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_idx)  # 행 추가
                    
                    for col_idx, key in enumerate(["file_name", "file_path", "extension", "file_size"]):
                        item = QtWidgets.QTableWidgetItem(str(row_data[key]))
                        item.setFlags(
                            item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                        item.setFlags(
                            item.flags() & ~QtCore.Qt.ItemFlag.ItemIsDropEnabled)
                        self.tableWidget.setItem(row_idx, col_idx, item)

    # 버튼에 대한 동작수행 함수 정의
    def goHome(self):
        # 메인 화면으로 이동
        if self.parent is not None and isinstance(self.parent, QtWidgets.QMainWindow):
            self.parent.close()  # 현재 파일 탐색기 창을 닫음

    def close_window(self):
        # 파일 종료
        sys.exit(0)

    def setDirectoryPath(self):
        # 폴더 경로 설정
        # 사용자에게 디렉토리 선택 대화상자 표시
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, "디렉토리 선택", os.getcwd())

        # 파일 경로를 넘겨받으면 해당 경로에 있는 목록 출력
        file_manager.setDirPath(self.directory)

        self.showTable()
        
    def check_extension(self):
        # 파일 확장자 및 마임 타입 검사
        selected_row = self.tableWidget.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(
                self.centralwidget, "경고", "파일을 선택하세요.", QtWidgets.QMessageBox.StandardButton.Ok)
            return

        # 현재 파일 이름 및 경로 가져오기
        current_file_name = self.tableWidget.item(selected_row, 0).text()
        current_file_path = self.tableWidget.item(selected_row, 1).text()
        file_path = os.path.join(current_file_path, current_file_name)

        # 파일 내용을 기반으로 마임 타입 검출
        mime = magic.Magic()
        mime_type = mime.from_file(file_path)

        # 직접 추가한 실행 파일 확장자 목록
        executable_extensions = {
            '.exe', '.bat', '.cmd', '.msi', '.sh', '.dll', '.ps1', '.com', '.jar', '.vbs'}

        # 파일 확장자가 실행 파일 확장자에 속하는지 확인
        is_executable = any(file_path.lower().endswith(ext)
                            for ext in executable_extensions)

        # 결과를 상태 표시줄에 표시
        self.statusbar.showMessage(
            f"File: {current_file_name}, Mime Type: {mime_type}")

        # 결과에 따라 메시지 박스 출력
        QtWidgets.QMessageBox.information(
            self.centralwidget, "Result",
            f"File: {current_file_name}\nMime Type: {mime_type}\nIs Executable: {is_executable}",
            QtWidgets.QMessageBox.StandardButton.Ok)

    def refresh(self):
        # 현재 디렉토리의 파일 목록을 다시 가져와서 테이블에 표시
        file_manager.setDirPath(self.directory)

        self.showTable()

        # 새로고침 시 화면이 빠르게 꺼졌다 켜지는 것 같은 이펙트 대신에 statusBar에 문구 출력
        # 문구 출력 후 1초 후에 timeout 시그널이 발생하면 statusBar에 있는 문구를 지움
        self.statusbar.showMessage("Status: 새로고침")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.statusbar.clearMessage)
        self.timer.start(1000)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 메인창 이름 설정
        MainWindow.setWindowTitle(_translate("MainWindow", "5Sorry"))

        # 버튼 이름 설정
        self.Btn_home.setText(_translate("MainWindow", "메인 홈으로 이동"))
        self.Btn_close.setText(_translate("MainWindow", "닫기"))
        self.Btn_SetDirectoryPath.setText(_translate("MainWindow", "폴더 선택"))
        self.Btn_checkExtension.setText(_translate("MainWindow", "숨겨진 확장자 검사"))
        self.Btn_refresh.setText(_translate("MainWindow", "새로고침(F5)"))

        # 콤보 박스 이름 설정
        self.comboBox.setItemText(0, _translate("MainWindow", "전체"))
        self.comboBox.setItemText(1, _translate("MainWindow", "문서"))
        self.comboBox.setItemText(2, _translate("MainWindow", "실행파일"))

        # 테이블 헤더 이름 설정
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "이름"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "경로"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "확장자"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "파일 크기"))

    def filter_table(self):
        selected_option = self.comboBox.currentText()

        for row_idx in range(self.tableWidget.rowCount()):
            # "사이즈" 열에 해당하는 아이템
            item = self.tableWidget.item(row_idx, 2)

            if item is not None:
                # 파일명, 파일 경로 추출
                file_name = self.tableWidget.item(row_idx, 0).text()
                file_path = self.tableWidget.item(row_idx, 1).text()

                item_path = os.path.join(file_path, file_name)
                _, file_extension = os.path.splitext(item_path)  # 확장자 추출

                if selected_option == "전체":
                    self.tableWidget.setRowHidden(row_idx, False)
                elif selected_option == "실행파일" and file_extension.lower() in {'.exe', '.bat', '.cmd', '.msi', '.sh', '.dll', '.ps1', '.com', '.jar', '.vbs'}:
                    self.tableWidget.setRowHidden(row_idx, False)
                elif selected_option == "문서" and file_extension.lower() in {'.txt', '.doc', '.docx', '.pdf', '.xml', '.docx', '.hwp', '.hwpx', '.py', '.c', '.cpp', '.java', '.ppt', '.html', '.css', '.js', '.md'}:
                    self.tableWidget.setRowHidden(row_idx, False)
                elif selected_option == "사진" and file_extension.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.ico', '.WMF', '.bmp'}:
                    self.tableWidget.setRowHidden(row_idx, False)
                else:
                    self.tableWidget.setRowHidden(row_idx, True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = kCheckFileExtension()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())