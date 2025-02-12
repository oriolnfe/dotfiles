# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

mod = "mod4"

groups = [Group(i) for i in [
    "term", "browser", "code", "media", "misc"
]]

for i, group in enumerate(groups):
    deskNum = str(i+1)
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                deskNum,
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                deskNum,
                lazy.window.togroup(group.name, switch_group=True),
                desc=f"Switch to & move focused window to group {group.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )