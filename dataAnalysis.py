import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
import scipy.stats as stats



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


# plot the callibration data
def part1():
    df = pd.read_csv('data/sr90Callibration.tsv',delimiter='\t')
    plt.figure(figsize=(10,5))
    plt.title('Sr-90 Geiger-Müller Callibration Plot')
    plt.scatter(df['Voltage'],df['Counts'],c='k')
    plt.xlabel('Voltage (V)')
    plt.axvline(x=900,linestyle='--',c='r',alpha=0.7,label='Selected Operating Voltage')
    plt.ylabel('Counts')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig('callibrationPlot.png')

# find the average number of counts and
def part2():
    sr90df = pd.read_csv('data/Sr-90.tsv',delimiter='\t')
    counts = np.array(sorted(sr90df['Counts']))
    N_hat = counts.mean()
    uncertainty = np.sqrt(counts.mean())
    lower_bound = N_hat - uncertainty
    upper_bound = N_hat + uncertainty

    i = 0
    for measurement in counts:
        if lower_bound < measurement < upper_bound:
            i += 1
        else: pass

    print('Average radiation counts {}'.format(N_hat))
    print('Statistical error: {}'.format(uncertainty))
    print('Number of trials: {}'.format(len(counts)))
    print('Approximately {} % of the counts are within 1 standard deviation of the mean'.format(round(i/len(counts)*100,2)))
    
    if i/len(counts) > 0.63:
        print('The theoretical metric is supported by the empirical data')
    else:
        print('The theoretical metric is not supported by the empirical data')





def part3():
    background_df = pd.read_csv('data/background30s.tsv',delimiter='\t')
    cs137_pb_df = pd.read_csv('data/cs-137-Pb.tsv',delimiter='\t')
    cs137_al_df = pd.read_csv('data/cs-137-Al.tsv',delimiter='\t')

    murho = 0.7

     

    background = background_df['Counts'].mean()

    N_0 = 533 - background

    pb_counts = cs137_pb_df['Counts'] - background
    al_counts = cs137_al_df['Counts'] - background
    pb_thicknesses = np.array([0.375,0.250,0.314,0.096,0.032,0.282,0.125])*2.54

    print(background)
    print(al_counts)


    plt.errorbar(pb_thicknesses,pb_counts,yerr=np.sqrt(pb_counts),fmt='o')
    pb_model = (N_0)*np.exp(-murho * pb_thicknesses)
    plt.scatter(pb_thicknesses,pb_model,c='g')


    plt.yscale('log')
    plt.show()


def main():
    '''df = pd.read_csv('data/Sr-90.tsv',delimiter='\t')
    print(df)'''
    #files = locate_files()



    print('==========================================')
    
    '''for i in files:
        df = pd.read_csv('data/'+i,delimiter='\t')
        print('file name:',i)
        print(df)
        print('==========================================')'''
    
    '''sr90 = pd.read_csv('data/Sr-90.tsv',delimiter='\t')


    print('Sr-90 C/M error: {}'.format(error(sr90.Counts * 6)))
    print('Sr-90 C/M error: {}'.format(error(sr90.Counts * 6)))'''
    #part1()
    #part2()
    part3()




if __name__ == main():
    main()