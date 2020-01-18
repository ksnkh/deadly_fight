# key = [number of frames, frame width, list of frames duration, loop, if char can turn during animation]
subzero_animations = {'stand': [12, 51, [1] * 12, [0, 11], True],
                      'walk': [9, 52, [1] * 9, [0, 8], True],
                      'jump': [3, 50, [3, 3, 5], [0, 2], False],
                      'move_jump': [8, 49, [1] * 8, [], False],
                      'duck': [3, 52, [1] * 5, [2, 2], False]}
