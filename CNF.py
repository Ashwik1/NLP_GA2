# Global dictionary used for storing the rules.
RULE_DICT = {}


def parseGrammar(item):
    with open(item) as i:
        lines = i.readlines()
    return [l.replace("->", "").split() for l in lines]


def addRule(value):
    global VAL_DICT
    if value[0] not in VAL_DICT:
        VAL_DICT[value[0]] = []
    VAL_DICT[value[0]].append(value[1:])
