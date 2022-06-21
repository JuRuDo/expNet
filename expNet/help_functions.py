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


def prepare_network_data(exp_percent, fas_scores, sample_dict, colors):
    data = {}
    nodes = []
    edges = {}
    for stype in fas_scores:
        edges[stype] = []
        for edge in fas_scores[stype]:
            for node in edge:
                if not node in nodes:
                    nodes.append(node)
            if not edge[0] == edge[1]:
                edges[stype].append({'data': {'source': edge[0], 'target': edge[1], 'weight': fas_scores[stype][edge]*5+1}})
    for condition in sample_dict:
        exp = {}
        data[condition] = {'mean': []}
        for node in nodes:
            exp[node] = []
        for sample in sample_dict[condition]:
            data[condition][sample] = []
            x = 0
            for node in nodes:
                blacken = 0
                if exp_percent[sample][node] > 0.0:
                    size = exp_percent[sample][node] * 50 + 10
                    exp[node].append(exp_percent[sample][node])
                else:
                    blacken = 1
                    size = 10
                    exp[node].append(0.0)
                data[condition][sample].append({'data': {'id': node, 'label': node, 'size': size, 'color': str(colors[0]), 'blacken':blacken}, 'position': {'x': 20*x, 'y': 20*x}})
                x += 1
        x = 0
        for node in nodes:

            meanexp = mean(exp[node])*50 + 10
            stdexp = int(round(std(exp[node]),2 ) * 100)
            if meanexp == 10:
                blacken = 1
            else:
                blacken = 0
            data[condition]['mean'].append({'data': {'id': node, 'label': node, 'size': meanexp, 'color': str(colors[stdexp]), 'blacken': blacken}, 'position': {'x': 20*x, 'y': 20*x}})
            x += 1
    return data, edges

