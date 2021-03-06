class Raga:
    def __init__(self, num, notes):
        self.num = num
        self.notes = notes

    def __repr__(self):
        return str(self.notes)

    def equalTo(self, rag, num):
        count = 0
        for j in range(len(self.notes) - (7 - num)):
            if (rag[j] == None or self.notes[j] == rag[j]):
                count += 1
        if (num >= 6 and rag[len(rag) - 1] == 1.5):
            if (rag[0] != 0.5):
                count -= 1
        return count

    def revEqualTo(self, rag, num):
        count = 0
        for j in range(len(self.notes) - (7 - num)):
            if (rag[j] == None or self.notes[len(self.notes) - 1 - j] == rag[j]):
                count += 1
        if (num >= 6 and rag[len(rag) - 1] == 1.5):
            if (rag[0] != 0.5):
                count -= 1
        return count

    def streak(self, rag, num):
        count = 0
        for j in range(len(self.notes) - (7 - num)):
            if (rag[j] == None or self.notes[j] == rag[j]):
                count += 1
            else:
                return count
        return count

def difference(upperBound, lowerBound):
    if lowerBound == 6.5:
        return upperBound - 0.5
    else:
        return upperBound - lowerBound


def identification():
    #main algorithm TBD
    pass

""" def reverseMap(differences, start):
    map = []
    map.append(start)
    for i in range(1, len(differences)):
        if map[i-1] != 6.5:
            map.append(differences[i] + map[i-1])
        else:
            map.append(differences[i] + 0.5)

    return map """

#Re-did this method a little bit
def reverseMap(differences, start):
    map = []
    map.append(start)
    for i in range(1, len(differences)):
        note = map[i - 1] + differences[i - 1]
        if (note >= 7):
            note = note % 7 + 1
        map.append(note)
    return map

def difCheck(inputRag, rag, ragInt):

    #Checking R and G and making sure lower/higher versions can not appear without complement
    if (ragInt.notes[0] + ragInt.notes[1] == 1) and (not(rag[1] in inputRag)):
        return False
    if (ragInt.notes[0] == 1.5) and (not(rag[2] in inputRag)):
        return False
    #Checking D and N and making sure lower/higher versions can not appear without complement
    if (ragInt.notes[4] + ragInt.notes[5] == 1) and (not(rag[5] in inputRag)):
        return False
    if (ragInt.notes[4] == 1.5) and (not(rag[6] in inputRag)):
        return False
    return True

melaScheme = []
posMela = []
melaScheme.append(Raga(1,[0.5,0.5,1.5,1,0.5,0.5,1.5]))
melaScheme.append(Raga(2,[0.5,0.5,1.5,1,0.5,1,1]))
melaScheme.append(Raga(3,[0.5,0.5,1.5,1,0.5,1.5,0.5]))
melaScheme.append(Raga(4,[0.5,0.5,1.5,1,1,0.5,1]))
melaScheme.append(Raga(5,[0.5,0.5,1.5,1,1,1,0.5]))
melaScheme.append(Raga(6,[0.5,0.5,1.5,1,1.5,0.5,0.5]))
melaScheme.append(Raga(7,[0.5,1,1,1,0.5,0.5,1.5]))
melaScheme.append(Raga(8,[0.5,1,1,1,0.5,1,1]))
melaScheme.append(Raga(9,[0.5,1,1,1,0.5,1.5,0.5]))
melaScheme.append(Raga(10,[0.5,1,1,1,1,0.5,1]))
melaScheme.append(Raga(11,[0.5,1,1,1,1,1,0.5]))
melaScheme.append(Raga(12,[0.5,1,1,1,1.5,0.5,0.5]))
melaScheme.append(Raga(13,[0.5,1.5,0.5,1,0.5,0.5,1.5]))
melaScheme.append(Raga(14,[0.5,1.5,0.5,1,0.5,1,1]))
melaScheme.append(Raga(15,[0.5,1.5,0.5,1,0.5,1.5,0.5]))
melaScheme.append(Raga(16,[0.5,1.5,0.5,1,1,0.5,1]))
melaScheme.append(Raga(17,[0.5,1.5,0.5,1,1,1,0.5]))
melaScheme.append(Raga(18,[0.5,1.5,0.5,1,1.5,0.5,0.5]))
melaScheme.append(Raga(19,[1,0.5,1,1,0.5,0.5,1.5]))
melaScheme.append(Raga(20,[1,0.5,1,1,0.5,1,1]))
melaScheme.append(Raga(21,[1,0.5,1,1,0.5,1.5,0.5]))
melaScheme.append(Raga(22,[1,0.5,1,1,1,0.5,1]))
melaScheme.append(Raga(23,[1,0.5,1,1,1,1,0.5]))
melaScheme.append(Raga(24,[1,0.5,1,1,1.5,0.5,0.5]))
melaScheme.append(Raga(25,[1,1,0.5,1,0.5,0.5,1.5]))
melaScheme.append(Raga(26,[1,1,0.5,1,0.5,1,1]))
melaScheme.append(Raga(27,[1,1,0.5,1,0.5,1.5,0.5]))
melaScheme.append(Raga(28,[1,1,0.5,1,1,0.5,1]))
melaScheme.append(Raga(29,[1,1,0.5,1,1,1,0.5]))
melaScheme.append(Raga(30,[1,1,0.5,1,1.5,0.5,0.5]))
melaScheme.append(Raga(31,[1.5,0.5,0.5,1,0.5,0.5,1.5]))
melaScheme.append(Raga(32,[1.5,0.5,0.5,1,0.5,1,1]))
melaScheme.append(Raga(33,[1.5,0.5,0.5,1,0.5,1.5,0.5]))
melaScheme.append(Raga(34,[1.5,0.5,0.5,1,1,0.5,1]))
melaScheme.append(Raga(35,[1.5,0.5,0.5,1,1,1,0.5]))
melaScheme.append(Raga(36,[1.5,0.5,0.5,1,1.5,0.5,0.5]))
melaScheme.append(Raga(37,[0.5,0.5,2,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(38,[0.5,0.5,2,0.5,0.5,1,1]))
melaScheme.append(Raga(39,[0.5,0.5,2,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(40,[0.5,0.5,2,0.5,1,0.5,1]))
melaScheme.append(Raga(41,[0.5,0.5,2,0.5,1,1,0.5]))
melaScheme.append(Raga(42,[0.5,0.5,2,0.5,1.5,0.5,0.5]))
melaScheme.append(Raga(43,[0.5,1,1.5,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(44,[0.5,1,1.5,0.5,0.5,1,1]))
melaScheme.append(Raga(45,[0.5,1,1.5,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(46,[0.5,1,1.5,0.5,1,0.5,1]))
melaScheme.append(Raga(47,[0.5,1,1.5,0.5,1,1,0.5]))
melaScheme.append(Raga(48,[0.5,1,1.5,0.5,1.5,0.5,0.5]))
melaScheme.append(Raga(49,[0.5,1.5,1,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(50,[0.5,1.5,1,0.5,0.5,1,1]))
melaScheme.append(Raga(51,[0.5,1.5,1,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(52,[0.5,1.5,1,0.5,1,0.5,1]))
melaScheme.append(Raga(53,[0.5,1.5,1,0.5,1,1,0.5]))
melaScheme.append(Raga(54,[0.5,1.5,1,0.5,1.5,0.5,0.5]))
melaScheme.append(Raga(55,[1,0.5,1.5,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(56,[1,0.5,1.5,0.5,0.5,1,1]))
melaScheme.append(Raga(57,[1,0.5,1.5,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(58,[1,0.5,1.5,0.5,1,0.5,1]))
melaScheme.append(Raga(59,[1,0.5,1.5,0.5,1,1,0.5]))
melaScheme.append(Raga(60,[1,0.5,1.5,0.5,1.5,0.5,0.5]))
melaScheme.append(Raga(61,[1,1,1,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(62,[1,1,1,0.5,0.5,1,1]))
melaScheme.append(Raga(63,[1,1,1,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(64,[1,1,1,0.5,1,0.5,1]))
melaScheme.append(Raga(65,[1,1,1,0.5,1,1,0.5]))
melaScheme.append(Raga(66,[1,1,1,0.5,1.5,0.5,0.5]))
melaScheme.append(Raga(67,[1.5,0.5,1,0.5,0.5,0.5,1.5]))
melaScheme.append(Raga(68,[1.5,0.5,1,0.5,0.5,1,1]))
melaScheme.append(Raga(69,[1.5,0.5,1,0.5,0.5,1.5,0.5]))
melaScheme.append(Raga(70,[1.5,0.5,1,0.5,1,0.5,1]))
melaScheme.append(Raga(71,[1.5,0.5,1,0.5,1,1,0.5]))
melaScheme.append(Raga(72,[1.5,0.5,1,0.5,1.5,0.5,0.5]))



input_notes = [1, 2, 3, 4.5, 6.5]
#input_notes = [1, 2.5, 3.5, 5, 6]
input_notes.sort()
input_diff = []
matches = []
matchNotes = []

#Determines the Matching Ragas
if len(input_notes) == 7:
    for x in input_notes:
        input_notes = input_notes[1:] + input_notes[:1]
        for i in range(0, len(input_notes)-1):
            input_diff.append(difference(input_notes[i+1], input_notes[i]))
        input_diff.append(difference(input_notes[0], input_notes[len(input_notes)-1]))
        for ragas in melaScheme:
            if input_diff == ragas.notes:
                matches.append(ragas)
                matchNotes.append(input_notes)
        input_diff = []

    print("Number of Matches Found: "  + str(len(matches)))
    for i in range (0, len(matches)):
        print("Difference " + str(matches[i].notes) + " | Notes: " + str(matchNotes[i]) + " | Raga Number: " + str(matches[i].num))
else:
    print(input_notes)
    for x in input_notes:
        input_notes = input_notes[1:] + input_notes[:1]

        #Instead of looping through all scales for each raga, as we rotate through input notes, we can just set the scale to the note in the SA position
        count = input_notes[0]

        max = len(input_notes)
        for ragas in melaScheme:
            ragNotes = reverseMap(ragas.notes, count)
            duplicates = len(set(ragNotes) & set(input_notes))
            if duplicates == max:
                gap = 0
                inIndex = 1
                #look at the SA and remove if not existent
                if input_notes[0] == ragNotes[0]:
                    #if two consecutive dont match, remove
                    for i in range(1, len(ragNotes),1):
                        if (input_notes[inIndex] != ragNotes[i]):
                            inIndex -= 1
                            gap -= 1
                            if(gap == -2):
                                break
                        else:
                            gap = 0
                        inIndex += 1
                        if (inIndex == len(input_notes)):
                            break
                    if gap > -2 and difCheck(input_notes,ragNotes,ragas):
                        matches.append(ragas)
                        matchNotes.append(ragNotes)
    print("Number of Matches Found: " + str(len(matches)))
    for i in range(0, len(matches)):
        print("Difference " + str(matches[i].notes) + " | Notes: " + str(matchNotes[i]) + " | Raga Number: " + str(
            matches[i].num))

