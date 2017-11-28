# -*- mode: python -*-

block_cipher = None


a = Analysis(['BirdRedux.py'],
             pathex=['C:\\Users\\DSU\\Documents\\GitHub\\CSV-Bird-Project\\CSV-Bird-Info-Converter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='oconsole',
          debug=False,
          strip=False,
          upx=True,
          console=True )
