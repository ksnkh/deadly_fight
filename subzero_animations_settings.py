# key = [number of frames,
# frame width,
# list of frames duration,
# loop,
# if char can turn during animation,
# frame with punch and damage ]
subzero_move_animations = {'stand': [12, [51] * 12, [1] * 12, [0, 11], True, False],
                           'walk_f': [9, [52] * 9, [1] * 9, [0, 8], True, False],
                           'walk_b': [9, [52] * 9, [1] * 9, [0, 8], True, False],
                           'jump': [3, [50] * 3, [3, 3, 5], [0, 2], False, False],
                           'move_jump': [8, [49] * 8, [1] * 8, [1, 7], False, False],
                           'duck': [3, [52] * 5, [1] * 5, [2, 2], False, False],
                           'block': [1, [50], [1], [0, 0], False, False],
                           'high_punch': [3, [60, 60, 75], [1, 1, 5], [], False, [2, 'weak_hit', 30, [4, 0]]],
                           'weak_hit': [3, [56, 59, 101], [1] * 3, [], False, False]}

subzero_attack_animations = ['low_punch', 'high_punch', 'low_kick', 'high_kick']
