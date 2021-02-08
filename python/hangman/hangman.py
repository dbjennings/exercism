# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.answer = word
        self.guessed = []
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        
        if self.get_status()==STATUS_LOSE:
            raise ValueError("You've already lost")
        elif self.get_status()==STATUS_WIN:
            raise ValueError("You've already won")

        # Check for duplicate/wrong guess
        if (char in self.guessed) or (not char in self.answer): self.remaining_guesses -= 1
        # Add guess to list
        self.guessed.append(char)

    def get_masked_word(self) -> str:
        a = ''
        for c in self.answer:
            a += c if c in self.guessed else '_'
        return a

    def get_status(self):
        # Full status check
        if not '_' in self.get_masked_word():
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING
        return self.status