class AlphabetRules:

    def __init__(self):
        pass

    def detect_A(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 1:
            return None
        if features.get('right_finger_count', 0) != 1:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if not features.get('right_thumb_up', False):
            return None
        left_curled = features.get('left_index_curled', False) and features.get('left_middle_curled', False) and features.get('left_ring_curled', False) and features.get('left_little_curled', False)
        right_curled = features.get('right_index_curled', False) and features.get('right_middle_curled', False) and features.get('right_ring_curled', False) and features.get('right_little_curled', False)
        if not left_curled or not right_curled:
            return None
        if features.get('thumbs_touching', False):
            return None
        left_direction = features.get('left_thumb_direction', None)
        right_direction = features.get('right_thumb_direction', None)
        if left_direction is not None and right_direction is not None:
            if left_direction != 'right':
                return None
            if right_direction != 'left':
                return None
        return 'A'

    def detect_B(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 1:
            return None
        if features.get('right_finger_count', 0) != 1:
            return None
        if not features.get('thumbs_touching', False):
            return None
        return 'B'

    def detect_C(self, features):
        if features.get('both_hands', False):
            return None
        if not (features.get('left_hand', False) or features.get('right_hand', False)):
            return None
        if features.get('left_hand', False):
            prefix = 'left'
        else:
            prefix = 'right'
        if not features.get(f'{prefix}_thumb_up', False):
            return None
        if features.get(f'{prefix}_index_up', False):
            return None
        if features.get(f'{prefix}_middle_up', False):
            return None
        if features.get(f'{prefix}_ring_up', False):
            return None
        if features.get(f'{prefix}_little_up', False):
            return None
        index_angle = features.get(f'{prefix}_index_angle', 0)
        middle_angle = features.get(f'{prefix}_middle_angle', 0)
        ring_angle = features.get(f'{prefix}_ring_angle', 0)
        little_angle = features.get(f'{prefix}_little_angle', 0)
        minimum_angle = 50
        maximum_angle = 140
        if not minimum_angle <= index_angle <= maximum_angle:
            return None
        if not minimum_angle <= middle_angle <= maximum_angle:
            return None
        if not minimum_angle <= ring_angle <= maximum_angle:
            return None
        if not minimum_angle <= little_angle <= maximum_angle:
            return None
        if features.get(f'{prefix}_thumb_touch_index', False):
            return None
        if features.get(f'{prefix}_thumb_touch_middle', False):
            return None
        if features.get(f'{prefix}_thumb_touch_ring', False):
            return None
        if features.get(f'{prefix}_thumb_touch_little', False):
            return None
        return 'C'

    def detect_D(self, features):
        if not features.get('both_hands', False):
            return None

        left_thumb_only = (
            features.get('left_finger_count', 0) == 1
            and features.get('left_thumb_up', False)
            and not features.get('left_index_up', False)
            and not features.get('left_middle_up', False)
            and not features.get('left_ring_up', False)
            and not features.get('left_little_up', False)
        )

        right_thumb_only = (
            features.get('right_finger_count', 0) == 1
            and features.get('right_thumb_up', False)
            and not features.get('right_index_up', False)
            and not features.get('right_middle_up', False)
            and not features.get('right_ring_up', False)
            and not features.get('right_little_up', False)
        )

        left_thumb_index = (
            features.get('left_finger_count', 0) == 2
            and features.get('left_thumb_up', False)
            and features.get('left_index_up', False)
            and not features.get('left_middle_up', False)
            and not features.get('left_ring_up', False)
            and not features.get('left_little_up', False)
        )

        right_thumb_index = (
            features.get('right_finger_count', 0) == 2
            and features.get('right_thumb_up', False)
            and features.get('right_index_up', False)
            and not features.get('right_middle_up', False)
            and not features.get('right_ring_up', False)
            and not features.get('right_little_up', False)
        )

        index_distance = features.get('index_fingers_distance', 999.0)

        if index_distance > 0.12:
            return None

        if left_thumb_only and right_thumb_index:
            return 'D'

        if right_thumb_only and left_thumb_index:
            return 'D'

        return None

    def detect_E(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 2:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if not features.get('left_index_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if features.get('right_finger_count', 0) != 2:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        index_distance = features.get('index_fingers_distance', 999)
        if index_distance > 0.1:
            return None
        return 'E'

    def detect_F(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_index_up', False):
            return None
        if not features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        return 'F'

    def detect_G(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_thumb_curled', False):
            return None
        if not features.get('left_index_curled', False):
            return None
        if not features.get('left_middle_curled', False):
            return None
        if not features.get('left_ring_curled', False):
            return None
        if not features.get('left_little_curled', False):
            return None
        if not features.get('right_thumb_curled', False):
            return None
        if not features.get('right_index_curled', False):
            return None
        if not features.get('right_middle_curled', False):
            return None
        if not features.get('right_ring_curled', False):
            return None
        if not features.get('right_little_curled', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        vertical_distance = features.get('hand_vertical_distance', 0)
        if vertical_distance < 0.1:
            return None
        return 'G'

    def detect_K(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_thumb_up', False):
            return None
        if features.get('left_index_up', False):
            return None
        if not features.get('left_ring_up', False):
            return None
        if not features.get('left_little_up', False):
            return None
        if features.get('left_thumb_touch_index', False):
            return None
        if features.get('left_finger_count', 0) < 3:
            return None
        if features.get('right_finger_count', 0) != 2:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        return 'K'

    def detect_L(self, features):
        if features.get('both_hands', False):
            return None
        if features.get('left_hand', False):
            prefix = 'left'
        elif features.get('right_hand', False):
            prefix = 'right'
        else:
            return None
        if not features.get(f'{prefix}_thumb_up', False):
            return None
        if not features.get(f'{prefix}_index_up', False):
            return None
        if features.get(f'{prefix}_middle_up', False):
            return None
        if features.get(f'{prefix}_ring_up', False):
            return None
        if features.get(f'{prefix}_little_up', False):
            return None
        return 'L'

    def detect_M(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 3:
            return None
        if not features.get('left_index_up', False):
            return None
        if not features.get('left_middle_up', False):
            return None
        if not features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if features.get('left_thumb_up', False):
            return None
        if not features.get('left_thumb_curled', False):
            return None
        if not features.get('left_little_curled', False):
            return None
        if not features.get('left_thumb_touch_little', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if not features.get('right_hand_above_left', False):
            return None
        if features.get('thumbs_touching', False):
            return None
        return 'M'

    def detect_N(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 2:
            return None
        if not features.get('left_index_up', False):
            return None
        if not features.get('left_middle_up', False):
            return None
        if features.get('left_thumb_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if not features.get('left_thumb_curled', False):
            return None
        if not features.get('left_ring_curled', False):
            return None
        if not features.get('left_little_curled', False):
            return None
        if features.get('right_finger_count', 0) != 5:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if not features.get('right_ring_up', False):
            return None
        if not features.get('right_little_up', False):
            return None
        if not features.get('right_hand_above_left', False):
            return None
        if features.get('thumbs_touching', False):
            return None
        return 'N'

    def detect_O(self, features):
        if features.get('both_hands', False):
            return None
        if features.get('left_hand', False):
            prefix = 'left'
        elif features.get('right_hand', False):
            prefix = 'right'
        else:
            return None
        if not features.get(f'{prefix}_thumb_up', False):
            return None
        if features.get(f'{prefix}_index_up', False):
            return None
        if features.get(f'{prefix}_middle_up', False):
            return None
        if features.get(f'{prefix}_ring_up', False):
            return None
        if features.get(f'{prefix}_little_up', False):
            return None
        if features.get(f'{prefix}_finger_count', 0) != 1:
            return None
        thumb_index_distance = features.get(f'{prefix}_thumb_index_distance', 999)
        if thumb_index_distance > 0.24:
            return None
        return 'O'

    def detect_P(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 4:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if features.get('left_index_up', False):
            return None
        if not features.get('left_middle_up', False):
            return None
        if not features.get('left_ring_up', False):
            return None
        if not features.get('left_little_up', False):
            return None
        if not features.get('left_index_curled', False):
            return None
        if not features.get('left_thumb_touch_index', False):
            return None
        if features.get('right_finger_count', 0) != 2:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        index_distance = features.get('index_fingers_distance', 999)
        if index_distance > 0.12:
            return None
        return 'P'

    def detect_V(self, features):
        if features.get('both_hands', False):
            return None
        if features.get('left_hand', False):
            prefix = 'left'
        elif features.get('right_hand', False):
            prefix = 'right'
        else:
            return None
        if features.get(f'{prefix}_finger_count', 0) != 2:
            return None
        if not features.get(f'{prefix}_index_up', False):
            return None
        if not features.get(f'{prefix}_middle_up', False):
            return None
        if features.get(f'{prefix}_thumb_up', False):
            return None
        if features.get(f'{prefix}_ring_up', False):
            return None
        if features.get(f'{prefix}_little_up', False):
            return None
        index_middle_distance = features.get(f'{prefix}_index_middle_distance', 0)
        if index_middle_distance < 0.38:
            return None
        return 'V'

    def detect_T(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 2:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if not features.get('left_index_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if features.get('right_finger_count', 0) != 2:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        index_distance = features.get('index_fingers_distance', 999.0)
        if index_distance < 0.2:
            return None
        if index_distance > 0.5:
            return None
        line_distance = features.get('right_index_left_line_distance', 999.0)
        if line_distance > 0.05:
            return None
        return 'T'

    def detect_U(self, features):
        if features.get('both_hands', False):
            return None
        if features.get('left_hand', False):
            prefix = 'left'
        elif features.get('right_hand', False):
            prefix = 'right'
        else:
            return None
        if features.get(f'{prefix}_finger_count', 0) != 2:
            return None
        if not features.get(f'{prefix}_index_up', False):
            return None
        if not features.get(f'{prefix}_middle_up', False):
            return None
        if features.get(f'{prefix}_thumb_up', False):
            return None
        if features.get(f'{prefix}_ring_up', False):
            return None
        if features.get(f'{prefix}_little_up', False):
            return None
        index_middle_distance = features.get(f'{prefix}_index_middle_distance', 0)
        if index_middle_distance >= 0.38:
            return None
        return 'U'

    def detect_W(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 5:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if not features.get('left_index_up', False):
            return None
        if not features.get('left_middle_up', False):
            return None
        if not features.get('left_ring_up', False):
            return None
        if not features.get('left_little_up', False):
            return None
        if features.get('right_finger_count', 0) < 4:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if not features.get('right_ring_up', False):
            return None
        if not features.get('thumbs_touching', False):
            return None
        if not features.get('right_hand_above_left', False):
            return None
        return 'W'

    def detect_R(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_thumb_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if not features.get('left_thumb_curled', False):
            return None
        if not features.get('left_middle_curled', False):
            return None
        if not features.get('left_ring_curled', False):
            return None
        if not features.get('left_little_curled', False):
            return None
        if features.get('right_thumb_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if not features.get('right_ring_up', False):
            return None
        if not features.get('right_little_up', False):
            return None
        if features.get('right_finger_count', 0) != 4:
            return None
        if not features.get('right_hand_above_left', False):
            return None
        return 'R'

    def detect_Q(self, features):
        if not features.get('both_hands', False):
            return None

        if features.get('left_finger_count', 0) != 1:
            return None
        if not features.get('left_index_up', False):
            return None
        if features.get('left_thumb_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if not features.get('left_index_curled', False):
            return None
        if not features.get('left_thumb_curled', False):
            return None

        if features.get('right_finger_count', 0) != 4:
            return None
        if not features.get('right_thumb_up', False):
            return None
        if features.get('right_index_up', False):
            return None
        if not features.get('right_middle_up', False):
            return None
        if not features.get('right_ring_up', False):
            return None
        if not features.get('right_little_up', False):
            return None
        if not features.get('right_index_curled', False):
            return None
        if not features.get('right_thumb_touch_index', False):
            return None

        if not features.get('right_hand_above_left', False):
            return None

        vertical_distance = features.get(
            'hand_vertical_distance',
            999.0
        )

        if vertical_distance < 0.07:
            return None

        if vertical_distance > 0.13:
            return None

        index_distance = features.get(
            'index_fingers_distance',
            999.0
        )

        # The Q capture has the two index fingers separated
        # by roughly 0.18 - 0.34 in the recorded frames.
        # Allow some extra live-camera variation.
        if index_distance < 0.12:
            return None

        if index_distance > 0.40:
            return None

        return 'Q'

    def detect_S(self, features):
        if not features.get('both_hands', False):
            return None
        if features.get('left_finger_count', 0) != 1:
            return None
        if not features.get('left_thumb_up', False):
            return None
        if features.get('left_index_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if features.get('right_finger_count', 0) != 1:
            return None
        if features.get('right_thumb_up', False):
            return None
        if features.get('right_index_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if not features.get('right_little_up', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        return 'S'

    def detect_X(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_index_up', False):
            return None
        if not features.get('right_index_up', False):
            return None
        if features.get('left_middle_up', False):
            return None
        if features.get('left_ring_up', False):
            return None
        if features.get('left_little_up', False):
            return None
        if features.get('right_middle_up', False):
            return None
        if features.get('right_ring_up', False):
            return None
        if features.get('right_little_up', False):
            return None
        if not features.get('left_thumb_up', False):
            return None
        if not features.get('right_thumb_up', False):
            return None
        if not features.get('thumbs_touching', False):
            return None
        if not features.get('index_fingers_crossed', False):
            return None
        return 'X'

    def detect_Z(self, features):
        if not features.get('both_hands', False):
            return None
        if not features.get('left_thumb_up', False):
            return None
        if features.get('left_finger_count', 0) != 1:
            return None
        if not features.get('right_index_up', False):
            return None
        if not features.get('left_hand_above_right', False):
            return None
        return 'Z'