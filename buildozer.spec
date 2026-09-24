[app]

title = My Kivy App
package.name = mykivyapp
package.domain = org.example

version = 1.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,wav,mp3

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21
android.ndk = 25b


[buildozer]

log_level = 2
warn_on_root = 1
