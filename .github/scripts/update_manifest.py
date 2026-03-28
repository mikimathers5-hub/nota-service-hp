#!/usr/bin/env python3
import re

manifest_path = "android/app/src/main/AndroidManifest.xml"

permissions = """    <!-- Permissions untuk Kontak -->
    <uses-permission android:name="android.permission.READ_CONTACTS" />
    <uses-permission android:name="android.permission.WRITE_CONTACTS" />
    <!-- Permissions untuk Bluetooth Printer -->
    <uses-permission android:name="android.permission.BLUETOOTH" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-permission android:name="android.permission.BLUETOOTH_SCAN" />
    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <!-- Permissions untuk FileSystem/Share -->
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <!-- Permissions untuk Camera -->
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-feature android:name="android.hardware.camera" android:required="false" />
"""

with open(manifest_path, 'r') as f:
    content = f.read()

# Hapus permission lama jika ada
lines = content.split('\n')
new_lines = []
for line in lines:
    if any(x in line for x in ['READ_CONTACTS', 'WRITE_CONTACTS', 'BLUETOOTH', 'ACCESS_FINE_LOCATION', 
                                'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE',
                                'CAMERA', 'hardware.camera']):
        continue
    new_lines.append(line)

content = '\n'.join(new_lines)

# Insert permissions sebelum <application
content = content.replace('<application', permissions + '\n    <application')

with open(manifest_path, 'w') as f:
    f.write(content)

print("AndroidManifest.xml updated successfully")
