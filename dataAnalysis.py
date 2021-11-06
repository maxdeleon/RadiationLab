import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt

'''
Sr-90 Operating Voltage: 900V

'''

'''
-Cs-137 With Al Slides
-

run 1: 0.395 in
run 2: 0.270 in
run 3: 0.170 in
run 4: 0.080 in
run 5: 0.120 in
run 6: 0.040 in
run 7: 0.072 in
'''


'''
-Cs-137 With Lead Slides
-Cs-137 N_0: 533 C/30s

run 1: 0.375 in
run 2: 0.250 in
run 3: 0.314 in
run 4: 0.096 in
run 5: 0.032 in
run 6: 0.282 in
run 7: 0.125 in
'''


'''
-Ts-204 Slides A-F
-Ts_204 N_0: 1773 C/30s

run 1: 11 mg/cm^2
run 2: 16.1 mg/cm^2
run 3: 28.8 mg/cm^2
run 4: 78.3 mg/cm^2
run 5: 161.1 mg/cm^2
run 6: 121.2 mg/cm^2
run 7: 111.6 mg/cm^2
'''

error = lambda count_series: np.sqrt(count_series.mean())

def locate_files():
    file_list= []
    for root, dirs, files in os.walk('./data', topdown=True):
            dirs.clear() #with topdown true, this will prevent walk from going into subs
            for file in files:
            #do some stuff
                if '.tsv' in file:
                    print(file)
                    file_list.append(file)
                else: pass
    return files



def part1():
    df = pd.read_csv('data/sr90Callibration.tsv',delimiter='\t')
    plt.figure(figsize=(10,5))
    plt.title('Sr-90 Geiger-Müller Callibration Plot')
    plt.scatter(df['Voltage'],df['Counts']/10,c='k')
    plt.xlabel('Voltage (V)')
    plt.axvline(x=900,linestyle='--',c='r',alpha=0.7,label='Selected Operating Voltage')
    plt.ylabel('Counts / Second')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    '''df = pd.read_csv('data/Sr-90.tsv',delimiter='\t')
    print(df)'''
    files = locate_files()



    print('==========================================')
    
    '''for i in files:
        df = pd.read_csv('data/'+i,delimiter='\t')
        print('file name:',i)
        print(df)
        print('==========================================')'''
    
    '''sr90 = pd.read_csv('data/Sr-90.tsv',delimiter='\t')


    print('Sr-90 C/M error: {}'.format(error(sr90.Counts * 6)))
    print('Sr-90 C/M error: {}'.format(error(sr90.Counts * 6)))'''
    part1()
    





if __name__ == main():
    main()