n, m = map(int, input().split())

dna = []

for i in range(n):
    newdna = input()
    dna.append(newdna)

hammingdistance = 0
hammingstring = ''

for j in range(m):
    sampledna = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    for i in range(n):
        
        if dna[i][j] == 'A':
            sampledna['A']+=1
        elif dna[i][j] == 'T':
            sampledna['T']+=1
        elif dna[i][j] == 'C':
            sampledna['C']+=1
        else:
            sampledna['G']+=1
            
    chosen = max(sampledna, key = sampledna.get) #A, T, C, G 중 1
    hammingstring += chosen
    hammingdistance += sum(sampledna.values()) - sampledna[chosen]

    
print(hammingstring)
print(hammingdistance)


