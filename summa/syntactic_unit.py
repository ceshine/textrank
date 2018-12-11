class SyntacticUnit(object):

    def __init__(self, text, token=None, tag=None, index=-1, paragraph=-1):
        self.text = text
        self.token = token
        self.tag = tag[:2] if tag else None  # just first two letters of tag
        self.index = index
        self.score = -1
        self.paragraph = paragraph

    def __str__(self):
        return (
            "Original unit: '" + self.text + "' *-* " + "Processed unit: '" +
            self.token + "'" + "%d %d" % (self.paragraph, self.index)
        )

    def __repr__(self):
        return str(self)
