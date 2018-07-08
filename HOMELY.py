from homely.files import mkdir, symlink
from homely.pipinstall import pipinstall

pipinstall("ranger")
pipinstall("pipenv")
pipinstall("raiseorlaunch")

mkdir("~/.config")

mkdir("~/.local/bin")
symlink("~/.local/bin", "~/bin")

symlink(".bashrc")
symlink(".bashrc.d")

symlink(".config/i3", "~/.config/i3")
symlink(".config/i3status", "~/.config/i3status")
symlink(".conkyrc")

symlink(".inputrc")
symlink(".profile")
symlink(".profile", "~/.bash_profile")
