class Placeholder:
    """Match a word in a command string."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.upper()

