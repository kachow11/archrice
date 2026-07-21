# Terminal Configuration (foot)

This is a configuration file for the `foot` terminal emulator, a lightweight Wayland‑native terminal.

## Features

- **Font** – JetBrains Mono Nerd Font, size 14.
- **Padding** – 4 pixels on all sides (`pad=4x4`).
- **Alpha** – fully opaque (`alpha=1`). Adjust if you want transparency.

## Installation

Place this configuration as `~/.config/foot/foot.ini`.  
Foot will load it automatically on next start.

## Dependencies

- `foot` – the terminal emulator itself (Wayland only).
- `ttf-jetbrains-mono` – a Nerd Font variant of JetBrains Mono.  
  If you use a different font, change the `font` line accordingly.

## Notes

- This config is for Wayland; foot does not support X11.
