import sys
import os
import pymysql
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QHeaderView, QTableWidgetItem, QDialog


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

        if product_id:
            self.load_product_data()

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