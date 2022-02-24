from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from views.theme import Theme


class NotificationItem(QWidget):
    def __init__(self, parent, notification_type: str, event: str, customer: str, id: str):
        """notification_type: low_stock | contract_end"""
        super().__init__(parent)
        self.setFixedSize(1320, 120)

        # Main Container (White background)
        container = QWidget(self)
        container.setFixedSize(1310, 120)
        container.setStyleSheet(f"""
            background-color: #{Theme.WHITE}; 
            border-radius: 15; 
            padding: 0
        """)

        grid_layout = QGridLayout()

        # Status Indicator
        circle_container = QWidget(self)
        status_circle = QLabel(circle_container)
        status_circle.setGeometry(40, 40, 25, 25)

        if notification_type == "low_stock":
            status_circle.setStyleSheet(f"""
                background-color: #{Theme.YELLOW}; 
                border-radius: 12;
            """)
        elif notification_type == "contract_end":
            status_circle.setStyleSheet(f"""
                background-color: #{Theme.RED}; 
                border-radius: 12;
            """)
        else:
            status_circle.setStyleSheet(f"""
                background-color: #{Theme.BLACK}; 
                border-radius: 12;
            """)

        # Card Labels
        event_label = QLabel(event, self)
        event_label.setFont(Theme.POPPINS_REGULAR_24)

        customer_label = QLabel(customer, self)
        customer_label.setFont(Theme.POPPINS_REGULAR_24)

        id_label = QLabel(id, self)
        id_label.setFont(Theme.POPPINS_REGULAR_24)

        # Label Position Setup
        grid_layout.addWidget(circle_container, 0, 0, 1, 1)
        grid_layout.addWidget(event_label, 0, 1, 1, 1)
        grid_layout.addWidget(customer_label, 0, 2, 1, 1)
        grid_layout.addWidget(id_label, 0, 3, 1, 1)

        # Label Space Setup
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 4)
        grid_layout.setColumnStretch(2, 2)
        grid_layout.setColumnStretch(3, 2)
        grid_layout.setHorizontalSpacing(40)

        container.setLayout(grid_layout)
