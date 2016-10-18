
from Queue import PriorityQueue
import csv


class HuffmanNode:
    def __init__(self, letter=None, freq=0.0, left=None, mid=None, right=None):
        self.letter, self.freq, self.left, self.mid, self.right = letter, freq, left, mid, right


def getEncodingForChar(letter, node, output):
    if letter == node.letter:
        return output
    else:
        result = ""
        if node.left is not None:
            result = getEncodingForChar(letter, node.left, output + '0')
        if node.mid is not None and result == "":
            result = getEncodingForChar(letter, node.mid, output + '1')
        if node.right is not None and result == "":
            result = getEncodingForChar(letter, node.right, output + '2')
        return result


def encodeString(inputStr, rootNode):
    encodingCache, outputStr = {}, ""
    for c in inputStr:
        if encodingCache.has_key(c):
            encodedChar = encodingCache[c]
        else:
            encodingCache[c] = encodedChar = getEncodingForChar(c, rootNode, "")
        outputStr += encodedChar
        # print('+++++|||||-------------')
        # print(encodedChar)
    return outputStr


def buildHuffmanTree(strlen, charFreqList):
    pq = PriorityQueue()
    
    for key, value in charFreqList.iteritems():
        pq.put((float(value) / float(strlen), HuffmanNode(key, float(value) / float(strlen))))
    
    while pq.qsize() > 2:
        x,y,z = pq.get(), pq.get(), pq.get()
        pq.put((x[0] + y[0] + z[0], HuffmanNode(None, x[0] + y[0] +z [0], x[1], y[1], z[1])))
    
    return pq.get()[1]


def determineCharFreq(inputStr):
    return {c: inputStr.count(c) for c in list(set(inputStr))}

def encodeDnaHuffman(code):
    last = 'A'
    dna = []
    for element in code:
        # print (element)
        new = singleElementDna(last,element)
        dna.append(new)
        last = new
    return dna

def singleElementDna(last,element):
    if last == 'A':
        if int(element) == 0:
            return 'C'
        if int(element) == 1:
            return 'G'
        else:
            return 'T'
    if last == 'C':
        if int(element) == 0:
            return 'G'
        if int(element) == 1:
            return 'T'
        else:
            return 'A'
    if last == 'G':
        if int(element) == 0:
            return 'T'
        if int(element) == 1:
            return 'A'
        else:
            return 'C'
    if last == 'T':
        if int(element) == 0:
            return 'A'
        if int(element) == 1:
            return 'C'
        else:
            return 'G'

def singleElementDnaDecode(last,element):
    if last == 'A':
        if str(element) == 'C':
            return 0
        if str(element) == 'G':
            return 1
        else:
            return 2
    if last == 'C':
        if str(element) == 'A':
            return 2
        if str(element) == 'G':
            return 0
        else:
            return 1
    if last == 'G':
        if str(element) == 'A':
            return 1
        if str(element) == 'C':
            return 2
        else:
            return 0
    if last == 'T':
        if str(element) == 'A':
            return 0
        if str(element) == 'C':
            return 1
        else:
            return 2

def decodeDnaHuffman(code):
    last = 'A'
    dna = []
    for element in code:
        # print (element)
        new = singleElementDnaDecode(last,element)
        dna.append(new)
        last = element
    print (dna)

def readFile(file):
    input_f = open(file,'r')
    text = input_f.read()
    input_f.close()
    return text

def outputFile(file,text):
    output_f = open(file,'w')
    for letter in text:
        output_f.write(str(letter))
    output_f.close()


def main():
    inputString = readFile('1984.txt');
    print (inputString)
    charFreqList = determineCharFreq(inputString)
    rootNode = buildHuffmanTree(len(inputString), charFreqList)
    huffman = encodeString(inputString, rootNode)
    print (huffman)
    dna_code = encodeDnaHuffman(huffman)
    outputFile('1984_dna.txt',dna_code)
    decodeDnaHuffman(dna_code)


if __name__ == '__main__':
    main()