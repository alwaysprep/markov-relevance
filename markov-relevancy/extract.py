from collections import defaultdict


def from_tsv_get(file_name, delimeter, *args):
    train, test = [], []
    with open(file_name) as tsv:
        tsv.readline() # first line is general info of file, it shouldn't be there

        columns = tsv.readline().split(delimeter) # second line column names
        columns[-1] = columns[-1].replace("\n", "")

        column_indexes = [columns.index(search_term) for search_term in args]
        for line in tsv:
            lis_line = line.split(delimeter)
            lis_line[-1] = lis_line[-1].replace("\n", "")

            if lis_line[column_indexes[1]] == "Added" or lis_line[column_indexes[1]] == "Excluded":
                train.append([lis_line[col] for col in column_indexes])
            elif lis_line[column_indexes[1]] == "None":
                test.append([lis_line[col] for col in column_indexes])

    return train, test


def is_relevant(line):
    return (line[1] == 'Added' or line[2] == "1") and (not line[1] == 'Excluded')


def hist(line, m, dic):
    mgram = [tuple(line[i:i+m]) for i in range(len(line)-m+1)]

    for element in mgram:
        dic[element] += 1



def hists(lis, m):
    rel_hist = defaultdict(int)
    non_rel_hist = defaultdict(int)
    for line in lis:
        if is_relevant(line):
            hist(line[0].split(), m, rel_hist)
        else:
            hist(line[0].split(), m, non_rel_hist)

            
    return rel_hist, non_rel_hist










