# run_template.py

import wx
from template_frame import MyFrame3 as MyFrame
from all_functions import get_bingo

class GuessFrame(MyFrame):
    def __init__(self):
        super().__init__(None)
        self.bingo1 = 50  # initial bingo number (you can set this to anything, or randomize it)
        self.bingo2 = 70  # another bingo number for the second game

        self.Show()

    def my_guess_func1(self, event):
        my_str = self.m_textCtrl5.GetValue()
        result_str, self.bingo1 = get_bingo(my_str, self.bingo1, 0, 100)
        self.m_staticText4.SetLabel(result_str)
        self.Layout()

    def my_guess_func2(self, event):
        my_str = self.m_textCtrl6.GetValue()
        result_str, self.bingo2 = get_bingo(my_str, self.bingo2, 100, 1000)
        self.m_staticText5.SetLabel(result_str)
        self.Layout()
