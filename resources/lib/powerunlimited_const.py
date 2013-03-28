import os
import xbmcaddon

#
# Constants
# 
__settings__    = xbmcaddon.Addon(id='plugin.video.powerunlimited')
__language__    = __settings__.getLocalizedString
__images_path__ = os.path.join( xbmcaddon.Addon(id='plugin.video.powerunlimited').getAddonInfo('path'), 'resources', 'images' )
__addon__       = "plugin.video.powerunlimited"
__plugin__      = "PowerUnlimited"
__author__      = "Skipmode A1"
__url__         = ""
__date__        = "17 march 2013"
__version__     = "1.0"