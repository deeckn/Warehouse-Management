from sqlalchemy import desc
from .schema import Session, engine
from .schema import User, Customer, ProductCategory, ProductLocation, Shelf, QuarterlyReport, Log, Product
from abc import ABC


class DAO(ABC):
    def __init__(self, session: Session):
        self.session: Session = session


class AppDAO:
    local_session = Session(bind=engine)

    @staticmethod
    def get_dao(type: str) -> DAO:
        """
        'user' returns UserDAO |
        'customer' returns CustomerDAO |
        'product' returns ProductDAO |
        'shelf' returns ShelfDAO |
        'log' returns LogDAO |
        'category' returns CategoryDAO |
        'location' returns LocationDAO |
        'report' returns ReportDAO
        """
        match type:
            case "user":
                return UserDAO(AppDAO.local_session)
            case "customer":
                return CustomerDAO(AppDAO.local_session)
            case "product":
                return ProductDAO(AppDAO.local_session)
            case "shelf":
                return ShelfDAO(AppDAO.local_session)
            case "log":
                return LogDAO(AppDAO.local_session)
            case "category":
                return CategoryDAO(AppDAO.local_session)
            case "location":
                return LocationDAO(AppDAO.local_session)
            case "report":
                return ReportDAO(AppDAO.local_session)
            case _:
                return None


class UserDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_user(self, user: User):
        """Adds a User persistent object to the database"""
        if user is None or self.exist(user):
            return

        self.session.add(user)
        self.session.commit()

    def get_all_users(self) -> list[User]:
        """Retrieves all users from the USERS table"""
        return self.session.query(User).all()

    def get_user_by_id(self, id: int) -> User:
        """Retreives a User object given an id"""
        return self.session.query(User).filter(User.user_id == id).first()

    def get_user_by_username(self, username: str) -> User:
        """Retreives a User object given a username"""
        return self.session.query(User).filter(User.username == username).first()

    def exist(self, user: User) -> bool:
        """Returns True if the User exist in the database"""
        if user is None:
            return False

        query = self.session.query(User).filter(
            User.first_name == user.get_first_name(),
            User.last_name == user.get_last_name(),
            User.username == user.get_username(),
            User.password == user.get_password(),
            User.access_level == user.get_access_level()
        ).first()
        return query is not None

    def delete_user_by_id(self, user_id: int):
        """Deletes user data given an id"""
        user: User = self.session.query(User).filter(
            User.user_id == user_id).first()

        if user is None:
            return

        self.session.delete(user)
        self.session.commit()

    def update_user(
        self,
        user_id: int,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password: str = None,
        access: str = None
    ):
        """
        Updates user data given an id |
        Example: update_user(4, first_name="John",
                             username="john.tr", access=AdminAccess())
        """
        user: User = self.session.query(User).filter(
            User.user_id == user_id).first()

        if user is None:
            return False

        if user_id is not None:
            user.user_id = user_id

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        if username is not None:
            user.username = username

        if password is not None:
            user.password = password

        if access is not None:
            user.access_level = access

        self.session.commit()


class CustomerDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_customer(self, customer: Customer):
        """Adds a Customer object to the database"""
        if customer is None or self.exist(customer):
            return

        self.session.add(customer)
        self.session.commit()

    def get_all_customers(self) -> list[Customer]:
        """Retreives all Customer objects"""
        return self.session.query(Customer).all()

    def get_customer(self, customer_id: int) -> Customer:
        """Retreives a Customer object given an id"""
        return self.session.query(Customer).filter(Customer.customer_id == customer_id).first()

    def get_customer_by_name(self, name: str) -> Customer:
        """Retreives a Customer object given a name"""
        return self.session.query(Customer).filter(Customer.name == name).first()

    def get_customer_contains_with(self, name_search: str) -> list[Customer]:
        """Returns a list of Customer objects that satisfy the search string"""
        return self.session.query(Customer).filter(Customer.name.like(f"%{name_search}%")).all()

    def exist(self, customer: Customer) -> bool:
        """Returns True if a customer exist in the database"""
        return self.session.query(Customer).filter(
            Customer.name == customer.get_name(),
            Customer.phone == customer.get_phone(),
            Customer.email == customer.get_email(),
            Customer.packing_service == customer.get_packing_service(),
            Customer.rental_duration == customer.get_rental_duration(),
            Customer.date_joined == customer.get_date_joined(),
            Customer.expiry_date == customer.get_expiry_date(),
            Customer.total_payment == customer.get_total_payment()
        ).first() is not None

    def delete_customer(self, customer_id: int):
        """Deletes customer data given an id"""
        customer = self.session.query(Customer).filter(
            Customer.customer_id == customer_id).first()

        if customer is None:
            return

        self.session.delete(customer)
        self.session.commit()

    def update_customer(
        self,
        id: int,
        name: str = None,
        phone: str = None,
        email: str = None,
        packing_service: bool = None,
        rental_duration: int = None,
        date_joined: str = None,
        expiry_date: str = None,
        total_payment: float = None
    ):
        """
        Updates customer data given an id.
        Example: update_customer(5, phone="1357924680", total_payment=12500)
        """
        customer: Customer = self.session.query(Customer).filter(
            Customer.customer_id == id).first()

        if customer is None:
            return

        if name is not None:
            customer.name = name

        if phone is not None:
            customer.phone = phone

        if email is not None:
            customer.email = email

        if packing_service is not None:
            customer.packing_service = packing_service

        if rental_duration is not None:
            customer.rental_duration = rental_duration

        if date_joined is not None:
            customer.date_joined = date_joined

        if expiry_date is not None:
            customer.expiry_date = expiry_date

        if total_payment is not None:
            customer.total_payment = total_payment

        self.session.commit()


class CategoryDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_product_category(self, category: ProductCategory):
        """Appends a product category to the PRODUCT_CATEGORIES table"""
        if category is None:
            return
        self.session.add(category)
        self.session.commit()

    def get_product_categories(self, product_id: int) -> list[ProductCategory]:
        """Returns a list of ProductCategory objects"""
        data = self.session.query(ProductCategory).filter(
            ProductCategory.product_id == product_id).all()

        if data is None:
            return None

        return data

    def remove_product_category(self, product_id: int, category: str):
        """Removes a category from a product"""
        query_data = self.session.query(ProductCategory).filter(
            ProductCategory.product_id == product_id,
            ProductCategory.category == category
        ).first()

        if query_data is None:
            return

        self.session.delete(query_data)
        self.session.commit()

    def remove_all_product_categories(self, product_id: int):
        """Removes all categories of a product"""
        categories = self.session.query(ProductCategory).filter(
            ProductCategory.product_id == product_id).all()

        if categories is None:
            return

        for category in categories:
            self.session.delete(category)
            self.session.commit()


class LocationDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_product_location(self, location: ProductLocation):
        """Adds a product and location entry to the PRODUCT_LOCATIONS table"""
        if location is None:
            return

        self.session.add(location)
        self.session.commit()

    def get_product_locations(self, product_id: int) -> list[ProductLocation]:
        """Returns list of Location objects given the product id"""
        data = self.session.query(ProductLocation).filter(
            ProductLocation.product_id == product_id).all()
        return data

    def get_products_on_shelf(self, shelf_label: str) -> list[tuple[int, int]]:
        """Returns a list of product and its quantity located in a shelf"""
        data: list[ProductLocation] = self.session.query(ProductLocation).filter(
            ProductLocation.shelf_label == shelf_label
        ).all()

        if data is None:
            return None

        formatted_data = []
        for location in data:
            formatted_data.append(
                (location.product_id, location.get_batch_quantity())
            )

        return formatted_data

    def get_batch_count(self, product_id: int) -> int:
        """Returns the number of batches a product has"""
        data = self.session.query(ProductLocation).filter(
            ProductLocation.product_id == product_id).count()
        return data

    def remove_product_location(self, product_id: int, batch_number: int):
        """Removes a shelf location of a product in the PRODUCT_LOCATIONS table"""
        location = self.session.query(ProductLocation).filter(
            ProductLocation.product_id == product_id,
            ProductLocation.batch_number == batch_number
        ).first()

        if location is None:
            return

        self.session.delete(location)
        self.session.commit()

    def remove_all_product_locations(self, product_id: int):
        """Removes the locations of a product"""
        locations = self.session.query(ProductLocation).filter(
            ProductLocation.product_id == product_id).all()

        if locations is None:
            return

        for location in locations:
            self.session.delete(location)
            self.session.commit()

    def get_occupied_slots(self, shelf_label: str) -> list[int]:
        locations = self.session.query(ProductLocation).filter(
            ProductLocation.shelf_label == shelf_label).all()
        if locations is None:
            return None

        slots = []
        for location in locations:
            slots.append(location.get_shelf_number())
        return slots


class ProductDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)
        self.__customer_dao: CustomerDAO = AppDAO.get_dao("customer")
        self.__category_dao: CategoryDAO = AppDAO.get_dao("category")
        self.__location_dao: LocationDAO = AppDAO.get_dao("location")

    def add_product(self, product: Product):
        """Adds a Product object to the PRODUCTS table"""
        if product is None or self.exist(product):
            return

        categories = product.get_category_list()
        locations = product.get_locations()

        if categories is None or locations is None:
            return

        for category in categories:
            self.__category_dao.add_product_category(category)

        for location in locations:
            self.__location_dao.add_product_location(location)

        self.session.add(product)
        self.session.commit()

    def exist(self, product: Product) -> bool:
        """Returns True if a Product exist in the database"""
        return self.session.query(Product).filter(
            Product.name == product.get_name(),
            Product.quantity == product.get_quantity(),
            Product.low_stock == product.low_stock,
            Product.weight == product.get_weight(),
            Product.last_stored == product.get_last_stored(),
            Product.owner == product.owner,
            Product.length == product.length,
            Product.width == product.width,
            Product.height == product.height,
        ).first() is not None

    def get_product(self, product_id: int) -> Product:
        """Returns a Product object given an id"""
        product: Product = self.session.query(Product).filter(
            Product.product_id == product_id).first()
        if product is None:
            return None

        owner = self.__customer_dao.get_customer(product.owner)
        categories = self.__category_dao.get_product_categories(
            product.product_id)
        locations = self.__location_dao.get_product_locations(
            product.product_id)

        product.set_owner_object(owner)
        product.insert_categories(categories)
        product.insert_locations(locations)
        return product

    def get_product_by_name(self, product_name: str, owner_id: int) -> Product:
        """Returns a Product object given the name and owner id"""
        product: Product = self.session.query(Product).filter(
            Product.name == product_name,
            Product.owner == owner_id
        ).first()

        if product is None:
            return None

        owner = self.__customer_dao.get_customer(product.owner)
        categories = self.__category_dao.get_product_categories(
            product.product_id)
        locations = self.__location_dao.get_product_locations(
            product.product_id)

        product.set_owner_object(owner)
        product.insert_categories(categories)
        product.insert_locations(locations)
        return product

    def get_customer_products(self, owner_id: int) -> list[Product]:
        """Returns a Product object list given the owner id"""
        products: list[Product] = self.session.query(
            Product).filter(Product.owner == owner_id).all()

        if products is None:
            return None

        for product in products:
            owner = self.__customer_dao.get_customer(product.owner)
            categories = self.__category_dao.get_product_categories(
                product.product_id)
            locations = self.__location_dao.get_product_locations(
                product.product_id)
            product.set_owner_object(owner)
            product.insert_categories(categories)
            product.insert_locations(locations)

        return products

    def get_all_products(self) -> list[Product]:
        """Returns all products as a list of Product objects"""
        products: list[Product] = self.session.query(Product).all()

        if products is None:
            return None

        for product in products:
            owner = self.__customer_dao.get_customer(product.owner)
            categories = self.__category_dao.get_product_categories(
                product.product_id)
            locations = self.__location_dao.get_product_locations(
                product.product_id)
            product.set_owner_object(owner)
            product.insert_categories(categories)
            product.insert_locations(locations)

        return products

    def get_total_product_count(self) -> int:
        """Returns the total number of products in the system"""
        return self.session.query(Product).count()

    def get_customer_product_count(self, customer_id: int) -> int:
        """Returns the total number of products owned by a customer"""
        return self.session.query(Product).filter(Product.owner == customer_id).count()

    def get_low_quantity_products(self) -> list[Product]:
        """Returns a list of low quantity products"""
        products: list[Product] = self.session.query(Product).filter(
            Product.quantity <= Product.low_stock).all()

        if products is None:
            return None

        for product in products:
            owner = self.__customer_dao.get_customer(product.owner)
            categories = self.__category_dao.get_product_categories(
                product.product_id)
            locations = self.__location_dao.get_product_locations(
                product.product_id)
            product.set_owner_object(owner)
            product.insert_categories(categories)
            product.insert_locations(locations)

        return products

    def get_product_contains_with(self, name: str) -> list[Product]:
        """Returns a list of Product objects based on a proper substring"""
        products: list[Product] = self.session.query(
            Product).filter(Product.name.like(f"%{name}%")).all()

        if products is None:
            return None

        for product in products:
            owner = self.__customer_dao.get_customer(product.owner)
            categories = self.__category_dao.get_product_categories(
                product.product_id)
            locations = self.__location_dao.get_product_locations(
                product.product_id)
            product.set_owner_object(owner)
            product.insert_categories(categories)
            product.insert_locations(locations)

        return products

    def update_product(
        self,
        id: int,
        name: str = None,
        quantity: int = None,
        low_stock: int = None,
        weight: float = None,
        last_stored: str = None,
        owner_id: int = None,
        length: float = None,
        width: float = None,
        height: float = None
    ):
        product: Product = self.session.query(Product).filter(
            Product.product_id == id).first()
        if product is None:
            return

        if name is not None:
            product.name = name

        if quantity is not None:
            product.quantity = quantity

        if low_stock is not None:
            product.low_stock = low_stock

        if weight is not None:
            product.weight = weight

        if last_stored is not None:
            product.last_stored = last_stored

        if owner_id is not None:
            product.owner = owner_id

        if length is not None:
            product.length = length

        if width is not None:
            product.width = width

        if height is not None:
            product.height = height

        self.session.commit()

    def delete_product(self, product_id: int):
        """Removes a product from the database"""
        product = self.session.query(Product).filter(
            Product.product_id == product_id).first()
        if product is None:
            return

        self.__location_dao.remove_all_product_locations(product_id)
        self.__category_dao.remove_all_product_categories(product_id)
        self.session.delete(product)
        self.session.commit()


class ShelfDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_shelf(self, shelf: Shelf):
        """Add shelf object to the STORAGE_SHELF table"""
        if shelf is None or self.exist(shelf):
            return
        self.session.add(shelf)
        self.session.commit()

    def exist(self, shelf: Shelf) -> bool:
        """Returns True if a Shelf exist in the database"""
        return self.session.query(Shelf).filter(
            Shelf.label == shelf.get_label()
        ).first() is not None

    def get_shelf_by_label(self, shelf_label: str) -> Shelf:
        """Returns a Shelf object given a label"""
        shelf = self.session.query(Shelf).filter(
            Shelf.label == shelf_label).first()
        return shelf

    def get_all_shelves(self) -> list[Shelf]:
        """Returns a list of all Shelf objects from the database"""
        return self.session.query(Shelf).all()

    def update_shelf(
        self,
        label: str,
        max_weight: float = None,
        length: float = None,
        width: float = None,
        height: float = None,
        rows: int = None,
        columns: int = None
    ):
        shelf: Shelf = self.session.query(
            Shelf).filter(Shelf.label == label).first()
        if shelf is None:
            return

        if max_weight is not None:
            shelf.max_weight = max_weight

        if length is not None:
            shelf.length = length

        if width is not None:
            shelf.width = width

        if height is not None:
            shelf.height = height

        if rows is not None:
            shelf.rows = rows

        if columns is not None:
            shelf.columns = columns

        self.session.commit()

    def delete_shelf(self, shelf_label: str):
        """Removes a shelf from the database"""
        shelf = self.session.query(Shelf).filter(
            Shelf.label == shelf_label).first()
        if shelf is None:
            return

        self.session.delete(shelf)
        self.session.commit()

    def get_shelves_contains_with(self, shelf_search: str) -> list[Shelf]:
        return self.session.query(Shelf).filter(Shelf.label.like(f"%{shelf_search}%")).all()


class ReportDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_report(self, report: QuarterlyReport):
        """Add QuarterlyReport object to the QUARTERLY_REPORT table"""
        if report is None or self.exists(report):
            return

        self.session.add(report)
        self.session.commit()

    def get_all_reports(self) -> list[QuarterlyReport]:
        """Returns a list of all QuarterlyReport objects in the database"""
        return self.session.query(QuarterlyReport).all()

    def update_report(self, year: int, quarter: int, utilization: float = None, revenue: float = None):
        report: QuarterlyReport = self.session.query(QuarterlyReport).filter(
            QuarterlyReport.year == year, QuarterlyReport.quarter == quarter).first()
        if report is None:
            return

        if utilization is not None:
            report.utilized_space = utilization

        if revenue is not None:
            report.total_revenue = revenue

        self.session.commit()

    def exists(self, report: QuarterlyReport) -> bool:
        return self.session.query(QuarterlyReport).filter(
            QuarterlyReport.year == report.get_year(),
            QuarterlyReport.quarter == report.get_quarter()
        ).first() is not None


class LogDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_all_log_entries(self) -> list[Log]:
        """Returns a list of Logs"""
        return self.session.query(Log).order_by(desc(Log.log_id)).limit(20).all()

    def add_log_entry(self, log_entry: Log):
        """Adds a log entry to the database"""
        if log_entry is None:
            return

        self.session.add(log_entry)
        self.session.commit()
