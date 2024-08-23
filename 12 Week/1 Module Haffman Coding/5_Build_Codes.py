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
        self.__code = {}

    def __makeFreqencyDict(self, text):
        freq = {}
        for el in text:
            freq[el] = freq.get(el, 0) + 1
        return freq

    # def __makeFreqencyDict(self, frequecyDict):
    #     for el in frequecyDict:
    #         self.__heap.append(el)
    #     heapq.heapify(self.__heap)

    def __buildHeap(self, frequencyDict):
        for key in frequencyDict:
            frequency = frequencyDict[key]
            binaryTreeNode = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binaryTreeNode)

    def __buildTree(self):
        while len(self.__heap) > 1:
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)
            totalFreq = node1.freq + node2.freq
            newNode = BinaryTreeNode(None, totalFreq)
            newNode.left = node1
            newNode.right = node2
            heapq.heappush(self.__heap, newNode)

    def __buildCodesHelper(self, root, currBits):
        if root is None:
            return
        if root.value is not None:
            self.__code[root.value] = currBits
        self.__buildCodesHelper(root.left, currBits + "0")
        self.__buildCodesHelper(root.right, currBits + "1")

    def __buildCode(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")

    def compress(self):
        # Get the file from path.

        # Read the text from file.
        #  i, n, d, e, x are 16, 7, 17, 25, 20 
        text = "iiiiiiiiiiiiiiiinnnnnnndddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxxxxxxxx"

        # Make frequency dictionary using the text.
        frequencyDict = self.__makeFreqencyDict(text)

        # Construct the heap from the frequencyDict.
        self.__buildHeap(frequencyDict)

        # Construct the binary tree from the heap.
        self.__buildTree()

        # Construct the codes from the binary tree.
        self.__buildCode()

        # Creating the encoded text using the codes.
        print(self.__code)
        # Put this encoded text into the binary file.

        # return this binary file as output.

        pass


h = HuffManCoding("abcd")
h.compress()
