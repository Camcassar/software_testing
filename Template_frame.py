# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Guess the generated number 0 ~ 100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"Guess", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer7, 0, 0, 5 )


		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.m_notebook3.AddPage( self.m_panel3, u"BINGO 1", False )
		self.m_panel5 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Guess the generated number 0 ~ 1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer41.Add( self.m_staticText31, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl51 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_textCtrl51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button81 = wx.Button( self.m_panel5, wx.ID_ANY, u"Guess", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_button81, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer71.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer41.Add( bSizer71, 0, 0, 5 )


		self.m_panel5.SetSizer( bSizer41 )
		self.m_panel5.Layout()
		bSizer41.Fit( self.m_panel5 )
		self.m_notebook3.AddPage( self.m_panel5, u"BINGO 2", False )

		bSizer10.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button8.Bind( wx.EVT_BUTTON, self.my_guess_func1 )
		self.m_button81.Bind( wx.EVT_BUTTON, self.my_guess_func2 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def my_guess_func1( self, event ):
		event.Skip()

	def my_guess_func2( self, event ):
		event.Skip()


