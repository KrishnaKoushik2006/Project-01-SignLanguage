import math


class HandUtils:

    def __init__(self, left_hand=None, right_hand=None):

        self.left_hand = left_hand
        self.right_hand = right_hand

    # -------------------------------------------------
    # Check if both hands are detected
    # -------------------------------------------------

    def both_hands_detected(self):

        return (
            self.left_hand is not None and
            self.right_hand is not None
        )

    # -------------------------------------------------
    # Distance between two landmarks
    # -------------------------------------------------

    def distance(self, point1, point2):

        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y

        return math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

    # -------------------------------------------------
    # Distance between wrists
    # -------------------------------------------------

    def wrist_distance(self):

        if not self.both_hands_detected():
            return None

        left_wrist = self.left_hand.landmark[0]
        right_wrist = self.right_hand.landmark[0]

        return self.distance(
            left_wrist,
            right_wrist
        )

    # -------------------------------------------------
    # Check if hands are close
    # -------------------------------------------------

    def hands_are_close(self, threshold=0.30):

        distance = self.wrist_distance()

        if distance is None:
            return False

        return distance < threshold