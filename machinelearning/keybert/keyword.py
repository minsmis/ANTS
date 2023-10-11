import keybert


class Keyword:
    def __init__(self):
        super(Keyword, self).__init__()

        self.keyword_model = keybert.KeyBERT()  # call KeyBERT model

        # extract keywords parameters
        self.range = (1, 1)
        self.stop_words = None

    def extractKeywords(self, command):
        # extract keywords
        keywords = self.keyword_model.extract_keywords(docs=command,
                                                       keyphrase_ngram_range=self.range,
                                                       stop_words=self.stop_words)
        return keywords
