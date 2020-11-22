from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

mod = "mod4"
alt = "mod1"

# in case I mess up configs
modkey = mod

keys = [
    # Screenshot Shortcuts
    Key([], "Print", lazy.spawn("scrot '/home/sansfont/Pictures/screenshots/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'")),
    Key(["control"], "Print", lazy.spawn("/scripts/scrot_s")),

    # [W]eb Browser
    Key([mod], "w", lazy.spawn('brave')),

    # [E]dit config
    Key([mod, "control"], "e", lazy.spawn('kitty -e vim /home/sansfont/.config/qtile/config.py')),

    # [R]anger file browser
    Key([mod], "r", lazy.spawn('kitty -e ranger')),

    # Brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

    # Volume Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle")),

    # Multimedia keys
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause')),
    Key([], "XF86AudioPrev", lazy.spawn('playerctl previous')),
    Key([], "XF86AudioNext", lazy.spawn('playerctl next')),

    # vim directional keys - switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # shift + vim directional keys - move windows
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # mod + shift + space - flip layout
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # mod + i/m - grow or shrink focused window
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # mod + n/o - normalize or maximize
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),

    # mod + enter - spawn terminal
    Key([mod], "Return", lazy.spawn("kitty")),

    # mod + Tab - toggle layouts
    Key([mod], "Tab", lazy.next_layout()),

    # mod + q - kill focused window
    Key([mod], "q", lazy.window.kill()),

    # mod + ctrl + r - restart qtile
    Key([mod, "control"], "r", lazy.restart()),

    # mod + ctrl + q - kill qtile
    Key([mod, "control"], "q", lazy.shutdown()),

    # mod + d - spawn (similar to dmenu)
    Key([mod], "d", lazy.spawncmd()),

    # lock screen with i3lockA (black screen)
    Key([mod, "control"], "l", lazy.spawn('i3lock -d -c #000000')),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(margin=10, border_focus='#a3bf48'),
    layout.Max()
]

widget_defaults = dict(
    font='NotoSans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    this_current_screen_border='a4ab67',
                    borderwidth=2,
                    font='monospace',
                    fontsize=12,
                    disable_drag=True
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.DF(format='💾{uf}{m} | '),
                widget.Mpris2(
                    name='spotify',
                    objname='org.mpris.MediaPlayer2.spotify',
                    display_metadata=['xesam:artist', 'xesam:title'],
                    scroll_chars=None,
                    stop_pause_text=''
                ),
                widget.Volume(emoji=True),
                widget.Volume(),
                widget.TextBox(text='|'),
                widget.Battery(
                    charge_char='🔌',
                    discharge_char='⚡',
                    full_char='🔋',
                    format='{char} {percent:2.0%}',
                    update_interval=5
                ),
                widget.TextBox(text='|'),
                widget.Systray(),
                widget.Clock(format=' %d-%m-%Y %a %H:%M'),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Java wmname fix
wmname = "LG3D"
