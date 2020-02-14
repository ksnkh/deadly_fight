liu_kang_move_animations = {'stand': [8, [55, 55, 59, 59, 55, 55, 55, 48], [1] * 8, [0, 7], True, False],
                            'walk_f': [9, [54, 46, 44, 42, 44, 47, 45, 45, 38], [1] * 9, [0, 8], True, False],
                            'walk_b': [9, [54, 46, 44, 42, 44, 47, 45, 45, 38], [1] * 9, [0, 8], True, False],
                            'jump': [4, [59, 55, 60, 45], [3, 3, 5, 3], [0, 3],  False, False],
                            'move_jump': [9, [43, 43, 50, 54, 51, 41, 46, 56, 41], [1] * 9, [1, 8], False, False],
                            'duck': [3, [57, 59, 48], [1] * 5, [2, 2], False, False],
                            'block': [1, [44], [1], [0, 0], False, False],

                            'low_punch': [3, [65, 63, 74], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],
                            'high_punch': [3, [57, 64, 70], [1, 1, 5], [], False, [[2], 'weak_hit', 30, [4, 0]]],
                            'low_kick': [5, [52, 47, 45, 53, 72], [1, 1, 1, 1, 3],
                                         [], False, [[4], 'weak_hit', 50, [6, 0]]],
                            'high_kick': [5, [53, 46, 46, 52, 65], [1, 1, 1, 1, 3], [], False,
                                          [[4], 'weak_hit', 50, [6, 0]]],
                            'uppercut': [6, [55, 66, 65, 45, 63, 44], [1, 1, 1, 6, 1, 1], [], False,
                                        [[2, 3, 4], 'heavy_hit', 60, [10, -20]]],
                            'sweep_kick': [7, [60, 56, 74, 87, 43, 69, 46], [1] * 7, [], False,
                                           [[3, 4], 'trip', 40, [0, 0]]],
                            'roundhouse': [7, [73, 58, 48, 67, 49, 56, 46], [1] * 7, [], False,
                                          [[2, 3], 'heavy_hit', 70, [10, -20]]],
                            'air_kick': [2, [62, 72], [3, 3], [], False, [[1], 'heavy_hit', 40, [7, 0]]],
                            # do this
                            'pinwheel': [13, [64, 94, 71, 95, 70, 79, 73, 58, 70, 69, 46, 65, 48],
                                         [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1], False, [[1], 'heavy_hit', 40, [2, -20]]],
                            'weak_hit': [5, [60, 46, 47, 62, 50], [2] * 5, [], False, False],
                            'heavy_hit': [8, [82, 86, 70, 60, 63, 59, 82, 80],
                                          [2, 5, 2, 2, 2, 2, 2, 2], [], False, False],
                            'trip': [5, [67, 86, 68, 91, 81], [1] * 5, [], False, False],

                            'stand_up': [7, [69, 57, 85, 71, 40, 45, 50], [1] * 7, [], False, False],
                            'thrown': [7, [61, 73, 66, 62, 60, 84, 81], [1, 1, 1, 1, 1, 1, 10], [], False, False],
                            'dead': [7, [56, 57, 59, 58, 58, 57, 45], [2] * 7, [0, 6], False, False]
                            }


liu_kang_attack_animations = ['low_punch', 'high_punch', 'low_kick', 'high_kick', 'uppercut', 'sweep_kick', 'roundhouse',
                             'air_kick', 'pinwheel']
