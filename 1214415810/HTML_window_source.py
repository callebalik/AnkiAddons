# -*- mode: Python ; coding: utf-8 -*-
# ' View HTML source with JavaScript and CSS styles
# https://ankiweb.net/shared/info/
# -- tested with Anki 2.0.36 .. 2.0.51 under Windows 7 SP1
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Copyright (c) 2016-2018 Dmitry Mikheev,
# No support. Use it AS IS on your own risk.
"""
- - -
 Просмотр исходного кода HTML карточки со стилями и скриптами
 Проверено в версиях 2.0.36 .44 .51 под Windows 7
 Без поддержки. Используйте на свой страх и риск.

 В меню главного окна Anki появится новый пункт Карточки:

 Показать Верхний Исходник
  для фрейма Колоды Добавить Обзор
 Показать Нижний Исходник
  для любого нижнего фрейма
 Показать Исходник HTML
  для любого центрального фрейма
  покажет весь его исходный код (вместе с jQuery 1.5)
 Показать Исходник HTML Body
  для любого центрального фрейма (прежде всего для карточек)
  покажет только суть (без jQuery 1.5)

 Кнопка 'Закрыть' в правом нижнем углу окна
 запомнит размеры и положение окна на экране
 для каждого профиля отдельно.

 Нажмите 'Esc' на клавиатуре
 или кликните по 'x' в правом верхнем углу окна
 для выхода без сохранения текущего размера и положения окна.
 (последние сохраненные значения будут использоваться при следующем запуске)
"""


import os
import sys

import anki
import aqt
from anki.lang import _
from aqt.qt import *

HOTKEY = {      # in aqt.mw Main Window (deckBrowser, Overview, Reviewer)
    'HTML_source': 'Ctrl+F3',
    'Body_source': 'Alt+F3',
}

# Get language class
# import anki.lang
lang = anki.lang.currentLang

MSG = {
    'en': {
        'Cards': _('&Cards'),
        'no_jQuery': _('View Source code &Body'),
        'view_source': _('&View Source code'),
        'toolbarWeb': _('View toolbar Source'),
        'bottomWeb': _('View bottomWeb Source'),
    },
    'ru': {
        'Cards': '&Карточки',
        'no_jQuery': 'Показать Ис&ходник HTML Body',
        'view_source': 'Показать И&сходник HTML',
        'toolbarWeb': 'Показать Верхний Исходник',
        'bottomWeb': 'Показать Нижний Исходник',
    },
}

try:
    MSG[lang]
except KeyError:
    lang = 'en'

# 'Показать Ис&ходник HTML Body' if lang == 'ru' else 'View Source code &Body'
# 'Показать И&сходник HTML' if lang == 'ru' else '&View Source code'

try:
    aqt.mw.addon_cards_menu
except AttributeError:
    aqt.mw.addon_cards_menu = QMenu(MSG[lang]['Cards'], aqt.mw)
    aqt.mw.form.menubar.insertMenu(
        aqt.mw.form.menuTools.menuAction(), aqt.mw.addon_cards_menu)


def _showSourceHTML(html):
    """To look at sourcne HTML+CSS code."""
    aqt.utils.showText(html, geomKey="ViewHTML")


def _getSourceHTML(mWeb):
    """To look at sourcne HTML+CSS code."""
    mWeb.evalWithCallback("""
        (function(){
             return document.documentElement.outerHTML
         }())
    """, _showSourceHTML)


get_HTML_Source_action = QAction(aqt.mw)
get_HTML_Source_action.setText(MSG[lang]['view_source'])
get_HTML_Source_action.setShortcut(
    QKeySequence(HOTKEY['HTML_source']))
get_HTML_Source_action.triggered.connect(lambda: _getSourceHTML(aqt.mw.web))

get_Top_Source_action = QAction(aqt.mw)
get_Top_Source_action.setText(MSG[lang]['toolbarWeb'])
get_Top_Source_action.triggered.connect(
    lambda: _getSourceHTML(aqt.mw.toolbar.web))

get_Bottom_Source_action = QAction(aqt.mw)
get_Bottom_Source_action.setText(MSG[lang]['bottomWeb'])
get_Bottom_Source_action.triggered.connect(
    lambda: _getSourceHTML(aqt.mw.bottomWeb))

# -- these work perfectly well
# aqt.mw.toolbar.web.hide()
# aqt.mw.toolbar.web.setFixedHeight(50)

if hasattr(aqt.mw, 'addon_cards_menu'):
    aqt.mw.addon_cards_menu.addSeparator()
    aqt.mw.addon_cards_menu.addAction(get_Top_Source_action)
    aqt.mw.addon_cards_menu.addAction(get_HTML_Source_action)
    aqt.mw.addon_cards_menu.addAction(get_Bottom_Source_action)
    aqt.mw.addon_cards_menu.addSeparator()
