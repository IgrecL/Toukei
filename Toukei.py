import os
from tkinter import *

BACKGROUND = "black"
FOREGROUND = "white"

# When pressing ENTER
def validate(e):
    if e.keysym == 'Return':
        # Global variables
        global characters, nbKanji, nbKana, dots
        characters = [0] * ord(u"\u9FFF")
        nbKanji = 0
        nbKana = 0
        dots = 0
        # Sort and count characters
        inputText = text.get(1.0, "end-1c")[:-1]
        for char in inputText:
            if char == '。':
                dots+=1
            elif isKanji(char):
                nbKanji += 1
                characters[ord(char)] += 1
            elif isKana(char):
                nbKana += 1
        # Fill the fields
        calculateFields()
        for i in range(4):
            for j in range(6):
                grid[i][j].config(text = gridLabels[i][j]+"\n"+field[i][j])

# Check the type of a character
def isIn(char, start, end):
    return start <= ord(char) <= end
def isKanji(char):
    return isIn(char, ord(u"\u4E00"), ord(u"\u9FFF")) 
def isKana(char):
    return isIn(char, ord(u"\u3040"), ord(u"\u30FF"))  

# Fill the fields correspondingly
def calculateFields():
    # Calculate the values
    individual = 0
    unique = 0
    for i in characters: individual += i > 0
    for i in characters: unique += i ==1
    # Fill the fiels
    global field
    field = [["-"] * 6, ["-"] * 6, ["-"] * 6, ["-"] * 6]
    # First line
    field[0][0] = str(nbKanji+nbKana)
    field[0][1] = str(nbKanji)
    if nbKanji > 0 or nbKana > 0: field[0][2] = str(round(100*nbKanji/(nbKanji+nbKana)))+"%"        
    field[0][3] = str(individual)
    field[0][4] = str(unique)
    if dots > 0: field[0][5] = str(round((nbKanji+nbKana)/dots))
    # Second line
    field[1][0] = compare("Grade1.txt")+"/80"
    field[1][1] = compare("Grade2.txt")+"/160"
    field[1][2] = compare("Grade3.txt")+"/200"
    field[1][3] = compare("Grade4.txt")+"/202"
    field[1][4] = compare("Grade5.txt")+"/193"
    field[1][5] = compare("Grade6.txt")+"/191"
    # Third line
    field[2][0] = compare("Kyouiku.txt")+"/1026"
    field[2][1] = compare("Jouyou.txt")+"/2136"
    field[2][2] = compare("Jinmeiyou.txt")+"/651"
    field[2][3] = str(individual-int(compare("Jouyou.txt"))-int(compare("Jinmeiyou.txt")))+"/∞"
    kyuujitai = compare("Kyuujitai.txt")
    field[2][4] = str(individual-int(kyuujitai))+"/"+str(individual)
    field[2][5] = kyuujitai+"/"+str(individual)
    # Fourth line
    field[3][0] = compare("JLPTN5.txt")+"/80"
    field[3][1] = compare("JLPTN4.txt")+"/170"
    field[3][2] = compare("JLPTN3.txt")+"/370"
    field[3][3] = compare("JLPTN2.txt")+"/380"
    field[3][4] = compare("JLPTN1.txt")+"/1136"
    field[3][5] = str(individual-int(compare("Jouyou.txt")))+"/∞"

# Compare kanji between the text and a given file
def compare(fileName):
    path = str(os.path.dirname(__file__))+"/Lists/"
    file = open(path+fileName)
    fileText = file.readlines()[0]
    c = 0
    for char in fileText:
        if isKanji(char):
            if characters[ord(char)] > 0:
                c += 1
    return str(c)

# Window config
window = Tk()
window.title("統計")
window.geometry("1080x720")
window.configure(bg=BACKGROUND)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Window split in two
upper = Frame(window, bg=BACKGROUND)
upper.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)
lower = Frame(window, bg=BACKGROUND)
lower.grid(row=1, column=0, sticky="nesw", padx=10, pady=10)

# Upper frame config (text input)
upper.grid_rowconfigure(0, weight=1)
upper.grid_rowconfigure(1, weight=20)
upper.grid_columnconfigure(0, weight=1)
textLabel = Label(upper, bg=BACKGROUND, fg=FOREGROUND, text="テキスト", font=('Meiryo',25))
textLabel.grid(row=0, column=0, sticky="n")
text = Text(upper, bg=BACKGROUND, fg=FOREGROUND, font=('Meiryo',10), yscrollcommand=True, height=0, borderwidth=3, relief=RIDGE)
text.grid(row=1, column=0, sticky="nesw")

# Lower frame config (statistics)
lower.grid_rowconfigure(0, weight=1)
lower.grid_rowconfigure(1, weight=10)
lower.grid_columnconfigure(0, weight=1)
statsLabel = Label(lower, bg=BACKGROUND, fg=FOREGROUND, text="統計", font=('Meiryo',25))
statsLabel.grid(row=0, column=0, sticky="n")
stats = Frame(lower, bg=BACKGROUND)
stats.grid(row=1, column=0, sticky="nsew")

# Stats grid
grid = [[""] * 6, [""] * 6, [""] * 6, [""] * 6]
gridLabels = [  ["文字数", "漢字数", "漢字割合", "唯一漢字", "一回漢字", "平均文長"],
                ["第1学年", "第2学年", "第3学年", "第4学年", "第5学年", "第6学年"],
                ["教育漢字", "常用漢字", "人名用漢字", "表外字", "新字体", "旧字体"],
                ["JLPT N5", "JLPT N4", "JLPT N3", "JLPT N2", "JLPT N1", "JLPT++"]
            ]
for i in range(4):
    stats.grid_rowconfigure(i, weight=1)
    for j in range(6):
        stats.grid_columnconfigure(j, weight=1)
        lb = Label(stats, text=gridLabels[i][j]+"\n-", font=('Meiryo',15), bg=BACKGROUND, fg=FOREGROUND)
        lb.grid(row=i, column=j, padx=0, pady=0)
        grid[i][j] = lb

window.bind('<KeyRelease>', validate)
window.mainloop()