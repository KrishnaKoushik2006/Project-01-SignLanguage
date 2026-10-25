import math

from vision.config import TOUCH_THRESHOLD


class Geometry:

    # -------------------------------------------------
    # Distance
    # -------------------------------------------------

    @staticmethod
    def distance(point1, point2):

        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y

        return math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

    # -------------------------------------------------
    # Touch Detection
    # -------------------------------------------------

    @staticmethod
    def is_touching(point1, point2):

        return (
            Geometry.distance(point1, point2)
            < TOUCH_THRESHOLD
        )

    # -------------------------------------------------
    # Finger Curvature
    # -------------------------------------------------

    @staticmethod
    def is_curled(tip, mcp, threshold=0.12):

        return (
            Geometry.distance(tip, mcp)
            < threshold
        )

    # -------------------------------------------------
    # Finger Angle
    # -------------------------------------------------

    @staticmethod
    def angle(point1, point2, point3):

        """
        Returns the angle (degrees) at point2.

        point1 ---- point2 ---- point3
        """

        a = (
            point1.x - point2.x,
            point1.y - point2.y
        )

        b = (
            point3.x - point2.x,
            point3.y - point2.y
        )

        dot = (
            a[0] * b[0] +
            a[1] * b[1]
        )

        mag_a = math.sqrt(
            a[0] ** 2 +
            a[1] ** 2
        )

        mag_b = math.sqrt(
            b[0] ** 2 +
            b[1] ** 2
        )

        if mag_a == 0 or mag_b == 0:
            return 0

        cos_theta = dot / (mag_a * mag_b)

        cos_theta = max(-1, min(1, cos_theta))

        theta = math.degrees(
            math.acos(cos_theta)
        )

        return theta

    # -------------------------------------------------
    # Finger Angles
    # -------------------------------------------------

    @staticmethod
    def index_angle(landmarks):

        return Geometry.angle(
            landmarks[5],
            landmarks[6],
            landmarks[8]
        )

    @staticmethod
    def middle_angle(landmarks):

        return Geometry.angle(
            landmarks[9],
            landmarks[10],
            landmarks[12]
        )

    @staticmethod
    def ring_angle(landmarks):

        return Geometry.angle(
            landmarks[13],
            landmarks[14],
            landmarks[16]
        )

    @staticmethod
    def little_angle(landmarks):

        return Geometry.angle(
            landmarks[17],
            landmarks[18],
            landmarks[20]
        )

    @staticmethod
    def thumb_angle(landmarks):

        return Geometry.angle(
            landmarks[2],
            landmarks[3],
            landmarks[4]
        )

    # -------------------------------------------------
    # Thumb Direction
    # -------------------------------------------------

    @staticmethod
    def thumb_direction(landmarks):

        """
        Determines the horizontal direction of the thumb
        relative to the thumb MCP.

        Returns:

        "left"
        "right"
        "center"
        """

        thumb_mcp = landmarks[2]
        thumb_tip = landmarks[4]

        dx = thumb_tip.x - thumb_mcp.x

        threshold = 0.03

        if dx < -threshold:
            return "left"

        elif dx > threshold:
            return "right"

        return "center"

    # -------------------------------------------------
    # Thumb Direction Vector
    # -------------------------------------------------

    @staticmethod
    def thumb_direction_vector(landmarks):

        """
        Returns the normalized 2D direction vector
        from thumb MCP to thumb tip.

        Returns:

        (dx, dy)
        """

        thumb_mcp = landmarks[2]
        thumb_tip = landmarks[4]

        dx = thumb_tip.x - thumb_mcp.x
        dy = thumb_tip.y - thumb_mcp.y

        magnitude = math.sqrt(
            dx ** 2 +
            dy ** 2
        )

        if magnitude == 0:
            return 0, 0

        return (
            dx / magnitude,
            dy / magnitude
        )

    # -------------------------------------------------
    # Thumb Direction Angle
    # -------------------------------------------------

    @staticmethod
    def thumb_direction_angle(landmarks):

        """
        Returns the angle of the thumb direction
        relative to the horizontal axis.

        Range:

        -180 to 180 degrees
        """

        dx, dy = Geometry.thumb_direction_vector(
            landmarks
        )

        if dx == 0 and dy == 0:
            return 0

        return math.degrees(
            math.atan2(dy, dx)
        )