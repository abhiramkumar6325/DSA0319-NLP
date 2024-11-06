class FSA:
    def __init__(self):
        self.state = 0

    def reset(self):
        """Reset the FSA to the initial state."""
        self.state = 0

    def process(self, char):
        """Process a single character based on the current state."""
        if self.state == 0:
            if char == 'a':
                self.state = 1  
            else:
                self.state = 0  
        elif self.state == 1:
            if char == 'b':
                self.state = 2 
            elif char == 'a':
                self.state = 1
            else:
                self.state = 0
        elif self.state == 2:
            if char == 'a':
                self.state = 1
            else:
                self.state = 0

    def accepts(self, string):
        """Determine if the FSA accepts a given string (i.e., ends with 'ab')."""
        self.reset()
        for char in string:
            self.process(char)
        return self.state == 2
fsa = FSA()
test_strings = ["ab", "aab", "baba", "xyzab", "abab", "abc", "aaa"]
for s in test_strings:
    result = fsa.accepts(s)
    print(f"The string '{s}' is {'accepted' if result else 'rejected'} by the FSA.")
