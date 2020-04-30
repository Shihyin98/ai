import re

class KB:
    def __init__(self):
        self.rules = []
        self.facts = {}
        self.dict = {}

    def load(self, code):
        lines = re.split(r'[\.]+ ?', code)
        # lines = code.split(/[\.]+ ?/);
        print(lines)
        for line in lines:
            if len(line.strip()) > 0:
                self.addRule(line)

    def isFact(self, term):
        if len(term) == 0:
            return True
        return self.facts.get(term) != None

    def check(self, rule):
        for term in rule['terms']:
            if self.isFact(term.strip()):
                continue
            else:
                return False
        return True

    def addFact(self, term):
        self.facts[term] = True
        print("addFact({})".format(term))

    def addRule(self, line):
        m = re.match(r"^([^<=]*)(<=(.*))?$", line)
        head = "" if m.group(1)==None else m.group(1).strip()
        # print('addRule: m.group(3)=', m.group(3))
        terms= "" if m.group(3)==None else m.group(3).strip().split(r"&")
        print("rule:head={} terms={}".format(head, terms))
        rule = {
          'head': head,
          'terms':terms,
          'satisfy':False
        }
        self.rules.append(rule)
        self.dict[head] = {
          'headHits': [rule],
          'bodyHits': []
        }

    def forwardChaining(self):
        while True:
            anySatisfy = False

            for rule in self.rules:
                if not rule['satisfy']:
                    if self.check(rule):
                        self.addFact(rule['head'])
                        rule['satisfy'] = True
                        anySatisfy = True
                
            if not anySatisfy:
                break

        print("facts=", self.facts.keys())
