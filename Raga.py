class Raga:
  def __init__(self, num, notes):
    self.num = num
    self.notes = notes

  def __repr__(self):  
    return str(self.notes)

  def equalTo(self, rag, num):  
    count = 0
    for j in range(len(self.notes) - (7-num)):
        if (rag[j] == None or self.notes[j] == rag[j]):
            count += 1
    if(num >= 6 and rag[len(rag)-1] == 1.5):
        if (rag[0] != 0.5):
            count -= 1
    return count
  
  def revEqualTo(self, rag, num):  
    count = 0
    for j in range(len(self.notes) - (7-num)):
        if (rag[j] == None or self.notes[len(self.notes) - 1 - j] == rag[j]):
            count += 1
    if(num >= 6 and rag[len(rag)-1] == 1.5):
        if (rag[0] != 0.5):
            count -= 1
    return count
  
  def streak(self, rag, num):
    count = 0
    for j in range(len(self.notes) - (7-num)):
        if (rag[j] == None or self.notes[j] == rag[j]):
            count += 1
        else:
            return count
    return count

def rotate(l):
    return l[1:] + l[:1]  

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

ragIn = input("Please type the notes of your raga ").upper()
userNotes = ragIn.split(" ")
userRaga = [None] * len(userNotes)


for x in range(len(userNotes)):
    if (userNotes[x] == "C"):
        userRaga[x] = 1.0
    if (userNotes[x] == "C#"):
        userRaga[x] = 1.5
    if (userNotes[x] == "D"):
        userRaga[x] = 2.0
    if (userNotes[x] == "D#"):
        userRaga[x] = 2.5
    if (userNotes[x] == "E"):
        userRaga[x] = 3.0
    if (userNotes[x] == "F"):
        userRaga[x] = 3.5
    if (userNotes[x] == "F#"):
        userRaga[x] = 4.0
    if (userNotes[x] == "G"):
        userRaga[x] = 4.5
    if (userNotes[x] == "G#"):
        userRaga[x] = 5.0
    if (userNotes[x] == "A"):
        userRaga[x] = 5.5
    if (userNotes[x] == "A#"):
        userRaga[x] = 6.0
    if (userNotes[x] == "B"):
        userRaga[x] = 6.5
userRaga.sort()
for x in range(len(userRaga)-1):
    userNotes[x] = userRaga[x+1] - userRaga[x]
userNotes[len(userNotes)-1] = (6 + userRaga[0]) - userRaga[len(userNotes)-1]


#print(userNotes)
#print(userRaga)
#print('\n')


if (len(userRaga) < 7):
    cnt = 0
    maxMatch = 0
    combo = [Raga(0,userNotes), userRaga]
    maxCombo = []
    maxCombo.append(combo)

    # finding rotation of notes with max matched notes
    while(cnt < len(userNotes)):
        userNotes = rotate(userNotes)
        userRaga = rotate(userRaga)
        cnt += 1
        for i in melaScheme:
            match = i.streak(userNotes,len(userNotes))
            if(match > maxMatch and userNotes[0] == i.notes[0]):
                maxMatch = match
            match = 0
        if (maxCombo[0][0].num <= maxMatch):
            if (maxCombo[0][0].num < maxMatch):
                maxCombo.clear()
            combo = [Raga(maxMatch,userNotes), userRaga]
            maxCombo.append(combo)
            maxMatch = 0
    #print("maxCombo" + str(maxCombo))

    posRagas = []
    for a in range(len(maxCombo)):
        # finding missing notes going forwards
        userNotes = maxCombo[a][0].notes
        print(userNotes)
        userRaga = maxCombo[a][1]
        print(userRaga)


        for x in range(maxCombo[a][0].num,7):
            found = False
            for y in range(len(melaScheme)):
                if (melaScheme[y].equalTo(userNotes, x+1) == x+1):
                    found = True
                    break
            if (not(found)):
                userNotes.pop(x)
                userNotes.insert(x, None)
                userNotes.insert(x, None)
                userRaga.insert(x+1, None)
        print(userNotes)
        print(userRaga)

        # finding missing notes going backwards
        revUserNotes = userNotes[maxCombo[a][0].num:] + userNotes[:maxCombo[a][0].num] 
        revUserRaga = userRaga[maxCombo[a][0].num:] + userRaga[:maxCombo[a][0].num]
        revUserNotes.reverse()
        revUserRaga.reverse()
        for x in range(maxCombo[a][0].num,7):
            found = False
            for y in range(len(melaScheme)):
                if (melaScheme[y].revEqualTo(revUserNotes, x+1) == x+1):
                    found = True
                    break
            if (not(found)):
                revUserNotes.pop(x)
                revUserNotes.insert(x, None)
                revUserNotes.insert(x, None)
                revUserRaga.insert(x, None)
        revUserNotes.reverse()
        revUserRaga.reverse()

        if (len(userNotes) == 7 and len(revUserNotes) == 7):
            one = [Raga(0, userNotes),userRaga]
            two = [Raga(0, revUserNotes), revUserRaga]
            for x in range(len(userNotes)):
                if (one[0].equalTo(revUserNotes,7)):
                    print("for and back same")
                    posRagas.append(one)
                    break
                revUserNotes = rotate(revUserNotes)
                revUserRaga = rotate(revUserRaga)
        else:
            if (len(revUserNotes) > len(userNotes)):
                one = [Raga(0, userNotes),userRaga]
                posRagas.append(one)
            elif (len(revUserNotes) < len(userNotes)):
                one = [Raga(0, revUserNotes), revUserRaga]
                posRagas.append(one)
    print(posRagas)
else:
    for x in range(len(melaScheme)):
        for y in range(len(userRaga)):
            if (melaScheme[x].equalTo(userNotes, 7) == 7):
                posMela.append(str(melaScheme[x].num) + " in " + str(userRaga[0]))
            userNotes = rotate(userNotes)
            userRaga = rotate(userRaga)
#print(posMela)

""" if (len(userRaga) == 5):
        cor = False
        while(not(cor) and (cnt != len(userNotes))):
            userNotes = rotate(userNotes)
            userRaga = rotate(userRaga)
            cnt += 1
            for i in melaScheme:
                if(i.equalTo(userNotes, 3) == 3):
                    cor = True
                    break
        if(cnt == len(userNotes)):
            while(not(cor)):
                userNotes = rotate(userNotes)
                userRaga = rotate(userRaga)
                for i in melaScheme:
                    if(i.equalTo(userNotes, 2) == 2):
                        cor = True
                        break
    elif (len(userRaga) == 6):
        cor = False
        while(not(cor) and (cnt != len(userNotes))):
            userNotes = rotate(userNotes)
            userRaga = rotate(userRaga)
            cnt += 1
            for i in melaScheme:
                if(i.equalTo(userNotes, 3) == 3):
                    cor = True
                    break
        if(cnt == len(userNotes)):
            while(not(cor)):
                userNotes = rotate(userNotes)
                userRaga = rotate(userRaga)
                for i in melaScheme:
                    if(i.equalTo(userNotes, 2) == 2):
                        cor = True
                        break """


        










