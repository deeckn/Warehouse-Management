from PySide6.QtCore import Qt
from views.forms.stack_page import StackPage
from PySide6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout
from views.items.notification_item import NotificationItem
from views.theme import Theme


class NotificationView(StackPage):
    def __init__(self) -> None:
        super().__init__()
        self.set_styleSheet("stack_page_theme.qss")

        # Page Title
        title = QLabel("Notification", self)
        title.setObjectName("page_name")
        title.setFont(Theme.POPPINS_BOLD_64)
        title.setGeometry(100, 60, 423, 96)

        # Low Stock Indicator
        yellow_circle = QLabel(self)
        yellow_circle.setGeometry(100, 165, 25, 25)
        yellow_circle.setStyleSheet(
            f"background-color: {Theme.YELLOW}; border-radius: 12;"
        )

        low_stock_label = QLabel("Low Stock", self)
        low_stock_label.setFont(Theme.POPPINS_REGULAR_24)
        low_stock_label.setGeometry(145, 160, 120, 40)

        # Contract End Indicator
        red_circle = QLabel(self)
        red_circle.setGeometry(320, 165, 25, 25)
        red_circle.setStyleSheet(
            f"background-color: {Theme.RED}; border-radius: 12;"
        )

        contract_end_label = QLabel("Contract Ending", self)
        contract_end_label.setFont(Theme.POPPINS_REGULAR_24)
        contract_end_label.setGeometry(370, 160, 200, 40)

        # Table Header Labels
        status_column_label = QLabel("Status", self)
        status_column_label.setFont(Theme.POPPINS_BOLD_24)
        status_column_label.setStyleSheet(f"color: {Theme.BLUE};")
        status_column_label.setGeometry(120, 246, 100, 40)

        event_column_label = QLabel("Event", self)
        event_column_label.setFont(Theme.POPPINS_BOLD_24)
        event_column_label.setStyleSheet(f"color: {Theme.BLUE};")
        event_column_label.setGeometry(285, 246, 100, 40)

        customer_column_label = QLabel("Customer", self)
        customer_column_label.setFont(Theme.POPPINS_BOLD_24)
        customer_column_label.setStyleSheet(f"color: {Theme.BLUE};")
        customer_column_label.setGeometry(845, 246, 130, 40)

        id_column_label = QLabel("ID", self)
        id_column_label.setFont(Theme.POPPINS_BOLD_24)
        id_column_label.setStyleSheet(f"color: {Theme.BLUE};")
        id_column_label.setGeometry(1150, 246, 30, 40)

        # Scroll Area Container
        self.notification_list_widget = QWidget(self)
        self.notification_list_widget.setGeometry(100, 300, 1320, 680)

        self.scroll_area = QScrollArea(self.notification_list_widget)
        self.scroll_area.setStyleSheet("border: 0; padding: 0")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.horizontalScrollBar().setEnabled(False)
        self.scroll_area.setGeometry(0, 0, 1320, 680)

        self.scroll_area_widget = QWidget(self.scroll_area)
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_layout.setSpacing(20)
        self.scroll_area_layout.setAlignment(Qt.AlignTop)
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)

    def add_event_card(self, notification_type: str, event: str, customer_name: str, id: str):
        """Inserts a new event card into the notication list. notification_type: low_stock | contract_end"""
        self.scroll_area_widget.layout().addWidget(
            NotificationItem(
                self,
                notification_type,
                event,
                customer_name,
                id
            )
        )

    def clear_notification_list(self):
        """Clear all event cards in the notification list view"""
        for i in reversed(range(self.scroll_area_widget.layout().count())):
            self.scroll_area_widget.layout().itemAt(i).widget().setParent(None)
