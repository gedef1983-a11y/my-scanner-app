[app]
title = WarehouseScanner
package.name = scannerapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,requests,pyjnius,sqlite3

orientation = portrait
fullscreen = 0
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

android.api = 33
android.minapi = 26
android.ndk_api = 26
android.arch_arm64_v8a = True
android.allow_backup = True

# Оставляем пустым, чтобы Buildozer сам скачал нужные версии в свою папку
android.sdk_path = 
android.ndk_path = 
android.build_tools_version = 

[buildozer]
log_level = 2
warn_on_root = 1
