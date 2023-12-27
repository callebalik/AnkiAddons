from typing import NamedTuple, Optional, Any
import math

from aqt import mw, gui_hooks
from aqt.webview import WebContent
from aqt.deckbrowser import DeckBrowser
from aqt.qt import QTimer

from .ankiaddonconfig import ConfigManager
from .ankiaddonconfig import *
from .calculate import (
    Goal,
    get_new_cards_count,
    get_study_days,
)


class Texts(NamedTuple):
    cards_left_in_days: str
    study_new_per: str

    @classmethod
    def from_goal(cls, goal: Goal) -> "Texts":
        study_days = get_study_days(goal)
        new_cards_cnt = get_new_cards_count(goal.query)
        # math.ceil, math.floor is set up to study more earlier.
        new_per_day = new_cards_cnt / study_days
        new_per_week = new_per_day * goal.days_per_week
        new_per_day = math.ceil(new_per_day)
        new_per_week = math.ceil(new_per_week)

        return cls(
            cards_left_in_days=f"You need to study <b>{new_cards_cnt}</b> new cards in <b>{study_days}</b> days",
            study_new_per=f"Study <b>{new_per_day}</b> new cards each day, <b>{new_per_week}</b> each week",
        )


def insert_html(web_content: WebContent, context: Optional[Any]) -> None:
    if not isinstance(context, DeckBrowser):
        return
    try:
        conf = ConfigManager()
        for item in conf.get("goals"):
            goal = Goal(**item)
            if not goal.show_on_main:
                continue
            texts = Texts.from_goal(goal)

            def format_text(text: str) -> str:
                return f"<div style='text-align: center;'>{text}</div>"

            web_content.body += "<br>"
            web_content.body += format_text(f"<b>{goal.name}</b>")
            web_content.body += format_text(texts.cards_left_in_days)
            web_content.body += format_text(texts.study_new_per)
    except Exception as e:
        # This makes sure the browser renders correctly when an exception is raised
        # The hook is removed when exception occurs, so is not triggered again.
        QTimer.singleShot(50, lambda: mw.moveToState("deckBrowser"))
        raise e


gui_hooks.webview_will_set_content.append(insert_html)  # anki v2.1.22
