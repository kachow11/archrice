vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.wrap = false
vim.opt.tabstop = 4
vim.opt.swapfile = false
vim.opt.signcolumn = "yes"
vim.opt.winborder = "rounded"
vim.opt.termguicolors = true
vim.g.mapleader = " "

local servers = { "clangd", "lua_ls", "pyright", "bashls", "pylsp" }


vim.keymap.set('n', '<leader>o', ':update<CR> :source<CR>')
vim.keymap.set('n', '<leader>w', ':write<CR>')
vim.keymap.set('n', '<leader>q', ':quit<CR>')
vim.keymap.set('n', '<leader>e', ':Oil<CR>')
vim.keymap.set('n', '<leader>f', ':FZF<CR>')
--vim.keymap.set('n', '<leader>g', ':Pick grep_live<CR>')
vim.keymap.set('n', '<leader>lf', vim.lsp.buf.format)


vim.pack.add({
	{ src = "https://github.com/neovim/nvim-lspconfig" },
	{ src = "https://github.com/brenoprata10/nvim-highlight-colors" },
	{ src = "https://github.com/slugbyte/lackluster.nvim" },
	{ src = "https://github.com/nvim-mini/mini.nvim" },
	{ src = "https://github.com/stevearc/oil.nvim" },
	{ src = "https://github.com/saghen/blink.lib" },
	{ src = "https://github.com/saghen/blink.cmp" },
})

--lsp
for _, server in ipairs(servers) do
	vim.lsp.enable(server)
end
-- colorscheme
vim.cmd("colorscheme lackluster-mint")
-- color highlight
require('nvim-highlight-colors').setup({})
-- mini
require('mini.statusline').setup()
require('mini.icons').setup()
require('mini.starter').setup()
require('mini.pairs').setup()
---- blink
require('blink.cmp').setup({
	fuzzy = { implementation = "prefer_rust" }
})
-- oil
require('oil').setup({
	columns = {
		"permissions",
		"icon"
	},
	view_options = {
		show_hidden = true
	}
})


-----------------------
--pack clean function--
-----------------------
local function pack_clean()
	local active_plugins = {}
	local unused_plugins = {}

	for _, plugin in ipairs(vim.pack.get()) do
		active_plugins[plugin.spec.name] = plugin.active
	end

	for _, plugin in ipairs(vim.pack.get()) do
		if not active_plugins[plugin.spec.name] then
			table.insert(unused_plugins, plugin.spec.name)
		end
	end

	if #unused_plugins == 0 then
		print("no unused plugins.")
		return
	end

	local choice = vim.fn.confirm("Remove unused plugins?", "&yes\n&no", 2)
	if choice == 1 then
		vim.pack.del(unused_plugins)
	end
end

--pack clean
vim.keymap.set('n', '<leader>pc', pack_clean)

vim.diagnostic.config({
	underline = false,
})
