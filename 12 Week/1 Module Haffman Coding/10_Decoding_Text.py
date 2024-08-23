import heapq
import os


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
        self.__revCodes = {}

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
            self.__revCodes[currBits] = root.value
        self.__buildCodesHelper(root.left, currBits + "0")
        self.__buildCodesHelper(root.right, currBits + "1")

    def __buildCode(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")

    def __getEncodedText(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__code[char]
        return encoded_text

    def __getPaddedEncodedText(self, encodedText):
        paddedAmount = 8 - len(encodedText) % 8
        padding = "0" * paddedAmount
        encodedText += padding
        paddedInfo = format(paddedAmount, "08b")
        paddedEncodedText = paddedInfo + encodedText
        return paddedEncodedText

    def __getBytesArray(self, paddedEncodedText):
        bytesArray = []
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i : 8 + i]
            bytesArray.append(int(byte, 2))
        return bytesArray

    def compress(self):
        # Get the file from path.

        # Reading the text directrly
        #  i, n, d, e, x are 16, 7, 17, 25, 20
        # text = "iiiiiiiiiiiiiiiinnnnnnndddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxxxxxxxx"

        # Read the text from file.
        fileName, fileExtencion = os.path.splitext(self.path)
        outputPath = fileName + ".bin"

        with open(self.path, "r+") as file, open(outputPath, "wb") as output:
            text = file.read()
            text = text.rstrip()
            text = "aeaaaabbaabbbccdd"

            # Make frequency dictionary using the text.
            frequencyDict = self.__makeFreqencyDict(text)

            # Construct the heap from the frequencyDict.
            self.__buildHeap(frequencyDict)

            # Construct the binary tree from the heap.
            self.__buildTree()

            # Construct the codes from the binary tree.
            self.__buildCode()

            # Creating the encoded text using the codes.
            encodedText = self.__getEncodedText(text)
            print(encodedText)
            # Pad this encodedText
            paddedEncodedText = self.__getPaddedEncodedText(encodedText)
            print(paddedEncodedText)
            print(self.__code)

            # Convert Into Bytes
            bytesArray = self.__getBytesArray(paddedEncodedText)
            print(bytesArray)
            # return this binary file as output.
            finalBytes = bytes(bytesArray)

            # Put this encoded text into the binary file.
            output.write(finalBytes)

        print("Hurray! Compressed.♦♠☻☻♥☺")
        return outputPath

    def __removePadding(self, text):
        paddedAmount = text[:8]
        extraPadding = int(paddedAmount, 2)
        text = text[8:]
        textAfterRemvalPadding = text[: -1 * extraPadding]
        return textAfterRemvalPadding

    def __decodeText(self, text):
        decodedText = ""
        currentBits = ""

        for char in text:
            currentBits += char
            if currentBits in self.__revCodes:
                decodedText += self.__revCodes[currentBits]
                currentBits = ""

        return decodedText

    def deCompress(self, inputPath):
        # Getting the input file name and extension.
        fileName, fileExtencion = os.path.splitext(inputPath)
        outputPath = fileName + "Decompressed" + ".txt"

        # Opening the compressed file in read mode.
        with open(inputPath, "rb") as file, open(outputPath, "w") as output:
            bitString = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bitString += bits
                byte = file.read(1)
            actualTextAfterRemovingPadding = self.__removePadding(bitString)
            decompressedText = self.__decodeText(actualTextAfterRemovingPadding)
            print(decompressedText)
            output.write(decompressedText)


path = "./temp.txt"
h = HuffManCoding(path)
outputPath = h.compress()
h.deCompress(outputPath)
