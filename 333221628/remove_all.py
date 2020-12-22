# -*- coding: utf-8 -*-
# License AGPLv3
  
from bs4 import BeautifulSoup

from anki.lang import _
from anki.hooks import addHook, wrap
from anki.utils import json
from aqt.editor import Editor
from aqt import mw


def load_config(conf):
    global config
    config=conf
load_config(mw.addonManager.getConfig(__name__))
mw.addonManager.setConfigUpdatedAction(__name__,load_config) 


def myRemoveAll(self):
    selected = self.web.selectedText()
    out=BeautifulSoup(selected,features="html.parser").getText()
    out=out.replace('StartFragment','').replace('EndFragment','')
    self.web.eval("document.execCommand('inserthtml', false, %s);"  % json.dumps(out))
Editor.myRemoveAll = myRemoveAll


if config.get("overwrite_built_in_removeFormat",False):
    Editor.removeFormat = myRemoveAll


def add_to_context(view, menu):
    a = menu.addAction(_("Full Clear"))
    a.triggered.connect(lambda _,e=view.editor: myRemoveAll(e))
if config.get("show_in_contextmenu",False):
    addHook("EditorWebView.contextMenuEvent", add_to_context)


def onSetupShortcuts21(cuts, editor):
    added_shortcuts = [
        (config.get("shortcut"),
            lambda: editor.myRemoveAll()),
    ]
    cuts.extend(added_shortcuts)

if config.get("shortcut",False):
    addHook("setupEditorShortcuts", onSetupShortcuts21)