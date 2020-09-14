from flask import  Flask,request,jsonify
import re

def ans(q):
  answ = ""
  dicts = (
    dict.fromkeys(("ukimwi","maana","nini"),"Ukimwi ni upungufu wa kinga mwilini"),
    dict.fromkeys(("vvu","maana","nini"),"vvu inamaanish virusi vya ukimwi.Ni virusi vinavosababisha ugonjwa wa ukimwi"),
    dict.fromkeys(("tofauti","vvu","ukimwi","kati"),"VVU ni Virusi vya ukimwi na UKIMWI ni Upungufu wa kinga mwilini "),
    dict.fromkeys(("kupata","ukimwi","vvu","ambukizwa","kuambukizwa"),"Unaweza kupata virusi vya ukimwi kwa njia mbali mbali mfano ngono zembe,kutoka kwa mama kwenda kwa mtoto"),
    dict.fromkeys(("kinga","kujikinga","ukimwi","vvu","kuepuka","kujiepusha"),"Unaweza kuepuka kupata vvu kwa kutumia condom wakati wa ngono n.k"),
    dict.fromkeys(("dalili","ukimwi","vvu","umeambukizwa","umepata"),"Kuna dalili mbalimbali mfano kukonda, kupata magonjwa mbalimbali kwa sababu ya kinga mwilini kudhoofika")
  )

  for i in range(len(dicts)):
    if set(q).issubset(dicts[i].keys()):
      answ = dicts[i][q[0]]
      break

  return answ

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def ask():
    quest = request.get_json(force=True)
    stopwords = ["","ya","anawezaje","anaweza","akasema","kujua","alikuwa","alisema","baada","basi","bila","cha","chini","hadi","hapo","hata","hivyo","hiyo","huku","huo","ili","ilikuwa","juu","kama","karibu","katika","kila","kima","kisha","kubwa","kutoka","kuwa","kwa","kwamba","kwenda","kwenye","la","lakini","mara","mdogo","mimi","mkubwa","mmoja","moja","muda","mwenye","na","naye","ndani","ng","ni","nini","nonkungu","pamoja","pia","sana","sasa","sauti","tafadhali","tena","tu","vile","wa","wakati","wake","walikuwa","wao","watu","wengine","wote","ya","yake","yangu","yao","yeye","yule","za","zaidi","zake"]
    return ans([word for word in re.split("\W+",quest["question"]) if word.lower() not in stopwords])
