import os
import sqlite3
import csv
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.utils import platform

# Интерфейс (упрощенный для стабильности)
KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Складской Сканер"
        
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'scan'
                text: 'Сканировать'
                icon: 'barcode-scan'
                BoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        id: status_label
                        text: "Готов к работе"
                        halign: "center"
                    MDRaisedButton:
                        text: "Камера"
                        pos_hint: {"center_x": .5}
                        on_release: app.start_camera()
            
            MDBottomNavigationItem:
                name: 'docs'
                text: 'Документы'
                icon: 'file-document'
                MDList:
                    id: doc_list
'''

class MainApp(MDApp):
    def build(self):
        self.db = sqlite3.connect("data.db")
        self.create_db()
        return Builder.load_string(KV)

    def create_db(self):
        cur = self.db.cursor()
        # Таблица товаров (номенклатура)
        cur.execute("CREATE TABLE IF NOT EXISTS items (gtin TEXT, name TEXT, plan INTEGER)")
        # Таблица сканов
        cur.execute("CREATE TABLE IF NOT EXISTS scans (barcode TEXT, doc_type TEXT)")
        self.db.commit()

    def process_barcode(self, code):
        # Логика сохранения (приемка/вывод)
        cur = self.db.cursor()
        cur.execute("INSERT INTO scans (barcode, doc_type) VALUES (?, ?)", (code, "приемка"))
        self.db.commit()
        self.root.ids.status_label.text = f"Считано: {code}"

    # Метод для Urovo (Broadcast Intent)
    def on_start(self):
        if platform == 'android':
            from jnius import autoclass
            # Настройка ресивера для Urovo будет здесь
            pass

    def import_from_csv(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.db.execute("INSERT INTO items VALUES (?,?,?)", (row['gtin'], row['name'], row['plan']))
            self.db.commit()

MainApp().run()
