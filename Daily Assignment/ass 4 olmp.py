gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
for x in country:
    try:
      country_gold.append(gold[x])
    except KeyError:
        country_gold.append("Did Not get Gold")      
print(country_gold)

'''for key,value in gold.items():
  print(key,'-',value)'''