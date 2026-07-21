# pylint: disable=C0111
import os

os.environ['TZ'] = 'America/New_York'
import qutebrowser.api as qt

# --- Lackluster Palette ---
# Mapping the provided colors to a usable dictionary
p = {
    "main_bg": "#101010",
    "menu_bg": "#191919",
    "popup_bg": "#1A1A1A",
    "status": "#242424",
    "comment": "#3A3A3A",
    "exception": "#505050",
    "keyword": "#666666",
    "param": "#8E8E8E",
    "white": "#202020",
    "lack": "#708090",
    "luster": "#deeeed",
    "orange": "#ffaa88",
    "yellow": "#abab77",
    "green": "#789978",
    "blue": "#7788AA",
    "red": "#D70000",
    "black": "#000000",
    "g1": "#080808",
    "g2": "#191919",
    "g3": "#2a2a2a",
    "g4": "#444444",
    "g5": "#555555",
    "g6": "#7a7a7a",
    "g7": "#aaaaaa",
    "g8": "#cccccc",
    "g9": "#DDDDDD",
}

c = c
config = config

# --- Local Startpage ---
# Use the file:// protocol to point to your local index.html
c.url.start_pages = ['file:///home/zzgeezfoo/.config/qutebrowser/startpage/index.html']
c.url.default_page = 'file:///home/zzgeezfoo/.config/qutebrowser/startpage/index.html'

# --- Adblocker & WebGL ---
c.content.blocking.enabled = True
config.set("content.webgl", False, "*")
c.qt.args = ['disable-gpu']
# --- Tabs (Vertical) ---
c.tabs.position = 'left'
c.tabs.width = '15%'
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 2
c.tabs.show = "multiple"
c.tabs.title.format = "{audio}{current_title}"

# --- Colors ---
# Statusbar
c.colors.statusbar.normal.bg = p["status"]
c.colors.statusbar.command.bg = p["status"]
c.colors.statusbar.command.fg = p["luster"]
c.colors.statusbar.normal.fg = p["luster"]
c.colors.statusbar.passthrough.fg = p["blue"]
c.colors.statusbar.url.fg = p["blue"]
c.colors.statusbar.url.success.https.fg = p["green"]
c.colors.statusbar.url.hover.fg = p["orange"]

# Tabs
c.colors.tabs.even.bg = p["main_bg"]
c.colors.tabs.odd.bg = p["main_bg"]
c.colors.tabs.bar.bg = p["main_bg"]
c.colors.tabs.even.fg = p["g6"]
c.colors.tabs.odd.fg = p["g6"]
c.colors.tabs.selected.even.bg = p["luster"]
c.colors.tabs.selected.odd.bg = p["luster"]
c.colors.tabs.selected.even.fg = p["black"]
c.colors.tabs.selected.odd.fg = p["black"]

# Completion / Menus
c.colors.completion.odd.bg = p["menu_bg"]
c.colors.completion.even.bg = p["menu_bg"]
c.colors.completion.fg = p["luster"]
c.colors.completion.category.bg = p["status"]
c.colors.completion.category.fg = p["luster"]
c.colors.completion.item.selected.bg = p["luster"]
c.colors.completion.item.selected.fg = p["black"]
c.colors.completion.item.selected.match.fg = p["blue"]
c.colors.completion.match.fg = p["blue"]

# Hints
c.colors.hints.bg = p["orange"]
c.colors.hints.fg = p["black"]
c.hints.border = p["orange"]

# Downloads / Messages
c.colors.downloads.bar.bg = p["status"]
c.colors.downloads.start.bg = p["blue"]
c.colors.downloads.stop.bg = p["green"]
c.colors.messages.info.bg = p["status"]
c.colors.messages.info.fg = p["luster"]
c.colors.messages.error.bg = p["red"]
c.colors.messages.error.fg = p["luster"]

# Misc Webpage
c.colors.tooltip.bg = p["popup_bg"]
c.colors.webpage.bg = p["main_bg"]
c.colors.tabs.indicator.start = p["blue"]
c.colors.tabs.indicator.stop = p["green"]

# --- Fonts ---
c.fonts.default_family = ["JetBrains Mono Nerd Font", "JetBrains Mono"]
c.fonts.default_size = '13pt'
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'jetbrainsmono nerd font'
c.fonts.web.size.default = 20

# --- Search Engines ---
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}',
    '!apkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
    '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
    '!yt': 'https://www.youtube.com/results?search_query={}',
}

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']
c.auto_save.session = True

# --- Privacy ---
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "disable-non-proxied-udp")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
c.content.headers.referer = 'same-domain'
c.content.headers.accept_language = 'en-US,en;q=0.9'
c.content.headers.do_not_track = True
config.set("content.notifications.enabled", False)
c.content.blocking.method = 'adblock'


# --- Dark Mode ---
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', False, 'file://*')

# --- Custom CSS Stylesheets ---
c.content.user_stylesheets = [
    '~/.config/qutebrowser/styles/youtube-tweaks.css',
    '~/.config/qutebrowser/styles/archwiki.css',
    '~/.config/qutebrowser/styles/ddg.css',
]


# --- Keybindings ---
config.bind('h', 'history')
config.bind('cs', 'cmd-set-text -s :config-source')
config.bind('T', 'hint links tab')
config.bind('pP', 'open -- {primary}')
config.bind('pp', 'open -- {clipboard}')
config.bind('pt', 'open -t -- {clipboard}')
config.bind('tT', 'config-cycle tabs.position top left')
config.bind('gJ', 'tab-move +')
config.bind('gK', 'tab-move -')
config.bind('gm', 'tab-move')
config.bind('<Ctrl+l>', 'cmd-set-text -s :open')

config.load_autoconfig()
