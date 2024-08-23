import heapq


class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


class HuffManCoding:
    def __init__(self, path):
        self.path = path
        self.__heap = []

    def __makeFreqencyDict(self, text):
        freq = {}
        for el in text:
            freq[el] = freq.get(el, 0) + 1
        return freq

    def __makeFreqencyDict(self, frequecyDict):
        for el in frequecyDict:
            self.__heap.append(el)
        self.__heap.heapify()

    def __buildHeap(self, frequencyDict):
        for key in frequencyDict:
            frequency = frequencyDict[key]
            binaryTreeNode = binaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binaryTreeNode)

    def compress(self):
        # Get the file from path.

        # Read the text from file.
        text = "askljfklakldfjaskldfjkasdfjaskjfaslkfjasdfasdfas"

        # Make frequency dictionary using the text.
        frequencyDict = self.__makeFreqencyDict(text)
        print(frequencyDict)

        # Construct the heap from the frequencyDict.
        self.__buildHeap(frequencyDict)

        # Construct the binary tree from the heap.

        # Construct the codes from the binary tree.

        # Creating the encoded text using the codes.

        # Put this encoded text into the binary file.

        # return this binary file as output.

        pass


h = HuffManCoding("abcd")
h.compress()
