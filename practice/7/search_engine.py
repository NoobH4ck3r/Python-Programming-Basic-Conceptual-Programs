def score(sentence1,sentence2):
    scores=0
    words1=sentence1.split(" ")
    words2=sentence2.split(" ")
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                scores+=1
    return scores
    
def sorting_with_count(scores,sentences):
    sortedlist=[sentscore for sentscore in sorted(zip(scores,sentences),reverse=True) ]
    return  sortedlist



if __name__=='__main__':
    sentences=["Python is a programming language", "Python is a good language","Python is not python snake","It's my search engine"]
    query=input("Enter the thing you want to search:\t")
    scores=[score(query,sentence) for sentence in sentences]
    print(scores)
    sorted_matches=sorting_with_count(scores,sentences)
    print(f"{len(sorted_matches)} results found")
    for count,item in sorted_matches:
        if count > 0:
            print(f"{item}")
        else:
            continue
            
