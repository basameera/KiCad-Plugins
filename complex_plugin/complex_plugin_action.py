import pcbnew
import os
import datetime
import re

class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin"
        self.show_toolbar_button = True  # Optional, defaults to False
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), 'icon.png')  # Optional

    def Run(self):
        pcb = pcbnew.GetBoard()
        for draw in pcb.GetDrawings():
            if draw.GetClass() == 'PTEXT':
                txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                             "$date$", draw.GetText())
                if txt == "$date$":
                    draw.SetText("%s" % datetime.date.today())
