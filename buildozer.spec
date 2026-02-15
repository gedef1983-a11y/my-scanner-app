[app]
title = WarehouseScanner
package.name = scannerapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,requests,pyjnius
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.arch_arm64_v8a = True
