liu_kang_move_animations = {'stand': [8, [58] * 8, [1] * 8, [0, 7], True, False],
                            'walk_f': [9, [59, 46, 44, 45, 44, 47, 43, 47], [1] * 9, [0, 8], True, False],
                            'walk_b': [9, [59, 46, 44, 45, 44, 47, 43, 47], [1] * 9, [0, 8], True, False],
                            'jump': [4, [62, 55, 59, 50], [3, 3, 5, 3], [0, 3],  False, False],
                            'move_jump': [9, [47, 41, 51, 56, 52, 43, 47, 57, 50], [1] * 9, [1, 8], False, False],
                            'duck': [3, [57, 59,  48], [1] * 3, [0,2], True, False],
                            'block': [1, [44], [1], [0, 0], False, False],

                            'low_punch': [3, [67, 63, 77], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],
                            'low_kick': [5, [56, 51, 49, 55, 74], [1, 1, 1, 1, 3],
                                         [], False, [[4], 'weak_hit', 50, [6, 0]]],
                            'high_kick': [5, [56, 50, 50, 56, 72], [1, 1, 1, 1, 3], [], False,
                                          [[4], 'weak_hit', 50, [6, 0]]],
                            'high_punch': [3, [59, 66, 72], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],

                            'uppercut': [6, [58, 69, 68, 48, 66, 47], [1, 1, 1, 6, 1, 1], [], False,
                                        [[2, 3, 4], 'heavy_hit', 60, [10, -20]]],
                            'sweep_kick': [7, [60, 56, 74, 88, 44, 70, 47], [1] * 7, [], False,
                                           [[3, 4], 'trip', 40, [0, 0]]],
                            'roundhouse': [7, [75, 58, 48, 67, 49, 56, 46], [1] * 7, [], False,
                                          [[2, 3], 'heavy_hit', 70, [10, -20]]],
                            'air_kick': [2, [62, 72], [3, 3], [], False, [[1], 'heavy_hit', 40, [7, 0]]],
                            'pinwheel': [13, [64, 94, 71, 95, 70, 79, 73, 58, 70, 69, 46, 65, 48],
                                         [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1], False, [[1], 'heavy_hit', 40, [2, -20]]],

                            'weak_hit': [5, [63, 47, 48, 63, 52], [2] * 5, [], False, False],
                            'heavy_hit': [8, [82, 86, 70, 60, 63, 59, 82, 80],
                                          [2, 5, 2, 2, 2, 2, 2, 2], [], False, False],
                            'trip': [5, [67, 86, 68, 91, 81], [1] * 5, [], False, False],
                            'stand_up': [7, [69, 57, 85, 71, 40, 45, 50], [1] * 7, [], False, False],
                            'thrown': [7, [61, 73, 66, 62, 60, 84, 81], [1, 1, 1, 1, 1, 1, 10], [], False, False],

                            'dead': [7, [56, 57, 59, 58, 58, 57, 45], [2] * 7, [0, 6], False, False]
                            }


liu_kang_attack_animations = ['low_punch', 'high_punch', 'low_kick', 'high_kick', 'uppercut', 'sweep_kick',
                              'roundhouse', 'air_kick', 'bicycle_kick']
