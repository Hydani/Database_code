import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from datetime import date
from datetime import timedelta
import dateutil.parser as parser    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        libraryBranches = ['Main Branch', 'West Branch', 'East Branch']

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 848)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTab.setGeometry(QtCore.QRect(-4, -1, 618, 831))

        self.MainTab.setObjectName("MainTab")

        """ Start of Search Tab """
        ## Search by Person Tab Frame
        self.searchTab_1 = QtWidgets.QWidget()
        self.searchTab_1.setObjectName("searchTab_1")

        self.searchTab_2 = QtWidgets.QTabWidget(self.searchTab_1)
        self.searchTab_2.setGeometry(QtCore.QRect(-4, 9, 611, 791))
        self.searchTab_2.setObjectName("searchTab_2")

        self.byPerson_tab = QtWidgets.QWidget()
        self.byPerson_tab.setObjectName("byPerson_tab")

        self.personSearchBt = QtWidgets.QPushButton(self.byPerson_tab)
        self.personSearchBt.setGeometry(QtCore.QRect(470, 20, 81, 31))
        self.personSearchBt.setObjectName("personSearchBt")
        self.personSearchBt.clicked.connect(self.searchByPersonAction)

        self.searchPerson = QtWidgets.QLineEdit(self.byPerson_tab)
        self.searchPerson.setGeometry(QtCore.QRect(60, 20, 391, 31))
        self.searchPerson.setObjectName("searchPerson")

        self.personResult = QtWidgets.QTableView(self.byPerson_tab)
        self.personResult.setGeometry(QtCore.QRect(60, 70, 491, 651))
        self.personResult.setObjectName("personResult")
        ## Search by Book Tab Frame
        self.searchTab_2.addTab(self.byPerson_tab, "")

        self.byBook_tab = QtWidgets.QWidget()
        self.byBook_tab.setObjectName("byBook_tab")

        self.searchBook = QtWidgets.QLineEdit(self.byBook_tab)
        self.searchBook.setGeometry(QtCore.QRect(60, 20, 391, 31))
        self.searchBook.setObjectName("searchBook")

        self.bookSearchBt = QtWidgets.QPushButton(self.byBook_tab)
        self.bookSearchBt.setGeometry(QtCore.QRect(470, 20, 81, 31))
        self.bookSearchBt.setObjectName("bookSearchBt")
        self.bookSearchBt.clicked.connect(self.searchByBookAction)

        self.bookResult = QtWidgets.QTableView(self.byBook_tab)
        self.bookResult.setGeometry(QtCore.QRect(60, 70, 491, 651))
        self.bookResult.setObjectName("bookResult")

        self.searchTab_2.addTab(self.byBook_tab, "")

        self.MainTab.addTab(self.searchTab_1, "")
        """ End of Search Tab """

        """ Start of Checkout Tab """
        self.checkoutTab = QtWidgets.QWidget()
        self.checkoutTab.setObjectName("checkoutTab")
        ## List of Books Frame
        self.bListFrame = QtWidgets.QFrame(self.checkoutTab)
        self.bListFrame.setGeometry(QtCore.QRect(20, 20, 571, 251))
        self.bListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bListFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bListFrame.setObjectName("bListFrame")

        self.bookListLabel = QtWidgets.QLabel(self.bListFrame)
        self.bookListLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.bookListLabel.setObjectName("bookListLabel")

        self.bookList = QtWidgets.QTableView(self.bListFrame)
        self.bookList.setGeometry(QtCore.QRect(10, 30, 551, 211))
        self.bookList.setObjectName("bookList")
        self.bookListModel = QSqlTableModel()
        self.bookListModel.setTable("book")
        self.queryBookList = QSqlQuery()
        self.queryBookList.prepare("select Branch_Name as Branch, Book_Id as ID, Title, Publisher_Name as Publisher, No_of_copies as Copies from (book natural join library_branch) natural join BOOK_COPIES;")
        if not self.queryBookList.exec():
            QMessageBox.warning(None, "Result", "Could not retrieve the available book list. Please try again later.")
        self.bookListModel.setQuery(self.queryBookList)
        self.bookList.setModel(self.bookListModel)
        self.bookList.resizeColumnsToContents()

        self.rentalInfoFrame = QtWidgets.QFrame(self.checkoutTab)
        self.rentalInfoFrame.setGeometry(QtCore.QRect(20, 290, 571, 481))
        self.rentalInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rentalInfoFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        ## Borrower Information Frame
        # Rental Information
        self.rentalInfoFrame.setObjectName("rentalInfoFrame")
        self.borrowerFrame = QtWidgets.QFrame(self.rentalInfoFrame)

        self.borrowerFrame.setGeometry(QtCore.QRect(10, 10, 551, 251))
        self.borrowerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.borrowerFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Borrower Information Frame
        self.borrowerFrame.setObjectName("borrowerFrame")

        self.fnameLabel = QtWidgets.QLabel(self.borrowerFrame)
        self.fnameLabel.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.fnameLabel.setObjectName("fnameLabel")

        self.fname = QtWidgets.QLineEdit(self.borrowerFrame)
        self.fname.setGeometry(QtCore.QRect(10, 60, 200, 20))
        self.fname.setObjectName("fname")

        self.addressLabel = QtWidgets.QLabel(self.borrowerFrame)
        self.addressLabel.setGeometry(QtCore.QRect(10, 120, 300, 13))
        self.addressLabel.setObjectName("addressLabel")

        self.address = QtWidgets.QLineEdit(self.borrowerFrame)
        self.address.setGeometry(QtCore.QRect(10, 140, 531, 20))
        self.address.setObjectName("address")

        self.phNumberLabel = QtWidgets.QLabel(self.borrowerFrame)
        self.phNumberLabel.setGeometry(QtCore.QRect(10, 200, 180, 16))
        self.phNumberLabel.setObjectName("phNumberLabel")

        self.phone = QtWidgets.QLineEdit(self.borrowerFrame)
        self.phone.setGeometry(QtCore.QRect(10, 220, 531, 20))
        self.phone.setObjectName("phone")

        self.borrowerLabel = QtWidgets.QLabel(self.borrowerFrame)
        self.borrowerLabel.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.borrowerLabel.setObjectName("borrowerLabel")

        self.bookFrame = QtWidgets.QFrame(self.rentalInfoFrame)
        self.bookFrame.setGeometry(QtCore.QRect(10, 270, 551, 131))
        self.bookFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bookFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Book Information Frame
        self.bookFrame.setObjectName("bookFrame")

        self.bookLabel = QtWidgets.QLabel(self.bookFrame)
        self.bookLabel.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.bookLabel.setObjectName("bookLabel")

        self.title = QtWidgets.QLineEdit(self.bookFrame)
        self.title.setGeometry(QtCore.QRect(10, 50, 531, 20))
        self.title.setObjectName("title")

        self.bNameLabel = QtWidgets.QLabel(self.bookFrame)
        self.bNameLabel.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.bNameLabel.setObjectName("bNameLabel")

        self.libraryLabel = QtWidgets.QLabel(self.bookFrame)
        self.libraryLabel.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.libraryLabel.setObjectName("libraryLabel")

        self.branchCombo = QtWidgets.QComboBox(self.bookFrame)
        self.branchCombo.addItems(libraryBranches)
        self.branchCombo.setGeometry(QtCore.QRect(10, 100, 261, 22))
        self.branchCombo.setObjectName("branchCombo")

        self.checkoutBt = QtWidgets.QPushButton(self.rentalInfoFrame)
        self.checkoutBt.setGeometry(QtCore.QRect(470, 420, 81, 41))
        self.checkoutBt.setCheckable(False)
        self.checkoutBt.setObjectName("checkoutBt")
        self.checkoutBt.clicked.connect(self.checkoutAction)

        self.MainTab.addTab(self.checkoutTab, "")
        """ End of Checkout Tab """

        """ Start of Books Tab """
        ## Add a New Book Frame
        self.addBookTab = QtWidgets.QWidget()
        self.addBookTab.setObjectName("addBookTab")

        self.addBookFrame = QtWidgets.QFrame(self.addBookTab)
        self.addBookFrame.setGeometry(QtCore.QRect(20, 20, 571, 231))
        self.addBookFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addBookFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addBookFrame.setObjectName("addBookFrame")

        self.addBookLabel = QtWidgets.QLabel(self.addBookFrame)
        self.addBookLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.addBookLabel.setObjectName("addBookLabel")

        self.bTitleLabel = QtWidgets.QLabel(self.addBookFrame)
        self.bTitleLabel.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.bTitleLabel.setObjectName("bTitleLabel")

        self.bookTitleInput = QtWidgets.QLineEdit(self.addBookFrame)
        self.bookTitleInput.setGeometry(QtCore.QRect(10, 50, 551, 20))
        self.bookTitleInput.setObjectName("bookTitleInput")

        self.publisherTitleLabel = QtWidgets.QLabel(self.addBookFrame)
        self.publisherTitleLabel.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.publisherTitleLabel.setObjectName("publisherTitleLabel")

        self.publisherInput = QtWidgets.QLineEdit(self.addBookFrame)
        self.publisherInput.setGeometry(QtCore.QRect(10, 100, 551, 20))
        self.publisherInput.setObjectName("publisherInput")

        self.authorLabel = QtWidgets.QLabel(self.addBookFrame)
        self.authorLabel.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.authorLabel.setObjectName("authorLabel")

        self.authorInput = QtWidgets.QLineEdit(self.addBookFrame)
        self.authorInput.setGeometry(QtCore.QRect(10, 150, 551, 20))
        self.authorInput.setObjectName("authorInput")

        self.addBt = QtWidgets.QPushButton(self.addBookFrame)
        self.addBt.setGeometry(QtCore.QRect(480, 180, 75, 41))
        self.addBt.setObjectName("addBt")
        self.addBt.clicked.connect(self.addBookAction)
        ## Late Returned Books Frame
        self.lateReturnFrame = QtWidgets.QFrame(self.addBookTab)
        self.lateReturnFrame.setGeometry(QtCore.QRect(20, 270, 571, 316))
        self.lateReturnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lateReturnFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lateReturnFrame.setObjectName("lateReturnFrame")

        self.lateReturnLabel = QtWidgets.QLabel(self.lateReturnFrame)
        self.lateReturnLabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.lateReturnLabel.setObjectName("lateReturnLabel")

        self.fromLabel = QtWidgets.QLabel(self.lateReturnFrame)
        self.fromLabel.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.fromLabel.setObjectName("fromLabel")

        self.toLabel = QtWidgets.QLabel(self.lateReturnFrame)
        self.toLabel.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.toLabel.setObjectName("toLabel")

        self.dateEdit_1 = QtWidgets.QDateEdit(self.lateReturnFrame)
        self.dateEdit_1.setGeometry(QtCore.QRect(10, 60, 111, 22))
        self.dateEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_1.setObjectName("dateEdit_1")

        self.dateEdit_2 = QtWidgets.QDateEdit(self.lateReturnFrame)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 110, 110, 22))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.dateBt = QtWidgets.QPushButton(self.lateReturnFrame)
        self.dateBt.setGeometry(QtCore.QRect(10, 160, 75, 41))
        self.dateBt.setObjectName("dateBt")
        self.dateBt.clicked.connect(self.lateReturnAction)

        self.lateReturnList = QtWidgets.QTableView(self.lateReturnFrame)
        self.lateReturnList.setGeometry(QtCore.QRect(140, 11, 421, 291))
        self.lateReturnList.setObjectName("lateReturnList")

        self.MainTab.addTab(self.addBookTab, "")
        ## Book Info Frame
        self.bookInfoFrame = QtWidgets.QFrame(self.addBookTab)
        self.bookInfoFrame.setGeometry(QtCore.QRect(20, 600, 571, 191))
        self.bookInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bookInfoFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bookInfoFrame.setObjectName("bookInfoFrame")

        self.bookInfoLabel = QtWidgets.QLabel(self.bookInfoFrame)
        self.bookInfoLabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.bookInfoLabel.setObjectName("bookInfoLabel")

        self.bookInfoInput = QtWidgets.QLineEdit(self.bookInfoFrame)
        self.bookInfoInput.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.bookInfoInput.setObjectName("bookInfoInput")

        self.bookInfoBt = QtWidgets.QPushButton(self.bookInfoFrame)
        self.bookInfoBt.setGeometry(QtCore.QRect(10, 130, 75, 41))
        self.bookInfoBt.setObjectName("dateBt")
        self.bookInfoBt.clicked.connect(self.bookInfoAction)

        self.bookInfoList = QtWidgets.QTableView(self.bookInfoFrame)
        self.bookInfoList.setGeometry(QtCore.QRect(140, 11, 421, 171))
        self.bookInfoList.setObjectName("bookInfoList")
        """ End of Books Tab """
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(2)
        self.searchTab_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management System 1.0"))

        ## Search
        self.personSearchBt.setText(_translate("MainWindow", "Search"))
        self.searchPerson.setPlaceholderText(_translate("MainWindow", "Type in Borrower\'s ID or Borrower\'s name to search."))
        self.searchTab_2.setTabText(self.searchTab_2.indexOf(self.byPerson_tab), _translate("MainWindow", "Search by Person"))
        self.searchBook.setPlaceholderText(_translate("MainWindow", "Type in Book ID or Book Title to search."))
        self.bookSearchBt.setText(_translate("MainWindow", "Search"))
        self.searchTab_2.setTabText(self.searchTab_2.indexOf(self.byBook_tab), _translate("MainWindow", "Search by Book"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.searchTab_1), _translate("MainWindow", "Search"))

        ## Check Out
        self.bookListLabel.setText(_translate("MainWindow", "List of Books"))
        self.fnameLabel.setText(_translate("MainWindow", "Name (e.g. John Doe)"))
        self.addressLabel.setText(_translate("MainWindow", "Address (1234 NW Bobcat Lane, St. Robert, MO 65584)"))
        self.phNumberLabel.setText(_translate("MainWindow", "Phone Number (123-456-7890)"))
        self.borrowerLabel.setText(_translate("MainWindow", "Borrower Information"))
        self.bookLabel.setText(_translate("MainWindow", "Book Information"))
        self.bNameLabel.setText(_translate("MainWindow", "Book Name"))
        self.libraryLabel.setText(_translate("MainWindow", "Library Branch"))
        self.checkoutBt.setText(_translate("MainWindow", "Check-out"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.checkoutTab), _translate("MainWindow", "Check Out"))
        
        ##Books
        self.addBookLabel.setText(_translate("MainWindow", "Add a New Book"))
        self.bTitleLabel.setText(_translate("MainWindow", "Book Title"))
        self.authorLabel.setText(_translate("MainWindow", "Author Title"))
        self.publisherTitleLabel.setText(_translate("MainWindow", "Publisher Title"))
        self.addBt.setText(_translate("MainWindow", "Add"))
        self.lateReturnLabel.setText(_translate("MainWindow", "Late Returned Books"))
        self.fromLabel.setText(_translate("MainWindow", "From"))
        self.toLabel.setText(_translate("MainWindow", "To"))
        self.dateBt.setText(_translate("MainWindow", "Search"))
        self.bookInfoLabel.setText(_translate("MainWindow", "Book Locations"))
        self.bookInfoBt.setText(_translate("MainWindow", "Search"))
        self.bookInfoInput.setPlaceholderText(_translate("MainWindow", "Type in a book title."))
        self.MainTab.setTabText(self.MainTab.indexOf(self.addBookTab), _translate("MainWindow", "Books"))

    def searchByPersonAction(self):
        print("person clicked.")
        borrower = self.searchPerson.text().strip()

        searchPersonModel = QSqlTableModel()
        searchPersonModel.setTable("searchPersonTable")
        query = QSqlQuery()

        if not borrower:
            query.prepare("WITH Late_Fee as (SELECT Card_No, Name, '$' || CASE WHEN Returned_Date > Due_Date THEN julianday(Returned_date)-julianday(Due_Date) ELSE 0 END LateFee FROM BORROWER NATURAL JOIN BOOK_LOANS) SELECT* FROM Late_Fee GROUP BY Card_No ORDER BY LateFee desc;")
            
        
        if borrower.isnumeric():
            query.prepare('WITH Late_Fee as (SELECT Card_No, Name, "$" || CASE WHEN Returned_Date > Due_Date THEN julianday(Returned_date)-julianday(Due_Date) ELSE 0 END LateFee FROM BORROWER NATURAL JOIN BOOK_LOANS) SELECT* FROM Late_Fee WHERE Card_No LIKE "%"||?||"%";')
            query.addBindValue(borrower)
        else:
            query.prepare('WITH Late_Fee as (SELECT Card_No, Name, "$" || CASE WHEN Returned_Date > Due_Date THEN julianday(Returned_date)-julianday(Due_Date) ELSE 0 END LateFee FROM BORROWER NATURAL JOIN BOOK_LOANS) SELECT* FROM Late_Fee WHERE Name LIKE "%"||?||"%";')
            query.addBindValue(borrower)

        query.exec()
        searchPersonModel.setQuery(query)
        self.personResult.setModel(searchPersonModel)

    def searchByBookAction(self):
        print("book clicked.")
        book = self.searchBook.text().strip()
        
        searchBookModel = QSqlTableModel()
        searchBookModel.setTable("searchBookTable")
        query = QSqlQuery()
        
        if not book:
            query.prepare("WITH Late_Fee as (SELECT Book_Id, Title, Publisher_name, CASE WHEN Returned_Date > Due_Date THEN '$' || cast(julianday(Returned_date)-julianday(Due_Date) as text) ELSE 'Not Applicable' END LateFee FROM BOOK NATURAL JOIN BOOK_LOANS) SELECT * FROM Late_Fee GROUP BY Book_Id ORDER BY LateFee asc;")
        
        if book.isnumeric():
            query.prepare('WITH Late_Fee as (SELECT Book_Id, Title, Publisher_name, CASE WHEN Returned_Date > Due_Date THEN "$" || cast(julianday(Returned_date)-julianday(Due_Date) as text) ELSE "Not Applicable" END LateFee FROM BOOK NATURAL JOIN BOOK_LOANS) SELECT * FROM Late_Fee WHERE Book_Id LIKE "%"||?||"%" ORDER BY LateFee asc;')
            query.addBindValue(book)
        else:
            query.prepare('WITH Late_Fee as (SELECT Book_Id, Title, Publisher_name, CASE WHEN Returned_Date > Due_Date THEN "$" || cast(julianday(Returned_date)-julianday(Due_Date) as text) ELSE "Not Applicable" END LateFee FROM BOOK NATURAL JOIN BOOK_LOANS) SELECT * FROM Late_Fee WHERE Title LIKE "%"||?||"%" ORDER BY LateFee asc;')
            query.addBindValue(book)

        query.exec()
        searchBookModel.setQuery(query)
        self.bookResult.setModel(searchBookModel)
        self.bookResult.resizeColumnsToContents()

    def checkoutAction(self):
        print("checkout clicked.")
        name = self.fname.text().strip()
        address = self.address.text().strip()
        phone = self.phone.text().strip()
        title = self.title.text().strip()
        branch = self.branchCombo.currentText()
        today = date.today()
        return_date = today + timedelta(days = 10)

        if branch == "Main Branch":
            branch = 1
        elif branch == "West Branch":
            branch = 2
        elif branch == "East Branch":
            branch = 3

        query = QSqlQuery()

        bookIdModel = QSqlTableModel()
        bookIdModel.setTable("bookIdModel")
        query.prepare("SELECT Book_Id FROM Book WHERE Title = (?);")
        query.addBindValue(title)
        query.exec()
        bookIdModel.setQuery(query)
        book_id = bookIdModel.record(0).value("Book_Id")
        if book_id == None:
            QMessageBox.warning(None, "Result", "The title you are looking for does not exist.")
            return

        namecheckModel = QSqlTableModel()
        namecheckModel.setTable("namecheckModel")
        query.prepare("SELECT Name FROM BORROWER;")
        query.exec()
        namecheckModel.setQuery(query)

        for i in range(namecheckModel.rowCount()):
            if name == namecheckModel.record(i).value("name"):
                cardNoModel = QSqlTableModel()
                cardNoModel.setTable("cardNoModel")
                query.prepare("SELECT Card_No FROM Borrower WHERE Name = (?);")
                query.addBindValue(name)
                query.exec()
                cardNoModel.setQuery(query)
                card_no = cardNoModel.record(0).value("Card_No")
                print(card_no)

                query.prepare("INSERT INTO Book_Loans (Book_Id, Branch_Id, Card_No, Date_Out, Due_Date) VALUES (?, ?, ?, ?, ?);")
                query.addBindValue(book_id)
                query.addBindValue(branch)
                query.addBindValue(card_no)
                query.addBindValue(today.strftime("%Y-%m-%d"))
                query.addBindValue(return_date.strftime("%Y-%m-%d"))
                query.exec()

                query.prepare("UPDATE Book_Copies SET No_Of_Copies = No_Of_Copies-1 WHERE Branch_Id = ? AND Book_Id = ?;")
                query.addBindValue(branch)
                query.addBindValue(book_id)
                query.exec()

                query.prepare("SELECT Branch_Name as Branch, Book_Id as ID, Title, Publisher_Name as Publisher, No_of_copies as Copies FROM (book NATURAL JOIN library_branch) NATURAL JOIN BOOK_COPIES;")
                query.exec()
                self.bookListModel.setQuery(query)
                self.bookList.setModel(self.bookListModel)
                self.bookList.resizeColumnsToContents()
                return

        if not name or not address or not phone or not title:
            QMessageBox.warning(None, "Result", "Please type in all the inputs if you are new.")
            return
        
        registerModel = QSqlTableModel()
        registerModel.setTable("registerModel")
        query.prepare("INSERT INTO Borrower (Name, Address, Phone) VALUES (?, ?, ?);")
        query.addBindValue(name)
        query.addBindValue(address)
        query.addBindValue(phone)
        query.exec()

        card_no = query.lastInsertId()
        print(card_no)
        
        query.prepare("INSERT INTO Book_Loans (Book_Id, Branch_Id, Card_No, Date_Out, Due_Date) VALUES (?, ?, ?, ?, ?);")
        query.addBindValue(book_id)
        query.addBindValue(branch)
        query.addBindValue(card_no)
        query.addBindValue(today.strftime("%Y-%m-%d"))
        query.addBindValue(return_date.strftime("%Y-%m-%d"))
        query.exec()

        query.prepare("UPDATE Book_Copies SET No_Of_Copies = No_Of_Copies-1 WHERE Branch_Id = ? AND Book_Id = ?;")
        query.addBindValue(branch)
        query.addBindValue(book_id)
        query.exec()

        query.prepare("select Branch_Name as Branch, Book_Id as ID, Title, Publisher_Name as Publisher, No_of_copies as Copies from (book natural join library_branch) natural join BOOK_COPIES;")
        query.exec()
        self.bookListModel.setQuery(query)
        self.bookList.setModel(self.bookListModel)
        self.bookList.resizeColumnsToContents()

        QMessageBox.information(None, "Welcome!", "You have been registered in the library system. Your ID is {}".format(card_no))

    def addBookAction(self):
        print("clicked.")
        # Get input values
        title = self.bookTitleInput.text().strip()
        publisher = self.publisherInput.text().strip()
        author = self.authorInput.text().strip()

        # Check if inputs are null
        if not title or not publisher or not author:
            QMessageBox.warning(None, "Result", "Please type in all the inputs.")
            return
        
        # Add book to Book table
        query = QSqlQuery()
        query.prepare("INSERT INTO Book (Title, Publisher_Name) VALUES (?, ?)")
        query.addBindValue(title)
        query.addBindValue(publisher)
        query.exec()

        # Get book ID
        book_id = query.lastInsertId()

        # Add book copies to all branches
        query.prepare("INSERT INTO BOOK_COPIES (Book_Id, Branch_Id, No_Of_Copies) SELECT ?, Branch_Id, 5 FROM LIBRARY_BRANCH")
        query.addBindValue(book_id)
        query.exec()

        # Add author information
        query.prepare("INSERT INTO BOOK_AUTHORs (Book_Id, Author_Name) VALUES (?, ?)")
        query.addBindValue(book_id)
        query.addBindValue(author)
        query.exec()

        # Refresh book list view
        query.prepare("select Branch_Name as Branch, Book_Id as ID, Title, Publisher_Name as Publisher, No_of_copies as Copies from (book natural join library_branch) natural join BOOK_COPIES;")
        query.exec()
        self.bookListModel.setQuery(query)
        self.bookList.setModel(self.bookListModel)
        self.bookList.resizeColumnsToContents()
        
    def lateReturnAction(self):
        print("date clicked.")
        start_date = parser.parse(self.dateEdit_1.text())
        end_date = parser.parse(self.dateEdit_2.text())

        start_date_string = start_date.strftime('%Y-%m-%d')
        end_date_string = end_date.strftime('%Y-%m-%d')
        
        if start_date > end_date:
            QMessageBox.warning(None, "Result", "The start date must be earlier than the end date.")
            return

        lateReturnModel = QSqlTableModel()
        lateReturnModel.setTable("lateReturn")
        query = QSqlQuery()
        query.prepare("SELECT Book_Id as 'Book ID', Branch_Id as 'Branch ID', Card_No as 'ID No.', Date_Out as 'Checkout Date', julianday(Returned_date)-julianday(Due_Date) as 'Late Days' FROM BOOK_LOANS WHERE Returned_Date > Due_Date AND Due_Date BETWEEN (?) AND (?);")
        query.addBindValue(start_date_string)
        query.addBindValue(end_date_string)
        query.exec()
        lateReturnModel.setQuery(query)
        self.lateReturnList.setModel(lateReturnModel)

    def bookInfoAction(self):
        title = self.bookInfoInput.text()

        bookInfoModel = QSqlTableModel()
        bookInfoModel.setTable("bookInfoModel")
        query = QSqlQuery()
        query.prepare("SELECT Branch_Name as Branch, Book_Id as ID, Title, Publisher_Name as Publisher, No_of_copies as Copies FROM (book NATURAL JOIN library_branch) NATURAL JOIN BOOK_COPIES WHERE Title = ?;")
        query.addBindValue(title)
        query.exec()
        bookInfoModel.setQuery(query)
        self.bookInfoList.setModel(bookInfoModel)
        self.bookInfoList.resizeColumnsToContents()

def dataBase():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "lms.sqlite")

    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(DB_PATH)

    if not con.open():
        QMessageBox.critical(
            None,
            "DB Connection Error",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if not dataBase():
        sys.exit(1)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
