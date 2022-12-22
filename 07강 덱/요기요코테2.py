import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    doc = nlp(sentences)
    list = []
    aplist = []
    for t in doc:
        if t.ent_type_ == "PERSON":
            try:
                if doc[t.i+1].ent_type_ == "PERSON":
                    aplist.append("X"*(len(t.text)+1))
                else:
                    aplist.append("X"*len(t.text))
                    list.append("".join(aplist))
                    aplist = []
            except:
                    aplist.append("X"*len(t.text))
                    list.append("".join(aplist))
                    aplist = []    
        elif t.text != ".":
            list.append(t.text)
        else:
            list[-1] = list[-1]+ "."
    return " ".join(list)

text = "Mark Oldham ate an apple. Mark Oldham did something"
print(anonymize_text(text))