import math


############# TABLE #############
####  '0'     '1'     '2'     '3'

# '0'

# '1'

# '2'

# '3'
############# TABLE #############


def toNode(dest_router_name, src_router_name, sent_vector, init=False):
    global global_distinct_table
    global_distinct_table[src_router_name] = sent_vector
    if dest_router_name == '0':
        r0_distance_table[src_router_name] = sent_vector
        if not init:
            rtUpdate0()
    elif dest_router_name == '1':
        r1_distance_table[src_router_name] = sent_vector
        if not init:
            rtUpdate1()
    elif dest_router_name == '2':
        r2_distance_table[src_router_name] = sent_vector
        if not init:
            rtUpdate2()
    elif dest_router_name == '3':
        r3_distance_table[src_router_name] = sent_vector
        if not init:
            rtUpdate3()
    print_table(global_distinct_table, "Global table")
    # print_table(r0_distance_table, "R0 table")
    # print_table(r1_distance_table, "R1 table")
    # print_table(r2_distance_table, "R2 table")
    # print_table(r3_distance_table, "R3 table")


def rInit0():
    global r0_distance_table
    r0_distance_table['0'] = distance_info['0']

    for i in connected_info['0']:
        toNode(i, '0', distance_info['0'], True)


def rtUpdate0():
    modified = False
    for i in range(0, 4):
        if i == 0:
            continue
        actual = r0_distance_table['0'][i]
        for j in range(0, 4):
            if i == j or j == 0:
                continue
            if actual > (r0_distance_table['0'][j] + r0_distance_table[str(j)][i]):
                r0_distance_table['0'][i] = r0_distance_table['0'][j] + r0_distance_table[str(j)][i]
                modified = True
    if modified:
        for i in connected_info['0']:
            toNode(i, '0', distance_info['0'])


def rInit1():
    global r1_distance_table
    r1_distance_table['1'] = distance_info['1']

    for i in connected_info['1']:
        toNode(i, '1', distance_info['1'], True)


def rtUpdate1():
    modified = False
    for i in range(0, 4):
        if i == 1:
            continue
        actual = r1_distance_table['1'][i]
        for j in range(0, 4):
            if i == j or j == 1:
                continue
            if actual > (r1_distance_table['1'][j] + r1_distance_table[str(j)][i]):
                r1_distance_table['1'][i] = r1_distance_table['1'][j] + r1_distance_table[str(j)][i]
                modified = True
    if modified:
        for i in connected_info['1']:
            toNode(i, '1', distance_info['1'])


def rInit2():
    global r2_distance_table
    r2_distance_table['2'] = distance_info['2']

    for i in connected_info['2']:
        toNode(i, '2', distance_info['2'], True)


def rtUpdate2():
    modified = False
    for i in range(0, 4):
        if i == 2:
            continue
        actual = r2_distance_table['2'][i]
        for j in range(0, 4):
            if i == j or j == 2:
                continue
            if actual > (r2_distance_table['2'][j] + r2_distance_table[str(j)][i]):
                r2_distance_table['2'][i] = r2_distance_table['2'][j] + r2_distance_table[str(j)][i]
                modified = True
    if modified:
        for i in connected_info['2']:
            toNode(i, '2', distance_info['2'])


def rInit3():
    global r3_distance_table
    r3_distance_table['3'] = distance_info['3']

    for i in connected_info['3']:
        toNode(i, '3', distance_info['3'], True)


def rtUpdate3():
    modified = False
    for i in range(0, 4):
        if i == 3:
            continue
        actual = r3_distance_table['3'][i]
        for j in range(0, 4):
            if i == j or j == 3:
                continue
            if actual > (r3_distance_table['3'][j] + r3_distance_table[str(j)][i]):
                r3_distance_table['3'][i] = r3_distance_table['3'][j] + r3_distance_table[str(j)][i]
                modified = True
    if modified:
        for i in connected_info['3']:
            toNode(i, '3', distance_info['3'])


def print_table(table, label):
    print("##########", label, "##########")
    for key, value in table.items():
        print('\t\t{}'.format(key), end="")
    print("")
    for key, value in table.items():
        print('{}\t\t'.format(key), end="")
        for item in value:
            print(item, end="\t\t")
        print("")
    print("##########", label, "##########\n")


if __name__ == '__main__':
    r0_distance_table = dict({
        '0': [math.inf, math.inf, math.inf, math.inf],
        '1': [math.inf, math.inf, math.inf, math.inf],
        '2': [math.inf, math.inf, math.inf, math.inf],
        '3': [math.inf, math.inf, math.inf, math.inf]})

    r1_distance_table = dict({
        '0': [math.inf, math.inf, math.inf, math.inf],
        '1': [math.inf, math.inf, math.inf, math.inf],
        '2': [math.inf, math.inf, math.inf, math.inf],
        '3': [math.inf, math.inf, math.inf, math.inf]})

    r2_distance_table = dict({
        '0': [math.inf, math.inf, math.inf, math.inf],
        '1': [math.inf, math.inf, math.inf, math.inf],
        '2': [math.inf, math.inf, math.inf, math.inf],
        '3': [math.inf, math.inf, math.inf, math.inf]})

    r3_distance_table = dict({
        '0': [math.inf, math.inf, math.inf, math.inf],
        '1': [math.inf, math.inf, math.inf, math.inf],
        '2': [math.inf, math.inf, math.inf, math.inf],
        '3': [math.inf, math.inf, math.inf, math.inf]})

    distance_info = dict({
        '0': None,
        '1': None,
        '2': None,
        '3': None
    })

    global_distinct_table = dict({
        '0': [math.inf, math.inf, math.inf, math.inf],
        '1': [math.inf, math.inf, math.inf, math.inf],
        '2': [math.inf, math.inf, math.inf, math.inf],
        '3': [math.inf, math.inf, math.inf, math.inf]})

    connected_info = dict({
        '0': ('1', '2', '3'),
        '1': ('0', '2'),
        '2': ('0', '1', '3'),
        '3': ('0', '2')
    })

    path_0_0 = 0
    path_0_1 = 1  # 2#1
    path_0_2 = 3  # 5#3
    path_0_3 = 7  # 9#7
    distance_info['0'] = [path_0_0, path_0_1, path_0_2, path_0_3]

    path_1_0 = path_0_1
    path_1_1 = 0
    path_1_2 = 1  # 2#1
    path_1_3 = math.inf  # none
    distance_info['1'] = [path_1_0, path_1_1, path_1_2, path_1_3]

    path_2_0 = path_0_2
    path_2_1 = path_1_2
    path_2_2 = 0
    path_2_3 = 2  # 2
    distance_info['2'] = [path_2_0, path_2_1, path_2_2, path_2_3]

    path_3_0 = path_0_3
    path_3_1 = path_1_3
    path_3_2 = path_2_3
    path_3_3 = 0
    distance_info['3'] = [path_3_0, path_3_1, path_3_2, path_3_3]

    print("PreInfo", distance_info)
    rInit0()
    rInit1()
    rInit2()
    rInit3()

    print("Initialization Finished ")

    # global_distinct_table = dict({'0': r0_distance_table['0'], '1': r0_distance_table['1'], '2': r0_distance_table['2'],
    #                               '3': r0_distance_table['3']})

    print_table(r0_distance_table, "R0 init table")
    print_table(r1_distance_table, "R1 init table")
    print_table(r2_distance_table, "R2 init table")
    print_table(r3_distance_table, "R3 init table")
    #
    # rtUpdate0()
    # rtUpdate1()
    # rtUpdate2()
    # rtUpdate3()
    #
    # print_table(r0_distance_table, "R0 first step table")
    # print_table(r1_distance_table, "R1 first step table")
    # print_table(r2_distance_table, "R2 first step table")
    # print_table(r3_distance_table, "R3 first step table")
    #
    rtUpdate0()
    rtUpdate1()
    rtUpdate2()
    rtUpdate3()
    #
    #
    print_table(r0_distance_table, "R0 second step table")
    print_table(r1_distance_table, "R1 second step table")
    print_table(r2_distance_table, "R2 second step table")
    print_table(r3_distance_table, "R3 second step table")

    print_table(global_distinct_table, "Last Global")
