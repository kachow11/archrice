
## Components

- **Neovim** (`~/.config/nvim/init.lua`) – Editor with LSP, `vim.pack`, and lackluster theme.
- **Mako** (`~/.config/mako/config`) – Notification daemon with dark minimal style.
- **Foot** (`~/.config/foot/foot.ini`) – Terminal emulator with custom lackluster palette.
- **Qutebrowser** (`~/.config/qutebrowser/`) – Browser with vertical tabs, adblock, local startpage, and site‑specific CSS.
  - Startpage: `~/.config/qutebrowser/startpage/index.html` (edit the user path to your own).
  - Styles: `styles/youtube-tweaks.css`, `styles/ddg.css`, `styles/archwiki.css`.
- **Scripts** (`~/.local/bin/`) – note, powermenu, screenshot, startdwl, volume and a privacy script.
- **dwl** – Custom compositor config (`config.def.h`, optional `config.mk`, patches).

## Installation

Place each file in its respective directory as noted. For qutebrowser, replace the username in `config.py` startpage paths. Make scripts executable (`chmod +x ~/.local/bin/*`). Build and install dwl from source using the provided config files.

## Dependencies

Refer to each component’s specific README for detailed dependencies. The main packages are: `neovim`, `mako`, `foot`, `ttf-jetbrains-mono-nerd`, `qutebrowser`, `wmenu`, `grim`, `slurp`, `waylock`, `pactl`, `dwl`, `wlr-randr`, `swaybg`, and relevant LSP servers.
