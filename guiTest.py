import wx, math

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='DnD5e Character Creator', size=(1000, 1000)) # Boilerplate
        panel = wx.Panel(self)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)
        attributes_sizer = self.create_statblock(panel)
        outer_sizer.Add(attributes_sizer)

        # Placeholder widget
        bla_widget = wx.StaticText(panel, label="SOME TEXT", style=wx.ALIGN_LEFT)
        outer_sizer.Add(bla_widget, 0, wx.ALL | wx.EXPAND, 5)
        
        panel.SetSizer(outer_sizer)
        self.Show() 
        
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
        print("Doing something...")

    def create_statblock(self, target_panel):
        attributes = ["STR", "DEX", "CON", "WIS", "INT", "CHA"] 
        classes = ["Fighter", "Rogue", "Wizard"]
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
        attributes_sizer.Add(self.class_select, 0, wx.ALL | wx.EXPAND, 5)
        generate_character_button = wx.Button(target_panel, label='Generate Character')
        generate_character_button.Bind(wx.EVT_BUTTON, self.generate_character)
        attributes_sizer.Add(generate_character_button, 0, wx.ALL | wx.CENTER, 5)
        return attributes_sizer

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
