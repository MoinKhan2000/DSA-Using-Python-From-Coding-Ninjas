class HuffManCoding:
    def __init__(self, path):
        self.path = path

    def __makeFreqencyDict(self, text):
        freq = {}
        for el in text:
            freq[el] = freq.get(el, 0) + 1
        return freq

    def compress(self):
        # Get the file from path.

        # Read the text from file.
        text = "askljfklakldfjaskldfjkasdfjaskjfaslkfjasdfasdfas"
        frequencyDict = self.__makeFreqencyDict(text)
        print(frequencyDict)

        # Make frequency dictionary using the text.

        # Construct the heap from the frequencyDict.

        # Construct the binary tree from the heap.

        # Construct the codes from the binary tree.

        # Creating the encoded text using the codes.

        # Put this encoded text into the binary file.

        # return this binary file as output.

        pass


h = HuffManCoding("abcd")
h.compress()
