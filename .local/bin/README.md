# Scripts

A collection of simple shell scripts for daily tasks on my Wayland setup with `dwl` and `wmenu`.

## Scripts

### note.sh
- **Purpose** – Create and edit notes in `~/notes/`. Lists existing notes, prompts with `wmenu` to select or type a new name, then opens the file with `nvim`.
- **Dependencies** – `wmenu`, `foot`, `nvim` (or adjust `EDITOR_CMD`).

### powermenu.sh
- **Purpose** – System power menu with sub‑menus for killing processes.
  - Main options: Shutdown, Reboot, Suspend, Logout, Lock, Kill (select a process by PID), Killall (kill all instances of a process name).
  - Uses `waylock` for locking.
- **Dependencies** – `wmenu`, `waylock`, `systemctl` (or `zzz` for suspend on non‑systemd), `ps`, `kill`, `killall`.

### screenshot.sh
- **Purpose** – Interactive region screenshot with `grim` and `slurp`. Saves to `~/Pictures/screenshots/` with a timestamp. Sends a notification via `mako` on success or failure.
- **Dependencies** – `grim`, `slurp`, `libnotify` (notify-send).

### startdwl.sh
- **Purpose** – Launches the `dwl` Wayland compositor with:
  - `slstatus` status bar.
  - Two monitors configured via `wlr-randr`.
  - `swaybg` with a wallpaper.
  - `mako` notification daemon.
- **Dependencies** – `dwl`, `slstatus`, `wlr-randr`, `swaybg`, `mako`.

### volume.sh
- **Purpose** – Control volume and show a notification bar.
  - Usage: `volume.sh up|down|mute`.
  - Displays a progress bar using Pango markup (filled `━`, empty `─`) in the notification.
- **Dependencies** – `pactl` (PulseAudio), `notify-send`.

