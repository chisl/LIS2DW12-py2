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
	# Register CTRL2
	# 8.5
	#       Control register 2 
	
	
	def setCTRL2(self, val):
		"""Set register CTRL2"""
		self.write(REG.CTRL2, val, 8)
	
	def getCTRL2(self):
		"""Get register CTRL2"""
		return self.read(REG.CTRL2, 8)
	
	# Bits BOOT
	# Boot enables retrieving the correct trimming parameters from nonvolatile memory
	#           into registers where trimming parameters are stored.
	#           Once the operation is over, this bit automatically returns to 0. 
	
	# Bits reserved_0
	# This bit must be set to ‘0’ for the correct operation of the device. 
	# Bits SOFT_RESET
	# Soft reset acts as reset for all control registers, then goes to 0. 
	# Bits CS_PU_DISC
	# Disconnect CS pull-up. 
	# Bits BDU
	# Block data update. 
	#           The BDU bit is used to inhibit the update of the output registers until both upper and lower
	#           register parts are read. In default mode (BDU = ‘0’) the output register values are updated continuously. When the BDU is activated (BDU = ‘1’), the content of the output registers is not updated until both MSB and LSB are read which avoids reading values related to different sample times. 
	
	# Bits IF_ADD_INC
	# Register address automatically incremented during multiple byte access with a serial interface (I2C or SPI). 
	# Bits I2C_DISABLE
	# Disable I2C communication protocol. 
	# Bits SIM
	# SPI serial interface mode selection. 
	# Register CTRL3
	# 8.6
	#       COntrol register 3 
	
	
	def setCTRL3(self, val):
		"""Set register CTRL3"""
		self.write(REG.CTRL3, val, 8)
	
	def getCTRL3(self):
		"""Get register CTRL3"""
		return self.read(REG.CTRL3, 8)
	
	# Bits ST
	# Bits PP_OD
	# Push-pull/open-drain selection on interrupt pad. 
	# Bits LIR
	# Latched Interrupt. Switches between latched ('1'-logic) and pulsed ('0'-logic) mode for function source
	#           signals and interrupts routed to pins (wakeup, single/double-tap). 
	
	# Bits H_LACTIVE
	# Interrupt active high, low. 
	# Bits unused_0
	# Bits SLP_MODE_SEL
	# Single data conversion on demand mode selection 
	# Bits SLP_MODE_1
	# Single data conversion on demand mode enable. When SLP_MODE_SEL = '1' and this bit is set to '1' logic, 
	#           single data conversion on demand mode starts. When XL data are available in the registers, this bit is set 
	#           to '0' automatically and the device is ready for another triggered session. 
	
	# Register CTRL4_INT1_PAD_CTRL
	# 8.7
	#       Control register 4 
	
	
	def setCTRL4_INT1_PAD_CTRL(self, val):
		"""Set register CTRL4_INT1_PAD_CTRL"""
		self.write(REG.CTRL4_INT1_PAD_CTRL, val, 8)
	
	def getCTRL4_INT1_PAD_CTRL(self):
		"""Get register CTRL4_INT1_PAD_CTRL"""
		return self.read(REG.CTRL4_INT1_PAD_CTRL, 8)
	
	# Bits INT1_6D
	# 6D recognition is routed to INT1 pad. 
	# Bits INT1_SINGLE_TAP
	# Single-tap recognition is routed to INT1 pad. 
	# Bits INT1_WU
	# Wakeup recognition is routed to INT1 pad. 
	# Bits INT1_FF
	# Free-fall recognition is routed to INT1 pad. 
	# Bits INT1_TAP
	# Double-tap recognition is routed to INT1 pad. 
	# Bits INT1_DIFF5
	# FIFO full recognition is routed to INT1 pad. 
	# Bits INT1_FTH
	# FIFO threshold interrupt is routed to INT1 pad. 
	# Bits INT1_DRDY
	# Data-Ready is routed to INT1 pad. 
	# Register CTRL5_INT2_PAD_CTRL
	# 8.8
	#       Control register 4 
	
	
	def setCTRL5_INT2_PAD_CTRL(self, val):
		"""Set register CTRL5_INT2_PAD_CTRL"""
		self.write(REG.CTRL5_INT2_PAD_CTRL, val, 8)
	
	def getCTRL5_INT2_PAD_CTRL(self):
		"""Get register CTRL5_INT2_PAD_CTRL"""
		return self.read(REG.CTRL5_INT2_PAD_CTRL, 8)
	
	# Bits INT2_SLEEP_STATE
	# Enable routing of SLEEP_STATE on INT2 pad.  
	# Bits INT2_SLEEP_CHG
	# Sleep change status routed to INT2 pad. 
	# Bits INT2_BOOT
	# Boot state routed to INT2 pad. 
	# Bits INT2_DRDY_T
	# Temperature data-ready is routed to INT2. 
	# Bits INT2_OVR
	# FIFO overrun interrupt is routed to INT2 pad. 
	# Bits INT2_DIFF5
	# FIFO full recognition is routed to INT2 pad. 
	# Bits INT2_FTH
	# FIFO threshold interrupt is routed to INT2 pad. 
	# Bits INT2_DRDY
	# Data-ready is routed to INT2 pad. 
	# Register CTRL6
	# 8.9
	#       Control register 6. 
	
	
	def setCTRL6(self, val):
		"""Set register CTRL6"""
		self.write(REG.CTRL6, val, 8)
	
	def getCTRL6(self):
		"""Get register CTRL6"""
		return self.read(REG.CTRL6, 8)
	
	# Bits BW_FILT
	# Bandwidth selection 
	# Bits FS
	# Full-scale selection. 
	# Bits FDS
	# Filtered data type selection. 
	# Bits LOW_NOISE
	# Low-noise configuration. 
	# Register OUT_T2
	# 8.10
	#       Temperature output register in 8-bit resolution (r)
	#       The value is expressed as two’s complement sign. Sensitivity = 1°C/LSB
	#       0 LSB represents T=25 °C ambient. 
	
	
	def setOUT_T2(self, val):
		"""Set register OUT_T2"""
		self.write(REG.OUT_T2, val, 8)
	
	def getOUT_T2(self):
		"""Get register OUT_T2"""
		return self.read(REG.OUT_T2, 8)
	
	# Bits OUT_T2
	# Register STATUS
	# 8.11
	#       Status register (r). 
	
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits FIFO_THS
	# FIFO threshold status flag. 
	# Bits WU_IA
	# Wakeup event detection status. 
	# Bits SLLEP_STATE
	# Sleep event status. 
	# Bits DOUBLE_TAP
	# Double-tap event status 
	# Bits SINGLE_TAP
	# Single-tap event status 
	# Bits D6_IA
	# Source of change in position portrait/landscape/face-up/face-down. 
	# Bits FF_IA
	# Free-fall event detection status. 
	# Bits DRDY
	# Data-ready status. 
	# Register OUT_X
	# X-axis output register (r). 
	#       It forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_X(self, val):
		"""Set register OUT_X"""
		self.write(REG.OUT_X, val, 16)
	
	def getOUT_X(self):
		"""Get register OUT_X"""
		return self.read(REG.OUT_X, 16)
	
	# Bits reserved_0
	# Bits OUT_X
	# NOTE: If Low-Power Mode 1 is enabled, this bit2 15..14 are set to 0. 
	# Register OUT_Y
	# Y-axis output register (r). 
	#       It forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_Y(self, val):
		"""Set register OUT_Y"""
		self.write(REG.OUT_Y, val, 16)
	
	def getOUT_Y(self):
		"""Get register OUT_Y"""
		return self.read(REG.OUT_Y, 16)
	
	# Bits reserved_0
	# Bits OUT_Y
	# NOTE: If Low-Power Mode 1 is enabled, this bit2 15..14 are set to 0. 
	# Register OUT_Z
	# Z-axis output register (r). 
	#       It forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_Z(self, val):
		"""Set register OUT_Z"""
		self.write(REG.OUT_Z, val, 16)
	
	def getOUT_Z(self):
		"""Get register OUT_Z"""
		return self.read(REG.OUT_Z, 16)
	
	# Bits reserved_0
	# Bits OUT_Z
	# NOTE: If Low-Power Mode 1 is enabled, this bit2 15..14 are set to 0. 
	# Register OUT_X_L
	# 8.12
	#       X-axis LSB output register (r).
	#       1.   If Low-Power Mode 1 is enabled, this bit is set to 0.
	#       The 8 least significant bits of linear acceleration sensor X-axis output. Together with the
	#       OUT_X_H (29h) register, it forms the output value expressed as a 16-bit word in 2's complement.
	#       X_H7	X_H6	X_H5	X_H4	X_H3	X_H2	X_H1	X_H0
	#       The 8 most significant bits of linear acceleration sensor X-axis output. Together with the
	#       OUT_X_L (28h) register, it forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_X_L(self, val):
		"""Set register OUT_X_L"""
		self.write(REG.OUT_X_L, val, 8)
	
	def getOUT_X_L(self):
		"""Get register OUT_X_L"""
		return self.read(REG.OUT_X_L, 8)
	
	# Bits OUT_X_L
	# Register OUT_Y_L
	# 8.14
	#       Y-axis LSB output register (r).
	#       1.   If Low-Power Mode 1 is enabled, this bit is set to 0.
	#       The 8 least significant bits of linear acceleration sensor Y-axis output. Together with the
	#       OUT_Y_H (2Bh) register, it forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_Y_L(self, val):
		"""Set register OUT_Y_L"""
		self.write(REG.OUT_Y_L, val, 8)
	
	def getOUT_Y_L(self):
		"""Get register OUT_Y_L"""
		return self.read(REG.OUT_Y_L, 8)
	
	# Bits OUT_Y_L
	# Register OUT_Y_H
	# 8.15
	#       Y-axis MSB output register (r).
	#       OUT_Y_L (2Ah) register, it forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_Y_H(self, val):
		"""Set register OUT_Y_H"""
		self.write(REG.OUT_Y_H, val, 8)
	
	def getOUT_Y_H(self):
		"""Get register OUT_Y_H"""
		return self.read(REG.OUT_Y_H, 8)
	
	# Bits OUT_Y_H
	# Register OUT_Z_L
	# 8.16
	#       Z-axis LSB output register (r).
	#       Z_L7	Z_L6	Z_L5	Z_L4	Z_L3(1)	Z_L2(1)	0	0
	#       1.   If Low-power Mode 1 is enabled, this bit is set to 0.
	#       The 8 least significant bits of linear acceleration sensor Z-axis output. Together with the
	#       OUT_Z_H (2Dh) register, it forms the output value expressed as a 16-bit word in 2's complement.
	#       Z_H7	Z_H6	Z_H5	Z_H4	Z_H3	Z_H2	Z_H1	Z_H0
	#       The 8 most significant bits of linear acceleration sensor Z-axis output. Together with the
	#       OUT_Z_L (2Ch) register, it forms the output value expressed as a 16-bit word in 2's complement. 
	
	
	def setOUT_Z_L(self, val):
		"""Set register OUT_Z_L"""
		self.write(REG.OUT_Z_L, val, 8)
	
	def getOUT_Z_L(self):
		"""Get register OUT_Z_L"""
		return self.read(REG.OUT_Z_L, 8)
	
	# Bits OUT_Z_L
	# Register FIFO_CTRL
	# 8.18
	#       FIFO control register 
	
	
	def setFIFO_CTRL(self, val):
		"""Set register FIFO_CTRL"""
		self.write(REG.FIFO_CTRL, val, 8)
	
	def getFIFO_CTRL(self):
		"""Get register FIFO_CTRL"""
		return self.read(REG.FIFO_CTRL, 8)
	
	# Bits FMODE
	# FIFO mode selection bits. 
	# Bits FTH
	# FIFO threshold level setting. 
	# Register FIFO_SAMPLES
	# 8.19
	#       FIFO_SAMPLES control register. 
	
	
	def setFIFO_SAMPLES(self, val):
		"""Set register FIFO_SAMPLES"""
		self.write(REG.FIFO_SAMPLES, val, 8)
	
	def getFIFO_SAMPLES(self):
		"""Get register FIFO_SAMPLES"""
		return self.read(REG.FIFO_SAMPLES, 8)
	
	# Bits FIFO_FTH
	# FIFO threshold status flag. 
	# Bits FIFO_OVR
	# FIFO overrun status. 
	# Bits DIFF
	# Represents the number of unread samples stored in FIFO. 
	#           (000000 = FIFO empty; 100000 = FIFO full, 32 unread samples. 
	
	# Register TAP_THS_X
	# 8.20
	#       4D configuration enable and TAP threshold configuration. 
	
	
	def setTAP_THS_X(self, val):
		"""Set register TAP_THS_X"""
		self.write(REG.TAP_THS_X, val, 8)
	
	def getTAP_THS_X(self):
		"""Get register TAP_THS_X"""
		return self.read(REG.TAP_THS_X, 8)
	
	# Bits D4_EN
	# 4D detection portrait/landscape position enable. 
	# Bits D6_THS
	# Thresholds for 4D/6D function @ FS = ±2 g 
	# Bits TAP_THSX
	# Threshold for TAP recognition @ FS = ±2 g on X direction 
	# Register TAP_THS_Y
	# 8.21 
	
	def setTAP_THS_Y(self, val):
		"""Set register TAP_THS_Y"""
		self.write(REG.TAP_THS_Y, val, 8)
	
	def getTAP_THS_Y(self):
		"""Get register TAP_THS_Y"""
		return self.read(REG.TAP_THS_Y, 8)
	
	# Bits TAP_PRIOR
	# Selection  of axis priority for tap detection. 
	#           Max priority / Mid priority / Min priority 
	
	# Bits TAP_THSY
	# Threshold for tap recognition @ FS = ±2 g on Y direction. 
	# Register TAP_THS_Z
	# 8.22 
	
	def setTAP_THS_Z(self, val):
		"""Set register TAP_THS_Z"""
		self.write(REG.TAP_THS_Z, val, 8)
	
	def getTAP_THS_Z(self):
		"""Get register TAP_THS_Z"""
		return self.read(REG.TAP_THS_Z, 8)
	
	# Bits TAP_X_EN
	# Enables X direction in tap recognition. 
	# Bits TAP_Y_EN
	# Enables Y direction in tap recognition. 
	# Bits TAP_Z_EN
	# Enables Z direction in tap recognition. 
	# Bits TAP_THSZ
	# Threshold for tap recognition @ FS = ±2 g on Z direction. 
	# Register INT_DUR
	# Interrupt duration register 
	
	def setINT_DUR(self, val):
		"""Set register INT_DUR"""
		self.write(REG.INT_DUR, val, 8)
	
	def getINT_DUR(self):
		"""Get register INT_DUR"""
		return self.read(REG.INT_DUR, 8)
	
	# Bits LATENCY
	# Duration of maximum time gap for double-tap recognition. When double-tap recognition is enabled, this 
	#           register expresses the maximum time between two successive detected taps to determine a double-tap event.
	#           Default value is LATENCY = 0000 (which is 16 * 1/ODR)
	#           1 LSB = 32 * 1/ODR. 
	
	# Bits QUIET
	# Expected quiet time after a tap detection: this register represents the time after the first detected 
	#           tap in which there must not be any overthreshold event.
	#           Default value is QUIET[1:0] = 00 (which is 2 * 1/ODR)
	#           1 LSB = 4 * 1/ODR 
	
	# Bits SHOCK
	# Maximum duration of over-threshold event: this register represents the maximum time of an 
	#           over-threshold signal detection to be recognized as a tap event. 
	#           Default value is SHOCK[1:0] = 00 (which is 4 * 1/ODR) 
	#           1 LSB = 8 *1/ODR 
	
	# Register WAKE_UP_THS
	# 8.24
	#       Wakeup threshold register. 
	
	
	def setWAKE_UP_THS(self, val):
		"""Set register WAKE_UP_THS"""
		self.write(REG.WAKE_UP_THS, val, 8)
	
	def getWAKE_UP_THS(self):
		"""Get register WAKE_UP_THS"""
		return self.read(REG.WAKE_UP_THS, 8)
	
	# Bits SINGLE_DOUBLE_TAP
	# Enable single/double-tap event. 
	# Bits SLEEP_ON
	# Sleep (inactivity) enable. 
	# Bits WK_THS
	# Wakeup threshold, 6-bit unsigned 1 LSB = 1/64 of FS. 
