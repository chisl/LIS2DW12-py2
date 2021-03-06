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

class REG:
	OUT_T = 13
	WHO_AM_I = 15
	CTRL1 = 32
	CTRL2 = 33
	CTRL3 = 34
	CTRL4_INT1_PAD_CTRL = 35
	CTRL5_INT2_PAD_CTRL = 36
	CTRL6 = 37
	OUT_T2 = 38
	STATUS = 39
	OUT_X = 40
	OUT_Y = 42
	OUT_Z = 44
	OUT_X_L = 40
	OUT_Y_L = 42
	OUT_Y_H = 43
	OUT_Z_L = 44
	FIFO_CTRL = 46
	FIFO_SAMPLES = 47
	TAP_THS_X = 48
	TAP_THS_Y = 49
	TAP_THS_Z = 50
	INT_DUR = 51
	WAKE_UP_THS = 52
	WAKE_UP_DUR = 53
	FREE_FALL = 54
	STATUS_DUP = 55
	WAKE_UP_SRC = 56
	TAP_SRC = 57
	SIXD_SRC = 58
	ALL_INT_SRC = 59
	X_OFS_USR = 60
	Y_OFS_USR = 61
	Z_OFS_USR = 62
