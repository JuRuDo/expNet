#!/bin/env python

from expNet import help_functions
from numpy import std,mean
import pandas as pd


def read_expression(path, gene_id):
    expression_dict = {}
    with open(path, 'r') as infile:
        line = infile.readline()
        cells = line.rstrip('\n').split('\t')
        indexsample = {}
        for i in range(2, 15):
            indexsample[i] = cells[i].split('[')[0]
        line = infile.readline()
        while line:
            cells = line.rstrip('\n').split('\t')
            if cells[0] == gene_id:
                expression_dict[cells[1]] = {}
                for i in range(2, 15):
                    scores = cells[i].split('/')
                    expression_dict[cells[1]][indexsample[i]] = float(scores[1])
            line = infile.readline()
    return expression_dict
    

def read_sample_dict(path):
    sample_dict = {}
    with open(path, 'r') as infile:
        for line in infile.readlines():
            cells = line.rstrip('\n').split('\t')
            if cells[1] not in sample_dict:
                sample_dict[cells[1]] = []
            sample_dict[cells[1]].append(cells[0])
    return sample_dict


def read_fas_scores(path, gene_id, types):
    fas_scores = {}
    for stype in types:
        fas_scores[stype] = {}
        with open(path + '/' + stype + '/' + gene_id + '.phyloprofile', 'r') as infile:
            line = infile.readline()
            line = infile.readline()
            while line:
                cells = line.rstrip('\n').split('\t')
                fas_scores[stype][(cells[0], cells[2])] = (float(cells[3]) + float(cells[4])) / 2
                line = infile.readline()
    return fas_scores


def calc_percent(expression, sample_dict):
    exp_stats = {}
    exp_percent = {}
    total = {}
    for condition in sample_dict:
        for sample in sample_dict[condition]:
            exp_stats[sample] = {}
            exp_percent[sample] = {}
            total[sample] = 0
    for transcript in expression:
        for sample in expression[transcript]:
            total[sample] += float(expression[transcript][sample])
    for transcript in expression:
        for sample in expression[transcript]:
            if total[sample] > 0:
                exp_stats[sample][transcript] = float(expression[transcript][sample])
                exp_percent[sample][transcript] = float(expression[transcript][sample] / total[sample])
            else:
                exp_stats[sample][transcript] = 0.0
                exp_percent[sample][transcript] = 0.0
    return exp_stats, exp_percent, total


def main(expression_path, fas_path, sample_path, gene_id, colors):
    exp = read_expression(expression_path, gene_id)
    sample_dict = read_sample_dict(sample_path)
    exp_stats, exp_percent, total = calc_percent(exp, sample_dict)
    fas_scores = read_fas_scores(fas_path, gene_id, ['normal', 'transmembrane'])
    nodes, edges = help_functions.prepare_network_data(exp_percent, fas_scores, sample_dict, colors)
    table = make_expression_table(total, sample_dict)
    return nodes, edges, table
    

def make_expression_table(total, sample_dict):
    table = {}
    length = 0
    for condition in sample_dict:
        if length < len(sample_dict[condition]):
            length = len(sample_dict[condition])
    for condition in sample_dict:
        table[condition] = []
        for i in range(length+1):
            table[condition].append('')
        i = 0
        l = []
        for sample in sample_dict[condition]:
            table[condition][i] = sample + f': {total[sample]:.5f}'
            l.append(total[sample])
            i += 1
        table[condition].append(f'Mean: {mean(l):.5f}')
    df = pd.DataFrame(table)
    return df

