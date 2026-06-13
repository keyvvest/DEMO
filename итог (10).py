# ----------------------------------------------------------------------
# Скрипт базы данных
# ----------------------------------------------------------------------
# -- =====================================================
# -- Создание БД
# -- =====================================================

# CREATE DATABASE IF NOT EXISTS shoestore
#     CHARACTER SET utf8mb4
#     COLLATE utf8mb4_unicode_ci;

# USE shoestore;

# -- =====================================================
# -- Таблица ролей
# -- =====================================================

# CREATE TABLE roles (
#     id_role INT PRIMARY KEY AUTO_INCREMENT,
#     role_name VARCHAR(20) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Таблица пользователей
# -- =====================================================

# CREATE TABLE users (
#     id_user INT PRIMARY KEY AUTO_INCREMENT,
#     username VARCHAR(40) NOT NULL UNIQUE,
#     password VARCHAR(40) NOT NULL,
#     full_name VARCHAR(70),
#     role_id INT,
#     FOREIGN KEY (role_id) REFERENCES roles(id_role)
# );

# -- =====================================================
# -- Категории обуви
# -- =====================================================

# CREATE TABLE categories (
#     id_category INT PRIMARY KEY AUTO_INCREMENT,
#     category_name VARCHAR(40) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Производители
# -- =====================================================

# CREATE TABLE manufacturers (
#     id_manufacturer INT PRIMARY KEY AUTO_INCREMENT,
#     manufacturer_name VARCHAR(40) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Поставщики
# -- =====================================================

# CREATE TABLE suppliers (
#     id_supplier INT PRIMARY KEY AUTO_INCREMENT,
#     supplier_name VARCHAR(40) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Единицы измерения
# -- =====================================================

# CREATE TABLE units (
#     id_unit INT PRIMARY KEY AUTO_INCREMENT,
#     unit_name VARCHAR(40) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Товары
# -- =====================================================

# CREATE TABLE products (
#     id_product INT PRIMARY KEY AUTO_INCREMENT,
#     product_name VARCHAR(40) NOT NULL,
#     description TEXT,
#     price DECIMAL(10,2) NOT NULL,
#     quantity_in_stock INT NOT NULL DEFAULT 0,
#     discount DECIMAL(5,2) NOT NULL DEFAULT 0,
#     image_path VARCHAR(255),
#     category_id INT,
#     manufacturer_id INT,
#     supplier_id INT,
#     unit_id INT,
#     FOREIGN KEY (category_id) REFERENCES categories(id_category),
#     FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id_manufacturer),
#     FOREIGN KEY (supplier_id) REFERENCES suppliers(id_supplier),
#     FOREIGN KEY (unit_id) REFERENCES units(id_unit)
# );

# -- =====================================================
# -- Статусы заказов
# -- =====================================================

# CREATE TABLE order_statuses (
#     id_status INT PRIMARY KEY AUTO_INCREMENT,
#     status_name VARCHAR(40) NOT NULL UNIQUE
# );

# -- =====================================================
# -- Точки выдачи
# -- =====================================================

# CREATE TABLE pickup_points (
#     id_pickup_point INT PRIMARY KEY AUTO_INCREMENT,
#     address VARCHAR(100) NOT NULL UNIQUE,
#     phone VARCHAR(20),
#     working_hours VARCHAR(100)
# );

# -- =====================================================
# -- Заказы
# -- =====================================================

# CREATE TABLE orders (
#     id_order INT PRIMARY KEY AUTO_INCREMENT,
#     article VARCHAR(40) NOT NULL,
#     order_date DATE NOT NULL,
#     delivery_date DATE,
#     status_id INT,
#     user_id INT,
#     pickup_point_id INT,
#     FOREIGN KEY (status_id) REFERENCES order_statuses(id_status),
#     FOREIGN KEY (user_id) REFERENCES users(id_user),
#     FOREIGN KEY (pickup_point_id) REFERENCES pickup_points(id_pickup_point)
# );

# -- =====================================================
# -- Позиции заказов
# -- =====================================================

# CREATE TABLE order_items (
#     id_order_item INT PRIMARY KEY AUTO_INCREMENT,
#     order_id INT,
#     product_id INT,
#     quantity INT NOT NULL,
#     FOREIGN KEY (order_id)
#         REFERENCES orders(id_order)
#         ON DELETE CASCADE,
#     FOREIGN KEY (product_id)
#         REFERENCES products(id_product)
# );

# -- =====================================================
# -- Заполнение таблиц
# -- =====================================================

# -- Роли
# INSERT INTO roles (role_name) VALUES
# ('Администратор'),
# ('Клиент'),
# ('Менеджер'),
# ('Гость');

# -- Пользователи
# INSERT INTO users (username, password, full_name, role_id) VALUES
# ('admin', 'admin', 'Иванов Иван Иванович', 1),
# ('client', 'client', 'Петрова Анна Сергеевна', 2),
# ('manager', 'manager', 'Сидоров Алексей Владимирович', 3),
# ('guest', 'guest', 'Гость', 4);

# -- Категории
# INSERT INTO categories (category_name) VALUES
# ('Туфли'),
# ('Ботинки'),
# ('Сапоги'),
# ('Кроссовки'),
# ('Сандалии');

# -- Производители
# INSERT INTO manufacturers (manufacturer_name) VALUES
# ('Фабрика "Обувь-Стиль"'),
# ('ЗАО "Комфорт"'),
# ('ООО "Лидер"'),
# ('ИП "Классика"');

# -- Поставщики
# INSERT INTO suppliers (supplier_name) VALUES
# ('ООО "Туфли-Трейд"'),
# ('ИП "Ботинки Опт"'),
# ('ООО "Сапоги Плюс"'),
# ('Склад "Кроссовки.ру"');

# -- Единицы измерения
# INSERT INTO units (unit_name) VALUES
# ('пара'),
# ('шт.');

# -- Товары
# INSERT INTO products (
#     product_name,
#     description,
#     price,
#     quantity_in_stock,
#     discount,
#     image_path,
#     category_id,
#     manufacturer_id,
#     supplier_id,
#     unit_id
# ) VALUES
# ('Туфли классические',
#  'Мужские туфли из натуральной кожи, черные',
#  4500.00, 25, 10.00, 'shoes1.jpg', 1, 1, 1, 1),

# ('Ботинки зимние',
#  'Утепленные ботинки на натуральном меху',
#  7800.00, 12, 15.00, 'shoes2.jpg', 2, 2, 2, 1),

# ('Сапоги резиновые',
#  'Высокие сапоги для рыбалки',
#  2900.00, 40, 5.00, 'shoes3.jpg', 3, 3, 3, 1),

# ('Кроссовки беговые',
#  'Легкие дышащие кроссовки',
#  6200.00, 18, 20.00, 'shoes4.jpg', 4, 4, 4, 1),

# ('Сандалии открытые',
#  'Женские сандалии на платформе',
#  3500.00, 30, 0.00, 'shoes5.jpg', 5, 2, 1, 1),

# ('Туфли лаковая кожа',
#  'Женские туфли на каблуке',
#  5100.00, 8, 25.00, 'shoes6.jpg', 1, 1, 1, 1);

# -- Статусы заказов
# INSERT INTO order_statuses (status_name) VALUES
# ('Новый'),
# ('В обработке'),
# ('Отправлен'),
# ('Доставлен'),
# ('Завершен'),
# ('Отменен');

# -- Точки выдачи
# INSERT INTO pickup_points (
#     address,
#     phone,
#     working_hours
# ) VALUES
# ('ТЦ "Галерея", ул. Ленина, 10',
#  '+7 (900) 111-11-11',
#  'Пн-Пт 10:00-20:00'),

# ('Пункт выдачи №5, пр. Мира, 23',
#  '+7 (900) 222-22-22',
#  'Ежедневно 09:00-21:00'),

# ('ТРЦ "Мега", ул. Победы, 45',
#  '+7 (900) 333-33-33',
#  'Ежедневно 10:00-22:00');

# -- Заказы
# INSERT INTO orders (
#     article,
#     order_date,
#     delivery_date,
#     status_id,
#     user_id,
#     pickup_point_id
# ) VALUES
# ('ORD-2025-001',
#  CURDATE(),
#  DATE_ADD(CURDATE(), INTERVAL 3 DAY),
#  1,
#  2,
#  1),

# ('ORD-2025-002',
#  CURDATE(),
#  DATE_ADD(CURDATE(), INTERVAL 5 DAY),
#  2,
#  2,
#  2);

# -- Позиции заказов
# INSERT INTO order_items (
#     order_id,
#     product_id,
#     quantity
# ) VALUES
# (1, 1, 2),
# (1, 4, 1),
# (2, 2, 1),
# (2, 5, 3);

# -- =====================================================
# -- Индексы
# -- =====================================================

# CREATE INDEX idx_products_category
# ON products(category_id);

# CREATE INDEX idx_orders_user
# ON orders(user_id);

# CREATE INDEX idx_orders_status
# ON orders(status_id);

# CREATE INDEX idx_orders_pickup_point
# ON orders(pickup_point_id);



# ----------------------------------------------------------------------
# ОСНОВНОЙ КОД
# ----------------------------------------------------------------------


import sys
import os
import pymysql
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QHeaderView, QTableWidgetItem, QDialog, QFileDialog
# import shutil

# ----------------------------------------------------------------------
# База данных
# ----------------------------------------------------------------------

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(host="localhost", user="root", password="root", database="shoestore")
            print("Успешное подключение к бд")
            return True
        except Exception as e:
            print(e)



class ProductTableLoader:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.product_ids = []  # список ID товаров в порядке строк таблицы

    def load_to_table(self, table_widget, search_text="", supplier="Все поставщики", sort_by_stock=0):
        cursor = self.db_connection.cursor()
        query = """
            SELECT p.id_product, c.category_name, p.product_name, p.description,
                   m.manufacturer_name, s.supplier_name, p.price,
                   u.unit_name, p.quantity_in_stock, p.image_path, p.discount
            FROM products p
            JOIN categories c ON c.id_category = p.category_id
            JOIN manufacturers m ON m.id_manufacturer = p.manufacturer_id
            JOIN suppliers s ON s.id_supplier = p.supplier_id
            JOIN units u ON u.id_unit = p.unit_id
            WHERE 1=1
        """
        params = []
        if supplier != "Все поставщики":
            query += " AND s.supplier_name = %s"
            params.append(supplier)
        if search_text:
            query += " AND (p.product_name LIKE %s OR c.category_name LIKE %s OR p.description LIKE %s OR m.manufacturer_name LIKE %s OR s.supplier_name LIKE %s)"
            like = f"%{search_text}%"
            params.extend([like, like, like, like, like])
        if sort_by_stock == 1:
            query += " ORDER BY p.quantity_in_stock ASC"
        elif sort_by_stock == 2:
            query += " ORDER BY p.quantity_in_stock DESC"
        else:
            query += " ORDER BY p.id_product"

        cursor.execute(query, params)
        rows = cursor.fetchall()
        table_widget.setRowCount(len(rows))
        table_widget.setColumnWidth(0, 210)
        table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        table_widget.setColumnWidth(2, 100)

        self.product_ids = []
        for i, (pid, cat, name, desc, manuf, sup, price, unit, stock, img, disc) in enumerate(rows):
            self.product_ids.append(pid)
            # ---------- Колонка 0: Фото ----------
            if img and os.path.exists(img):
                pix = QPixmap(img).scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio)
            else:
                placeholder = "images/picture.png"
                if os.path.exists(placeholder):
                    pix = QPixmap(placeholder).scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio)
                else:
                    pix = QPixmap(200, 150)
                    pix.fill(Qt.GlobalColor.lightGray)
            label_img = QLabel()
            label_img.setPixmap(pix)
            table_widget.setCellWidget(i, 0, label_img)

            # ---------- Колонка 1: Текст с HTML ----------
            if disc > 0:
                new_price = price * (100 - disc) / 100
                price_html = (f'<span style="text-decoration: line-through; color: red;">{round(price, 2)} Р</span> '
                              f'{round(new_price, 2)} Р')
            else:
                price_html = f"{price} Р"

            html_text = (f'<b>{cat} | {name}</b><br>'
                         f'Описание: {desc}<br>'
                         f'Производитель: {manuf}<br>'
                         f'Поставщик: {sup}<br>'
                         f'Цена: {price_html}<br>'
                         f'Ед.изм: {unit}<br>'
                         f'Остаток: {stock}')

            label_text = QLabel(html_text)
            label_text.setTextFormat(Qt.TextFormat.RichText)
            table_widget.setCellWidget(i, 1, label_text)

            # ---------- Колонка 2: Скидка ----------
            label_disc = QLabel(f"{int(disc)}%")
            label_disc.setAlignment(Qt.AlignmentFlag.AlignCenter)
            table_widget.setCellWidget(i, 2, label_disc)

            # ---------- Цвет фона ----------
            if stock == 0:
                bg_color = QColor("#ADD8E6")
            elif disc > 15:
                bg_color = QColor("#2E8B57")
            else:
                bg_color = QColor(255, 255, 255)

            table_widget.cellWidget(i, 0).setStyleSheet(f"background-color: {bg_color.name()};")
            table_widget.cellWidget(i, 1).setStyleSheet(f"background-color: {bg_color.name()};")
            table_widget.cellWidget(i, 2).setStyleSheet(f"background-color: {bg_color.name()};")




class ProductEditDialog(QDialog):
    def __init__(self, db, product_id=None, parent=None):
        super().__init__(parent)
        self.db = db
        self.product_id = product_id
        uic.loadUi("add_product_dialog.ui", self)

        if product_id is None:
            self.setWindowTitle("Добавление товара")
        else:
            self.setWindowTitle("Редактирование товара")

        self.save_button.clicked.connect(self.save_product)
        self.cancel_button.clicked.connect(self.reject)
        # self.pushButton.clicked.connect(self.choose_image)

        if product_id:
            self.load_product_data()

    # def choose_image(self):
    #     file_path, _ = QFileDialog.getOpenFileName(
    #         self,
    #         "Выбор изображения",
    #         "",
    #         "Images (*.png *.jpg *.jpeg)"
    #     )
    #
    #     if not file_path:
    #         return
    #
    #     # --- создаём папку images если нет ---
    #     images_dir = "images"
    #     os.makedirs(images_dir, exist_ok=True)
    #
    #     # --- имя файла ---
    #     file_name = os.path.basename(file_path)
    #     new_path = os.path.join(images_dir, file_name)
    #
    #     # --- копируем файл в проект ---
    #     shutil.copy(file_path, new_path)
    #
    #     # --- сохраняем путь ---
    #     self.image_path_edit.setText(new_path)
    #

    
    def load_product_data(self):
        cursor = self.db.connection.cursor()
        cursor.execute("""
            SELECT p.product_name, p.description, p.price, p.quantity_in_stock, p.discount, p.image_path, c.category_name, m.manufacturer_name, s.supplier_name, u.unit_name
            FROM products p
            JOIN categories c ON p.category_id = c.id_category
            JOIN manufacturers m ON p.manufacturer_id = m.id_manufacturer
            JOIN suppliers s ON p.supplier_id = s.id_supplier
            JOIN units u ON p.unit_id = u.id_unit
            WHERE p.id_product = %s
        """, (self.product_id,))
        row = cursor.fetchone()
        if row:
            (name, desc, price, stock, disc, img, cat_name, man_name, sup_name, unit_name) = row
            self.name_input.setText(name)
            self.category_combo.setCurrentText(cat_name)
            self.description_input.setPlainText(desc or "")
            self.manufacturer_combo.setCurrentText(man_name)
            self.supplier_combo.setCurrentText(sup_name)
            self.price_input.setValue(price)
            self.unit_combo.setCurrentText(unit_name)
            self.quantity_input.setValue(stock)
            self.discount_input.setValue(disc)
            self.image_path_edit.setText(img if img else "")

    def save_product(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите наименование")
            return

        image_path = self.image_path_edit.text().strip()
        cursor = self.db.connection.cursor()

        category_name = self.category_combo.currentText()
        cursor.execute("SELECT id_category FROM categories WHERE category_name = %s", (category_name,))
        row = cursor.fetchone()
        category_id = row[0]

        manufacturer_name = self.manufacturer_combo.currentText()
        cursor.execute("SELECT id_manufacturer FROM manufacturers WHERE manufacturer_name = %s", (manufacturer_name,))
        row = cursor.fetchone()
        manufacturer_id = row[0]

        supplier_name = self.supplier_combo.currentText()
        cursor.execute("SELECT id_supplier FROM suppliers WHERE supplier_name = %s", (supplier_name,))
        row = cursor.fetchone()
        supplier_id = row[0]

        unit_name = self.unit_combo.currentText()
        cursor.execute("SELECT id_unit FROM units WHERE unit_name = %s", (unit_name,))
        row = cursor.fetchone()
        unit_id = row[0]

        description = self.description_input.toPlainText().strip()
        price = self.price_input.value()
        quantity = self.quantity_input.value()
        discount = self.discount_input.value()

        if price <= 0:
            QMessageBox.warning(self, "Ошибка", "Цена должна быть больше 0")
            return

        # pix = QPixmap(image_path)
        #
        # if not pix.isNull():
        #     pix = pix.scaled(300, 200)
        #     pix.save(image_path)

        
        try:
            if self.product_id is None:
                # Проверка уникальности названия
                cursor.execute("SELECT id_product FROM products WHERE product_name = %s", (name,))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Ошибка", "Товар с таким названием уже есть")
                    return
                cursor.execute("""
                    INSERT INTO products (product_name, description, price, quantity_in_stock,
                                         discount, image_path, category_id, manufacturer_id,
                                         supplier_id, unit_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (name, description, price, quantity, discount, image_path,
                      category_id, manufacturer_id, supplier_id, unit_id))
            else:
                cursor.execute("SELECT id_product FROM products WHERE product_name = %s AND id_product != %s", (name, self.product_id))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Ошибка", "Товар с таким названием уже существует")
                    return
                    
                # # --- получаем старое изображение ---
                # cursor.execute("SELECT image_path FROM products WHERE id_product=%s", (self.product_id,))
                # old_img = cursor.fetchone()[0]
                #
                # # --- если картинка изменилась ---
                # if old_img and old_img != image_path and os.path.exists(old_img):
                #     os.remove(old_img)
                
                cursor.execute("""
                    UPDATE products
                    SET product_name=%s, description=%s, price=%s, quantity_in_stock=%s,
                        discount=%s, image_path=%s, category_id=%s, manufacturer_id=%s,
                        supplier_id=%s, unit_id=%s
                    WHERE id_product=%s
                """, (name, description, price, quantity, discount, image_path,
                      category_id, manufacturer_id, supplier_id, unit_id, self.product_id))
            self.db.connection.commit()
            QMessageBox.information(self, "Успех", "Товар сохранён")
            self.accept()
        except Exception as e:
            self.db.connection.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {e}")


class OrderEditDialog(QDialog):
    def __init__(self, db, order_id=None, parent=None):
        super().__init__(parent)
        self.db = db
        self.order_id = order_id
        uic.loadUi("order_dialog.ui", self)

        if order_id is None:
            self.setWindowTitle("Добавление заказа")
        else:
            self.setWindowTitle("Редактирование заказа")

        # Подключаем кнопки
        self.save_button.clicked.connect(self.save_order)
        self.cancel_button.clicked.connect(self.reject)

        # Если редактируем, загружаем данные заказа
        if order_id:
            self.load_order_data()

    def load_order_data(self):
        """Загружает данные выбранного заказа в поля формы"""
        cursor = self.db.connection.cursor()
        cursor.execute("""
            SELECT o.article, os.status_name,
                   COALESCE(pp.address, ''),
                   o.order_date, o.delivery_date
            FROM orders o
            JOIN order_statuses os ON o.status_id = os.id_status
            LEFT JOIN pickup_points pp ON o.pickup_point_id = pp.id_pickup_point
            WHERE o.id_order = %s
        """, (self.order_id,))
        row = cursor.fetchone()
        if row:
            article, status_name, address, order_date, delivery_date = row
            self.article_edit.setText(article)
            self.status_combo.setCurrentText(status_name)
            self.address_edit.setText(address)
            if order_date:
                self.order_date_edit.setDate(order_date)
            if delivery_date:
                self.delivery_date_edit.setDate(delivery_date)

    def save_order(self):
        """Сохраняет заказ (новый или изменённый)"""
        try:
            cursor = self.db.connection.cursor()

            article = self.article_edit.text().strip()
            order_date = self.order_date_edit.date().toPyDate()
            delivery_date = self.delivery_date_edit.date().toPyDate()

            status_name = self.status_combo.currentText()
            cursor.execute("SELECT id_status FROM order_statuses WHERE status_name = %s", (status_name,))
            row = cursor.fetchone()
            status_id = row[0]

            address = self.address_edit.text().strip()

            if not article or not address:
                QMessageBox.warning(self, "Ошибка", "Артикул или адрес не может быть пустым")
                return

            cursor.execute("SELECT id_pickup_point FROM pickup_points WHERE address = %s", (address,))
            row = cursor.fetchone()
            if row:
                pickup_point_id = row[0]
            else:
                cursor.execute("INSERT INTO pickup_points (address) VALUES (%s)", (address,))
                pickup_point_id = cursor.lastrowid


            if self.order_id is None:
                cursor.execute("SELECT id_order FROM orders WHERE article = %s", (article,))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Ошибка", "Заказ с таким артикулом уже существует")
                    return

                cursor.execute("""
                    INSERT INTO orders (article, status_id, pickup_point_id, order_date, delivery_date, user_id)
                    VALUES (%s, %s, %s, %s, %s, 1)
                """, (article, status_id, pickup_point_id, order_date, delivery_date))
            else:
                cursor.execute("SELECT id_order FROM orders WHERE article = %s AND id_order != %s", (article, self.order_id))
                if cursor.fetchone():
                    QMessageBox.warning(self, "Ошибка", "Заказ с таким артикулом уже существует")
                    return
                cursor.execute("""
                    UPDATE orders
                    SET article=%s, status_id=%s, pickup_point_id=%s, order_date=%s, delivery_date=%s
                    WHERE id_order=%s
                """, (article, status_id, pickup_point_id, order_date, delivery_date, self.order_id))
            self.db.connection.commit()
            QMessageBox.information(self, "Успех", "Заказ сохранён")
            self.accept()
        except Exception as e:
            self.db.connection.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {e}")

# ----------------------------------------------------------------------
# Окно входа
# ----------------------------------------------------------------------
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cur_user = None
        self.role_window = None
        self.db = Database()
        uic.loadUi("login.ui", self)
        self.login_button.clicked.connect(self.auth)
        self.guest_button.clicked.connect(self.guest_auth)

    def guest_auth(self):
        self.cur_user = {'id': 0, 'username': "guest", 'full_name': "Гость", 'role': "Гость"}
        QMessageBox.information(self, "Добро пожаловать", "Вы вошли как гость")
        self.role_select()
        self.hide()

    def auth(self):
        login = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("""SELECT u.id_user, u.username, u.full_name, r.role_name
                              FROM users u JOIN roles r ON u.role_id = r.id_role
                              WHERE u.username=%s AND u.password=%s""", (login, password))
            if user := cursor.fetchone():
                self.cur_user = {'id': user[0], 'username': user[1], 'full_name': user[2], 'role': user[3]}
                QMessageBox.information(self, "Успех", f"Добро пожаловать {user[2]}")
                self.role_select()
                self.hide()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")
                self.password_input.clear()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Ошибка авторизации: {e}")

    def role_select(self):
        role = self.cur_user['role']
        if role == "Клиент":
            self.role_window = ClientWindow(self.db, self.cur_user)
        elif role == "Администратор":
            self.role_window = AdminWindow(self.db, self.cur_user)
        elif role == "Менеджер":
            self.role_window = ManagerWindow(self.db, self.cur_user)
        elif role == "Гость":
            self.role_window = GuestWindow(self.db, self.cur_user)
        else:
            QMessageBox.warning(self, "Ошибка", "Неизвестная роль")
            return
        self.role_window.login_window = self
        self.role_window.show()

    def show_login(self):
        self.cur_user = None
        self.role_window = None
        self.username_input.clear()
        self.password_input.clear()
        self.show()


# ----------------------------------------------------------------------
# Окно клиента
# ----------------------------------------------------------------------
class ClientWindow(QMainWindow):
    def __init__(self, db, user):
        super().__init__()
        self.db = db
        self.user = user
        self.login_window = None
        uic.loadUi("guest_window.ui", self)

        ProductTableLoader(self.db.connection).load_to_table(self.menu_list)
        self.logout_button.clicked.connect(self.logout)


    def logout(self):
        if self.login_window:
            self.login_window.show_login()
        self.close()



# ----------------------------------------------------------------------
# Окно менеджера (управление меню)
# ----------------------------------------------------------------------
class ManagerWindow(QMainWindow):
    def __init__(self, db, user):
        super().__init__()
        self.db = db
        self.user = user
        self.login_window = None
        uic.loadUi("admin_window.ui", self)

        self.logout_button.clicked.connect(self.logout)

        self.add_product_btn.hide()
        self.edit_product_btn.hide()
        self.delete_product_btn.hide()

        self.add_order_btn.hide()
        self.delete_order_btn.hide()
        self.edit_order_btn.hide()

        self.product_loader = ProductTableLoader(self.db.connection)

        self.search_input.textChanged.connect(self.refresh_products)
        self.supplier_combo.currentIndexChanged.connect(self.refresh_products)
        self.sort_combo.currentIndexChanged.connect(self.refresh_products)

        # Первоначальная загрузка
        self.refresh_products()

        self.load_orders_as_cards()


    def refresh_products(self):
        """Обновляет таблицу товаров с учётом поиска, фильтра и сортировки"""
        search = self.search_input.text()
        supplier = self.supplier_combo.currentText()
        sort = self.sort_combo.currentIndex()
        self.product_loader.load_to_table(self.menu_list, search, supplier, sort)

        # ---------- Заказы ----------
    def load_orders_as_cards(self):
        cursor = self.db.connection.cursor()
        cursor.execute("""
                            SELECT o.id_order, o.article, os.status_name,
                                         COALESCE(pp.address, 'Не указан'),
                                         o.order_date,
                                         COALESCE(o.delivery_date, 'не назначена')
                                  FROM orders o
                                  JOIN order_statuses os ON o.status_id = os.id_status
                                  LEFT JOIN pickup_points pp ON o.pickup_point_id = pp.id_pickup_point
                                  ORDER BY o.order_date DESC
                              """)
        rows = cursor.fetchall()
        self.orders_list.setRowCount(len(rows))

        self.orders_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.orders_list.setColumnWidth(1, 200)

        self.order_ids = []
        self.articles = []

        for i, (oid, article, status, address, order_date, delivery_date) in enumerate(rows):
            self.order_ids.append(oid)
            self.articles.append(article)
            text = f"Артикул заказа: {article}\nСтатус заказа: {status}\nАдрес пункта выдачи: {address}\nДата заказа: {order_date}"
            self.orders_list.setItem(i, 0, QTableWidgetItem(text))
            text1 = f"Дата доставки: {delivery_date}"
            self.orders_list.setItem(i, 1, QTableWidgetItem(text1))


    def logout(self):
        if self.login_window:
            self.login_window.show_login()
        self.close()

# ----------------------------------------------------------------------
# Окно гостя
# ----------------------------------------------------------------------
class GuestWindow(QMainWindow):
    def __init__(self, db, user):
        super().__init__()
        self.db = db
        self.user = user
        self.login_window = None
        uic.loadUi("guest_window.ui", self)

        ProductTableLoader(self.db.connection).load_to_table(self.menu_list)
        self.logout_button.clicked.connect(self.logout)


    def logout(self):
        if self.login_window:
            self.login_window.show_login()
        self.close()


# ----------------------------------------------------------------------
# Окно администратора
# ----------------------------------------------------------------------
class AdminWindow(QMainWindow):
    def __init__(self, db, user):
        super().__init__()
        self.db = db
        self.user = user
        self.login_window = None
        uic.loadUi("admin_window.ui", self)
        self.setWindowTitle("Админ 123")

        self.logout_button.clicked.connect(self.logout)

        self.add_product_btn.clicked.connect(self.add_product)
        self.edit_product_btn.clicked.connect(self.edit_product)
        self.delete_product_btn.clicked.connect(self.delete_product)

        self.delete_order_btn.clicked.connect(self.delete_order)
        self.add_order_btn.clicked.connect(self.add_order)
        self.edit_order_btn.clicked.connect(self.edit_order)

        self.product_loader = ProductTableLoader(self.db.connection)

        self.search_input.textChanged.connect(self.refresh_products)
        self.supplier_combo.currentIndexChanged.connect(self.refresh_products)
        self.sort_combo.currentIndexChanged.connect(self.refresh_products)

        # Первоначальная загрузка
        self.refresh_products()

        self.load_orders_as_cards()

    def refresh_products(self):
        """Обновляет таблицу товаров с учётом поиска, фильтра и сортировки"""
        search = self.search_input.text()
        supplier = self.supplier_combo.currentText()
        sort = self.sort_combo.currentIndex()
        self.product_loader.load_to_table(self.menu_list, search, supplier, sort)

        # ---------- Заказы ----------
    def load_orders_as_cards(self):
        cursor = self.db.connection.cursor()
        cursor.execute("""
                       SELECT o.id_order, o.article, os.status_name,
                              COALESCE(pp.address, 'Не указан'),
                              o.order_date,
                              COALESCE(o.delivery_date, 'не назначена')
                       FROM orders o
                       JOIN order_statuses os ON o.status_id = os.id_status
                       LEFT JOIN pickup_points pp ON o.pickup_point_id = pp.id_pickup_point
                       ORDER BY o.order_date DESC
                   """)
        rows = cursor.fetchall()
        self.orders_list.setRowCount(len(rows))

        self.orders_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.orders_list.setColumnWidth(1, 200)

        self.order_ids = []
        self.articles = []

        for i, (oid, article, status, address, order_date, delivery_date) in enumerate(rows):
            self.order_ids.append(oid)
            self.articles.append(article)
            text = f"Артикул заказа: {article}\nСтатус заказа: {status}\nАдрес пункта выдачи: {address}\nДата заказа: {order_date}"
            self.orders_list.setItem(i, 0, QTableWidgetItem(text))
            text1 = f"Дата доставки: {delivery_date}"
            self.orders_list.setItem(i, 1, QTableWidgetItem(text1))

    def delete_order(self):
        row = self.orders_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Удаление", "Выберите заказ для удаления")
            return

        order_id = self.order_ids[row]
        article = self.articles[row]

        if QMessageBox.question(self, "Удалить", f"Удалить заказ {article}?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            try:
                cursor = self.db.connection.cursor()
                # Сначала удаляем все позиции заказа
                cursor.execute("DELETE FROM order_items WHERE order_id = %s", (order_id,))
                # Затем удаляем сам заказ
                cursor.execute("DELETE FROM orders WHERE id_order = %s", (order_id,))
                self.db.connection.commit()
                self.load_orders_as_cards()
            except Exception as e:
                self.db.connection.rollback()
                QMessageBox.warning(self, "Ошибка", f"Ошибка удаления: {e}")


    def add_order(self):
        dialog = OrderEditDialog(self.db, None, self)
        if dialog.exec():
            self.load_orders_as_cards()

    def edit_order(self):
        row = self.orders_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите заказ для редактирования")
            return
        order_id = self.order_ids[row]
        dialog = OrderEditDialog(self.db, order_id, self)
        if dialog.exec():
            self.load_orders_as_cards()



    def add_product(self):
        dialog = ProductEditDialog(self.db, None, self)
        if dialog.exec():
            self.refresh_products()

    def edit_product(self):
        row = self.menu_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите товар для редактирования")
            return

        product_id = self.product_loader.product_ids[row]
        dialog = ProductEditDialog(self.db, product_id, self)
        if dialog.exec():
            self.refresh_products()

    def delete_product(self):
        row = self.menu_list.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите товар для удаления")
            return
        product_id = self.product_loader.product_ids[row]
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT product_name FROM products WHERE id_product = %s", (product_id,))
        row_data = cursor.fetchone()
        name = row_data[0] if row_data else "товар"

        cursor.execute("SELECT COUNT(*) FROM order_items WHERE product_id = %s", (product_id,))
        if cursor.fetchone()[0] > 0:
            QMessageBox.warning(self, "", "Нельзя удалить товар, он есть в заказах")
            return

        if QMessageBox.question(self, "Удаление", f"Удалить '{name}'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            try:
                cursor = self.db.connection.cursor()
                cursor.execute("DELETE FROM products WHERE id_product = %s", (product_id,))
                self.db.connection.commit()
                self.refresh_products()
            except Exception as e:
                self.db.connection.rollback()
                QMessageBox.warning(self, "Ошибка", f"Не удалось удалить товар: {e}")


    def logout(self):
        if self.login_window:
            self.login_window.show_login()
        self.close()

# ----------------------------------------------------------------------
# Точка входа
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


    # def load_menu(self):
    #     try:
    #         cursor = self.db.connection.cursor()
    #         cursor.execute("""SELECT item_id, name, price, category, description FROM menuitems ORDER BY item_id""")
    #         items = cursor.fetchall()
    #
    #         self.menu_table.setRowCount(len(items))
    #
    #         for i, item in enumerate(items):
    #             for j, val in enumerate(item):
    #                 self.menu_table.setItem(i, j, QTableWidgetItem(str(val)))
    #
    #         headers = self.menu_table.horizontalHeader()
    #         for i in range(self.menu_table.columnCount()):
    #             headers.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
    #
    #     except Exception as e:
    #         QMessageBox.warning(self, "", f"Ошибка {e}")

# ----------------------------------------------------------------------
# ОСНОВНОЙ КОД
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# login.ui
# ----------------------------------------------------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>LoginWindow</class>
#  <widget class="QMainWindow" name="LoginWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>400</width>
#     <height>300</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>Вход в систему</string>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <layout class="QVBoxLayout" name="verticalLayout">
#     <item>
#      <widget class="QLabel" name="label_login">
#       <property name="text">
#        <string>Логин</string>
#       </property>
#      </widget>
#     </item>
#     <item>
#      <widget class="QLineEdit" name="username_input"/>
#     </item>
#     <item>
#      <widget class="QLabel" name="label_pass">
#       <property name="text">
#        <string>Пароль</string>
#       </property>
#      </widget>
#     </item>
#     <item>
#      <widget class="QLineEdit" name="password_input">
#       <property name="echoMode">
#        <enum>QLineEdit::Password</enum>
#       </property>
#      </widget>
#     </item>
#     <item>
#      <widget class="QPushButton" name="login_button">
#       <property name="text">
#        <string>Войти</string>
#       </property>
#      </widget>
#     </item>
#     <item>
#      <widget class="QPushButton" name="guest_button">
#       <property name="text">
#        <string>Вход как гость</string>
#       </property>
#      </widget>
#     </item>
#    </layout>
#   </widget>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>




# ----------------------------------------------------------------------
# guest_window.ui
# ----------------------------------------------------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>GuestWindow</class>
#  <widget class="QMainWindow" name="GuestWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>650</width>
#     <height>450</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>Гость - Меню пиццерии</string>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <layout class="QVBoxLayout" name="verticalLayout">
#     <item>
#      <widget class="QLabel" name="label">
#       <property name="text">
#        <string/>
#       </property>
#      </widget>
#     </item>
#     <item>
#      <widget class="QTableWidget" name="menu_list">
#       <property name="styleSheet">
#        <string notr="true">color: black;</string>
#       </property>
#       <property name="editTriggers">
#        <set>QAbstractItemView::NoEditTriggers</set>
#       </property>
#       <property name="showGrid">
#        <bool>false</bool>
#       </property>
#       <attribute name="horizontalHeaderVisible">
#        <bool>false</bool>
#       </attribute>
#       <attribute name="verticalHeaderVisible">
#        <bool>false</bool>
#       </attribute>
#       <attribute name="verticalHeaderDefaultSectionSize">
#        <number>170</number>
#       </attribute>
#       <column>
#        <property name="text">
#         <string/>
#        </property>
#       </column>
#       <column>
#        <property name="text">
#         <string/>
#        </property>
#       </column>
#       <column>
#        <property name="text">
#         <string/>
#        </property>
#       </column>
#      </widget>
#     </item>
#     <item>
#      <widget class="QPushButton" name="logout_button">
#       <property name="styleSheet">
#        <string notr="true"/>
#       </property>
#       <property name="text">
#        <string>Выйти</string>
#       </property>
#      </widget>
#     </item>
#    </layout>
#   </widget>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>


# ----------------------------------------------------------------------
# admin_window.ui
# ----------------------------------------------------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>AdminWindow</class>
#  <widget class="QMainWindow" name="AdminWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>1100</width>
#     <height>650</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>Администратор – Магазин обуви</string>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <layout class="QVBoxLayout" name="verticalLayout">
#     <item>
#      <widget class="QTabWidget" name="tabWidget">
#       <property name="currentIndex">
#        <number>0</number>
#       </property>
#       <widget class="QWidget" name="tab_products">
#        <attribute name="title">
#         <string>Товары</string>
#        </attribute>
#        <layout class="QVBoxLayout" name="verticalLayout_products">
#         <item>
#          <layout class="QHBoxLayout" name="productsSearchLayout">
#           <item>
#            <widget class="QLabel" name="label_search">
#             <property name="text">
#              <string>Поиск:</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QLineEdit" name="search_input">
#             <property name="placeholderText">
#              <string>Введите текст...</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QLabel" name="label_supplier">
#             <property name="text">
#              <string>Поставщик:</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QComboBox" name="supplier_combo">
#             <item>
#              <property name="text">
#               <string>Все поставщики</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>ООО &quot;Туфли-Трейд&quot;</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>ИП &quot;Ботинки Опт&quot;</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>ООО &quot;Сапоги Плюс&quot;</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>Склад &quot;Кроссовки.ру&quot;</string>
#              </property>
#             </item>
#            </widget>
#           </item>
#           <item>
#            <widget class="QLabel" name="label_sort">
#             <property name="text">
#              <string>Сортировка по кол-ву:</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QComboBox" name="sort_combo">
#             <item>
#              <property name="text">
#               <string>Без сортировки</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>По возрастанию</string>
#              </property>
#             </item>
#             <item>
#              <property name="text">
#               <string>По убыванию</string>
#              </property>
#             </item>
#            </widget>
#           </item>
#          </layout>
#         </item>
#         <item>
#          <widget class="QTableWidget" name="menu_list">
#           <property name="styleSheet">
#            <string notr="true">color: black;</string>
#           </property>
#           <property name="showGrid">
#            <bool>false</bool>
#           </property>
#           <attribute name="horizontalHeaderVisible">
#            <bool>false</bool>
#           </attribute>
#           <attribute name="verticalHeaderVisible">
#            <bool>false</bool>
#           </attribute>
#           <attribute name="verticalHeaderDefaultSectionSize">
#            <number>170</number>
#           </attribute>
#           <column>
#            <property name="text">
#             <string/>
#            </property>
#           </column>
#           <column>
#            <property name="text">
#             <string/>
#            </property>
#           </column>
#           <column>
#            <property name="text">
#             <string/>
#            </property>
#           </column>
#          </widget>
#         </item>
#         <item>
#          <layout class="QHBoxLayout" name="tab_orders_2">
#           <item>
#            <widget class="QPushButton" name="add_product_btn">
#             <property name="text">
#              <string>Добавить товар</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QPushButton" name="edit_product_btn">
#             <property name="text">
#              <string>Редактировать</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QPushButton" name="delete_product_btn">
#             <property name="text">
#              <string>Удалить</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QWidget" name="stretch_products" native="true">
#             <property name="sizePolicy">
#              <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
#               <horstretch>0</horstretch>
#               <verstretch>0</verstretch>
#              </sizepolicy>
#             </property>
#            </widget>
#           </item>
#          </layout>
#         </item>
#        </layout>
#       </widget>
#       <widget class="QWidget" name="tab_orders">
#        <attribute name="title">
#         <string>Заказы</string>
#        </attribute>
#        <layout class="QVBoxLayout" name="verticalLayout_orders">
#         <item>
#          <widget class="QTableWidget" name="orders_list">
#           <property name="editTriggers">
#            <set>QAbstractItemView::NoEditTriggers</set>
#           </property>
#           <property name="showGrid">
#            <bool>true</bool>
#           </property>
#           <attribute name="horizontalHeaderVisible">
#            <bool>false</bool>
#           </attribute>
#           <attribute name="verticalHeaderVisible">
#            <bool>false</bool>
#           </attribute>
#           <attribute name="verticalHeaderDefaultSectionSize">
#            <number>100</number>
#           </attribute>
#           <attribute name="verticalHeaderHighlightSections">
#            <bool>false</bool>
#           </attribute>
#           <column>
#            <property name="text">
#             <string/>
#            </property>
#           </column>
#           <column>
#            <property name="text">
#             <string/>
#            </property>
#           </column>
#          </widget>
#         </item>
#         <item>
#          <layout class="QHBoxLayout" name="tab_orders_3">
#           <item>
#            <widget class="QPushButton" name="add_order_btn">
#             <property name="text">
#              <string>Добавить заказ</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QPushButton" name="edit_order_btn">
#             <property name="text">
#              <string>Редактировать</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QPushButton" name="delete_order_btn">
#             <property name="text">
#              <string>Удалить</string>
#             </property>
#            </widget>
#           </item>
#           <item>
#            <widget class="QWidget" name="stretch_orders" native="true">
#             <property name="sizePolicy">
#              <sizepolicy hsizetype="Expanding" vsizetype="Preferred">
#               <horstretch>0</horstretch>
#               <verstretch>0</verstretch>
#              </sizepolicy>
#             </property>
#            </widget>
#           </item>
#          </layout>
#         </item>
#        </layout>
#       </widget>
#      </widget>
#     </item>
#     <item>
#      <widget class="QPushButton" name="logout_button">
#       <property name="text">
#        <string>Выйти из системы</string>
#       </property>
#      </widget>
#     </item>
#    </layout>
#   </widget>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>


# ----------------------------------------------------------------------
# add_product_dialog.ui
# ----------------------------------------------------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>AddProductDialog</class>
#  <widget class="QDialog" name="AddProductDialog">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>550</width>
#     <height>550</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>Товар</string>
#   </property>
#   <layout class="QVBoxLayout" name="verticalLayout">
#    <item>
#     <layout class="QFormLayout" name="formLayout">
#      <item row="0" column="0">
#       <widget class="QLabel" name="label_name">
#        <property name="text">
#         <string>Наименование:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="0" column="1">
#       <widget class="QLineEdit" name="name_input"/>
#      </item>
#      <item row="1" column="0">
#       <widget class="QLabel" name="label_category">
#        <property name="text">
#         <string>Категория:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="1" column="1">
#       <widget class="QComboBox" name="category_combo">
#        <item>
#         <property name="text">
#          <string>Туфли</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Ботинки</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Сапоги</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Кроссовки</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Сандалии</string>
#         </property>
#        </item>
#       </widget>
#      </item>
#      <item row="2" column="0">
#       <widget class="QLabel" name="label_description">
#        <property name="text">
#         <string>Описание:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="2" column="1">
#       <widget class="QTextEdit" name="description_input"/>
#      </item>
#      <item row="3" column="0">
#       <widget class="QLabel" name="label_manufacturer">
#        <property name="text">
#         <string>Производитель:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="3" column="1">
#       <widget class="QComboBox" name="manufacturer_combo">
#        <item>
#         <property name="text">
#          <string>Фабрика &quot;Обувь-Стиль&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>ЗАО &quot;Комфорт&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>ООО &quot;Лидер&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>ИП &quot;Классика&quot;</string>
#         </property>
#        </item>
#       </widget>
#      </item>
#      <item row="4" column="0">
#       <widget class="QLabel" name="label_supplier">
#        <property name="text">
#         <string>Поставщик:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="4" column="1">
#       <widget class="QComboBox" name="supplier_combo">
#        <item>
#         <property name="text">
#          <string>ООО &quot;Туфли-Трейд&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>ИП &quot;Ботинки Опт&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>ООО &quot;Сапоги Плюс&quot;</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Склад &quot;Кроссовки.ру&quot;</string>
#         </property>
#        </item>
#       </widget>
#      </item>
#      <item row="5" column="0">
#       <widget class="QLabel" name="label_price">
#        <property name="text">
#         <string>Цена (₽):</string>
#        </property>
#       </widget>
#      </item>
#      <item row="5" column="1">
#       <widget class="QDoubleSpinBox" name="price_input">
#        <property name="decimals">
#         <number>2</number>
#        </property>
#        <property name="minimum">
#         <double>0.000000000000000</double>
#        </property>
#        <property name="maximum">
#         <double>999999.989999999990687</double>
#        </property>
#       </widget>
#      </item>
#      <item row="6" column="0">
#       <widget class="QLabel" name="label_unit">
#        <property name="text">
#         <string>Ед. измерения:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="6" column="1">
#       <widget class="QComboBox" name="unit_combo">
#        <item>
#         <property name="text">
#          <string>пара</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>шт.</string>
#         </property>
#        </item>
#       </widget>
#      </item>
#      <item row="7" column="0">
#       <widget class="QLabel" name="label_quantity">
#        <property name="text">
#         <string>Количество на складе:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="7" column="1">
#       <widget class="QSpinBox" name="quantity_input">
#        <property name="minimum">
#         <number>0</number>
#        </property>
#        <property name="maximum">
#         <number>999999</number>
#        </property>
#       </widget>
#      </item>
#      <item row="8" column="0">
#       <widget class="QLabel" name="label_discount">
#        <property name="text">
#         <string>Скидка (%):</string>
#        </property>
#       </widget>
#      </item>
#      <item row="8" column="1">
#       <widget class="QDoubleSpinBox" name="discount_input">
#        <property name="decimals">
#         <number>2</number>
#        </property>
#        <property name="minimum">
#         <double>0.000000000000000</double>
#        </property>
#        <property name="maximum">
#         <double>100.000000000000000</double>
#        </property>
#       </widget>
#      </item>
#      <item row="9" column="0">
#       <widget class="QLabel" name="label_image">
#        <property name="text">
#         <string>Фото товара:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="9" column="1">
#       <widget class="QLineEdit" name="image_path_edit">
#        <property name="placeholderText">
#         <string>images/picture.png</string>
#        </property>
#       </widget>
#      </item>
#     </layout>
#    </item>
#    <item>
#     <layout class="QHBoxLayout" name="buttonLayout">
#      <item>
#       <spacer name="horizontalSpacer">
#        <property name="orientation">
#         <enum>Qt::Horizontal</enum>
#        </property>
#        <property name="sizeHint" stdset="0">
#         <size>
#          <width>40</width>
#          <height>20</height>
#         </size>
#        </property>
#       </spacer>
#      </item>
#      <item>
#       <widget class="QPushButton" name="save_button">
#        <property name="text">
#         <string>Сохранить</string>
#        </property>
#       </widget>
#      </item>
#      <item>
#       <widget class="QPushButton" name="cancel_button">
#        <property name="text">
#         <string>Отмена</string>
#        </property>
#       </widget>
#      </item>
#     </layout>
#    </item>
#   </layout>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>



# ----------------------------------------------------------------------
# order_dialog.ui
# ----------------------------------------------------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>OrderDialog</class>
#  <widget class="QDialog" name="OrderDialog">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>400</width>
#     <height>350</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>Заказ</string>
#   </property>
#   <layout class="QVBoxLayout" name="verticalLayout">
#    <item>
#     <layout class="QFormLayout" name="formLayout">
#      <item row="0" column="0">
#       <widget class="QLabel" name="label_article">
#        <property name="text">
#         <string>Артикул:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="0" column="1">
#       <widget class="QLineEdit" name="article_edit"/>
#      </item>
#      <item row="1" column="0">
#       <widget class="QLabel" name="label_status">
#        <property name="text">
#         <string>Статус заказа:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="1" column="1">
#       <widget class="QComboBox" name="status_combo">
#        <item>
#         <property name="text">
#          <string>Новый</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>В обработке</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Отправлен</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Доставлен</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Завершен</string>
#         </property>
#        </item>
#        <item>
#         <property name="text">
#          <string>Отменен</string>
#         </property>
#        </item>
#       </widget>
#      </item>
#      <item row="2" column="0">
#       <widget class="QLabel" name="label_address">
#        <property name="text">
#         <string>Адрес пункта выдачи:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="2" column="1">
#       <widget class="QLineEdit" name="address_edit"/>
#      </item>
#      <item row="3" column="0">
#       <widget class="QLabel" name="label_order_date">
#        <property name="text">
#         <string>Дата заказа:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="3" column="1">
#       <widget class="QDateEdit" name="order_date_edit">
#        <property name="calendarPopup">
#         <bool>true</bool>
#        </property>
#        <property name="date">
#         <date>
#          <year>2000</year>
#          <month>1</month>
#          <day>1</day>
#         </date>
#        </property>
#       </widget>
#      </item>
#      <item row="4" column="0">
#       <widget class="QLabel" name="label_delivery_date">
#        <property name="text">
#         <string>Дата доставки:</string>
#        </property>
#       </widget>
#      </item>
#      <item row="4" column="1">
#       <widget class="QDateEdit" name="delivery_date_edit">
#        <property name="calendarPopup">
#         <bool>true</bool>
#        </property>
#        <property name="date">
#         <date>
#          <year>2000</year>
#          <month>1</month>
#          <day>1</day>
#         </date>
#        </property>
#       </widget>
#      </item>
#      <item row="5" column="0">
#       <layout class="QHBoxLayout" name="horizontalLayout"/>
#      </item>
#      <item row="6" column="0">
#       <widget class="QPushButton" name="save_button">
#        <property name="text">
#         <string>Сохранить</string>
#        </property>
#       </widget>
#      </item>
#      <item row="6" column="1">
#       <widget class="QPushButton" name="cancel_button">
#        <property name="text">
#         <string>Отменить</string>
#        </property>
#       </widget>
#      </item>
#     </layout>
#    </item>
#   </layout>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>

# ----------------------------------------------------------------------
# README
# ----------------------------------------------------------------------

"""
# 👟 Shoe Store Management System

**Система управления магазином обуви с ролевой моделью доступа**
*Python + PyQt6 + MySQL*

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📌 Основные возможности

* 🔐 Авторизация по логину и паролю
* 🚪 Гостевой вход без авторизации
* 👥 Ролевая модель доступа:

  * Гость
  * Клиент
  * Менеджер
  * Администратор
* 👟 Просмотр каталога товаров
* 🔍 Поиск, фильтрация и сортировка товаров
* 📦 Управление заказами
* 🎨 Визуальная индикация скидок и остатков товара
* 🛠️ CRUD-операции для товаров и заказов (в зависимости от роли)

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install pymysql PyQt6
```

### 2. Импорт базы данных

Создайте базу данных:

```sql
CREATE DATABASE shoestore;
```

Затем выполните файл `database.sql`, содержащий структуру таблиц и тестовые данные.

### 3. Запуск приложения

```bash
python main.py
```

> ⚠️ Важно: все файлы `.ui` должны находиться в одной директории с файлом `main.py`.

---

## 🔑 Тестовые учетные записи

| Роль             | Логин     | Пароль    |
| ---------------- | --------- | --------- |
| 👑 Администратор | `admin`   | `admin`   |
| 📊 Менеджер      | `manager` | `manager` |
| 🧑‍💼 Клиент     | `client`  | `client`  |
| 🚪 Гость         | `guest`   | `guest`   |

Также доступна кнопка **«Войти как гость»**, позволяющая выполнить вход без ввода логина и пароля.

---

## 🧠 Возможности ролей

| Роль             | Просмотр товаров | Поиск / Фильтр / Сортировка | Управление товарами | Просмотр заказов | Управление заказами |
| ---------------- | :--------------: | :-------------------------: | :-----------------: | :--------------: | :-----------------: |
| 🚪 Гость         |         ✅        |              ❌              |          ❌          |         ❌        |          ❌          |
| 🧑‍💼 Клиент     |         ✅        |              ❌              |          ❌          |         ❌        |          ❌          |
| 📊 Менеджер      |         ✅        |              ✅              |          ❌          |         ✅        |          ❌          |
| 👑 Администратор |         ✅        |              ✅              |       ✅ (CRUD)      |         ✅        |       ✅ (CRUD)      |

> **CRUD** — создание, чтение, редактирование и удаление записей.

---

## 🎨 Визуальные особенности

### Остатки товара

| Цвет       | Значение                                              |
| ---------- | ----------------------------------------------------- |
| 🔵 Голубой | Товар отсутствует на складе (`quantity_in_stock = 0`) |

### Скидки

| Цвет         | Значение         |
| ------------ | ---------------- |
| 🟢 `#2E8B57` | Скидка более 15% |

Дополнительно:

* ❌ Старая цена отображается зачёркнутой красным цветом.
* 💰 Итоговая цена отображается чёрным цветом.

---

## 📁 Структура проекта

```text
.
├── main.py                   # Основной исполняемый файл
├── login.ui                  # Окно авторизации
├── guest_window.ui           # Интерфейс гостя и клиента
├── admin_window.ui           # Интерфейс администратора и менеджера
├── add_product_dialog.ui     # Диалог добавления/редактирования товара
├── order_dialog.ui           # Диалог добавления/редактирования заказа
├── images/
│   └── picture.png           # Изображение-заглушка
└── database.sql              # Скрипт базы данных
```

---

## 🛠️ Настройка подключения к базе данных

При необходимости измените параметры подключения в классе `Database` (`main.py`):

```python
self.connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="shoestore"
)
```

---

## 📄 Примечания

* ⚠️ Пароли хранятся в открытом виде. Для учебного проекта это допустимо, однако в реальных системах рекомендуется использовать хеширование.
* ⚠️ При создании нового заказа администратором значение `user_id` автоматически устанавливается в `1` (упрощение согласно требованиям проекта).
* ⚠️ Для корректного отображения изображений убедитесь, что пути, указанные в поле `image_path` таблицы `products`, соответствуют существующим файлам.

---

## 🎓 Учебный проект

Проект разработан в образовательных целях для демонстрации:

* работы с **PyQt6**;
* взаимодействия с **MySQL** через **PyMySQL**;
* реализации **ролевой модели доступа**;
* выполнения **CRUD-операций**;
* построения настольных приложений на Python.
"""



# ----------------------------------------------------------------------
# БЛОК СХЕМА (draw.io -> упорядочить -> вставить -> mermaid (может быть русалка))
# ----------------------------------------------------------------------




# flowchart TD

#     A([Начало]) --> B[Окно авторизации]

#     B --> C[/Ввод логина и пароля<br/>или вход как Гость/]

#     C --> D{Поля пусты?}

#     D -- Да --> E[Ошибка]
#     E --> B

#     D -- Нет --> F{Пользователь найден в БД?}

#     F -- Нет --> G[Ошибка]
#     G --> B

#     F -- Да --> H{Определение роли}

#     %% Администратор
#     H -- Администратор --> A1[Поиск, сортировка и фильтрация товаров]
#     A1 --> A2[Добавление, редактирование и удаление товаров]
#     A2 --> A3[Просмотр заказов]
#     A3 --> A4[Добавление, редактирование и удаление заказов]
#     A4 --> X[Выход]

#     %% Менеджер
#     H -- Менеджер --> M1[Поиск, сортировка и фильтрация товаров]
#     M1 --> M2[Просмотр заказов]
#     M2 --> X

#     %% Клиент
#     H -- Клиент --> C1[Просмотр товаров]
#     C1 --> X

#     %% Гость
#     H -- Гость --> G1[Просмотр товаров]
#     G1 --> X

#     X --> Z([Конец])
