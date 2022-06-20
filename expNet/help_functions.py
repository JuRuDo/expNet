#!/bin/env python

from colour import Color
from numpy import std, mean

def get_colorscale(start, mid, stop):
    green = Color(start)
    yellow = Color(mid)
    red = Color(stop)
    colors = list(green.range_to(Color("yellow"),26))
    colors.pop()
    colors = colors + list(yellow.range_to(Color("red"),26))
    return colors


def prepare_network_data(exp_percent, fas_scores, sample_dict):
    data = {}
    nodes = []
    edges = {}
    for stype in fas_score:
        edges[stype] = []
        for edge in fas_scores[stype]:
            for node in edge:
                if not node in nodes:
                    nodes.append(node)
            edges[stype].append({'data': {'source': edges[0], 'target': edges[1], 'weight': fas_scores[stype][edges]*20}})
    for condition in sample_dict:
        exp = {}
        data[condition] = {'mean': []}
        for node in nodes:
            exp[node] = []
        for sample in sample_dict[condition]:
            data[condition][sample] = []
            for node in nodes:
                if node in exp_percent[sample]:
                    opacity = 0
                    size = exp_percent[sample][node] * 50 + 10
                    exp[node].append(exp_percent[sample][node])
                else:
                    blacken = 1
                    size = 10
                    exp[node].append(0.0)
                data[condition][sample].append({'data': {'id': node, 'label': node, 'size': size, 'color': 0, 'blacken':blacken}, 'position': {'x': 0, 'y': 0}})
        for node in nodes:
            meanexp = mean(exp[node])*50 + 10
            stdexp = int(round(std(exp[node]),2 ) * 50)
            if meanexp == 10:
                blacken = 1
            else:
                blacken = 0
            data[condition]['mean'].append({'data': {'id': node, 'label': node, 'size': meanexp, 'color': stdexp, 'blacken': blacken}, 'position': {'x': 0, 'y': 0}})
    return data, edges

