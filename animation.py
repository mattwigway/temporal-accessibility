#!/usr/bin/python
# animation.py: animate a whole bunch of GeoTIFFs using the QGIS Python API

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import QImage, QPainter, QFont, QColor
from PyQt4.QtCore import QSize, QRectF

layerName = 'access'

paths = '''/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_0_0Su_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_100_4Th_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_10_0Su_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_101_4Th_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_102_4Th_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_103_4Th_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_104_4Th_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_105_4Th_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_106_4Th_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_107_4Th_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_108_4Th_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_109_4Th_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_1_0Su_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_110_4Th_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_11_0Su_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_111_4Th_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_112_4Th_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_113_4Th_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_114_4Th_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_115_4Th_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_116_4Th_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_117_4Th_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_118_4Th_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_119_4Th_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_120_5Fr_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_12_0Su_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_121_5Fr_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_122_5Fr_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_123_5Fr_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_124_5Fr_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_125_5Fr_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_126_5Fr_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_127_5Fr_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_128_5Fr_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_129_5Fr_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_130_5Fr_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_13_0Su_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_131_5Fr_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_132_5Fr_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_133_5Fr_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_134_5Fr_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_135_5Fr_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_136_5Fr_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_137_5Fr_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_138_5Fr_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_139_5Fr_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_140_5Fr_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_14_0Su_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_141_5Fr_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_142_5Fr_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_143_5Fr_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_144_6Sa_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_145_6Sa_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_146_6Sa_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_147_6Sa_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_148_6Sa_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_149_6Sa_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_150_6Sa_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_15_0Su_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_151_6Sa_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_152_6Sa_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_153_6Sa_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_154_6Sa_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_155_6Sa_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_156_6Sa_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_157_6Sa_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_158_6Sa_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_159_6Sa_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_160_6Sa_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_16_0Su_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_161_6Sa_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_162_6Sa_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_163_6Sa_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_164_6Sa_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_165_6Sa_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_166_6Sa_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_167_6Sa_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_17_0Su_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_18_0Su_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_19_0Su_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_20_0Su_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_2_0Su_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_21_0Su_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_22_0Su_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_23_0Su_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_24_1Mo_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_25_1Mo_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_26_1Mo_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_27_1Mo_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_28_1Mo_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_29_1Mo_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_30_1Mo_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_3_0Su_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_31_1Mo_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_32_1Mo_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_33_1Mo_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_34_1Mo_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_35_1Mo_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_36_1Mo_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_37_1Mo_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_38_1Mo_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_39_1Mo_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_40_1Mo_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_4_0Su_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_41_1Mo_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_42_1Mo_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_43_1Mo_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_44_1Mo_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_45_1Mo_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_46_1Mo_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_47_1Mo_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_48_2Tu_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_49_2Tu_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_50_2Tu_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_5_0Su_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_51_2Tu_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_52_2Tu_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_53_2Tu_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_54_2Tu_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_55_2Tu_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_56_2Tu_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_57_2Tu_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_58_2Tu_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_59_2Tu_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_60_2Tu_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_6_0Su_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_61_2Tu_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_62_2Tu_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_63_2Tu_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_64_2Tu_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_65_2Tu_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_66_2Tu_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_67_2Tu_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_68_2Tu_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_69_2Tu_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_70_2Tu_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_7_0Su_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_71_2Tu_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_72_3We_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_73_3We_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_74_3We_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_75_3We_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_76_3We_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_77_3We_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_78_3We_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_79_3We_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_80_3We_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_8_0Su_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_81_3We_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_82_3We_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_83_3We_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_84_3We_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_85_3We_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_86_3We_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_87_3We_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_88_3We_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_89_3We_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_90_3We_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_9_0Su_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_91_3We_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_92_3We_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_93_3We_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_94_3We_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_95_3We_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_96_4Th_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_97_4Th_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_98_4Th_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/bicycle_eateries_99_4Th_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_0_0Su_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_100_4Th_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_10_0Su_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_101_4Th_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_102_4Th_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_103_4Th_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_104_4Th_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_105_4Th_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_106_4Th_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_107_4Th_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_108_4Th_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_109_4Th_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_1_0Su_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_110_4Th_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_11_0Su_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_111_4Th_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_112_4Th_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_113_4Th_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_114_4Th_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_115_4Th_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_116_4Th_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_117_4Th_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_118_4Th_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_119_4Th_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_120_5Fr_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_12_0Su_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_121_5Fr_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_122_5Fr_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_123_5Fr_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_124_5Fr_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_125_5Fr_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_126_5Fr_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_127_5Fr_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_128_5Fr_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_129_5Fr_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_130_5Fr_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_13_0Su_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_131_5Fr_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_132_5Fr_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_133_5Fr_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_134_5Fr_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_135_5Fr_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_136_5Fr_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_137_5Fr_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_138_5Fr_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_139_5Fr_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_140_5Fr_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_14_0Su_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_141_5Fr_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_142_5Fr_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_143_5Fr_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_144_6Sa_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_145_6Sa_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_146_6Sa_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_147_6Sa_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_148_6Sa_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_149_6Sa_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_150_6Sa_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_15_0Su_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_151_6Sa_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_152_6Sa_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_153_6Sa_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_154_6Sa_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_155_6Sa_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_156_6Sa_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_157_6Sa_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_158_6Sa_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_159_6Sa_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_160_6Sa_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_16_0Su_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_161_6Sa_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_162_6Sa_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_163_6Sa_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_164_6Sa_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_165_6Sa_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_166_6Sa_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_167_6Sa_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_17_0Su_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_18_0Su_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_19_0Su_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_20_0Su_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_2_0Su_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_21_0Su_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_22_0Su_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_23_0Su_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_24_1Mo_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_25_1Mo_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_26_1Mo_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_27_1Mo_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_28_1Mo_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_29_1Mo_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_30_1Mo_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_3_0Su_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_31_1Mo_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_32_1Mo_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_33_1Mo_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_34_1Mo_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_35_1Mo_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_36_1Mo_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_37_1Mo_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_38_1Mo_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_39_1Mo_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_40_1Mo_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_4_0Su_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_41_1Mo_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_42_1Mo_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_43_1Mo_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_44_1Mo_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_45_1Mo_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_46_1Mo_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_47_1Mo_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_48_2Tu_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_49_2Tu_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_50_2Tu_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_5_0Su_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_51_2Tu_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_52_2Tu_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_53_2Tu_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_54_2Tu_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_55_2Tu_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_56_2Tu_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_57_2Tu_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_58_2Tu_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_59_2Tu_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_60_2Tu_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_6_0Su_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_61_2Tu_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_62_2Tu_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_63_2Tu_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_64_2Tu_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_65_2Tu_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_66_2Tu_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_67_2Tu_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_68_2Tu_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_69_2Tu_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_70_2Tu_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_7_0Su_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_71_2Tu_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_72_3We_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_73_3We_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_74_3We_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_75_3We_03:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_76_3We_04:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_77_3We_05:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_78_3We_06:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_79_3We_07:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_80_3We_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_8_0Su_08:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_81_3We_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_82_3We_10:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_83_3We_11:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_84_3We_12:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_85_3We_13:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_86_3We_14:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_87_3We_15:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_88_3We_16:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_89_3We_17:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_90_3We_18:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_9_0Su_09:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_91_3We_19:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_92_3We_20:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_93_3We_21:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_94_3We_22:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_95_3We_23:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_96_4Th_00:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_97_4Th_01:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_98_4Th_02:05.tif
/home/matthewc/microaccessibility/times/data/tiffs/walk_eateries_99_4Th_03:05.tif'''.split('\n')


def parseToTime(text):
    spt = text[:-4].split('_')

    days = {
        '0Su' : 'Sunday',
        '1Mo' : 'Monday',
        '2Tu' : 'Tuesday',
        '3We' : 'Wednesday',
        '4Th' : 'Thursday',
        '5Fr' : 'Friday',
        '6Sa' : 'Saturday'
        }

    day = days[spt[3]]

    sptime = spt[4].split(':')

    hours = int(sptime[0])

    if hours == 0:
        hours = 12
        pm = False

    elif hours < 13:
        pm = False

    else:
        hours = hours % 12
        pm = True

    if pm:
        ap = 'PM'
    else:
        ap = 'AM'

    final = '%s %s:%s %s' % (day, hours, sptime[1], ap)
    return final


def run_script(iface):
    canvas = iface.mapCanvas()

    img = QImage(QSize(1920, 1080), QImage.Format_ARGB32_Premultiplied)
    color = QColor(255, 255, 255)
    p = QPainter(img)

    for path in paths:
        #accessibilityLayer.setDataProvider(path)

        # http://www.qgisworkshop.org/html/workshop/python_in_qgis_tutorial2.html
        rlayer = iface.addRasterLayer(path)
        # http://gis.stackexchange.com/questions/26846
        rlayer.loadNamedStyle('/home/matthewc/microaccessibility/times/colors.qml')

        # add the vector layers
        poly = iface.addVectorLayer('dbname=\'matthewc\' host=localhost port=5432 user=\'matthewc\' password=\'password\' sslmode=disable key=\'tid\' srid=4326 type=POLYGON table="public"."ucsb_final_polygon" (way) sql=', 'poly', 'postgres')
        poly.loadNamedStyle('/home/matthewc/microaccessibility/times/poly.qml')
        
        line = iface.addVectorLayer('dbname=\'matthewc\' host=localhost port=5432 user=\'matthewc\' password=\'password\' sslmode=disable key=\'tid\' srid=4326 type=LINESTRING table="public"."ucsb_final_line" (way) sql=', 'line', 'postgres')
        line.loadNamedStyle('/home/matthewc/microaccessibility/times/line.qml')

        renderer = canvas.mapRenderer()

        img.fill(color.rgb())
        p.begin(img)
        p.setRenderHint(QPainter.Antialiasing)
        renderer.setOutputSize(img.size(), img.logicalDpiX())
        renderer.render(p)
        
        p.setFont(QFont("Ubuntu", 48, QFont.Bold))
        p.setPen(QColor(0,0,0))
        p.drawText(10, 58, parseToTime(path))

        p.end()
        img.save(path + ".png", "png")

        QgsMapLayerRegistry.instance().removeMapLayer(rlayer.id())
        QgsMapLayerRegistry.instance().removeMapLayer(poly.id())
        QgsMapLayerRegistry.instance().removeMapLayer(line.id())
