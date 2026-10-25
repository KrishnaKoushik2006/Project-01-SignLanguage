class WordBuilder:

    def __init__(self):

        self.word = ""

        # Last accepted letter
        self.previous_letter = None

        # Current detected letter
        self.current_letter = None

        # Number of consecutive frames
        self.frame_count = 0

        # Frames required before accepting a letter
        self.stable_frames = 5

    # ---------------------------------
    # Add Letter
    # ---------------------------------

    def add_letter(self, letter):

        # No letter detected
        if letter == "Unknown":
            self.current_letter = None
            self.frame_count = 0
            self.previous_letter = None
            return

        # Same letter continues
        if letter == self.current_letter:
            self.frame_count += 1
        else:
            # New letter starts
            self.current_letter = letter
            self.frame_count = 1

        # Wait until the letter is stable
        if self.frame_count < self.stable_frames:
            return

        # Prevent duplicates while holding the sign
        if letter == self.previous_letter:
            return

        # Accept the letter
        self.word += letter
        self.previous_letter = letter

    # ---------------------------------
    # Get Word
    # ---------------------------------

    def get_word(self):
        return self.word

    # ---------------------------------
    # Clear Word
    # ---------------------------------

    def clear(self):
        self.word = ""
        self.previous_letter = None
        self.current_letter = None
        self.frame_count = 0