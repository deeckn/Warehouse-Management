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
        query = self.session.query(Customer).filter(
            Customer.name == customer.get_name() and
            Customer.phone == customer.get_phone() and
            Customer.email == customer.get_email() and
            Customer.packing_service == customer.get_packing_service() and
            Customer.rental_duration == customer.get_rental_duration() and
            Customer.date_joined == customer.get_date_joined() and
            Customer.expiry_date == customer.get_expiry_date() and
            Customer.total_payment == customer.get_total_payment()
        )
        return query is not None

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
        data = self.session.query(ProductLocation).filter(
            ProductLocation.shelf_label == shelf_label
        ).all()
        return data

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

    def add_product(self, product: Product):
        """Adds a Product object to the PRODUCTS table"""
        if product is None:
            return

        self.session.add(product)
        self.session.commit()

    def exist(self, product: Product) -> bool:
        """Returns True if a Product exist in the database"""
        pass

    def get_product(self, product_id: int) -> Product:
        """Returns a Product object given an id"""
        pass

    def get_product_by_name(self, product_name: str, owner_id: int) -> Product:
        """Returns a Product object given the name and owner id"""
        pass

    def get_customer_products(self, owner_id: int) -> list[Product]:
        """Returns a Product object list given the owner id"""
        pass

    def get_all_products(self) -> list[Product]:
        """Returns all products as a list of Product objects"""
        pass

    def get_total_product_count(self) -> int:
        pass

    def get_customer_product_count(self, customer_id: int) -> int:
        pass

    def get_low_quantity_products(self) -> list[Product]:
        pass

    def get_product_contains_with(self, name: str) -> list[Product]:
        """Returns a list of Product objects based on a proper substring"""
        pass

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
        pass

    def delete_product(self, product_id: int):
        """Removes a product from the database"""
        pass


class ShelfDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def add_shelf(self, shelf: Shelf):
        """Add shelf object to the STORAGE_SHELF table"""
        if shelf is None:
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
        shelf: Shelf = self.session.query(Shelf).filter(Shelf.label == label).first()
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
        pass

    def get_all_reports(self) -> list[QuarterlyReport]:
        """Returns a list of all QuarterlyReport objects in the database"""
        pass

    def update_report(self, year: int, quarter: int, utilization: float = None, revenue: float = None):
        pass


class LogDAO(DAO):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_all_log_entries(self) -> list[Log]:
        pass

    def add_log_entry(self, log_entry: Log):
        pass
