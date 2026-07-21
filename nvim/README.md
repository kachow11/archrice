# Neovim Configuration

This is a minimal and super based one file Neovim configuration built using the built‑in `vim.pack` plugin manager.

## Features

- **Line numbers** – absolute and relative.
- **No line wrapping**, 4‑space tabs, no swap files.
- **Sign column** always visible, rounded window borders, truecolor support.
- **LSP** enabled for C/C++ (clangd), Lua (lua_ls), Python (pyright and pylsp), and Bash (bashls).
- **File explorer** – Oil.nvim (`<leader>e`).
- **Fuzzy finder** – FZF (`<leader>f`). Requires `fzf` and `fzf.vim` (not managed by this config).
- **Formatting** – LSP‑based formatting (`<leader>lf`).
- **Plugin management** – `vim.pack` adds and updates plugins automatically.  
  A custom mapping (`<leader>pc`) removes unused plugins interactively.
- **Statusline, icons, starter screen, and auto‑pairing** via `mini.nvim`.
- **Inline color previews** – `nvim-highlight-colors`.
- **Colorscheme** – `lackluster-mint`.

## Keybindings

| Mapping | Action |
|---------|--------|
| `<leader>` | Space |
| `<leader>o` | Update and source the current config file |
| `<leader>w` | Write current buffer |
| `<leader>q` | Quit current window |
| `<leader>e` | Open Oil |
| `<leader>f` | Open FZF fuzzy finder |
| `<leader>lf` | Format buffer with LSP |
| `<leader>pc` | Check and remove unused plugins |

## Installed Plugins

All plugins are fetched from their Git repositories using `vim.pack.add`:

- [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) – LSP client configuration.
- [nvim-highlight-colors](https://github.com/brenoprata10/nvim-highlight-colors) – show color codes inline.
- [lackluster.nvim](https://github.com/slugbyte/lackluster.nvim) – colorscheme.
- [mini.nvim](https://github.com/nvim-mini/mini.nvim) – statusline, icons, starter, and pairs.
- [oil.nvim](https://github.com/stevearc/oil.nvim) – file explorer.
- [blink.lib](https://github.com/saghen/blink.lib) – dependency for blink.cmp.
- [blink.cmp](https://github.com/saghen/blink.cmp) – completion plugin (Rust‑based fuzzy implementation).

## Dependencies

### Neovim

- **Neovim >= 0.11** (required for `vim.pack`).  
  Using an older version will break plugin management.

### LSP Servers (must be installed separately)

Install these via your system package manager or language‑specific tools:

- `clangd` – for C/C++.
- `lua-language-server` – for Lua.
- `pyright` – Python (type checking and language server).
- `bash-language-server` – for Bash.
- `python-language-server` – Python (alternative LSP).  

## Installation

Place the configuration file as `~/.config/nvim/init.lua` (or `~/.config/nvim/lua/user/init.lua`). The first time you start Neovim, `vim.pack` will download and install all listed plugins automatically.

## Notes

- The `pack_clean` function removes plugins that are no longer listed in the `vim.pack.add` block. Use `<leader>pc` to invoke it.
- Diagnostic underlining is disabled (`underline = false`); you can adjust this in the `vim.diagnostic.config` call.
