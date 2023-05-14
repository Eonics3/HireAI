def evaluate_filler():

    filler_words = ["um", "ah", "like", "you know", "er", "right", "alright", "hmm", "hm", "oh", "so"]

    f = open('transcript.txt', 'r')

    total = 0.0
    filler = 0

    for line in f:
        for word in line.split():
            if word in filler_words:
                filler+=1
            total+=1

    f = open('filler_num.txt', 'w')
    print("filler/total: ", filler/total)

    f.write(str(100-(100 * (filler/total))))
