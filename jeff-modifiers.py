# Jeff's Modifier Dictionary
import re

# Trigger ending: -TZ
#
# * `F`: Control
# * `R`: Shift
# * `P`: Super
# * `B`: Alt
#
# Mode selected by AOL keys
# L not pressed:  Fingerspelling
# `L` pressed:  Navigation layer
# `OL` pressed:  Keys layer
# `AOL` pressed: Numbers layer

LONGEST_KEY = 1

STROKE_MAP = {
    # Fingerspelling.
    "A": "a",
    "PW": "b",
    "KR": "c",
    "TK": "d",
    "E": "e",
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "SKWR": "j",
    "K": "k",
    "HR": "l",
    "PH": "m",
    "TPH": "n",
    "O": "o",
    "P": "p",
    "KW": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STKPW": "z",

    # Navigation layer
    "PL": "up",
    "KL": "left",
    "WL": "down",
    "RL": "right",
    "TPHL": "page_up",
    "KWRL": "page_down",
    "TKL": "home",
    "HRL": "end",
    "TL": "backspace",
    "HL": "delete",

    # Keys layer
    "TKOL": "escape",
    "HROL": "tab",
    "HOL": "quoteright",
    "WROL": "space",
    "WHROL": "return",
    "KWHROL": "return",
    "KPOL": "slash",
    "TWOL": "backslash",
    "PHOL": "minus",
    "TKPWOL": "equal",
    "KOL": "period",
    "WOL": "comma",
    "KWOL": "semicolon",
    "POL": " quoteleft",
    "TPHOL": "braceleft",
    "KWROL": "braceright",

    # Number layer
    "AOL": "0",
    "RAOL": "1",
    "WAOL": "2",
    "WRAOL": "3",
    "KAOL": "4",
    "KRAOL": "5",
    "KWAOL": "6",
    "KWRAOL": "7",
    "SAOL": "8",
    "SRAOL": "9",

    "TPRAOL": "F1",
    "TPWAOL": "F2",
    "TPWRAOL": "F3",
    "TKPAOL": "F4",
    "TKPRAOL": "F5",
    "TKPWAOL": "F6",
    "TKPWRAOL": "F7",
    "STPAOL": "F8",
    "STPRAOL": "F9",
    "STPWAOL": "F10",
    "STPWRAOL": "F11",
    "STKPAOL": "F12",
    "STKPRAOL": "F13",
    "STKPWAOL": "F14",
    "STKPWRAOL": "F15",
}

PARTS_MATCHER = re.compile(
    r'(S?T?K?P?W?H?R?)(A?O?)([-*]?)(E?U?)(F?R?P?B?)(L?)TZ')


def lookup(chord):
    if len(chord) != 1:
        raise KeyError

    stroke = chord[0]
    match = PARTS_MATCHER.fullmatch(stroke)
    if not match:
        raise KeyError

    (keys, vowels1, separator, vowels2, modifiers, layer) = match.groups()
    pattern = keys + vowels1 + vowels2 + layer

    result = STROKE_MAP.get(pattern)
    if not result:
        return ' '

    if "F" in modifiers:
        result = "control(%s)" % result
    if "R" in modifiers:
        result = "shift(%s)" % result
    if "P" in modifiers:
        result = "super(%s)" % result
    if "B" in modifiers:
        result = "alt(%s)" % result

    return "{#%s}" % result
