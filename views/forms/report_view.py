from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QGridLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from views.forms.stack_page import StackPage 
from views.theme import Theme
from data.data_classes import Customer
from views.items.report_card_item import ReportCardItem

class ReportView(StackPage):

    def __init__(self, img_type: str):
        super().__init__()
        self.set_styleSheet("stack_page_theme.qss")

        self.img_type = img_type  

        report_label = QLabel("Report", self)
        report_label.setObjectName("report_label")
        report_label.setGeometry(100, 60, 240, 80)
        report_label.setFont(Theme.POPPINS_BOLD_72)

        report_widget = QWidget(self)
        report_widget.setObjectName("container")
        report_widget.setGeometry(100, 220, 580, 770)

        customer_list_label = QLabel("Customer List", report_widget)
        customer_list_label.setObjectName("customer_list_label")
        customer_list_label.setGeometry(0, 0, 580, 100)
        customer_list_label.setFont(Theme.POPPINS_BOLD_36)
        customer_list_label.setAlignment(Qt.AlignCenter)

        self.scrollArea = QScrollArea(report_widget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(0, 100, 580, 670)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)

        self.scrollArea_widget = QWidget()
        self.scrollArea_widget.setObjectName("container")
        self.scrollArea_widget.setGeometry(0, 0, 580, 670)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)
        self.scrollArea_widget.setLayout(self.layout)
        self.scrollArea.setWidget(self.scrollArea_widget)

        widget_2 = QWidget(self)
        widget_2.setObjectName("container")
        widget_2.setGeometry(760, 220, 660, 770)

        self.back_button = QPushButton(widget_2)
        self.back_button.setObjectName("back_btn")
        self.back_button.setGeometry(50, 50, 50, 50)

        self.next_button = QPushButton(widget_2)
        self.next_button.setObjectName("next_btn")
        self.next_button.setGeometry(560, 50, 50, 50)
    
        self.quarter_label = QLabel("2021/2", widget_2)
        self.quarter_label.setGeometry(130, 50, 400, 50)
        self.quarter_label.setFont(Theme.POPPINS_REGULAR_36)
        self.quarter_label.setAlignment(Qt.AlignCenter)

        unused_space_label = QLabel("Unused Space", widget_2)
        unused_space_label.setGeometry(420, 235, 180, 40)
        unused_space_label.setFont(Theme.POPPINS_REGULAR_24)

        utilized_space_label = QLabel("Utilized Space", widget_2)
        utilized_space_label.setGeometry(420, 285, 180, 40)
        utilized_space_label.setFont(Theme.POPPINS_REGULAR_24)

        self.export_button = QPushButton("EXPORT", widget_2)
        self.export_button.setObjectName("export_btn")
        self.export_button.setGeometry(420, 660, 190, 70)
        self.export_button.setFont(Theme.POPPINS_BOLD_24)

        total_revenue_label = QLabel("Total Revenue", widget_2)
        total_revenue_label.setGeometry(80, 500, 180, 40)
        total_revenue_label.setFont(Theme.POPPINS_REGULAR_24)

        monthly_revenue_label = QLabel("Monthly Revenue", widget_2)
        monthly_revenue_label.setGeometry(80, 540, 210, 40)
        monthly_revenue_label.setFont(Theme.POPPINS_REGULAR_24)

        capacity_utilization_label = QLabel("Capacity Utilization", widget_2)
        capacity_utilization_label.setGeometry(80, 580, 230, 40)
        capacity_utilization_label.setFont(Theme.POPPINS_REGULAR_24)

        self.total_show_label = QLabel("0", widget_2)
        self.total_show_label.setObjectName("legend")
        self.total_show_label.setGeometry(280, 500, 150, 40)
        self.total_show_label.setFont(Theme.POPPINS_REGULAR_24) 

        self.monthly_show_label = QLabel("0", widget_2)
        self.monthly_show_label.setObjectName("legend")
        self.monthly_show_label.setGeometry(310, 540, 150, 40)
        self.monthly_show_label.setFont(Theme.POPPINS_REGULAR_24)

        self.capacity_show_label = QLabel("0", widget_2)
        self.capacity_show_label.setObjectName("legend")
        self.capacity_show_label.setGeometry(340, 580, 150, 40)
        self.capacity_show_label.setFont(Theme.POPPINS_REGULAR_24) 

        unused_button = QPushButton(widget_2)
        unused_button.setObjectName("symbol_red")
        unused_button.setGeometry(370, 240, 30, 30)

        utilized_button = QPushButton(widget_2)
        utilized_button.setObjectName("symbol_green")
        utilized_button.setGeometry(370, 290, 30, 30)

        self.pie_chart_widget = QWidget(widget_2)
        self.pie_chart_widget.setGeometry(20,130,370,370)
        self.pie_chart_widget.setStyleSheet("background-color: transparent;")
        self.series = None
        self.chart = QChart()
        self.chart.legend().hide()
        self.chartview = QChartView(self.chart)
        self.gridlayout = QGridLayout()
        self.pie_chart_widget.setLayout(self.gridlayout)

        # IMG
        img = QPixmap(f":/icons/{img_type}.svg").scaled(50, 50)
        self.paint(img, "#F8F8FF")  # paint the svg to ghost white
        self.img_label = QLabel(self)
        self.img_label.setPixmap(img)
        self.img_label.setGeometry(38, 21, 50, 50)

    def draw_pie_chart_of_selected_customer(self, name:str, percent: float)->None:
        if(not self.gridlayout.isEmpty()):
            self.series.clear()
            self.chart.removeAllSeries()
        self.series = QPieSeries()
        slice = QPieSlice(name, percent)
        slice.setBrush(QColor("#2ACAB0"))
        slice.setBorderColor("black")
        slice.setBorderWidth(5)
        self.series.append(slice)
        slice2 = QPieSlice("Blank", 100-percent)
        slice2.setBrush(QColor("#FF7474"))
        slice2.setBorderColor("black")
        slice2.setBorderWidth(5)
        self.series.append(slice2)
        self.chart.addSeries(self.series)
        self.gridlayout.addWidget(self.chartview)

    def set_quarter_label(self, quarter: str):
        return self.quarter_label.setText(quarter)

    def set_total_show_label(self, total:int):
        return self.total_show_label.setText("$"+total)

    def set_monthly_show_label(self, monthly:int):
        return self.monthly_show_label.setText("$"+monthly)

    def set_capacity_show_label(self, capacity:int):
        return self.total_show_label.setText(capacity+"%")

    # Set Button Listeners

    def set_back_button_listener(self, function):
        self.back_button.clicked.connect(function)

    def set_next_button_listener(self, function):
        self.next_button.clicked.connect(function)

    def set_export_button_listener(self, function):
        self.export_button.clicked.connect(function)

    #Report card
    def add_report_card(self, customer: Customer, percent: int):
        """Inserts a new CustomerCardItem object to the list given an Customer object"""
        card = ReportCardItem(self, customer, percent)
        self.scrollArea_widget.layout().addWidget(card)

    def clear_employee_list(self):
        """Clears the list represented in the scrollarea"""
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)