from .gui import init_preferences, init_deckconf
from .lib import init_review_hook, init_sync_hook
from .deckoptions import init_deckoptions

def init():
    init_preferences()
    init_deckconf()
    init_review_hook()
    init_sync_hook()
    init_deckoptions()
