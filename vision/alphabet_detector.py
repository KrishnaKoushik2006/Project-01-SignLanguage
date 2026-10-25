from vision.alphabet_rules import AlphabetRules


class AlphabetDetector:

    def __init__(self):

        self.rules = AlphabetRules()

        # -------------------------------------------------
        # H Motion State
        # -------------------------------------------------

        self.h_started = False
        self.h_crossing_seen = False

        self.h_missing_frames = 0
        self.h_max_missing_frames = 8

        # -------------------------------------------------
        # H Result Hold
        # -------------------------------------------------

        self.h_result_frames = 0
        self.h_result_hold = 30

        # -------------------------------------------------
        # I Motion State
        # -------------------------------------------------

        self.i_started = False

        self.i_start_distance = 0
        self.i_movement_threshold = 0.18
        self.i_min_start_distance = 0.95

        # -------------------------------------------------
        # I Result Hold
        # -------------------------------------------------

        self.i_result_frames = 0
        self.i_result_hold = 30

        # -------------------------------------------------
        # J Motion State
        # -------------------------------------------------

        self.j_started = False
        self.j_movement_seen = False

        self.j_missing_frames = 0
        self.j_max_missing_frames = 8

        # -------------------------------------------------
        # J Result Hold
        # -------------------------------------------------

        self.j_result_frames = 0
        self.j_result_hold = 30

        # -------------------------------------------------
        # Y Motion State
        # -------------------------------------------------

        self.y_started = False
        self.y_movement_frames = 0

        self.y_baseline_thumb_distance = 0
        self.y_movement_threshold = 0.45
        self.y_required_movement_frames = 2

        # -------------------------------------------------
        # Y Result Hold
        # -------------------------------------------------

        self.y_result_frames = 0
        self.y_result_hold = 30

    # -------------------------------------------------
    # Detect H Movement
    # -------------------------------------------------

    def detect_H(self, features):

        if self.h_result_frames > 0:

            self.h_result_frames -= 1

            return "H"

        both_hands = features.get(
            "both_hands",
            False
        )

        if both_hands:

            left_above = features.get(
                "left_hand_above_right",
                False
            )

            right_above = features.get(
                "right_hand_above_left",
                False
            )

            self.h_missing_frames = 0

            if not self.h_started:

                if right_above:

                    self.h_started = True
                    self.h_crossing_seen = False

                return None

            if self.h_crossing_seen:

                if left_above:

                    self.h_started = False
                    self.h_crossing_seen = False
                    self.h_missing_frames = 0

                    self.h_result_frames = (
                        self.h_result_hold
                    )

                    return "H"

                return None

            if left_above:

                self.h_started = False
                self.h_crossing_seen = False
                self.h_missing_frames = 0

                self.h_result_frames = (
                    self.h_result_hold
                )

                return "H"

            return None

        if self.h_started:

            self.h_missing_frames += 1
            self.h_crossing_seen = True

            if (
                self.h_missing_frames
                > self.h_max_missing_frames
            ):

                self.h_started = False
                self.h_crossing_seen = False
                self.h_missing_frames = 0

        return None

    # -------------------------------------------------
    # Detect I Movement
    # -------------------------------------------------

    def detect_I(self, features):

        # -------------------------------------------------
        # Keep I visible after recognition.
        # -------------------------------------------------

        if self.i_result_frames > 0:

            self.i_result_frames -= 1

            return "I"

        # -------------------------------------------------
        # I requires one hand.
        # -------------------------------------------------

        if features.get(
            "both_hands",
            False
        ):

            self.i_started = False
            self.i_start_distance = 0

            return None

        # -------------------------------------------------
        # Determine which hand is visible.
        # -------------------------------------------------

        if features.get(
            "left_hand",
            False
        ):

            prefix = "left"

        elif features.get(
            "right_hand",
            False
        ):

            prefix = "right"

        else:

            self.i_started = False
            self.i_start_distance = 0

            return None

        # -------------------------------------------------
        # I hand shape
        #
        # Index finger up.
        # Middle finger down.
        # Ring finger down.
        # Little finger down.
        # -------------------------------------------------

        if not features.get(
            f"{prefix}_index_up",
            False
        ):

            self.i_started = False
            self.i_start_distance = 0

            return None

        if features.get(
            f"{prefix}_middle_up",
            False
        ):

            self.i_started = False
            self.i_start_distance = 0

            return None

        if features.get(
            f"{prefix}_ring_up",
            False
        ):

            self.i_started = False
            self.i_start_distance = 0

            return None

        if features.get(
            f"{prefix}_little_up",
            False
        ):

            self.i_started = False
            self.i_start_distance = 0

            return None

        # -------------------------------------------------
        # Read thumb-index distance.
        # -------------------------------------------------

        distance = features.get(
            f"{prefix}_thumb_index_distance",
            0
        )

        # -------------------------------------------------
        # PHASE 1
        #
        # Wait for the starting position.
        #
        # The real I capture begins with the thumb and
        # index separated by roughly 1.0 or more.
        # -------------------------------------------------

        if not self.i_started:

            if distance >= self.i_min_start_distance:

                self.i_started = True
                self.i_start_distance = distance

            return None

        # -------------------------------------------------
        # PHASE 2
        #
        # Detect the inward movement.
        #
        # The captured motion reduces the thumb-index
        # distance by roughly 0.2 or more.
        # -------------------------------------------------

        movement = (
            self.i_start_distance
            - distance
        )

        if movement >= self.i_movement_threshold:

            self.i_started = False
            self.i_start_distance = 0

            self.i_result_frames = (
                self.i_result_hold
            )

            return "I"

        return None

    # -------------------------------------------------
    # Detect J Movement
    # -------------------------------------------------

    def detect_J(self, features):

        if self.j_result_frames > 0:

            self.j_result_frames -= 1

            return "J"

        right_hand = features.get(
            "right_hand",
            False
        )

        left_hand = features.get(
            "left_hand",
            False
        )

        if not right_hand:

            self.j_started = False
            self.j_movement_seen = False
            self.j_missing_frames = 0

            return None

        if not features.get(
            "right_index_up",
            False
        ):

            self.j_started = False
            self.j_movement_seen = False
            self.j_missing_frames = 0

            return None

        if not self.j_started:

            if (
                left_hand
                and features.get(
                    "left_index_up",
                    False
                )
            ):

                self.j_started = True
                self.j_movement_seen = False
                self.j_missing_frames = 0

            return None

        if not left_hand:

            self.j_missing_frames += 1
            self.j_movement_seen = True

            if (
                self.j_missing_frames
                > self.j_max_missing_frames
            ):

                self.j_started = False
                self.j_movement_seen = False
                self.j_missing_frames = 0

            return None

        self.j_missing_frames = 0

        if not features.get(
            "left_index_up",
            False
        ):

            self.j_movement_seen = True

            return None

        if self.j_movement_seen:

            if features.get(
                "thumbs_touching",
                False
            ):

                self.j_started = False
                self.j_movement_seen = False
                self.j_missing_frames = 0

                self.j_result_frames = (
                    self.j_result_hold
                )

                return "J"

        return None

    # -------------------------------------------------
    # Detect Y Movement
    # -------------------------------------------------

    def detect_Y(self, features):

        if self.y_result_frames > 0:

            self.y_result_frames -= 1

            return "Y"

        # -------------------------------------------------
        # Y requires both hands
        # -------------------------------------------------

        if not features.get(
            "both_hands",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        # -------------------------------------------------
        # Left hand = thumb + index
        #
        # The feature extractor can report extra raised
        # fingers on the left hand for this sign, so do not
        # use left_finger_count or reject the other fingers.
        # -------------------------------------------------

        if not features.get(
            "left_thumb_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        if not features.get(
            "left_index_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        # -------------------------------------------------
        # Right hand = index
        #
        # The extractor may incorrectly report the right
        # thumb as raised, so do not reject right_thumb_up.
        # -------------------------------------------------

        if not features.get(
            "right_index_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        if features.get(
            "right_middle_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        if features.get(
            "right_ring_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        if features.get(
            "right_little_up",
            False
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            return None

        # -------------------------------------------------
        # Track right index relative to left thumb
        # -------------------------------------------------

        current_distance = features.get(
            "right_index_left_thumb_distance",
            0
        )

        if current_distance <= 0:

            return None

        # -------------------------------------------------
        # Establish starting position
        # -------------------------------------------------

        if not self.y_started:

            self.y_started = True
            self.y_movement_frames = 0

            self.y_baseline_thumb_distance = (
                current_distance
            )

            return None

        # -------------------------------------------------
        # Detect movement
        # -------------------------------------------------

        distance_change = abs(
            current_distance
            - self.y_baseline_thumb_distance
        )

        if (
            distance_change
            >= self.y_movement_threshold
        ):

            self.y_movement_frames += 1

        else:

            self.y_movement_frames = 0

        # -------------------------------------------------
        # Confirm Y movement
        # -------------------------------------------------

        if (
            self.y_movement_frames
            >= self.y_required_movement_frames
        ):

            self.y_started = False
            self.y_movement_frames = 0
            self.y_baseline_thumb_distance = 0

            self.y_result_frames = (
                self.y_result_hold
            )

            return "Y"

        return None

    # -------------------------------------------------
    # Detect Alphabet
    # -------------------------------------------------

    def detect_alphabet(self, features):

        # -------------------------------------------------
        # I MUST COME FIRST
        #
        # I and L have the same starting hand shape:
        #
        # Thumb  = UP
        # Index  = UP
        # Middle = DOWN
        # Ring   = DOWN
        # Little = DOWN
        #
        # Therefore L would otherwise consume every I
        # frame before the I motion detector can track it.
        # -------------------------------------------------

        letter = self.detect_I(features)

        if letter:
            return letter

        # A
        letter = self.rules.detect_A(features)

        if letter:
            return letter

        # B
        letter = self.rules.detect_B(features)

        if letter:
            return letter

        # C
        letter = self.rules.detect_C(features)

        if letter:
            return letter

        # D
        letter = self.rules.detect_D(features)

        if letter:
            return letter

        # E
        letter = self.rules.detect_E(features)

        if letter:
            return letter

        # F
        letter = self.rules.detect_F(features)

        if letter:
            return letter

        # G
        letter = self.rules.detect_G(features)

        if letter:
            return letter

        # K
        letter = self.rules.detect_K(features)

        if letter:
            return letter

        # L
        letter = self.rules.detect_L(features)

        if letter:
            return letter

        # M
        letter = self.rules.detect_M(features)

        if letter:
            return letter

        # N
        letter = self.rules.detect_N(features)

        if letter:
            return letter

        # O
        letter = self.rules.detect_O(features)

        if letter:
            return letter

        # P
        letter = self.rules.detect_P(features)

        if letter:
            return letter

        # Q
        letter = self.rules.detect_Q(features)

        if letter:
            return letter

        # R
        letter = self.rules.detect_R(features)

        if letter:
            return letter

        # S
        letter = self.rules.detect_S(features)

        if letter:
            return letter

        # T
        letter = self.rules.detect_T(features)

        if letter:
            return letter

        # U
        letter = self.rules.detect_U(features)

        if letter:
            return letter

        # V
        letter = self.rules.detect_V(features)

        if letter:
            return letter

        # W
        letter = self.rules.detect_W(features)

        if letter:
            return letter

        # X
        letter = self.rules.detect_X(features)

        if letter:
            return letter

        # Z
        letter = self.rules.detect_Z(features)

        if letter:
            return letter

        # Y
        letter = self.detect_Y(features)

        if letter:
            return letter

        # H
        letter = self.detect_H(features)

        if letter:
            return letter

        # J
        letter = self.detect_J(features)

        if letter:
            return letter

        return "Unknown"