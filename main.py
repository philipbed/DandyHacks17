import neuron
if __name__ == "__main__":
    with open("2015 ranks.txt") as f:
        for i in range(1000):
            pair = []
            n = neuron.ParentNeuron()
            for line in f:

                line = line.strip("\n")
                if line == "----":
                    n.train(pair,pair[0])
                teamRank = line.split(',')
                pair.append(teamRank[1])

