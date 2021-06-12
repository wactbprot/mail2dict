import sys

class RD():
    def __init__(self):
        self.trans = {"*Unternehmen*":"company",
                      "*Ort*":"location",
                      "*Webseite*":"page",
                      "*Name*":"name"}
        self.data = {}
        self.op = "*"
        self.start_save = "*Unternehmen*"
        self.stop_save = "*Datenschutz*"
        self.empty_line = ["", "\n", "\r\n"]
        self.save = False

    def gen_dict(self, filename):
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line in self.empty_line:
                    continue

                if self.start_save in line:
                    self.save = True
                    
                if self.stop_save in line:
                    break

                if line.startswith(self.op):
                    self.key = None
                    
                if line in self.trans:
                    self.key = self.trans.get(line)
                    if self.data.get(self.key) is None:
                        self.data[self.key] = ""
                    continue
                        
                if self.save and self.key:
                    self.data[self.key] += line 

if __name__ == '__main__':
    i = sys.argv.index("-i")
    rd = RD()
    rd.gen_dict(sys.argv[i + 1])
    print(rd.data)
