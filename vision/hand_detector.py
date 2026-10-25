import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.mp_draw = mp.solutions.drawing_utils

    # -------------------------------------------------
    # Detect Hands
    # -------------------------------------------------

    def detect_hands(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.hands.process(
            rgb_frame
        )

        left_hand = None
        right_hand = None

        # -------------------------------------------------
        # Process Detected Hands
        # -------------------------------------------------

        if (
            results.multi_hand_landmarks
            and results.multi_handedness
        ):

            for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness
            ):

                # Draw landmarks

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                # MediaPipe handedness

                hand_label = (
                    handedness.classification[0].label
                )

                # Keep original MediaPipe assignment

                if hand_label == "Left":

                    left_hand = hand_landmarks

                else:

                    right_hand = hand_landmarks

        return (
            frame,
            results,
            left_hand,
            right_hand
        )