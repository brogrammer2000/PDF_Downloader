import requests
from datetime import date

market_type = "Marktkauf"

market_name = ["Loehne", "Herford", "Buende", "Espelkamp", "Belm", "Rinteln", "Bad_Salzuflen" ,"Hameln", "Osnabrueck", "Luebbecke", "Meppen",
"Wilhelmshaven", "Osterholz_Scharmbeck", "Wunstorf", "Hannover"]

weekNumber = date.today().isocalendar()[1]

url_parts = ["20018_Loehne", "20004_Herford", "20009_Buende", "20071_Espelkamp", "20015_Belm", "20014_Rinteln", "20013_Bad_Salzuflen", 
"20046_Hameln", "20002_Osnabrueck", "20007_Luebbecke", "20017_Meppen", "20026_Wilhelmshaven", "20102_Osterholz_Scharmbeck", "20022_Wunstorf", 
"20025_Hannover"]

for part in url_parts:
 url = "https://static.edeka.de/media/handzettel/MINDEN/MARKTKAUF_"+part+"/blaetterkatalog/pdf/complete.pdf"
 myfile = requests.get(url)
 for name in market_name:
  with open('C:\Users\user\Desktop\LeafletFiles\{0}_{1}_{2}.pdf'.format(market_type,name,str(weekNumber)), 'w') as pdf:
    pdf.write(myfile.content)

