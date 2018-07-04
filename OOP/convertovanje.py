import re

#Radjeno uz pomoc saradnika
#fala vam

class convertujem:
    def __init__(self):

        Fajlic = open("source.html")
        Linijice = Fajlic.readlines();

	self.source = "";
        for Linijica in Linijice:
            l = Linijica.strip();
            try:
                content = re.search('>(.*)<', l).group(1)
            except:
                content = ""
            if l[1] == "h" and l[2].isdigit():
                pref = "#" * int(l[2])
                self.source += (pref + " " + content + "\n")
            if l[1] == "a":
                href = re.search('href="(.*)"', l).group(1)
                self.source += "[" + content + "](" + href + ")" + "\n"
            if l[1:4] == "img":
                href = re.search('src="(.*)"', l).group(1)
                try:
                    alt = re.search('alt="(.*)"', l).group(1)
                except:
                        alt = ""
                self.source += "![" + alt + "](" + href + ")\n"
            if l[1:3] == "br":
                self.source += "\n"

t = convertujem();
print(t.source);
