class FingerCounter:

    def __init__(self):
        pass

    def count_fingers(self, hand_landmarks, hand_type):

        landmarks = hand_landmarks.landmark

        fingers = []

        # -----------------------------
        # Thumb
        # -----------------------------

        if hand_type == "Left":
            thumb_up = landmarks[4].x > landmarks[3].x
        else:
            thumb_up = landmarks[4].x < landmarks[3].x

        fingers.append(
            1 if thumb_up else 0
        )

        # -----------------------------
        # Other Fingers
        # -----------------------------

        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]

        for tip, pip in zip(
            finger_tips,
            finger_pips
        ):

            if landmarks[tip].y < landmarks[pip].y:

                fingers.append(1)

            else:

                fingers.append(0)

        # -----------------------------
        # Finger Count
        # -----------------------------

        count = sum(fingers)

        return fingers, count