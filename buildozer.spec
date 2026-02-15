[app]
title = WarehouseScanner
package.name = scannerapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Основные зависимости
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,requests,pyjnius,sqlite3

orientation = portrait
fullscreen = 0
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

# Версии SDK и NDK (проверенная связка)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = 
android.ndk_api = 21
android.arch_arm64_v8a = True
android.allow_backup = True

# Настройки сборки
python_for_android.branch = master
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
