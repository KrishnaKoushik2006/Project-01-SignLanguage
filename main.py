import cv2
import time

from camera.camera import Camera
from vision.hand_detector import HandDetector
from vision.gesture_detector import GestureDetector
from vision.alphabet_detector import AlphabetDetector
from vision.feature_extractor import FeatureExtractor


def save_capture(capture_type, captured_frames):

    if capture_type == "static":

        filename = "output/static_feature_capture.txt"
        title = "STATIC FEATURE CAPTURE"

    else:

        filename = "output/motion_feature_capture.txt"
        title = "MOTION FEATURE CAPTURE"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "========================================\n"
        )

        file.write(
            f"{title}\n"
        )

        file.write(
            "========================================\n\n"
        )

        file.write(
            f"Total frames captured: "
            f"{len(captured_frames)}\n\n"
        )

        for frame_number, frame_data in enumerate(
            captured_frames,
            start=1
        ):

            file.write(
                "----------------------------------------\n"
            )

            file.write(
                f"FRAME {frame_number}\n"
            )

            file.write(
                f"TIME: "
                f"{frame_data['time']:.3f} seconds\n"
            )

            file.write(
                "----------------------------------------\n"
            )

            for (
                feature_name,
                feature_value
            ) in frame_data["features"].items():

                file.write(
                    f"{feature_name}: "
                    f"{feature_value}\n"
                )

            file.write("\n")

    print(
        "\n========================================"
    )

    print(
        f"{title} SAVED"
    )

    print(
        f"File: {filename}"
    )

    print(
        f"Frames captured: "
        f"{len(captured_frames)}"
    )

    print(
        "========================================\n"
    )


def main():

    # -------------------------------------------------
    # Initialize Modules
    # -------------------------------------------------

    camera = Camera()
    hand_detector = HandDetector()
    gesture_detector = GestureDetector()
    alphabet_detector = AlphabetDetector()

    # -------------------------------------------------
    # Capture State
    # -------------------------------------------------

    capture_requested = False

    capture_type = None

    capture_start_time = 0

    capture_countdown = 3

    capture_duration = 2

    captured_frames = []

    # -------------------------------------------------
    # Main Loop
    # -------------------------------------------------

    while True:

        # -------------------------------------------------
        # Capture Frame
        # -------------------------------------------------

        frame = camera.get_frame()

        if frame is None:
            break

        # -------------------------------------------------
        # Detect Hands
        # -------------------------------------------------

        frame, results, left_hand, right_hand = (
            hand_detector.detect_hands(frame)
        )

        # -------------------------------------------------
        # Extract Features
        # -------------------------------------------------

        feature_extractor = FeatureExtractor(
            left_hand,
            right_hand
        )

        features = feature_extractor.extract()

        # -------------------------------------------------
        # Thumb Direction Debug
        # -------------------------------------------------

        print(
            "LEFT THUMB:",
            features.get("left_thumb_direction")
        )

        print(
            "RIGHT THUMB:",
            features.get("right_thumb_direction")
        )

        # =================================================
        # CAPTURE PROCESS
        # =================================================

        if capture_requested:

            elapsed = (
                time.time()
                - capture_start_time
            )

            remaining = (
                capture_countdown
                - int(elapsed)
            )

            # -------------------------------------------------
            # Countdown
            # -------------------------------------------------

            if remaining > 0:

                cv2.putText(
                    frame,
                    f"GET READY: {remaining}",
                    (400, 250),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 255, 255),
                    3
                )

            else:

                # -------------------------------------------------
                # Actual Capture Time
                # -------------------------------------------------

                capture_elapsed = (
                    elapsed
                    - capture_countdown
                )

                # -------------------------------------------------
                # Record Frames
                # -------------------------------------------------

                if capture_elapsed <= capture_duration:

                    captured_frames.append(
                        {
                            "time": capture_elapsed,
                            "features": features.copy()
                        }
                    )

                    if capture_type == "static":

                        message = "HOLD STATIC SIGN"

                    else:

                        message = "PERFORM MOTION NOW"

                    cv2.putText(
                        frame,
                        message,
                        (350, 250),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2,
                        (0, 255, 255),
                        3
                    )

                # -------------------------------------------------
                # Capture Finished
                # -------------------------------------------------

                else:

                    save_capture(
                        capture_type,
                        captured_frames
                    )

                    capture_requested = False
                    capture_type = None
                    capture_start_time = 0
                    captured_frames = []

        # =================================================
        # Feature Display
        # =================================================

        y = 30

        for key, value in features.items():

            cv2.putText(
                frame,
                f"{key}: {value}",
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1
            )

            y += 20

            if y > 700:
                break

        # =================================================
        # Gesture Recognition
        # =================================================

        gesture = "Unknown"

        if left_hand:

            gesture = gesture_detector.detect_gesture(
                left_hand
            )

        # =================================================
        # Alphabet Recognition
        # =================================================

        alphabet = alphabet_detector.detect_alphabet(
            features
        )

        # -------------------------------------------------
        # Display Gesture
        # -------------------------------------------------

        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (500, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        # -------------------------------------------------
        # Display Alphabet
        # -------------------------------------------------

        cv2.putText(
            frame,
            f"Alphabet: {alphabet}",
            (500, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        # -------------------------------------------------
        # Dedicated Thumb Direction Display
        # -------------------------------------------------

        left_direction = features.get(
            "left_thumb_direction"
        )

        right_direction = features.get(
            "right_thumb_direction"
        )

        cv2.putText(
            frame,
            f"L Thumb: {left_direction}",
            (500, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"R Thumb: {right_direction}",
            (500, 175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # =================================================
        # Capture Status
        # =================================================

        if not capture_requested:

            cv2.putText(
                frame,
                "Press 1 = Static Capture",
                (400, 220),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                "Press 0 = Motion Capture",
                (400, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

        # =================================================
        # Display Frame
        # =================================================

        cv2.imshow(
            "Sign Language Recognition",
            frame
        )

        # =================================================
        # Keyboard Controls
        # =================================================

        key = cv2.waitKey(1) & 0xFF

        # -------------------------------------------------
        # Static Capture
        # -------------------------------------------------

        if (
            key == ord("1")
            and not capture_requested
        ):

            capture_requested = True

            capture_type = "static"

            capture_start_time = time.time()

            captured_frames = []

            print(
                "\n========================================"
            )

            print(
                "STATIC FEATURE CAPTURE PREPARING"
            )

            print(
                "Make the static sign."
            )

            print(
                "Capture begins in 3 seconds..."
            )

            print(
                "========================================\n"
            )

        # -------------------------------------------------
        # Motion Capture
        # -------------------------------------------------

        if (
            key == ord("0")
            and not capture_requested
        ):

            capture_requested = True

            capture_type = "motion"

            capture_start_time = time.time()

            captured_frames = []

            print(
                "\n========================================"
            )

            print(
                "MOTION FEATURE CAPTURE PREPARING"
            )

            print(
                "Get ready to perform the motion."
            )

            print(
                "Capture begins in 3 seconds..."
            )

            print(
                "Recording for 2 seconds..."
            )

            print(
                "========================================\n"
            )

        # -------------------------------------------------
        # Quit
        # -------------------------------------------------

        if key == ord("q"):

            break

    # -------------------------------------------------
    # Cleanup
    # -------------------------------------------------

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()