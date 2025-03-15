class Validater:
    def __init__(self, language: str, architecture: str):
        self.language = language
        self.architecture = architecture

    def validate(self):
        if not self.language.isalpha() or not self.architecture.isalpha():
            raise ValueError("Invalid Input")

    def fetch(self):
        self.validate()
        return f"Fetching for {self.language} with {self.architecture}"
