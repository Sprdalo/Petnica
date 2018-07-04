class zadatak:
    def __init__(self):
        self.source = "" 

    def addElement(self, tag, content="", href=""):
        if tag[0] == "h": 
            sup = "#" * int(tag[1])
            self.source += sup + " " + content + "\n"
        elif tag == "a": 
            self.source += "[" + content + "][" + href + "]\n"
        elif tag == "code":
            self.source += "```\n" + content + "\n```"
        else:
            self.source += tag + " " + content + "\n"

class HTML: 
    def __init__(self):
        self.source = ""

    def addElement(self, tag, content="", elClass="", elId="", additional=""): 
        self.source += '<' + tag + ' class="' + elClass + '" id="' + elId + '"' + additional + ">" + content + "</" + tag + ">\n"

tmp = HTML();
tmp.addElement('p', 'sprdalo', 'e', 'i', 'onclick="sprdalo()"');
tmp.addElement('h1', 'test');
print(tmp.source);

mm = zadatak();
mm.addElement("h5", "sprdalo");
mm.addElement("a", "google", "https://google.com");
mm.addElement("code", 'printf("Ja sam zakon")');
print(mm.source);
