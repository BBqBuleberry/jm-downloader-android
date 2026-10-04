[app]
title = JM 下载器
package.name = jmdl
package.domain = org.bbq

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,ttc
source.exclude_dirs = tests,bin,.github,.git,.venv

version = 0.1.0

requirements = python3==3.11.9,kivy==2.2.1,plyer,requests,urllib3,chardet,idna,certifi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

p4a.branch = master
p4a.bootstrap = sdl2

log_level = 2
warn_on_root = 1