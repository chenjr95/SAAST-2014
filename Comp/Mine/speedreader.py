import sys
from drawingpanel import *

class WordGenerator:

    def __init__(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines()]
            self.words = []
            for line in lines:
                self.words.extend(line.split())
            self.pos = 0
            self.state = False

    def is_empty(self):
        return self.pos >= len(self.words)

    def next_word(self):
        ans = self.words[self.pos]
        self.pos += 1
        return ans

    def in_quotes(self,word):
        if ("\"" in word):
            self.state = not self.state

def focus_letter_list(word):
    actual_word = ""
    colored_word = ""
    if (len(word) >= 3) and (len(word) <= 5):
        actual_word = ((len(word) - 3) * " ") + word
        colored_word = ((len(word)-2) * " ") + word[1] + ((len(word)-2) * " ")
    elif len(word) == 2:
        actual_word = word + " "
        colored_word = " " + word[1] + " "
    elif len(word) == 1:
        actual_word = word
        colored_word = word
    elif (len(word) >= 6) and (len(word) <= 9):
        actual_word = ((len(word) - 5) * " ") + word 
        colored_word = ((len(word) - 3) * " ") + word[2] + ((len(word)-3) * " ")
    elif (len(word) >= 10) and (len(word) <= 13):
        actual_word = ((len(word) - 7) * " ") + word
        colored_word = ((len(word) - 4) * " ") + word[3] + ((len(word)-4) * " ")
    elif (len(word) > 13):
        actual_word = ((len(word) -9)* " ") + word
        colored_word = ((len(word) - 5) * " ") + word[4] + ((len(word) - 5) * " ")
    else:
        pass
    return [actual_word, colored_word]

def animate_text(gen, width, height, size, delay):
    panel = DrawingPanel(width, height)
    canvas = panel.canvas
    panel.set_background("Beige")
    while not (gen.is_empty()):
        word = gen.next_word()
        # actual_letter_index = len(word)/2
        # colored_index = focus_letter_index(word)
        # index_dif = focus_letter_index(word) - actual_letter_index
        # colored_letter = word[focus_letter_index(word)]
        # colored_word = ""
        # if index_dif < 0:
        #     word = ((index_dif * -1) * "-") + word
        #     colored_word = list(" " * len(word))
        #     colored_word[colored_index+(index_dif*-1)] = colored_letter
        #     colored_word = "".join(colored_word)
        # elif index_dif > 0:
        #     word = word + (index_dif * "-")
        #     colored_word = list(" " * len(word))
        #     colored_word[colored_index] = colored_letter
        #     colored_word = "".join(colored_word)
        # else:
        #     if len(word)==2:
        #         colored_word = " " + colored_letter
        #     else:
        #         colored_word = colored_letter
        canvas.create_rectangle(0,0, width, height, fill = "Beige")
        gen.in_quotes(word)
        prin_words = focus_letter_list(word)
        if gen.state or "\"" in word:
            canvas.create_text(width/2, height/2, text=prin_words[0], font=("Courier", size*2))
            canvas.create_text(width/2, height/2, text=prin_words[1], font=("Courier", size*2), fill="Red")
        else:
            canvas.create_text(width/2, height/2, text=prin_words[0], font=("Courier", size))
            canvas.create_text(width/2, height/2, text=prin_words[1], font=("Courier", size), fill="Red")
        if ("." in word) or ("," in word) or (";" in word):
            panel.sleep(1.3 * delay)
        else:
            panel.sleep(delay)

def main(args):
    gen = WordGenerator(args[1])
    animate_text(gen, int(args[2]), int(args[3]), int(args[4]), 1.0/(float(args[5])/60000.0))

if __name__ == "__main__":
    main(sys.argv)