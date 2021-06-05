class C32:
    def __init__(self):
        self.state = 'A'

    def make(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'E'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise RuntimeError

    def scan(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'C'
            return 4
        else:
            raise RuntimeError

    def group(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 8
        else:
            raise RuntimeError
