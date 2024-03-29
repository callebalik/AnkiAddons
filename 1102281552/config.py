from aqt import mw

userOption = None


def _getUserOption(refresh):
    global userOption
    if userOption is None or refresh:
        userOption = mw.addonManager.getConfig(__name__)


def getUserOption(key=None, default=None, refresh=False):
    _getUserOption(refresh)
    if key is None:
        return userOption
    if key in userOption:
        return userOption[key]
    else:
        return default


def getDefaultConfig():
    addon = __name__.split(".")[0]
    return mw.addonManager.addonConfigDefaults(addon)


def writeConfig():
    mw.addonManager.writeConfig(__name__, userOption)


def update(_):
    global userOption, fromName
    userOption = None
    fromName = None


mw.addonManager.setConfigUpdatedAction(__name__, update)

fromName = None


def getFromName(name):
    global fromName
    if fromName is None:
        fromName = dict()
        for dic in getUserOption("columns"):
            fromName[dic["name"]] = dic
    return fromName.get(name)


def setUserOption(key, value):
    _getUserOption()
    userOption[key] = value
    writeConfig()
