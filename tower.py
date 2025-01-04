import pyxel
import random
import math
import json

# 画面サイズ
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 200

# プレイヤーの初期位置とパラメータ
PLAYER_X = 72
PLAYER_Y = 100
PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2
JUMP_POWER = 3.5
GRAVITY = 0.2

# 床の高さ
FLOOR_HEIGHT = 8

# スクロール速度
SCROLL_SPEED = 0.5

# 床のパラメータ
FLOOR_Y_INTERVAL = 32  # 床の間隔
FLOOR_MIN_WIDTH = 32  # 床の最小幅
FLOOR_MAX_WIDTH = 96  # 床の最大幅

# トゲのパラメータ
SPIKE_HEIGHT = 4


MUSIC = [['c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3rrrrrrrrrrrrrrrrrrrrb2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrrrra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rrf2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrd3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3rrrrrrrrrrrrrrrrrrrrb2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrrrra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rrf2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrrrr', 'S', '112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333322211100000000000000000000112223344455666666666666663333112223344455666666666666663333112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333333333333333333333333333333333333333333333333333333332221110000000000000112223344455666666666666666666666655555555555555555555444444444444444444443333333322211100112223344455666666666666666666666655555555555555555555444444444444444444443333333322211100112223344455666666666666666666666655555555555555555533332221112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333322211100000112223344455666666666666666666666655555555555555555533332221112223344455666666666666666666666655555555555555555533332221112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333322211100000000000000000000112223344455666666666666663333112223344455666666666666663333112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333333333333333333333333333333333333333333333333333333332221110000000000000112223344455666666666666666666666655555555555555555555444444444444444444443333333322211100112223344455666666666666666666666655555555555555555555444444444444444444443333333322211100112223344455666666666666666666666655555555555555555533332221112223344455666666666666663333112223344455666666666666663333112223344455666666666666666666666655555555555555555555444444444444444444443333333333333333333333333333333333333333333333333333333333333333333333333333333333333332221110000000000000', 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnn', 1],['a0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrra0a0a0a0a0a0a0a0a0a0a0rrrrrrrrrrrrrrrrrrra1a1a1a1a1a1a1a1a1a1a1rrrra1a1a1a1a1a1a1a1a1a1a1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf0f0f0f0f0f0f0f0f0f0f0rrrrrrrrrrrrrrrrrrrf1f1f1f1f1f1f1f1f1f1f1rrrrf1f1f1f1f1f1f1f1f1f1f1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg0g0g0g0g0g0g0g0g0g0g0rrrrrrrrrrrrrrrrrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg1g1g1g1g1g1g1g1g1g1g1rrrrg#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0rrrrrrrrrrrrrrrrrrrg#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1rrrrg#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1rrrrg#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0g#0rrrrrrrrg#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1g#1rrrrrrrr', 'T', '777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777770000000000000000000777777777770000777777777770000777777777777777777777700000000777777777777777777777700000000', 'n', 1],['rrrrrrrrrrrrrrrc3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3rrrrrrrrrrrrrrrrrrrrb2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrrrra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rrf2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrd3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3rrrrrrrrrrrrrrrrrrrrb2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrrrra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rra2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2rrf2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3d3g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2g2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2rrrrrrrrrrr', 'S', '111111111000000111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000000000000111111122222222222222222221111111111122222222222222222221111111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110000000000000111111122222222222222222222222222222222222222222222222222222222222222222221111111111111100111111122222222222222222222222222222222222222222222222222222222222222222221111111111111100111111122222222222222222222222222222222222222222222211111111111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111100000111111122222222222222222222222222222222222222222222211111111111111122222222222222222222222222222222222222222222211111111111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000000000000111111122222222222222222221111111111122222222222222222221111111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110000000000000111111122222222222222222222222222222222222222222222222222222222222222222221111111111111100111111122222222222222222222222222222222222222222222222222222222222222222221111111111111100111111122222222222222222222222222222222222222222222211111111111111122222222222222222221111111111122222222222222222221111111111122222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000', 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnnnnnnnnnnnnnnnnnnn', 1],['rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'T', '0', 'n', 1]]

class Player:
    def __init__(self):
        self.x = PLAYER_X
        self.y = PLAYER_Y
        self.vy = 0
        self.is_jumping = False
        self.color = random.randint(1, 8)

    def update(self):
        # 左右移動
        if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)):
            self.x -= PLAYER_SPEED
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)):
            self.x += PLAYER_SPEED

        # ジャンプ
        if (
            pyxel.btnp(pyxel.KEY_SPACE)
            or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)
            or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B)
            or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X)
            or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)
            ) and not self.is_jumping:
            pyxel.sounds[3].set(
                "D3G3",  # ドミソの和音で明るい感じに
                "S",  # トライアングル系の音色で軽快さを出す
                "7",  # 音量は大きめに
                "s",  # エフェクトはなし
                10,  # 再生速度を速めて短く切る
            )
            pyxel.play(3, 3)
            self.vy = -JUMP_POWER
            self.is_jumping = True

        # 重力
        self.vy += GRAVITY
        self.y += self.vy

        # 画面外に出ないようにする
        self.x = max(0, min(self.x, SCREEN_WIDTH - PLAYER_WIDTH))

    def draw(self):
        pyxel.rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT, self.color)

    def check_floor_collision(self, floors, scroll_y):  # scroll_y を引数に追加
        for floor in floors:
            # プレイヤーの底辺が床の上面に接触しているか
            if (
                self.x < floor.x + floor.width
                and self.x + PLAYER_WIDTH > floor.x
                and self.y + PLAYER_HEIGHT > floor.y - scroll_y  # スクロール量を考慮
                and self.y + PLAYER_HEIGHT < floor.y - scroll_y + FLOOR_HEIGHT  # スクロール量を考慮
                and self.vy >= 0  # 下向きに移動しているときのみ衝突判定
            ):
                self.y = floor.y - scroll_y - PLAYER_HEIGHT  # スクロール量を考慮
                self.vy = 0
                self.is_jumping = False
                return  # 衝突したらループを抜ける

    def check_spike_collision(self, spikes, scroll_y):  # scroll_y を引数に追加
        for spike in spikes:
            # プレイヤーの中心座標がトゲの矩形範囲内にあるか
            if (
                self.x < spike.x + SPIKE_HEIGHT * 2 - 1
                and self.x + PLAYER_WIDTH > spike.x + 1
                and self.y < spike.y - scroll_y + SPIKE_HEIGHT - 1  # スクロール量を考慮
                and self.y + PLAYER_HEIGHT > spike.y - scroll_y + 1  # スクロール量を考慮
            ):
                # 衝突時の処理 (ゲームオーバーなど)
                return True
        return False
    
    def check_out_of_boundary(self):
        if (self.y < -1 * PLAYER_HEIGHT or self.y > SCREEN_HEIGHT + PLAYER_HEIGHT):
            return True
        else:
            return False


class Floor:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def draw(self, scroll_y):  # scroll_y を引数に追加
        pyxel.rect(self.x, self.y - scroll_y, self.width, FLOOR_HEIGHT, 3)  # y座標をスクロール量でずらす


class Spike:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, scroll_y):  # scroll_y を引数に追加
        pyxel.tri(self.x, self.y - scroll_y + SPIKE_HEIGHT, self.x + SPIKE_HEIGHT, self.y - scroll_y, 
                  self.x + SPIKE_HEIGHT * 2, self.y - scroll_y + SPIKE_HEIGHT, 10)  # y座標をスクロール量でずらす

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, math.pi*2)  # 0〜360度の方向をランダムに決定
        speed = random.uniform(1, 3)  # 速度をランダムに決定
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 30  # パーティクルの寿命
        self.color = random.randint(1, 8)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.vy < 3:
            self.vy += GRAVITY / 2
        self.life -= 1

    def draw(self):
        if self.life > 0:
            pyxel.pset(self.x, self.y, self.color)

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="天空の塔")
        # リソースファイルの読み込み (後で作成)
        # pyxel.load("my_resource.pyxres")  
        self.music = MUSIC
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def generate_initial_floors(self):
        y = SCREEN_HEIGHT - FLOOR_HEIGHT

        # Initial platform
        self.floors.append(Floor(50, y, 50))
        y -= FLOOR_Y_INTERVAL

        while y > -SCREEN_HEIGHT:
            width = random.randint(FLOOR_MIN_WIDTH, FLOOR_MAX_WIDTH)
            x = random.randint(0, SCREEN_WIDTH - width)
            self.floors.append(Floor(x, y, width))

            # 床の上にトゲを配置
            for i in range(random.randint(0, 3)):
                spike_x = random.randint(x, x + width - SPIKE_HEIGHT * 2)
                self.spikes.append(Spike(spike_x, y - SPIKE_HEIGHT))

            y -= FLOOR_Y_INTERVAL
        self.floors.reverse()


    def update(self):
        for particle in self.particles:
            particle.update()

        if not self.is_game_over:  # ゲームオーバーでない場合のみ更新
            self.player.update()
            self.scroll_y += SCROLL_SPEED + (self.scroll_y // 100) * 0.1

            # 新しい床の生成
            if self.floors[-1].y - self.scroll_y < SCREEN_HEIGHT - FLOOR_Y_INTERVAL:
                self.generate_floor()

            # 衝突判定
            self.player.check_floor_collision(self.floors, self.scroll_y)
            if self.player.check_spike_collision(self.spikes, self.scroll_y):
                self.is_game_over = True
            if self.player.check_out_of_boundary():
                self.is_game_over = True

            if self.is_game_over:
                pyxel.sounds[3].set(
                    "C4 C3 C2",  # 短い音符を組み合わせて、破裂感を出す
                    "N",  # ノイズ音を使用
                    "765",  # 音量を徐々に下げていく
                    "N",  # エフェクトはなし
                    15,  # 再生速度を速くする
                )
                pyxel.play(3, 3)
                [pyxel.stop(i) for i in [0,1,2]]
                for _ in range(30):  # 30個のパーティクルを生成
                   self.particles.append(Particle(self.player.x + PLAYER_WIDTH/2, self.player.y + PLAYER_HEIGHT/2))

        else:
            # ゲームオーバー時の処理 (リトライなど)
            if (
                pyxel.btnp(pyxel.KEY_R)
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B)
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X)
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)
                ):  # Rキーでリトライ
                self.reset_game()

        # Play music
        if (pyxel.play_pos(0) is None
            and not self.is_game_over):
            for ch, sound in enumerate(self.music):
                pyxel.sound(ch).set(*sound)
                pyxel.play(ch, ch, loop=True)

    def reset_game(self):  # ゲームをリセットするメソッド
        self.player = Player()
        self.scroll_y = 0
        self.floors = []
        self.spikes = []
        self.particles = []
        self.is_game_over = False
        self.generate_initial_floors()



    def generate_floor(self):
        y = self.floors[-1].y + FLOOR_Y_INTERVAL
        width = random.randint(FLOOR_MIN_WIDTH, FLOOR_MAX_WIDTH)
        x = random.randint(0, SCREEN_WIDTH - width)
        self.floors.append(Floor(x, y, width))

        # 床の上にトゲを配置
        for i in range(random.randint(0, 3)):
            spike_x = random.randint(x, x + width - SPIKE_HEIGHT * 2)
            self.spikes.append(Spike(spike_x, y - SPIKE_HEIGHT))

    def draw(self):
        pyxel.cls(0)

        for floor in self.floors:
            floor.draw(self.scroll_y)

        # トゲの描画
        for spike in self.spikes:
            spike.draw(self.scroll_y)

        # Draw score
        pyxel.text(0, 0, f"Score: {self.scroll_y:.0f}", 7)

        # Draw particles.
        for particle in self.particles:
            particle.draw()

        if self.is_game_over:  # ゲームオーバー時の表示
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 8, "GAME OVER", pyxel.frame_count % 15 + 1)
            pyxel.text(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 8, "PRESS BUTTON TO RETRY", 8)
        else:
            self.player.draw()

App()