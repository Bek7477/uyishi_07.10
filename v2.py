def election_results(votes):
    yes_votes = sum(1 for vote in votes.values() if vote == 1)
    no_votes = sum(1 for vote in votes.values() if vote == 0)
    
    if yes_votes > no_votes:
        result = "1"
    elif no_votes > yes_votes:
        result = "0"
    else:
        result = "1 va 0"
    
    names = [name for name, vote in votes.items() if (vote == 1 and yes_votes >= no_votes) or (vote == 0 and no_votes >= yes_votes)]
    
    print(result)
    for name in names:
        print(name)

votes = {}
num_voters = int(input("Necha kishi ovoz beradi?: "))
for _ in range(num_voters):
    name = input("Ismni kiriting: ")
    vote = int(input("Ovoz berishni kiriting (1 yoki 0): "))
    votes[name] = vote

election_results(votes)