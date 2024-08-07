# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['npyconverter/main.py'],
pathex=['.'],
binaries=[],
datas=[],
hiddenimports=[
    'numpy', 
    'numpy.*',
    'scipy', 
    'scipy.*',
    'scipy._lib.*',
    'scipy.sparse.csgraph._validation',
    'scipy.io.matlab.miobase',
    'scipy.io.matlab.mio5_params',
    'scipy.io.matlab.streams',
    'scipy.io.matlab._mio_utils',
    'scipy.io.matlab.mio5',
    'scipy.io.matlab.mio4',
    'scipy._lib._ccallback_c'
],
hookspath=[],
runtime_hooks=[],
excludes=[],
win_no_prefer_redirects=False,
win_private_assemblies=False,
cipher=block_cipher,
noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='npyConverter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='npyConverter',
)
