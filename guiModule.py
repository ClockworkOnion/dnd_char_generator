import wx, math, chargen

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='DnD5e Character Creator', size=(500, 500)) # Boilerplate

        self.info_lines = []

        panel = wx.Panel(self)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)
        right_inner_sizer = wx.BoxSizer(wx.VERTICAL)
        attributes_sizer = self.create_statblock(panel)
        outer_sizer.Add(attributes_sizer)

        self.info_text = wx.StaticText(panel, label="Dnd5e Character Creator. Welcome!", style=wx.ALIGN_LEFT)
        self.info_text.SetFont(self.mono_font)
        right_inner_sizer.Add(self.info_text, 0, wx.ALL | wx.EXPAND, 5)
        
        self.statblock = wx.TextCtrl(panel, size=(80,80), value="Stats will appear here\nAlso another line.")
        right_inner_sizer.Add(self.statblock, 0, wx.ALL | wx.EXPAND, 5)

        outer_sizer.Add(right_inner_sizer, 0, wx.ALL | wx.EXPAND,5)
        panel.SetSizer(outer_sizer)
        self.Show() 

    def set_infotext(self, string):
        if (len(self.info_lines) > 3):
            self.info_lines.pop(0)
        self.info_lines.append(string)

        whole_string = ""
        for l in self.info_lines:
            whole_string += (l+"\n")
        self.info_text.SetLabel(whole_string)
        
    def minus_button_triggered(self, event, value):
        val = int(self.attribute_box_pointers[value].GetValue())
        new_val:int = (val-1)
        self.attribute_box_pointers[value].SetValue(str(new_val))
        self.attribute_mod_pointers[value].SetLabel(self.attribute_mod_from_total(new_val))
    
    def plus_button_triggered(self, event, value):
        val = int(self.attribute_box_pointers[value].GetValue())
        new_val:int = (val+1)
        self.attribute_box_pointers[value].SetValue(str(new_val))
        self.attribute_mod_pointers[value].SetLabel(self.attribute_mod_from_total(new_val))
    
    def attribute_mod_from_total(self, value):
        mod = math.floor((value-10)/2)
        return str(mod) if (mod < 0) else ("+"+ str(mod))

    def generate_character(self, event):
        c = self.class_select.GetValue()
        if (c == ""):
            self.set_infotext("No class selected!")
            return
        self.set_infotext("Creating stats for a " + c)
        stats = chargen.get_attribute_rolls(c)
        attributes = ["STR", "DEX", "CON", "WIS", "INT", "CHA"] 
        for a in attributes:
            self.attribute_box_pointers[a].SetValue(str(stats[a]))
            self.attribute_mod_pointers[a].SetLabel(self.attribute_mod_from_total(stats[a]))

        self.set_infotext("Pointbuy value: " + str(chargen.calculate_pointbuy_value(stats.values())))
        self.calculate_statblock()
    
    def calculate_statblock(self):
        self.statblock.SetValue("Hallo")


    def on_class_selected(self, event):
        print("Selected " + self.class_select.GetValue())

    def on_armor_selected(self, event):
        print("Selected " + self.armor_select.GetValue())

    def create_statblock(self, target_panel):
        attributes = ["STR", "DEX", "CON", "WIS", "INT", "CHA"] 
        classes = ["Fighter", "Rogue", "Wizard"]
        armor_types = ["None", "Leather (AC11)", "Studded Leather (AC12)", "Chain Mail (AC16)"]
        self.attribute_box_pointers = dict()
        self.attribute_mod_pointers = dict()
        self.mono_font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.NORMAL, wx.NORMAL, faceName="Monospace")
        attributes_sizer = wx.BoxSizer(wx.VERTICAL) # Vertical lineup
        attributes_sizer.AddSpacer(10)
        attributes_heading = wx.StaticText(target_panel, label="  Attributes")
        attributes_heading.SetFont(self.mono_font)
        attributes_sizer.Add(attributes_heading)
        for index, attr in enumerate(attributes):
            inner_sizer = wx.BoxSizer(wx.HORIZONTAL)
            attribute_name_statictext = wx.StaticText(target_panel, label=attr, style=wx.ALIGN_LEFT)
            attribute_name_statictext.SetFont(self.mono_font)
            attribute_value_textbox = wx.TextCtrl(target_panel, size=(25,20), value="10")

            attr_plusbutton = wx.Button(target_panel, label="+", size=(25,25))
            attr_minusbutton = wx.Button(target_panel, label="-", size=(25,25))
            attr_plusbutton.Bind(wx.EVT_BUTTON, lambda event, temp=attr: self.plus_button_triggered(event, temp))
            attr_minusbutton.Bind(wx.EVT_BUTTON, lambda event, temp=attr: self.minus_button_triggered(event, temp))

            attribute_modifier_statictext = wx.StaticText(target_panel, label="+0", style=wx.ALIGN_LEFT)
            attribute_modifier_statictext.SetFont(self.mono_font)

            inner_sizer.Add (attribute_name_statictext, 0, wx.ALL | wx.EXPAND, 5)
            inner_sizer.AddStretchSpacer()
            inner_sizer.Add(attribute_value_textbox, 0, wx.ALL | wx.EXPAND, 5)
            inner_sizer.Add(attribute_modifier_statictext, 0, wx.ALL | wx.EXPAND, 5)
            inner_sizer.AddStretchSpacer()
            inner_sizer.Add(attr_minusbutton, 0, wx.ALL | wx.EXPAND, 5)
            inner_sizer.Add(attr_plusbutton, 0, wx.ALL | wx.EXPAND, 5)
            self.attribute_box_pointers[attribute_name_statictext.GetLabel()] = attribute_value_textbox
            self.attribute_mod_pointers[attribute_name_statictext.GetLabel()] = attribute_modifier_statictext
            attributes_sizer.Add(inner_sizer)
        self.class_select = wx.ComboBox(target_panel, choices=classes, style=wx.CB_READONLY)
        self.class_select.Bind(wx.EVT_COMBOBOX, self.on_class_selected)
        self.armor_select = wx.ComboBox(target_panel, choices=armor_types, style=wx.CB_READONLY)
        self.armor_select.Bind(wx.EVT_COMBOBOX, self.on_armor_selected)

        attributes_sizer.Add(self.class_select, 0, wx.ALL | wx.EXPAND, 5)
        attributes_sizer.Add(self.armor_select, 0, wx.ALL | wx.EXPAND, 5)
        generate_character_button = wx.Button(target_panel, label='Generate Character')
        generate_character_button.Bind(wx.EVT_BUTTON, self.generate_character)
        attributes_sizer.Add(generate_character_button, 0, wx.ALL | wx.CENTER, 5)
        return attributes_sizer

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
