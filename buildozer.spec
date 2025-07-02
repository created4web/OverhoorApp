[app]
title = VraagApp
package.name = vraagapp
package.domain = org.example
source.dir = .
source.include_exts = py,txt
version = 1.0
requirements = python3,kivy,gtts,playsound,keyboard
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
permissions = INTERNET
