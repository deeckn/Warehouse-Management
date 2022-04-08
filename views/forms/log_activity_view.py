from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel
from PySide6.QtGui import Qt
from data.data_classes import LogEntry
from views.theme import Theme
import os.path
from views.items.log_item import LogItem


class LogWindowView(QWidget):
    def __init__(self, parent=None) -> None:
        QWidget.__init__(self, parent)
        header_activity_log = QLabel("Activity Log", self)
        header_activity_log.setObjectName("h1")
        header_activity_log.setFont(Theme.POPPINS_BOLD_24)
        header_activity_log.setGeometry(60, 40, 145, 36)

        # UI
        ui_linebreak = QLabel(self)
        ui_linebreak.setObjectName("line_break_top_bottom")
        ui_linebreak.setGeometry(60, 85, 381, 47)

        ui_legend_Date = QLabel("Date", self)
        ui_legend_Time = QLabel("Time", self)
        ui_legend_Event = QLabel("Event", self)

        for legend in (ui_legend_Date, ui_legend_Time, ui_legend_Event):
            legend.setFont(Theme.POPPINS_REGULAR_18)
            legend.setObjectName("legend")

        ui_legend_Date.setGeometry(60, 95, 43, 27)
        ui_legend_Time.setGeometry(165, 95, 44, 27)
        ui_legend_Event.setGeometry(260, 95, 49, 27)

        scroll_area = QScrollArea(self)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(60, 147, 390, 620)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setObjectName("container")
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setSpacing(15)
        self.scroll_area_layout.setContentsMargins(5, 5, 5, 0)
        scroll_area.setWidget(self.scroll_area_widget)
        self.spacer = QSpacerItem(
            0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    def add_log(self, log_entry: LogEntry):
        self.scroll_area_layout.removeItem(self.spacer)
        self.scroll_area_layout.addWidget(LogItem(log_entry))
        self.scroll_area_layout.addItem(self.spacer)

    def clear_logs(self):
        childs = self.scroll_area_widget.children()
        if len(childs) > 1:
            childs = childs[1:]
            for widget in childs:
                widget.close()
