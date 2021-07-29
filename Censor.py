#The words taken here are entirely used for the working of the Program. In real world Scenario it helps a lot to hide this kind of languages to maintain the decorundum. No strict actions shall be entertained later. I myself give the consent these words are not meant to hurt any sentiments.
#Harshil Jani.
words = ['dumb','stupid','shit','fuck','ass','moron','bitch','piss off','bugger off','bloody hell','bastard','wanker','bollocks','sex','jerk','fucker','motherfucker','dick','asshole','shit','dick head','cunt','choad','crikey','porn']

with open("Censor_Test_Check.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"******")
    word2 = word.capitalize()
    content = content.replace(word2,"******")

with open("Article.txt","w") as f:
   content = f.write(content)

