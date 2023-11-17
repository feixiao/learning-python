class MultiLineScanner:
    def __init__(self, text):
        self.lines = text.splitlines()
        self.current_line = 0
        self.tokens = []

    def scan(self):
        if self.current_line < len(self.lines):
            if not self.tokens:
                self.tokens = self.lines[self.current_line].split()
            if self.tokens:
                token = self.tokens.pop(0)
                return True, token  # Return a tuple indicating a successful token retrieval
            else:
                self.current_line += 1
                self.tokens = []  # Reset tokens for the next line
                return False, None  # Signal the end of the line
        else:
            return None, None  # Signal the end of scanning


# 示例用法
multi_line_input = """This is line one
This is line two
And this is line three"""

scanner = MultiLineScanner(multi_line_input)

while True:
    success, token = scanner.scan()
    if success is None:
        break
    elif success:
        print("Scanned token:", token)
    else:
        print("End of line reached")
