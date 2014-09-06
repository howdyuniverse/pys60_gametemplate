"""
    Game Template for pys60 platform
"""
import os
import sys
import e32

GAME_DIRNAME = u"gametemplate"
# looking for install dir   
DEFDIR = u"e:\\python"
for drive in e32.drive_list():
    appd = os.path.join(drive, u"\\data\\python\\%s\\" % GAME_DIRNAME)
    if os.path.exists(os.path.join(appd, u"game.py")):
        DEFDIR = appd
        break

sys.path.append(DEFDIR)

try:
    import game
    game.Game().run()
except Exception, e:
    #import appuifw
    #appuifw.note(u"Exception: %s" % (e))
    print e
