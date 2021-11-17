import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #homepage
        self.browser = QWebEngineView()
        argument = sys.argv
        path = sys.argv[0].replace("\\PineApple Browser.py","")
        try:
            self.browser.setUrl(QUrl("file:///"+os.path.realpath(argument[1]).replace("\\","/")))
            os.chdir(path)
        except:
            os.chdir(path)
            self.browser.setUrl(QUrl("file:///"+os.path.realpath("files/home.html").replace("\\","/")))
        self.setWindowIcon(QIcon('files/logo.ico'))
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        #display
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        self.create_menu_bar()

        back_btn = QAction(QIcon("files/back.png"),"Back",self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon("files/forward.png"),"Forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon("files/reload.png"),"Reload",self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        stop_btn = QAction(QIcon("files/stop.png"),"Stop", self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        home_btn = QAction(QIcon("files/home.png"),"Home",self)
        home_btn.triggered.connect(self.homepage)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        search_btn = QAction(QIcon("files/search.png"),"Search",self)
        search_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(search_btn)

        self.setStyleSheet("""QWidget{
                               background-color: rgb(48, 48, 48);
                               color: rgb(255, 255, 255);
                            }

                            /* Style the tab using the tab sub-control. Note that
                                it reads QTabBar _not_ QTabWidget */
                            QLabel, QToolButton, QTabBar::tab {
                                background: rgb(90, 90, 90);
                                border: 2px solid rgb(90, 90, 90);
                                /*border-bottom-color: #C2C7CB; /* same as the pane color */
                                border-radius: 10px;
                                min-width: 8ex;
                                padding: 5px;
                                margin-right: 2px;
                                color: rgb(255, 255, 255);
                            }

                            QLabel:hover, QToolButton::hover, QTabBar::tab:selected, QTabBar::tab:hover {
                                background: rgb(49, 49, 49);
                                border: 2px solid rgb(0, 36, 36);
                                background-color: rgb(0, 36, 36);
                            }

                            QLineEdit {
                                border: 2px solid rgb(0, 36, 36);
                                border-radius: 10px;
                                padding: 5px;
                                background-color: rgb(0, 36, 36);
                                color: rgb(255, 255, 255);
                            }
                            QLineEdit:hover {
                                border: 2px solid rgb(0, 66, 124);
                            }
                            QLineEdit:focus{
                                border: 2px solid rgb(0, 136, 255);
                                color: rgb(200, 200, 200);
                            }
                            QPushButton{
                                background: rgb(49, 49, 49);
                                border: 2px solid rgb(0, 36, 36);
                                background-color: rgb(0, 36, 36);
                                padding: 5px;
                                border-radius: 10px;
                            }""")

    def create_menu_bar(self):
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        google_btn = QAction("Google Search", self)
        google_btn.triggered.connect(self.google)
        menu_bar.addAction(google_btn)

        maps_btn = QAction("Google Maps", self)
        maps_btn.triggered.connect(self.maps)
        menu_bar.addAction(maps_btn)

        translate_btn = QAction("Google Translate", self)
        translate_btn.triggered.connect(self.translate)
        menu_bar.addAction(translate_btn)

        bing_btn = QAction("Bing Search", self)
        bing_btn.triggered.connect(self.bing)
        menu_bar.addAction(bing_btn)

        yahoo_btn = QAction("Yahoo Search", self)
        yahoo_btn.triggered.connect(self.yahoo)
        menu_bar.addAction(yahoo_btn)

        duckduckgo_btn = QAction("Duckduckgo Search", self)
        duckduckgo_btn.triggered.connect(self.duckduckgo)
        menu_bar.addAction(duckduckgo_btn)

        wikipedia_btn = QAction("Wikipedia Search", self)
        wikipedia_btn.triggered.connect(self.wikipedia)
        menu_bar.addAction(wikipedia_btn)

        proton_btn = QAction("Protonmail", self)
        proton_btn.triggered.connect(self.proton)
        menu_bar.addAction(proton_btn)

        dropbox_btn = QAction("dropbox", self)
        dropbox_btn.triggered.connect(self.dropbox)
        menu_bar.addAction(dropbox_btn)

        yt_btn = QAction("Youtube", self)
        yt_btn.triggered.connect(self.yt)
        menu_bar.addAction(yt_btn)

        facebook_btn = QAction("Facebook", self)
        facebook_btn.triggered.connect(self.facebook)
        menu_bar.addAction(facebook_btn)

        instagram_btn = QAction("Instagram", self)
        instagram_btn.triggered.connect(self.instagram)
        menu_bar.addAction(instagram_btn)

        messenger_btn = QAction("Messenger", self)
        messenger_btn.triggered.connect(self.messenger)
        menu_bar.addAction(messenger_btn)

        whatsapp_btn = QAction("Whatsapp", self)
        whatsapp_btn.triggered.connect(self.whatsapp)
        menu_bar.addAction(whatsapp_btn)

        telegram_btn = QAction("Telegram", self)
        telegram_btn.triggered.connect(self.telegram)
        menu_bar.addAction(telegram_btn)

        github_btn = QAction("Github", self)
        github_btn.triggered.connect(self.github)
        menu_bar.addAction(github_btn)

        more = QMenu("More  ", self)
        menu_bar.addMenu(more)

        replit_btn = QAction("Replit", self)
        replit_btn.triggered.connect(self.replit)
        more.addAction(replit_btn)

        hackerrank_btn = QAction("HackerRank",self)
        hackerrank_btn.triggered.connect(self.hackerrank)
        more.addAction(hackerrank_btn)
        
        sololearn_btn = QAction("Sololearn",self)
        sololearn_btn.triggered.connect(self.sololearn)
        more.addAction(sololearn_btn)

        w3schools_btn = QAction("W3schools",self)
        w3schools_btn.triggered.connect(self.w3schools)
        more.addAction(w3schools_btn)

        freecodecamp_btn = QAction("FreeCodeCamp",self)
        freecodecamp_btn.triggered.connect(self.freecodecamp)
        more.addAction(freecodecamp_btn)

        leetcode_btn = QAction("Leetcode",self)
        leetcode_btn.triggered.connect(self.leetcode)
        more.addAction(leetcode_btn)

        codingbat_btn = QAction("Codingbat",self)
        codingbat_btn.triggered.connect(self.codingbat)
        more.addAction(codingbat_btn)

        option = QMenu("Option",self)
        menu_bar.addMenu(option)

        about_btn = QAction("About", self)
        about_btn.triggered.connect(self.about_url)
        option.addAction(about_btn)
        
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s " % title)
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        if url[:2] == "C:":
            url = "file:///"+url
        if url[:4] != "http" and url[:8] != "file:///" and url[:3] != "www":
            url = "https://google.com/search?q="+url
        if url[:3] == "www":
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self,url):
        if "home.html" in url.toString():
            txt = "pineapple://home"
        elif "about.html" in url.toString():
            txt="pineapple://about"
        else:
            txt=url.toString()
        self.url_bar.setText(txt)

    def about_url(self):
        path = os.path.realpath("files/about.html")
        url = "file:///" + path.replace("\\", "/")
        self.browser.setUrl(QUrl(url))

    def homepage(self):
        self.browser.setUrl(QUrl("file:///"+os.path.realpath("files/home.html").replace("\\","/")))

    def duckduckgo(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))

    def facebook(self):
        self.browser.setUrl(QUrl("https://www.facebook.com/"))

    def messenger(self):
        self.browser.setUrl(QUrl("https://www.messenger.com/"))

    def yt(self):
        self.browser.setUrl(QUrl("https://www.youtube.com/"))

    def whatsapp(self):
        self.browser.setUrl(QUrl("https://web.whatsapp.com/"))

    def instagram(self):
        self.browser.setUrl(QUrl("https://www.instagram.com/"))

    def google(self):
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def github(self):
        self.browser.setUrl(QUrl("https://github.com/"))

    def bing(self):
        self.browser.setUrl(QUrl("https://www.bing.com/"))

    def yahoo(self):
        self.browser.setUrl(QUrl("https://www.yahoo.com/"))
        
    def replit(self):
        self.browser.setUrl(QUrl("https://replit.com/~"))

    def maps(self):
        self.browser.setUrl(QUrl("https://www.google.com/maps/@22.3259344,91.8198678,12z"))

    def translate(self):
        self.browser.setUrl(QUrl("https://translate.google.com/"))

    def proton(self):
        self.browser.setUrl(QUrl("https://mail.protonmail.com/inbox"))
        
    def telegram(self):
        self.browser.setUrl(QUrl("https://web.telegram.org/"))

    def dropbox(self):
        self.browser.setUrl(QUrl("https://www.dropbox.com/"))

    def wikipedia(self):
        self.browser.setUrl(QUrl("https://www.wikipedia.org/"))

    def hackerrank(self):
        self.browser.setUrl(QUrl("https://www.hackerrank.com/dashboard"))

    def sololearn(self):
        self.browser.setUrl(QUrl("https://www.sololearn.com/profile/19855955"))

    def leetcode(self):
        self.browser.setUrl(QUrl("https://leetcode.com/"))

    def w3schools(self):
        self.browser.setUrl(QUrl("https://www.w3schools.com/"))

    def freecodecamp(self):
        self.browser.setUrl(QUrl("https://www.freecodecamp.org/learn/?messages=success%5B0%5D%3DSuccess%2521%2520You%2520have%2520signed%2520in%2520to%2520your%2520account.%2520Happy%2520Coding%2521"))

    def codingbat(self):
        self.browser.setUrl(QUrl("https://codingbat.com/python"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("PineApple Browser")
    QApplication.setApplicationVersion("1.02")
    QApplication.setApplicationDisplayName("PineApple Browser")
    QApplication.setDesktopFileName("PineApple Browser")
    window = MainWindow()
    app.exec()
