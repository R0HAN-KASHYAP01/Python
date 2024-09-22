def matchwords(sentance1, sentance2):
    words1 = sentance1.split(" ")
    words2 = sentance2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.casefold() == word2.casefold():
                score += 1
    return score

if __name__ == "__main__":
    resources = ["This is good", "Python is good", "python is not python snake"]
    search = input("What you want to search\n")
    scores = [matchwords(search, resource) for resource in resources]
    results =[ result for result in  sorted(zip(scores, resources), reverse=True)if result[0] != 0 ]

    print(f"{len(results)} results are founded:-")
    for faltu, items in results:
        print("  ",items)