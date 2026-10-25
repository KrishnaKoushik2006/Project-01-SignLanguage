from vision.finger_counter import FingerCounter


class GestureDetector:

    def __init__(self):
        self.finger_counter = FingerCounter()

    def detect_gesture(self, hand_landmarks, hand_type="Left"):

        fingers, count = self.finger_counter.count_fingers(
            hand_landmarks,
            hand_type
        )

        # -----------------------------
        # Open Palm
        # -----------------------------
        if fingers == [1, 1, 1, 1, 1]:
            return "Open Palm"

        # -----------------------------
        # Fist
        # -----------------------------
        elif fingers == [0, 0, 0, 0, 0]:
            return "Fist"

        # -----------------------------
        # Victory
        # -----------------------------
        elif fingers == [0, 1, 1, 0, 0]:
            return "Victory"

        # -----------------------------
        # Thumbs Up
        # -----------------------------
        elif fingers == [1, 0, 0, 0, 0]:
            return "Thumbs Up"

        return "Unknown"