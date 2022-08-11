import pcbnew
import os
import re
import datetime
import wx


class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin"
        self.show_toolbar_button = True  # Optional, defaults to False
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), 'icon.png')  # Optional

    def Run(self):
        '''
        Replace a text containing $date$ with today's date.
        '''
        # pcb = pcbnew.GetBoard()
        # for draw in pcb.GetDrawings():
        #     if draw.GetClass() == 'PTEXT':
        #         txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
        #                      "$date$", draw.GetText())
        #         if txt == "$date$":
        #             draw.SetText("%s" % datetime.date.today())

        start_GUI2()


def start_GUI2():
    app = wx.App(False)
    frame = MyFrame(None, 'Small editor')
    app.MainLoop()


class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    '''https://docs.wxwidgets.org/2.8.12/wx_stdevtid.html'''

    def __init__(self, parent, title):
        height = 600
        width = 800
        height_half = height//2
        width_half = width//2

        wx.Frame.__init__(self, parent, title=title, size=(width, height), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        # add panel
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0),
                              size=(width_half, height))
        panel1 = wx.Panel(self, wx.ID_ANY, pos=(width_half, 0),
                          size=(width_half, height))

        # add button
        button = wx.Button(self.panel, wx.ID_ANY, 'About', (10, 200))
        button.Bind(wx.EVT_BUTTON, self.OnAbout)

        button1 = wx.Button(panel1, wx.ID_ANY, 'Exit', (10, 10))
        button1.Bind(wx.EVT_BUTTON, self.OnExit)

        # text
        self.output = wx.StaticText(self.panel, label="Output:", pos=(10, 10),
                                    size=(100, 20), style=wx.SIMPLE_BORDER)
        self.result = wx.StaticText(self.panel, label="--output--", pos=(110, 10),
                                    size=(100, 20), style=wx.SIMPLE_BORDER)
        self.result.SetForegroundColour(wx.RED)

        self.input = wx.StaticText(self.panel, label="Input:", pos=(10, 40),
                                   size=(100, 20), style=wx.SIMPLE_BORDER)
        self.editname = wx.TextCtrl(self.panel, pos=(110, 40),
                                    size=(140, -1))
        self.button = wx.Button(self.panel, label="Save", pos=(10, 70))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        self.Show(True)

    def OnAbout(self, event):
        wx.LogMessage("on about")
        # if (some_condition):
        #     do_something()
        # else:
        #     event.Skip()

    def OnExit(self, e):
        self.Close(True)  # Close the frame.

    def OnButton(self, e):
        self.result.SetLabel(self.editname.GetValue())
