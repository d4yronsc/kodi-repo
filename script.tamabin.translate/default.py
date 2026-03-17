# -*- coding: utf-8 -*-
"""TaMaBin - Quick translate trigger.

Run while playing a video to translate subtitles.
"""
import xbmc
import xbmcgui

player = xbmc.Player()
if not player.isPlaying():
    xbmcgui.Dialog().notification(
        "TaMaBin",
        "Reproduce un video primero",
        xbmcgui.NOTIFICATION_WARNING,
        3000
    )
else:
    xbmc.executebuiltin('NotifyAll(force_translate_tamabin, force_translate_tamabin)')
    xbmcgui.Dialog().notification(
        "TaMaBin",
        "Traduciendo subtitulos...",
        xbmcgui.NOTIFICATION_INFO,
        3000
    )
