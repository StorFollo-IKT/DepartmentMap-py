# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DepartmentMapFrame
###########################################################################

class DepartmentMapFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Organisasjonsenheter",
                          pos=wx.DefaultPosition, size=wx.Size(560, 533),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.Size(600, -1))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        buttonGridSizer = wx.GridSizer(0, 2, 0, 0)

        self.expandAllButton = wx.Button(self, wx.ID_ANY, u"Utvid alle", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        buttonGridSizer.Add(self.expandAllButton, 0, wx.ALL, 5)

        self.collapseAllButton = wx.Button(self, wx.ID_ANY, u"Slå sammen alle", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        buttonGridSizer.Add(self.collapseAllButton, 0, wx.ALL, 5)

        bSizer1.Add(buttonGridSizer, 0, 0, 5)

        self.orgTree = wx.TreeCtrl(self, wx.ID_ANY, wx.Point(-1, -1), wx.Size(-1, -1),
                                   wx.TR_DEFAULT_STYLE)
        self.orgTree.SetMinSize(wx.Size(-1, 1000))

        bSizer1.Add(self.orgTree, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.expandAllButton.Bind(wx.EVT_BUTTON, self.expandAll)
        self.collapseAllButton.Bind(wx.EVT_BUTTON, self.collapseAll)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def expandAll(self, event):
        event.Skip()

    def collapseAll(self, event):
        event.Skip()


###########################################################################
## Class LoadingFrame
###########################################################################

class LoadingFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Laster data", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.loadingText = wx.StaticText(self, wx.ID_ANY, u"Laster data", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.loadingText.Wrap(-1)

        self.loadingText.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                    wx.EmptyString))

        bSizer2.Add(self.loadingText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
