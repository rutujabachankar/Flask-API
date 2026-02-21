import requests

apikey="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"
word=input("enter the name or word")

res= requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
print("status cod:",res.status_code)

if res.status_code == 200:

    meanings=res.json()[0]["meanings"]


    for meaning in meanings:
        defn=meaning['definitions']
        for d in defn:
            print(d["definition"])

    
