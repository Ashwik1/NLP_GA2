import os.path, sys


def inside(words, unary, binary, nts):
    in_prob = []
    new = []
    for p in range(0, len(words)):
        for q in range(0, len(words)):
            new.append({})
        in_prob.append(new)
        new = []

    for p in range(0, len(words)):
        for unary_rule in unary:
            if unary_rule[1] == words[p]:
                in_prob[p][p][unary_rule[0]] = unary_rule[2]

    q = 1
    while q < len(words):
        for p in range(0, len(words)):
            if (p + q) < len(words):
                for left_nt in nts:
                    for right_nt in nts:
                        for rule_bi in binary:
                            if rule_bi[1] == left_nt and rule_bi[2] == right_nt:
                                prob_sum = 0
                                for d in range(p, p + q):
                                    if left_nt in in_prob[p][d].keys() and right_nt in in_prob[d + 1][p + q].keys():
                                        prob_sum += rule_bi[3] * in_prob[p][d][left_nt] * in_prob[d + 1][p + q][
                                            right_nt]

                                if prob_sum > 0:
                                    if rule_bi[0] in in_prob[p][p + q].keys():
                                        in_prob[p][p + q][rule_bi[0]] += prob_sum
                                    else:
                                        in_prob[p][p + q][rule_bi[0]] = prob_sum
        q += 1

    return in_prob
