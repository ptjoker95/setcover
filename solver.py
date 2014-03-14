#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Set = namedtuple("Set", ['index', 'cost', 'items'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    item_count = int(parts[0])
    set_count = int(parts[1])
    
    sets = []
    for i in range(1, set_count+1):
        parts = lines[i].split()
        sets.append(Set(i-1, float(parts[0]), map(int, parts[1:])))

    # build a trivial solution
    # pick add sets one-by-one until all the items are covered
    solution = [0]*set_count
    coverted = set()

    #set의 비용이 적은 순으로 정렬
    sets = sorted( sets, key=lambda sets:sets.cost, reverse=False )

    #set의 갯수를 셀 변수
    cancoverset = []
    # cover count를 셀 리스트
    itemcovercount = [0]*item_count
    
    loop_count = 0

    # 다 커버할 때 까지 루프를 돌린다.
    while len(coverted) <= item_count-1 and loop_count < 100:
        loop_count += 1
        # 가장 적게 커버하는 곳을 찾는다.
        for s in sets:
            #print "s[2] for cancoverset: ", s[2]
            if len(s[2]) is not 0:
                cancoverset += s[2]
        #print "cancoverset: ", cancoverset
            
        for i in range(0,item_count):
            itemcovercount[i] = cancoverset.count(i)
        #print "itemcovercount: ", itemcovercount
 
        minindex = itemcovercount.index(min( i for i in itemcovercount if i is not 0 ))
        #print "minindex: ", minindex
               
        # 가장 적게 커버하는 곳을 가지는 소방서 중에 비용이 가장 작은 곳을 선택한다.
        for s in sets:
            #print "s[2] for solution: ", s[2]
            if minindex in s[2]:
                #print "s.index: ", s.index
                solution[s.index] = 1
                coverted |= set(s.items)
                break
        #print "solution: ", solution
        #print "coverted: ", coverted
        
        # 중복된 것 지우기
        for s in sets:
            for c in coverted:
                if c in s[2]:
                    s[2].remove(c)
        
        cancoverset = []

        # 다 채워졌으면 루프 종료
       # if len(coverted) == 9:
       #     break

    """
    for s in sets:
        solution[s.index] = 1
        coverted |= set(s.items)
        if len(coverted) >= item_count:
            break
    """        
    #set이 선택되었는지 확인

    # calculate the cost of the solution
    obj = sum([s.cost*solution[s.index] for s in sets])

    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    #print "coverted:", coverted
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print 'Solving:', file_location
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/sc_6_1)'

