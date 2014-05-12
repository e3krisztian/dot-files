# ~/.bashrc: executed by bash(1) for non-login shells.

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

for script in ~/.bashrc.d/*
do
    [ -x "$script" ] && . "$script"
done
unset script
