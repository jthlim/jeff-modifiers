# Jeff's Modifiers Dictionary for Plover

## Features

* Uses a single suffix to handle control, shift, alt, super for letters and navigation.
* Letters, navigation, numbers, function keys and other keys can be entered.
* Single-key up/down/left/right simplifies cursor movement.

This dictionary is activated by using `-TZ`:
```
 πππΏπ·βπΎβπ΅πΏπ»ππ³
 ππΊππβπΎβππ±πΆππ
 γγγπ°πΎβπ΄π
```

# Control keys

* `-F`: Control
* `-R`: Shift
* `-P`: Super (Windows Key/Command Key)
* `-B`: Alt

```
 πππΏπ·βπΎβπ΅πΏπ»ππ³
 ππΊππβπΎβππ±πΆππ
 γγγπ°πΎβπ΄π
```

These can be combined with finger-spelling characters:

For example, to type Command-C, stroke `KR-PTZ`
```
 πππΏπ·βπΎβπ΅πΏπ»ππ³
 ππΊππβπΎβππ±πΆππ
 γγγπ°πΎβπ΄π
```

# Navigation and delete

Navigation and delete use the `TKPWHR` block with `-LTZ`

```
 πππΏπ·βπΎβπ΅πΏπ»ππ³
 ππΊππβπΎβππ±πΆππ
 γγγπ°πΎβπ΄π
```

| Key       | Stroke         |
| --------- | -------------- |
| Up        | `ππΏπ·`<br>`πΊππ` |
| Down      | `ππΏπ·`<br>`πΊππ` |
| Left      | `ππΏπ·`<br>`πΊππ` |
| Right     | `ππΏπ·`<br>`πΊππ` |
| Page Up   | `ππΏπ·`<br>`πΊππ` |
| Page Down | `ππΏπ·`<br>`πΊππ` |
| Home      | `ππΏπ·`<br>`πΊππ` |
| End       | `ππΏπ·`<br>`πΊππ` |
| Backspace | `ππΏπ·`<br>`πΊππ` |
| Delete    | `ππΏπ·`<br>`πΊππ` |
 
# Other keys

Other keys use the `TKPWHR` block with `ULTZ`
```
 πππΏπ·βπΎβπ΅πΏπ»ππ³
 ππΊππβπΎβππ±πΆππ
 γγγπ°πΎβπ΄π
```

| Key                  | Stroke         |
| -------------------- | -------------- |
| Escape               | `ππΏπ·`<br>`πΊππ` |
| Tab                  | `ππΏπ·`<br>`πΊππ` |
| Apostrophe           | `ππΏπ·`<br>`πΊππ` |
| Backtick             | `ππΏπ·`<br>`πΊππ` |
| Period               | `ππΏπ·`<br>`πΊππ` |
| Comma                | `ππΏπ·`<br>`πΊππ` |
| Semicolon            | `ππΏπ·`<br>`πΊππ` |
| Equal                | `ππΏπ·`<br>`πΊππ` |
| Minus (Hyphen)       | `ππΏπ·`<br>`πΊππ` |
| Space                | `ππΏπ·`<br>`πΊππ` |
| Slash (/)            | `ππΏπ·`<br>`πΊππ` |
| Backslash (\)        | `ππΏπ·`<br>`πΊππ` |
| Left Square Bracket  | `ππΏπ·`<br>`πΊππ` |
| Right Square Bracket | `ππΏπ·`<br>`πΊππ` |
| Return               | `ππΏπ·`<br>`πΊππ` |

# Numbers and Function keys

Numbers and function keys use the `STKPWR` block with `EULTZ`

```
πππΏπ·βπΎβπ΅πΏπ»ππ³
ππΊππβπΎβππ±πΆππ
γγγπ°πΎβπ΄π
```

Numbers are formed using binary:
* `S-`: 8
* `K-`: 4
* `W-`: 2
* `R-`: 1

To press a NumPad key, add in `P-`, to use a function key, add in `TP-`.

Example: To press Command-Shift-F2, stroke: `TPWEUFRLTZ`
```
πππΏπ·βπΎβπ΅πΏπ»ππ³
ππΊππβπΎβππ±πΆππ
γγγπ°πΎβπ΄π
```

For Shift-NumPad-2, stroke: `PWEURLTZ`
```
πππΏπ·βπΎβπ΅πΏπ»ππ³
ππΊππβπΎβππ±πΆππ
γγγπ°πΎβπ΄π
```

## Binary chart

| Number | Stroke |
| ------ | ------ |
| 1      | `ππΊππ` |
| 2      | `ππΊππ` |
| 3      | `ππΊππ` |
| 4      | `ππΊππ` |
| 5      | `ππΊππ` |
| 6      | `ππΊππ` |
| 7      | `ππΊππ` |
| 8      | `ππΊππ` |
| 9      | `ππΊππ` |
| 10     | `ππΊππ` |
| 11     | `ππΊππ` |
| 12     | `ππΊππ` |
| 13     | `ππΊππ` |
| 14     | `ππΊππ` |
| 15     | `ππΊππ` |

Example: To press Alt-F12, stroke: `STKPEUBLTZ`
```
πππΏπ·βπΎβπ΅πΏπ»ππ³
ππΊππβπΎβππ±πΆππ
γγγπ°πΎβπ΄π
```

# Installation

1. In plover, first install plover-python-dictionary
2. Save jeff-modifiers.py from this repository
3. Drag and drop the file into plover

Diagrams created with [jeff-visual-stroke](https://github.com/jthlim/jeff-visual-stroke) dictionary.

You may also be interested in [jeff-numbers](https://github.com/jthlim/jeff-numbers)
You may also be interested in:
* [jeff-numbers](https://github.com/jthlim/jeff-numbers)
* [jeff-phrasing](https://github.com/jthlim/jeff-phrasing)
* [jeff-visual-stroke](https://github.com/jthlim/jeff-visual-stroke)
