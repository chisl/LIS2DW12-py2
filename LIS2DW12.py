#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LIS2DW12: MEMS digital output motion sensor: high-performance ultra-low-power 3-axis 'femto' accelerometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from LIS2DW12_constants import *

# name:        LIS2DW12
# description: MEMS digital output motion sensor: high-performance ultra-low-power 3-axis 'femto' accelerometer
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lis2dw12.pdf
# date:        2018-02-05


# Derive from this class and implement read and write
class LIS2DW12_Base:
	"""MEMS digital output motion sensor: high-performance ultra-low-power 3-axis 'femto' accelerometer"""
	# Register OUT_T
	# 8.1-2
	#       Temperature output register in 12-bit resolution (r). 
	
	
	def setOUT_T(self, val):
		"""Set register OUT_T"""
		self.write(REG.OUT_T, val, 16)
	
	def getOUT_T(self):
		"""Get register OUT_T"""
		return self.read(REG.OUT_T, 16)
	
	# Bits TEMP
	# The temperature sensor output. Sensitivity = 16 LSB/°C.
	#           This forms the output value expressed as a 16-bit word in 2's complement. 
	
	# Register WHO_AM_I
	# 8.3
	#       Who_AM_I register (r). This register is a read-only register. Its value is fixed at 44h. 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL1
	# Control register 1 
	
	def setCTRL1(self, val):
		"""Set register CTRL1"""
		self.write(REG.CTRL1, val, 8)
	
	def getCTRL1(self):
		"""Get register CTRL1"""
		return self.read(REG.CTRL1, 8)
	
	# Bits ODR
	# Output data rate and mode selection (see Table 30) 
	#           ODR is used to set the power mode and ODR selection. The following table lists the bit
	#           settings for power-down mode and each available frequency. 
	
	# Bits MODE
	# Mode selection (see Table 31)  
	# Bits LP_MODE
	# Low-power mode selection (see Table 32) 
