# Qutebrowser Configuration

A custom Qutebrowser setup with a custom startpage, site‑specific CSS tweaks, adblocking, and vertical tabs.

## Files

Place all files in `~/.config/qutebrowser/`:

- `config.py` – main configuration
- `startpage/index.html` – startpage HTML (create the `startpage` directory)
- `styles/youtube-tweaks.css` – YouTube styling
- `styles/ddg.css` – DuckDuckGo styling
- `styles/archwiki.css` – ArchWiki styling

The configuration references these CSS files via `~/.config/qutebrowser/styles/...`. Adjust the paths if you place them elsewhere.

## Important: Startpage Path

In `config.py`, the startpage is set to:
c.url.start_pages = ['file:///home/USERNAME/.config/qutebrowser/startpage/index.html']
c.url.default_page = 'file:///home/USERNAME/.config/qutebrowser/startpage/index.html'

Replace `USERNAME` with your actual username.

## Features

- Vertical tabs on the left (toggle with `tT`).
- Dark theme with custom colors for statusbar, tabs, completion, hints.
- Adblocking using uBlock Origin filter lists (fetched from GitHub).(doesnt really work im sorry)
- Dark mode enabled for web content (except local files).
- Custom search engines: DuckDuckGo default, ArchWiki, Arch packages, GitHub, YouTube.
- Keybindings for quick commands: `=` (open URL), `h` (history), `cc` (copy image link to clipboard), etc.
- Local startpage with a search box and quick links.

## Dependencies

- `qutebrowser` – the browser itself.
- `ttf-jetbrains-mono` – font used in the interface (optional; change `c.fonts.default_family` if you want a different font).
- Internet connection for adblock list downloads (they are fetched on startup).

## Installation

1. Create the directories if they don’t exist:
mkdir -p ~/.config/qutebrowser/startpage ~/.config/qutebrowser/styles
3. Place `config.py` in `~/.config/qutebrowser/`.
4. Place `index.html` in `~/.config/qutebrowser/startpage/`.
5. Place the three CSS files (`youtube-tweaks.css`, `ddg.css`, `archwiki.css`) in `~/.config/qutebrowser/styles/`.
6. Edit `config.py` and replace `USERNAME` with your username in the startpage URLs.
7. Launch qutebrowser.

## Notes

- Dark mode is enabled via Qutebrowser’s built‑in `darkmode` for all sites except local files (`file://*`).
