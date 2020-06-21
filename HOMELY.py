from homely.files import mkdir, symlink
# from homely.install import installpkg

mkdir("~/.config")

mkdir("~/.local/bin")
symlink("~/.local/bin", "~/bin")

symlink(".profile")
symlink(".profile", "~/.bash_profile")

symlink(".bashrc")
symlink(".bashrc.d")

# installpkg("i3-wm")
# installpkg("i3lock")
symlink(".config/i3", "~/.config/i3")

# installpkg("i3status")
symlink(".config/i3status", "~/.config/i3status")

# installpkg("keynav")
symlink(".keynavrc")

symlink(".inputrc")
# installpkg("tmux")
symlink(".tmux.conf")
