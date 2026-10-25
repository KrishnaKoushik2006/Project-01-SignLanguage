from vision.hand_utils import HandUtils
from vision.finger_counter import FingerCounter
from vision.pose_utils import PoseUtils
from vision.geometry import Geometry


class FeatureExtractor:

    def __init__(self, left_hand=None, right_hand=None):

        self.left_hand = left_hand
        self.right_hand = right_hand

        self.hand = HandUtils(
            left_hand,
            right_hand
        )

        self.finger_counter = FingerCounter()

    # -------------------------------------------------
    # Geometry Helpers
    # -------------------------------------------------

    @staticmethod
    def _distance_2d(point_a, point_b):

        dx = point_a.x - point_b.x
        dy = point_a.y - point_b.y

        return (dx * dx + dy * dy) ** 0.5

    @staticmethod
    def _point_to_segment_distance(point, start, end):

        dx = end.x - start.x
        dy = end.y - start.y

        length_squared = (dx * dx) + (dy * dy)

        if length_squared <= 1e-12:
            return FeatureExtractor._distance_2d(
                point,
                start
            ), 0.0

        px = point.x - start.x
        py = point.y - start.y

        projection = (
            (px * dx + py * dy)
            / length_squared
        )

        clamped_projection = max(
            0.0,
            min(1.0, projection)
        )

        closest_x = (
            start.x
            + clamped_projection * dx
        )

        closest_y = (
            start.y
            + clamped_projection * dy
        )

        distance = (
            (point.x - closest_x) ** 2
            + (point.y - closest_y) ** 2
        ) ** 0.5

        return distance, clamped_projection

    @staticmethod
    def _orientation(point_a, point_b, point_c):

        value = (
            (point_b.y - point_a.y)
            * (point_c.x - point_b.x)
            -
            (point_b.x - point_a.x)
            * (point_c.y - point_b.y)
        )

        if abs(value) < 1e-9:
            return 0

        return 1 if value > 0 else 2

    @staticmethod
    def _on_segment(point_a, point_b, point_c):

        return (
            min(point_a.x, point_c.x) - 1e-9
            <= point_b.x
            <= max(point_a.x, point_c.x) + 1e-9
            and
            min(point_a.y, point_c.y) - 1e-9
            <= point_b.y
            <= max(point_a.y, point_c.y) + 1e-9
        )

    @staticmethod
    def _segments_intersect(
        a1,
        a2,
        b1,
        b2
    ):

        o1 = FeatureExtractor._orientation(
            a1,
            a2,
            b1
        )

        o2 = FeatureExtractor._orientation(
            a1,
            a2,
            b2
        )

        o3 = FeatureExtractor._orientation(
            b1,
            b2,
            a1
        )

        o4 = FeatureExtractor._orientation(
            b1,
            b2,
            a2
        )

        if o1 != o2 and o3 != o4:
            return True

        if (
            o1 == 0
            and FeatureExtractor._on_segment(
                a1,
                b1,
                a2
            )
        ):
            return True

        if (
            o2 == 0
            and FeatureExtractor._on_segment(
                a1,
                b2,
                a2
            )
        ):
            return True

        if (
            o3 == 0
            and FeatureExtractor._on_segment(
                b1,
                a1,
                b2
            )
        ):
            return True

        if (
            o4 == 0
            and FeatureExtractor._on_segment(
                b1,
                a2,
                b2
            )
        ):
            return True

        return False

    @staticmethod
    def _index_fingers_crossed(
        left_landmarks,
        right_landmarks
    ):

        left_start = left_landmarks[5]
        left_end = left_landmarks[8]

        right_start = right_landmarks[5]
        right_end = right_landmarks[8]

        return FeatureExtractor._segments_intersect(
            left_start,
            left_end,
            right_start,
            right_end
        )

    # -------------------------------------------------
    # Extract Features
    # -------------------------------------------------

    def extract(self):

        features = {}

        # =================================================
        # HAND PRESENCE
        # =================================================

        features["left_hand"] = (
            self.left_hand is not None
        )

        features["right_hand"] = (
            self.right_hand is not None
        )

        features["both_hands"] = (
            self.hand.both_hands_detected()
        )

        # =================================================
        # LEFT HAND
        # =================================================

        if self.left_hand:

            fingers, count = (
                self.finger_counter.count_fingers(
                    self.left_hand,
                    "Left"
                )
            )

            pose = PoseUtils(
                self.left_hand.landmark
            )

            # -------------------------------------------------
            # Finger State
            # -------------------------------------------------

            features["left_thumb_up"] = (
                fingers[0] == 1
            )

            features["left_index_up"] = (
                fingers[1] == 1
            )

            features["left_middle_up"] = (
                fingers[2] == 1
            )

            features["left_ring_up"] = (
                fingers[3] == 1
            )

            features["left_little_up"] = (
                fingers[4] == 1
            )

            features["left_finger_count"] = count

            # -------------------------------------------------
            # Touch Features
            # -------------------------------------------------

            features["left_thumb_touch_index"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.index_tip
                )
            )

            features["left_thumb_touch_middle"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.middle_tip
                )
            )

            features["left_thumb_touch_ring"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.ring_tip
                )
            )

            features["left_thumb_touch_little"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.little_tip
                )
            )

            features["left_index_touch_middle"] = (
                Geometry.is_touching(
                    pose.index_tip,
                    pose.middle_tip
                )
            )

            features["left_middle_touch_ring"] = (
                Geometry.is_touching(
                    pose.middle_tip,
                    pose.ring_tip
                )
            )

            features["left_ring_touch_little"] = (
                Geometry.is_touching(
                    pose.ring_tip,
                    pose.little_tip
                )
            )

            # -------------------------------------------------
            # Finger Curvature
            # -------------------------------------------------

            features["left_thumb_curled"] = (
                Geometry.is_curled(
                    pose.thumb_tip,
                    pose.thumb_mcp
                )
            )

            features["left_index_curled"] = (
                Geometry.is_curled(
                    pose.index_tip,
                    pose.index_mcp
                )
            )

            features["left_middle_curled"] = (
                Geometry.is_curled(
                    pose.middle_tip,
                    pose.middle_mcp
                )
            )

            features["left_ring_curled"] = (
                Geometry.is_curled(
                    pose.ring_tip,
                    pose.ring_mcp
                )
            )

            features["left_little_curled"] = (
                Geometry.is_curled(
                    pose.little_tip,
                    pose.little_mcp
                )
            )

            # -------------------------------------------------
            # Finger Angles
            # -------------------------------------------------

            landmarks = self.left_hand.landmark

            features["left_thumb_angle"] = (
                Geometry.thumb_angle(landmarks)
            )

            features["left_index_angle"] = (
                Geometry.index_angle(landmarks)
            )

            features["left_middle_angle"] = (
                Geometry.middle_angle(landmarks)
            )

            features["left_ring_angle"] = (
                Geometry.ring_angle(landmarks)
            )

            features["left_little_angle"] = (
                Geometry.little_angle(landmarks)
            )

            # -------------------------------------------------
            # Thumb ↔ Index Normalized Distance
            # -------------------------------------------------

            palm_scale = Geometry.distance(
                self.left_hand.landmark[0],
                self.left_hand.landmark[9]
            )

            if palm_scale > 0:

                features["left_thumb_index_distance"] = (
                    Geometry.distance(
                        pose.thumb_tip,
                        pose.index_tip
                    ) / palm_scale
                )

            else:

                features["left_thumb_index_distance"] = 0

            # -------------------------------------------------
            # Index ↔ Middle Normalized Distance
            # -------------------------------------------------

            if palm_scale > 0:

                features["left_index_middle_distance"] = (
                    Geometry.distance(
                        pose.index_tip,
                        pose.middle_tip
                    ) / palm_scale
                )

            else:

                features["left_index_middle_distance"] = 0

        else:

            # -------------------------------------------------
            # Left Hand Defaults
            # -------------------------------------------------

            left_defaults = [

                "left_thumb_up",
                "left_index_up",
                "left_middle_up",
                "left_ring_up",
                "left_little_up",

                "left_thumb_touch_index",
                "left_thumb_touch_middle",
                "left_thumb_touch_ring",
                "left_thumb_touch_little",

                "left_index_touch_middle",
                "left_middle_touch_ring",
                "left_ring_touch_little",

                "left_thumb_curled",
                "left_index_curled",
                "left_middle_curled",
                "left_ring_curled",
                "left_little_curled"

            ]

            for key in left_defaults:
                features[key] = False

            features["left_finger_count"] = 0

            features["left_thumb_angle"] = 0
            features["left_index_angle"] = 0
            features["left_middle_angle"] = 0
            features["left_ring_angle"] = 0
            features["left_little_angle"] = 0

            features["left_thumb_index_distance"] = 0
            features["left_index_middle_distance"] = 0

        # =================================================
        # RIGHT HAND
        # =================================================

        if self.right_hand:

            fingers, count = (
                self.finger_counter.count_fingers(
                    self.right_hand,
                    "Right"
                )
            )

            pose = PoseUtils(
                self.right_hand.landmark
            )

            # -------------------------------------------------
            # Finger State
            # -------------------------------------------------

            features["right_thumb_up"] = (
                fingers[0] == 1
            )

            features["right_index_up"] = (
                fingers[1] == 1
            )

            features["right_middle_up"] = (
                fingers[2] == 1
            )

            features["right_ring_up"] = (
                fingers[3] == 1
            )

            features["right_little_up"] = (
                fingers[4] == 1
            )

            features["right_finger_count"] = count

            # -------------------------------------------------
            # Touch Features
            # -------------------------------------------------

            features["right_thumb_touch_index"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.index_tip
                )
            )

            features["right_thumb_touch_middle"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.middle_tip
                )
            )

            features["right_thumb_touch_ring"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.ring_tip
                )
            )

            features["right_thumb_touch_little"] = (
                Geometry.is_touching(
                    pose.thumb_tip,
                    pose.little_tip
                )
            )

            features["right_index_touch_middle"] = (
                Geometry.is_touching(
                    pose.index_tip,
                    pose.middle_tip
                )
            )

            features["right_middle_touch_ring"] = (
                Geometry.is_touching(
                    pose.middle_tip,
                    pose.ring_tip
                )
            )

            features["right_ring_touch_little"] = (
                Geometry.is_touching(
                    pose.ring_tip,
                    pose.little_tip
                )
            )

            # -------------------------------------------------
            # Finger Curvature
            # -------------------------------------------------

            features["right_thumb_curled"] = (
                Geometry.is_curled(
                    pose.thumb_tip,
                    pose.thumb_mcp
                )
            )

            features["right_index_curled"] = (
                Geometry.is_curled(
                    pose.index_tip,
                    pose.index_mcp
                )
            )

            features["right_middle_curled"] = (
                Geometry.is_curled(
                    pose.middle_tip,
                    pose.middle_mcp
                )
            )

            features["right_ring_curled"] = (
                Geometry.is_curled(
                    pose.ring_tip,
                    pose.ring_mcp
                )
            )

            features["right_little_curled"] = (
                Geometry.is_curled(
                    pose.little_tip,
                    pose.little_mcp
                )
            )

            # -------------------------------------------------
            # Finger Angles
            # -------------------------------------------------

            landmarks = self.right_hand.landmark

            features["right_thumb_angle"] = (
                Geometry.thumb_angle(landmarks)
            )

            features["right_index_angle"] = (
                Geometry.index_angle(landmarks)
            )

            features["right_middle_angle"] = (
                Geometry.middle_angle(landmarks)
            )

            features["right_ring_angle"] = (
                Geometry.ring_angle(landmarks)
            )

            features["right_little_angle"] = (
                Geometry.little_angle(landmarks)
            )

            # -------------------------------------------------
            # Thumb ↔ Index Normalized Distance
            # -------------------------------------------------

            palm_scale = Geometry.distance(
                self.right_hand.landmark[0],
                self.right_hand.landmark[9]
            )

            if palm_scale > 0:

                features["right_thumb_index_distance"] = (
                    Geometry.distance(
                        pose.thumb_tip,
                        pose.index_tip
                    ) / palm_scale
                )

            else:

                features["right_thumb_index_distance"] = 0

            # -------------------------------------------------
            # Index ↔ Middle Normalized Distance
            # -------------------------------------------------

            if palm_scale > 0:

                features["right_index_middle_distance"] = (
                    Geometry.distance(
                        pose.index_tip,
                        pose.middle_tip
                    ) / palm_scale
                )

            else:

                features["right_index_middle_distance"] = 0

        else:

            # -------------------------------------------------
            # Right Hand Defaults
            # -------------------------------------------------

            right_defaults = [

                "right_thumb_up",
                "right_index_up",
                "right_middle_up",
                "right_ring_up",
                "right_little_up",

                "right_thumb_touch_index",
                "right_thumb_touch_middle",
                "right_thumb_touch_ring",
                "right_thumb_touch_little",

                "right_index_touch_middle",
                "right_middle_touch_ring",
                "right_ring_touch_little",

                "right_thumb_curled",
                "right_index_curled",
                "right_middle_curled",
                "right_ring_curled",
                "right_little_curled"

            ]

            for key in right_defaults:
                features[key] = False

            features["right_finger_count"] = 0

            features["right_thumb_angle"] = 0
            features["right_index_angle"] = 0
            features["right_middle_angle"] = 0
            features["right_ring_angle"] = 0
            features["right_little_angle"] = 0

            features["right_thumb_index_distance"] = 0
            features["right_index_middle_distance"] = 0

        # =================================================
        # TWO-HAND FEATURES
        # =================================================

        features["wrist_distance"] = (
            self.hand.wrist_distance()
        )

        features["hands_close"] = (
            self.hand.hands_are_close()
        )

        # -------------------------------------------------
        # Hand Vertical Position
        # -------------------------------------------------

        if self.left_hand and self.right_hand:

            left_wrist_y = (
                self.left_hand.landmark[0].y
            )

            right_wrist_y = (
                self.right_hand.landmark[0].y
            )

            features["left_wrist_y"] = left_wrist_y
            features["right_wrist_y"] = right_wrist_y

            features["hand_vertical_distance"] = abs(
                left_wrist_y - right_wrist_y
            )

            # Smaller Y means physically higher in the image.
            features["left_hand_above_right"] = (
                left_wrist_y < right_wrist_y
            )

            features["right_hand_above_left"] = (
                right_wrist_y < left_wrist_y
            )

            # -------------------------------------------------
            # Thumb-to-Thumb Touch
            # -------------------------------------------------

            left_pose = PoseUtils(
                self.left_hand.landmark
            )

            right_pose = PoseUtils(
                self.right_hand.landmark
            )

            features["thumbs_touching"] = (
                Geometry.is_touching(
                    left_pose.thumb_tip,
                    right_pose.thumb_tip
                )
            )

            # -------------------------------------------------
            # Index-to-Index Distance
            # -------------------------------------------------

            left_palm_scale = Geometry.distance(
                self.left_hand.landmark[0],
                self.left_hand.landmark[9]
            )

            right_palm_scale = Geometry.distance(
                self.right_hand.landmark[0],
                self.right_hand.landmark[9]
            )

            average_palm_scale = (
                left_palm_scale + right_palm_scale
            ) / 2

            if average_palm_scale > 0:

                features["index_fingers_distance"] = (
                    Geometry.distance(
                        left_pose.index_tip,
                        right_pose.index_tip
                    ) / average_palm_scale
                )

            else:

                features["index_fingers_distance"] = 0

            # -------------------------------------------------
            # Index Finger Crossing
            # -------------------------------------------------

            features["index_fingers_crossed"] = (
                self._index_fingers_crossed(
                    self.left_hand.landmark,
                    self.right_hand.landmark
                )
            )

            # -------------------------------------------------
            # Y Movement Geometry
            #
            # Right index moves along the line between
            # the left index tip and left thumb tip.
            # -------------------------------------------------

            left_index_tip = (
                left_pose.index_tip
            )

            left_thumb_tip = (
                left_pose.thumb_tip
            )

            right_index_tip = (
                right_pose.index_tip
            )

            line_distance, line_progress = (
                self._point_to_segment_distance(
                    right_index_tip,
                    left_index_tip,
                    left_thumb_tip
                )
            )

            if average_palm_scale > 0:

                features[
                    "right_index_left_index_distance"
                ] = (
                    Geometry.distance(
                        right_index_tip,
                        left_index_tip
                    ) / average_palm_scale
                )

                features[
                    "right_index_left_thumb_distance"
                ] = (
                    Geometry.distance(
                        right_index_tip,
                        left_thumb_tip
                    ) / average_palm_scale
                )

                features[
                    "right_index_left_line_distance"
                ] = (
                    line_distance
                    / average_palm_scale
                )

            else:

                features[
                    "right_index_left_index_distance"
                ] = 0

                features[
                    "right_index_left_thumb_distance"
                ] = 0

                features[
                    "right_index_left_line_distance"
                ] = 0

            # -------------------------------------------------
            # Y Line Progress
            #
            # 0.0 = left index endpoint
            # 1.0 = left thumb endpoint
            #
            # Values between them indicate where the
            # right index lies along the line.
            # -------------------------------------------------

            features[
                "right_index_y_line_progress"
            ] = line_progress

        else:

            features["left_wrist_y"] = 0
            features["right_wrist_y"] = 0

            features["hand_vertical_distance"] = 0

            features["left_hand_above_right"] = False
            features["right_hand_above_left"] = False

            features["thumbs_touching"] = False

            features["index_fingers_distance"] = 0

            features["index_fingers_crossed"] = False

            features[
                "right_index_left_index_distance"
            ] = 0

            features[
                "right_index_left_thumb_distance"
            ] = 0

            features[
                "right_index_left_line_distance"
            ] = 0

            features[
                "right_index_y_line_progress"
            ] = 0

        return features