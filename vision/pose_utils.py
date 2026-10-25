class PoseUtils:

    def __init__(self, landmarks):

        self.landmarks = landmarks

        # Wrist
        self.wrist = landmarks[0]

        # -----------------------------
        # Thumb
        # -----------------------------

        self.thumb_cmc = landmarks[1]
        self.thumb_mcp = landmarks[2]
        self.thumb_ip = landmarks[3]
        self.thumb_tip = landmarks[4]

        # -----------------------------
        # Index
        # -----------------------------

        self.index_mcp = landmarks[5]
        self.index_pip = landmarks[6]
        self.index_dip = landmarks[7]
        self.index_tip = landmarks[8]

        # -----------------------------
        # Middle
        # -----------------------------

        self.middle_mcp = landmarks[9]
        self.middle_pip = landmarks[10]
        self.middle_dip = landmarks[11]
        self.middle_tip = landmarks[12]

        # -----------------------------
        # Ring
        # -----------------------------

        self.ring_mcp = landmarks[13]
        self.ring_pip = landmarks[14]
        self.ring_dip = landmarks[15]
        self.ring_tip = landmarks[16]

        # -----------------------------
        # Little
        # -----------------------------

        self.little_mcp = landmarks[17]
        self.little_pip = landmarks[18]
        self.little_dip = landmarks[19]
        self.little_tip = landmarks[20]