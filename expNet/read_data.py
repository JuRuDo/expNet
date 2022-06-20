#!/bin/env python

import help_functions


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
    return nodes, edges
    
    
    


def plot(path, exp_stats, total, gene):
    keys = ['ERR2856510', 'ERR2856511', 'ERR2856512', 'ERR2856513', 'ERR2856514', 'ERR2856515', 'ERR2856516', 'ERR2856517', 'ERR2856518', 'ERR2856519', 'ERR2856520', 'ERR4578910', 'ERR4578911']
    df = pd.DataFrame(exp_stats)
    labels = list(df.index)
    titles = ['', '', 'R634Q#CRISPR', '', '', '', '', 'WT_NC_#no_CRISPR', '', '', '', '', 'WT#CRISPR_mock', '', '', '', '', 'P633L#CRISPR', '', '', ]
    for key in keys:
        titles.append(key + ': ' + str(total[key]))
    fig = make_subplots(rows=4, cols=5, subplot_titles=titles, horizontal_spacing=0.0, vertical_spacing=0.1,
                        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}],
                               [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}],
                               [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}],
                               [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}]])

    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856510']), name='ERR2856510', textinfo='none', scalegroup='one'), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856511']), name='ERR2856511', textinfo='none', scalegroup='one'), 1, 2)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856512']), name='ERR2856512', textinfo='none', scalegroup='one'), 1, 3)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856513']), name='ERR2856513', textinfo='none', scalegroup='one'), 1, 4)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856514']), name='ERR2856514', textinfo='none', scalegroup='one'), 2, 2)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856515']), name='ERR2856515', textinfo='none', scalegroup='one'), 2, 3)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856516']), name='ERR2856516', textinfo='none', scalegroup='one'), 3, 1)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856517']), name='ERR2856517', textinfo='none', scalegroup='one'), 3, 2)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856518']), name='ERR2856518', textinfo='none', scalegroup='one'), 3, 3)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856519']), name='ERR2856519', textinfo='none', scalegroup='one'), 3, 4)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR2856520']), name='ERR2856520', textinfo='none', scalegroup='one'), 3, 5)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR4578910']), name='ERR4578910', textinfo='none', scalegroup='one'), 4, 2)
    fig.add_trace(go.Pie(labels=labels, values=list(df['ERR4578911']), name='ERR4578911', textinfo='none', scalegroup='one'), 4, 3)
#    a,b = 1,1
#    for key in keys:
#        fig.add_trace(go.Pie(labels=labels, values=list(df[key]), name=key, textinfo='none', scalegroup='one'), a, b)
#        b += 1
#        if b == 6:
#            a += 1
#            b = 1
    fig.update_layout(title_text='Transcript Expression ' + gene)
    fig.write_image(file=path + '.svg', width=1200, height=800)
    fig.write_html(path + '.html')


