from aqt import mw
from aqt.qt import *
from aqt.utils import askUser, tooltip

from .ankiaddonconfig import *
from .calculate import (
    Goal,
    parse_excluded_dates,
    parse_date,
    InvalidDateLikeStringError,
)
from .display import Texts
from .gui.anking_widgets import AnkiPalaceLayout

# TODO: Allow changing goal colors!

conf = ConfigManager()


def setup_goals_window(conf_window: ConfigWindow) -> None:
    to_deletes = (
        conf_window.main_tab,
        conf_window.reset_btn,
        conf_window.cancel_btn,
        conf_window.save_btn,
    )
    for to_del in to_deletes:
        to_del.setParent(None)
        to_del.deleteLater()
    close_btn = QPushButton("Close")
    close_btn.setDefault(True)
    close_btn.clicked.connect(conf_window.close)
    conf_window.btn_layout.addWidget(close_btn)
    conf_window.main_layout.setContentsMargins(0, 0, 0, 0)

    layout = conf_window.main_layout.vscroll_layout(always=True)
    conf_window.main_layout.hseparator()
    conf_window.widget_updates.append(
        lambda l=layout: setup_goals_list(l)  # type: ignore
    )


def setup_goals_list(scroll_layout: ConfigLayout) -> None:
    if scroll_layout.count():
        container = scroll_layout.takeAt(0).widget()
        container.setParent(None)
        container.deleteLater()

    goals = conf.get("goals")
    layout = scroll_layout.vcontainer()

    for idx, item in enumerate(goals):
        goal = Goal(**item)
        display_goal_item(layout, goal, idx)

    layout.space(5)
    new_btn = QPushButton("New Goal")
    new_btn.clicked.connect(create_new_goal)
    new_btn_lay = layout.hlayout()
    new_btn_lay.addWidget(new_btn)
    new_btn_lay.stretch()

    layout.space(30)
    ankipalacewidget = QWidget()
    AnkiPalaceLayout(ankipalacewidget)
    layout.addWidget(ankipalacewidget)
    layout.stretch(1)


def create_new_goal() -> None:
    example_goal = Goal(
        name="Example",
        query="",
        due="Aug 27 2022",
        days_per_week=7,
        excluded_dates="",
        show_on_main=False,
    )
    goals = conf.get("goals")
    goals.append(example_goal._asdict())
    conf.set("goals", goals)
    conf.save()
    conf.config_window.update_widgets()


def display_goal_item(parent: ConfigLayout, goal: Goal, idx: int) -> ConfigLayout:
    """Renders a goal item in the goals list."""

    texts = Texts.from_goal(goal)

    container = QFrame()
    parent.addWidget(container)
    container.setLineWidth(2)
    container.setFrameShape(QFrame.Box)
    container.setFrameShadow(QFrame.Plain)
    layout = ConfigLayout(parent.config_window, QBoxLayout.TopToBottom)
    container.setLayout(layout)
    upper = layout.hlayout()
    layout.space(8)
    below = layout.vlayout()
    bottom = layout.hlayout()

    upper.text(goal.name, bold=True, size=28)
    upper.stretch()
    upper.text(goal.due)
    # upper.text(goal.due + f" (D-{d_minus})")
    below.text(texts.cards_left_in_days, html=True)

    bottom_left = bottom.vlayout()
    bottom.stretch()
    bottom_right = bottom.vlayout()
    bottom_left.text(texts.study_new_per, html=True)
    bottom_left.stretch()
    bottom_left.space(15)
    bottom_right.stretch()
    bottom_right.text_button(
        "Edit... ", "Edit this goal", on_click=lambda u, i=idx: goal_editor(i)
    )
    return layout


# Goal Editor


def goal_editor(idx: int) -> None:
    goal_window = ConfigWindow(conf)
    setup_goal_editor(goal_window, idx)
    goal_window.setMinimumWidth(500)
    goal_window.setFixedHeight(goal_window.sizeHint().height())
    goal_window.geom_key = "addonconfig-calculate-goaleditor"
    goal_window.setWindowTitle("Edit Goal")
    goal_window.on_open()
    goal_window.exec_()
    conf.config_window.update_widgets()


def setup_goal_editor(goal_window: ConfigWindow, idx: int) -> None:
    to_delete = (goal_window.reset_btn, goal_window.main_tab, goal_window.advanced_btn)
    for obj in to_delete:
        obj.setParent(None)
        obj.deleteLater()

    def on_delete_goal() -> None:
        goal_name = conf.get(f"goals.{idx}.name")
        if askUser(f"Delete goal {goal_name}?"):
            conf.pop(f"goals.{idx}")
            goal_window.on_save()

    delete_btn = QPushButton("Delete")
    delete_btn.setStyleSheet("color: red;")
    delete_btn.pressed.connect(on_delete_goal)
    goal_window.btn_layout.insertWidget(0, delete_btn)

    layout = goal_window.main_layout.vcontainer()
    upper = layout.hlayout()
    upper.text_input(f"goals.{idx}.name", "Name:")
    upper.space(15)
    due = upper.text_input(f"goals.{idx}.due", "Due:")
    due.setPlaceholderText("Eg. Oct 27 2021")
    query = layout.text_input(
        f"goals.{idx}.query", "Query:", tooltip="Query you put in card browser."
    )
    query.setPlaceholderText("Eg. tag:anatomy deck:medical")

    layout.space(20)
    layout.hseparator()
    layout.space(15)

    exclude = layout.text_input(f"goals.{idx}.excluded_dates", "Exclude these dates:")
    exclude.setPlaceholderText("Eg. Oct 27 2021-Dec 27 2021, Jan 1 2022")

    number_lay = layout.hlayout()
    number_lay.text("Study")
    number_lay.number_input(f"goals.{idx}.days_per_week", minimum=1, maximum=7)
    number_lay.text("days / week")
    number_lay.stretch()

    layout.checkbox(f"goals.{idx}.show_on_main", "Show on main screen")

    def should_save() -> bool:
        try:
            parse_date(due.text())
        except InvalidDateLikeStringError as e:
            msg = "Due - " + str(e)
            msg = msg.replace("\n", "<br>")
            tooltip(msg)
            return False
        try:
            parse_excluded_dates(exclude.text())
        except InvalidDateLikeStringError as e:
            msg = "Exclude Dates - " + str(e)
            msg = msg.replace("\n", "<br>")
            tooltip(msg)
            return False
        return True

    def on_close() -> None:
        if mw.state == "deckBrowser":
            mw.deckBrowser.refresh()

    goal_window.should_save_hook.append(should_save)
    goal_window.execute_on_close(on_close)


conf.use_custom_window()
conf.on_window_open(setup_goals_window)
