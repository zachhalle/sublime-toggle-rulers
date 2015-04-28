# sublime-toggle-rulers

This is a tiny script which allows the user to display rulers at given character marks using a keyboard shortcut.

# Installation

Clone the repository into your Sublime Text packages directory. If you install Sublime normally, this can be done with the following terminal commands on OS X:

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/ToggleRulers.py
git clone https://github.com/zachhalle/sublime-toggle-rulers/
```

Then, open Sublime and go to Sublime Text > Key Bindings - User and add the following

```json
{ 
    	"keys": ["super+shift+r"], "command": "toggle_rulers", 
    	"args": { "rulers": [80] } 
}
```

This will bind the command to the shortcut command-shift-r on OS X, but you can whatever shortcut makes you happy. The rulers displayed can be changed by modifying the rulers list.

Without rulers:
![No rulers](http://i.imgur.com/BcxkKbG.png)

With rulers:
![Yes rulers](http://i.imgur.com/EWOIU2d.png)
