import neuron
if __name__ == "__main__":
    n = neuron.ParentNeuron(2, .01)
    pair = []
    with open("2015 ranks.txt") as f:

        for i in range(1000):
            for line in f:

                line = line.strip("\n")
                if line == "----":
                    n.train(pair,pair[0])
                    pair = []
                    continue
                teamRank = line.split(',')
                pair.append(int(teamRank[1]))

    print(n.feedForward([5,1]))