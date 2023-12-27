from typing import List

from aqt.qt import *
from aqt.utils import openLink
from aqt.theme import theme_manager

from .ankiaddonconfig import ConfigManager, ConfigWindow, ConfigLayout
from .colors import recolor_python

conf = ConfigManager()


def header_layout(conf_window: ConfigWindow) -> QHBoxLayout:
    icons_layout = QHBoxLayout()
    icons_layout.addStretch()
    images = [
        ("AnKingSmall.png", (31, 31), "www.ankingmed.com"),
        ("YouTube.png", (31, 31), "www.youtube.com/theanking"),
        ("Patreon.png", (221, 31), "www.patreon.com/ankingmed"),
        ("Instagram.png", (31, 31), "instagram.com/ankingmed"),
        ("Facebook.png", (31, 31), "facebook.com/ankingmed"),
    ]
    for image in images:
        icon = QIcon()
        icon.addPixmap(QPixmap(f":/ReColor/{image[0]}"), QIcon.Normal, QIcon.Off)
        button = QToolButton(conf_window)
        button.setIcon(icon)
        button.setIconSize(QSize(*image[1]))
        button.setMaximumSize(QSize(*image[1]))
        button.setMinimumSize(QSize(*image[1]))
        button.clicked.connect(lambda _, url=image[2]: open_web(url))
        button.setCursor(QCursor(Qt.PointingHandCursor))
        button.setStyleSheet("QToolButton { border: none; }")
        icons_layout.addWidget(button)
    icons_layout.addStretch()
    return icons_layout


def on_save() -> None:
    conf.save()
    recolor_python()


def with_window(conf_window: ConfigWindow) -> None:
    conf_window.setWindowTitle("ReColor Settings")
    conf_window.setMinimumWidth(500)
    conf_window.execute_on_save(on_save)
    conf_window.main_layout.insertLayout(0, header_layout(conf_window))
    conf_window.main_layout.insertSpacing(1, 10)


def color_idx() -> int:
    return 2 if theme_manager.night_mode else 1


def populate_tab(tab: ConfigLayout, conf_keys: List[str]) -> None:
    for conf_key in conf_keys:
        description = conf.get(f"colors.{conf_key}.0")
        tab.color_input(f"colors.{conf_key}.{color_idx()}", description)
    tab.stretch()


def general_tab(conf_window: ConfigWindow) -> None:
    conf_keys = [
        "TEXT_FG",
        "WINDOW_BG",
        "FRAME_BG",
        "BUTTON_BG",
        "BORDER",
        "MEDIUM_BORDER",
        "FAINT_BORDER",
        "HIGHLIGHT_BG",
        "HIGHLIGHT_FG",
        "LINK",
        "DISABLED",
    ]
    tab = conf_window.add_tab("General")
    populate_tab(tab, conf_keys)


def decks_tab(conf_window: ConfigWindow) -> None:
    conf_keys = [
        "CURRENT_DECK",
        "NEW_COUNT",
        "LEARN_COUNT",
        "REVIEW_COUNT",
        "ZERO_COUNT",
    ]
    tab = conf_window.add_tab("Decks")
    populate_tab(tab, conf_keys)


def browse_sidebar_tab(conf_window: ConfigWindow) -> None:
    conf_keys = [
        "BURIED_FG",
        "SUSPENDED_FG",
        "FLAG1_FG",
        "FLAG2_FG",
        "FLAG3_FG",
        "FLAG4_FG",
        "FLAG5_FG",
        "FLAG6_FG",
        "FLAG7_FG",
    ]
    tab = conf_window.add_tab("Browse Sidebar")
    populate_tab(tab, conf_keys)


def browse_cards_list_tab(conf_window: ConfigWindow) -> None:
    conf_keys = [
        "SLIGHTLY_GREY_TEXT",
        "HIGHLIGHT_BG",
        "HIGHLIGHT_FG",
        "SUSPENDED_BG",
        "MARKED_BG",
        "FLAG1_BG",
        "FLAG2_BG",
        "FLAG3_BG",
        "FLAG4_BG",
        "FLAG5_BG",
        "FLAG6_BG",
        "FLAG7_BG",
    ]
    tab = conf_window.add_tab("Browse Cards List")
    populate_tab(tab, conf_keys)


def open_web(url: str) -> None:
    openLink(f"https://{url}")


conf.use_custom_window()
conf.on_window_open(with_window)
conf.add_config_tab(general_tab)
conf.add_config_tab(decks_tab)
conf.add_config_tab(browse_sidebar_tab)
conf.add_config_tab(browse_cards_list_tab)
