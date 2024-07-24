from optparse import OptionParser
import numpy as np
import os
import sys

from threading import Thread
from combine_parameters import toy_number,nice_priority,upperFactor


def readNorm(f_cscCard):
    f = open(f_cscCard,"r")
    norm = float(f.readline().split()[3])
    return norm

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2:
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-l', '--limits',type='string', action='store',
                    default   =   'Asymptotic',
                    dest      =   'limits',
                    help      =   'string to chose the type of limit computation, asymptotic or full CLS')
    parser.add_option('-s', '--significance', action='store_true',
                    default   =   False,
                    dest      =   'sig',
                    help      =   'Perform significance computation if bool is true')

    parser.add_option('-d', '--debug', type='int',
                    default       =       1,
                    dest          =       'debug',
                    help          =       'Debug level')

    (options, args) = parser.parse_args()
    debug = options.debug
    

    #input_dir='datacards_SR3_test_bkg_div2'
    #tree_dir='limitTrees_SR3_test_bkg_div2'

    #input_dir='datacards_SR1_test_UnB_v4_Raph_withGoodSignals'
    #tree_dir='limitTrees_SR1_test_UnB_v4_Raph_withGoodSignals'

    #input_dir='datacards_SR2_test_UnB_v4_Raph_withGoodSignals'
    #tree_dir='limitTrees_SR2_test_UnB_v4_Raph_withGoodSignals'

    input_dir='datacards_SR3_test_UnB_v4_Raph_withGoodSignals'
    tree_dir='limitTrees_SR3_test_UnB_v4_Raph_withGoodSignals_hybrid'

 
    #input_dir='datacards_SR3_test_UnB_v4_Raph_largeWindows_withGoodSignals'
    #tree_dir='limitTrees_SR3_test_UnB_v4_Raph_largeWindows_withGoodSignals'
    #input_dir='datacards_SR3_UnB_v4'
    #tree_dir='limitTrees_SR3_UnB_v4_sigStr1'
	
    os.system("mkdir -p {0}/".format(input_dir))
    os.system("mkdir -p {0}/".format(tree_dir))



    samples = [

        #'Gluino800_2018',
        'Gluino1000_2018',
        'Gluino1400_2018',
        'Gluino1600_2018',
	'Gluino1800_2018',
        'Gluino2000_2018',
        'Gluino2200_2018',
        'Gluino2400_2018',
        'Gluino2600_2018',
        #'Stop400_2018',
        #'Stop500_2018',
        #'Stop800_2018',
        'Stop1000_2018',
        'Stop1200_2018',
        'Stop1400_2018',
        'Stop1600_2018',
	'Stop1800_2018',
        'Stop2000_2018',
        'Stop2200_2018',
        'Stop2400_2018',
        'Stop2600_2018',
        'pairStau308_2018',
        'pairStau432_2018',
        'pairStau557_2018',
        'pairStau651_2018',
        'pairStau745_2018',
        'pairStau871_2018',
        'pairStau1029_2018',
        #'DYcharge1e_500_2018',
        'DYcharge1e_800_2018',
        'DYcharge1e_1000_2018',
        'DYcharge1e_1400_2018',
        'DYcharge1e_1800_2018',
        'DYcharge1e_2200_2018',
        'DYcharge1e_2600_2018',
        'DYcharge2e_500_2018',
        #'DYcharge2e_800_2018',
        'DYcharge2e_1000_2018',
        'DYcharge2e_1400_2018',
        'DYcharge2e_1800_2018',
        'DYcharge2e_2200_2018',
        'DYcharge2e_2600_2018',
        'gmsbStau200_2018',
        'gmsbStau247_2018',
        'gmsbStau308_2018',
        'gmsbStau432_2018',
        'gmsbStau557_2018',
        'gmsbStau651_2018',
        'gmsbStau745_2018',
        'gmsbStau871_2018',
        'gmsbStau1029_2018',
        'tauPrime2e-200-ZPrime-3000_2018',
        'tauPrime2e-200-ZPrime-4000_2018',
        'tauPrime2e-200-ZPrime-5000_2018',
        'tauPrime2e-200-ZPrime-6000_2018',
        'tauPrime2e-200-ZPrime-7000_2018',
        'tauPrime2e-200-ZPrimeSSM-3000_2018',
        'tauPrime2e-200-ZPrimeSSM-4000_2018',
        'tauPrime2e-200-ZPrimeSSM-5000_2018',
        'tauPrime2e-200-ZPrimeSSM-6000_2018',
        'tauPrime2e-200-ZPrimeSSM-7000_2018',
        'tauPrime2e-400-ZPrime-3000_2018',
        'tauPrime2e-400-ZPrime-4000_2018',
        'tauPrime2e-400-ZPrime-5000_2018',
        'tauPrime2e-400-ZPrime-6000_2018',
        'tauPrime2e-400-ZPrime-7000_2018',
        'tauPrime2e-400-ZPrimeSSM-3000_2018',
        'tauPrime2e-400-ZPrimeSSM-4000_2018',
        'tauPrime2e-400-ZPrimeSSM-5000_2018',
        'tauPrime2e-400-ZPrimeSSM-6000_2018',
        'tauPrime2e-400-ZPrimeSSM-7000_2018',
        'tauPrime2e-600-ZPrime-3000_2018',
        'tauPrime2e-600-ZPrime-4000_2018',
        'tauPrime2e-600-ZPrime-5000_2018',
        'tauPrime2e-600-ZPrime-6000_2018',
        'tauPrime2e-600-ZPrime-7000_2018',
        'tauPrime2e-600-ZPrimeSSM-3000_2018',
        'tauPrime2e-600-ZPrimeSSM-4000_2018',
        'tauPrime2e-600-ZPrimeSSM-5000_2018',
        'tauPrime2e-600-ZPrimeSSM-6000_2018',
        'tauPrime2e-600-ZPrimeSSM-7000_2018',
        'tauPrime2e-800-ZPrime-4000_2018',
        'tauPrime2e-800-ZPrime-5000_2018',
        'tauPrime2e-800-ZPrime-6000_2018',
        'tauPrime2e-800-ZPrime-7000_2018',
        'tauPrime2e-800-ZPrimeSSM-4000_2018',
        'tauPrime2e-800-ZPrimeSSM-5000_2018',
        'tauPrime2e-800-ZPrimeSSM-6000_2018',
        'tauPrime2e-800-ZPrimeSSM-7000_2018',
        'tauPrime2e-1000-ZPrime-3000_2018',
        'tauPrime2e-1000-ZPrime-4000_2018',
        'tauPrime2e-1000-ZPrime-5000_2018',
        'tauPrime2e-1000-ZPrime-6000_2018',
        'tauPrime2e-1000-ZPrime-7000_2018',
        'tauPrime2e-1000-ZPrimeSSM-3000_2018',
        'tauPrime2e-1000-ZPrimeSSM-4000_2018',
        'tauPrime2e-1000-ZPrimeSSM-5000_2018',
        'tauPrime2e-1000-ZPrimeSSM-6000_2018',
        'tauPrime2e-1000-ZPrimeSSM-7000_2018',
        'tauPrime2e-1200-ZPrime-3000_2018',
        'tauPrime2e-1200-ZPrime-4000_2018',
        'tauPrime2e-1200-ZPrime-5000_2018',
        'tauPrime2e-1200-ZPrime-6000_2018',
        'tauPrime2e-1200-ZPrime-7000_2018',
        'tauPrime2e-1200-ZPrimeSSM-3000_2018',
        'tauPrime2e-1200-ZPrimeSSM-4000_2018',
        'tauPrime2e-1200-ZPrimeSSM-5000_2018',
        'tauPrime2e-1200-ZPrimeSSM-6000_2018',
        'tauPrime2e-1200-ZPrimeSSM-7000_2018',
        'tauPrime2e-1400-ZPrime-3000_2018',
        'tauPrime2e-1400-ZPrime-4000_2018',
        'tauPrime2e-1400-ZPrime-5000_2018',
        'tauPrime2e-1400-ZPrime-6000_2018',
        'tauPrime2e-1400-ZPrime-7000_2018',
        'tauPrime2e-1400-ZPrimeSSM-3000_2018',
        'tauPrime2e-1400-ZPrimeSSM-4000_2018',
        'tauPrime2e-1400-ZPrimeSSM-5000_2018',
        'tauPrime2e-1400-ZPrimeSSM-6000_2018',
        'tauPrime2e-1400-ZPrimeSSM-7000_2018',
    ]

    #for sample in samples:
    paramTest = [45,45,45,45,45]

    paramGlu1000 = [0.0003,0.0005,0.0008,0.0015,0.0026]
    paramGlu1400 = [0.0038,0.0064,0.0120,0.0234,0.0365]
    paramGlu1600 = [0.0130,0.0222,0.0425,0.0846,0.1293]
    paramGlu1800 = [0.0419,0.0729,0.1411,0.2829,0.4292]
    paramGlu2000 = [0.1341,0.2371,0.4639,0.9298,1.41]
    paramGlu2200 = [0.5,0.8,1.6,3.2,4.8]
    paramGlu2400 = [1.5,2.4,4.7,9.4,14.2]
    paramGlu2600 = [4,7,14,29,43]

    paramStop800 = [0.005,0.007,0.012,0.019,0.032]
    paramStop1000 = [0.015,0.023,0.04,0.073,0.12]
    paramStop1200 = [0.05,0.08,0.14,0.28,0.42]
    paramStop1400 = [0.17,0.27,0.52,1,1.55]
    paramStop1600 = [0.55,1,1.8,3.55,5.5]
    paramStop1800 = [1.8,3.2,6,12,18]
    paramStop2000 = [5.6,10,20,38,60]
    paramStop2200 = [18,31,60,120,180]
    paramStop2400 = [50,90,180,350,540]
    paramStop2600 = [140,250,500,1000,1500]


    paramStau308 = [0.1,0.13,0.19,0.3,0.42]
    paramStau432 = [0.1,0.14,0.22,0.31,0.45]
    paramStau557 = [0.2,0.26,0.38,0.6,0.95]
    paramStau651 = [0.3,0.42,0.65,1.1,1.8]
    paramStau745 = [0.42,0.62,1,1.65,2.8]
    paramStau871 = [0.75,1.1,1.9,3.3,5.6]
    paramStau1029 = [1.8,2.7,4.8,9,15]

    paramDY1e800 = [0.07,0.1,0.17,0.28,0.5]
    paramDY1e1000 = [0.16,0.25,0.44,0.8,1.3]
    paramDY1e1400 = [1,1.7,3.1,6,10]
    paramDYie1800 = [6,11,20,40,60]
    paramDY1e2200 = [35,65,120,230,360]
    paramDY1e2600 = [210,360,700,1400,2100]

    paramDY2e500 = [0.0035,0.0045,0.0065,0.0095,0.014]
    paramDY2e1000 = [0.04,0.06,0.1,0.18,0.3]
    paramDY2e1400 = [0.25,0.42,0.8,1.5,2.3]
    paramDY2e1800 = [1.5,2.8,5,10,16]
    paramDY2e2200 = [10,15,30,60,100]
    paramDY2e2600 = [50,90,170,330,510]



    paramZprime3000Tau200 = [0.03,0.045,0.08,0.15,0.24]
    paramZprime4000Tau200 = [0.22,0.36,0.67,1.25,2]
    paramZprime5000Tau200 = [2,3.3,6.1,11.5,19]
    paramZprime6000Tau200 = [24,38,70,132,215]
    paramZprime7000Tau200 = [580,840,1330,2150,3400]

    paramZprime3000Tau400 = [0.03,0.05,0.08,0.14,0.24]
    paramZprime4000Tau400 = [0.22,0.36,0.67,1.25,2]
    paramZprime5000Tau400 = [2,3.3,6,11.5,18]
    paramZprime6000Tau400 = [20,34,64,125,200]
    paramZprime7000Tau400 = [270,440,800,1500,2400]

    paramZprime3000Tau600 = [0.04,0.06,0.09,0.15,0.24]
    paramZprime4000Tau600 = [0.22,0.36,0.65,1.22,2]
    paramZprime5000Tau600 = [1.9,3.2,6,11.5,18]
    paramZprime6000Tau600 = [19,32,61,120,190]
    paramZprime7000Tau600 = [210,370,700,1300,2100]


    paramZprime4000Tau800 = [0.2,0.34,0.64,1.21,2]
    paramZprime5000Tau800 = [1.8,3.1,5.8,11.5,18]
    paramZprime6000Tau800 = [18,32,60,115,185]
    paramZprime7000Tau800 = [190,330,630,1210,1930]

    paramZprime3000Tau1000 = [0.026,0.042,0.08,0.15,0.24]
    paramZprime4000Tau1000 = [0.2,0.35,0.64,1.2,2]
    paramZprime5000Tau1000 = [1.8,3,5.7,11,17.5]
    paramZprime6000Tau1000 = [18,32,60,115,184]
    paramZprime7000Tau1000 = [183,320,610,1200,1900]


    paramZprime3000Tau1200 = [0.04,0.07,0.13,0.25,0.38]
    paramZprime4000Tau1200 = [0.2,0.35,0.63,1.2,1.9]
    paramZprime5000Tau1200 = [1.7,3,5.7,11,17.5]
    paramZprime6000Tau1200 = [18,31,60,114,180]
    paramZprime7000Tau1200 = [205,360,700,1340,2100]


    paramZprime3000Tau1400 = [3,4.2,6.5,10.5,17]
    paramZprime4000Tau1400 = [0.2,0.35,0.67,1.25,2]
    paramZprime5000Tau1400 = [1.8,3,5.6,11,17]
    paramZprime6000Tau1400 = [18,31,60,113,180]
    paramZprime7000Tau1400 = [205,355,680,1300,2100]

    paramZprimeSSM3000Tau600 = [0.01,0.02,0.025,0.042,0.07]
    paramZprimeSSM4000Tau600 = [0.07,0.11,0.2,0.4,0.6]
    paramZprimeSSM5000Tau600 = [0.6,1,1.8,3.5,5.5]
    paramZprimeSSM6000Tau600 = [6,10,20,36,57]
    paramZprimeSSM7000Tau600 = [60,100,200,360,580]

    def task(sample):
        name=sample
        name2="datacard_"+sample
        name2=sample
        print name
        paramsRange = []

        paramsRange = paramTest
        if(sample == 'Gluino1000_2018'):
            paramsRange=paramGlu1000
        if(sample == 'Gluino1400_2018'):
            paramsRange=paramGlu1400
        if(sample == 'Gluino1600_2018'):
            paramsRange=paramGlu1600
        if(sample == 'Gluino1800_2018'):
            paramsRange=paramGlu1800
        if(sample == 'Gluino2000_2018'):
            paramsRange=paramGlu2000
        if(sample == 'Gluino2200_2018'):
            paramsRange=paramGlu2200
        if(sample == 'Gluino2400_2018'):
            paramsRange=paramGlu2400
        if(sample == 'Gluino2600_2018'):
            paramsRange=paramGlu2600

        if(sample=='Stop800_2018'):
            paramsRange = paramStop800
        if(sample=='Stop1000_2018'):
            paramsRange = paramStop1000
        if(sample=='Stop1200_2018'):
            paramsRange = paramStop1200
        if(sample=='Stop1400_2018'):
            paramsRange = paramStop1400
        if(sample=='Stop1600_2018'):
            paramsRange = paramStop1600
        if(sample=='Stop1800_2018'):
            paramsRange = paramStop1800
        if(sample=='Stop2000_2018'):
            paramsRange = paramStop2000
        if(sample=='Stop2200_2018'):
            paramsRange = paramStop2200
        if(sample=='Stop2400_2018'):
            paramsRange = paramStop2400
        if(sample=='Stop2600_2018'):
            paramsRange = paramStop2600

        if(sample == 'pairStau308_2018'):
            paramsRange=paramStau308
        if(sample == 'pairStau432_2018'):
            paramsRange=paramStau432
        if(sample == 'pairStau557_2018'):
            paramsRange=paramStau557
        if(sample == 'pairStau651_2018'):
            paramsRange=paramStau651
        if(sample == 'pairStau745_2018'):
            paramsRange=paramStau745
        if(sample == 'pairStau871_2018'):
            paramsRange=paramStau871
        if(sample == 'pairStau1029_2018'):
            paramsRange=paramStau1029

        if(sample=='DYcharge1e_800_2018'):    
            paramsRange=paramDY1e800
        if(sample=='DYcharge1e_1000_2018'):    
            paramsRange=paramDY1e1000
        if(sample=='DYcharge1e_1400_2018'):    
            paramsRange=paramDY1e1400
        if(sample=='DYcharge1e_1800_2018'):    
            paramsRange=paramDY1e1800
        if(sample=='DYcharge1e_2200_2018'):    
            paramsRange=paramDY1e2200
        if(sample=='DYcharge1e_2600_2018'):    
            paramsRange=paramDY1e2600

        if(sample=='DYcharge2e_500_2018'):    
            paramsRange=paramDY2e500
        if(sample=='DYcharge2e_1000_2018'):    
            paramsRange=paramDY2e1000
        if(sample=='DYcharge2e_1400_2018'):    
            paramsRange=paramDY2e1400
        if(sample=='DYcharge2e_1800_2018'):    
            paramsRange=paramDY2e1800
        if(sample=='DYcharge2e_2200_2018'):    
            paramsRange=paramDY2e2200
        if(sample=='DYcharge2e_2600_2018'):    
            paramsRange=paramDY2e2600

        if(sample == 'tauPrime2e-200-ZPrime-3000_2018' or sample == 'tauPrime2e-200-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime3000Tau200
        if(sample == 'tauPrime2e-200-ZPrime-4000_2018' or sample == 'tauPrime2e-200-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau200
        if(sample == 'tauPrime2e-200-ZPrime-5000_2018' or sample == 'tauPrime2e-200-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau200
        if(sample == 'tauPrime2e-200-ZPrime-6000_2018' or sample == 'tauPrime2e-200-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau200
        if(sample == 'tauPrime2e-200-ZPrime-7000_2018' or sample == 'tauPrime2e-200-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau200


        if(sample == 'tauPrime2e-400-ZPrime-3000_2018' or sample == 'tauPrime2e-400-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime3000Tau400
        if(sample == 'tauPrime2e-400-ZPrime-4000_2018' or sample == 'tauPrime2e-400-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau400
        if(sample == 'tauPrime2e-400-ZPrime-5000_2018' or sample == 'tauPrime2e-400-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau400

        if(sample == 'tauPrime2e-400-ZPrime-6000_2018' or sample == 'tauPrime2e-400-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau400
        if(sample == 'tauPrime2e-400-ZPrime-7000_2018' or sample == 'tauPrime2e-400-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau400


        if(sample == 'tauPrime2e-600-ZPrime-3000_2018'):
            paramsRange=paramZprime3000Tau600
        if(sample == 'tauPrime2e-600-ZPrime-4000_2018'):
            paramsRange=paramZprime4000Tau600
        if(sample == 'tauPrime2e-600-ZPrime-5000_2018'):
            paramsRange=paramZprime5000Tau600
        if(sample == 'tauPrime2e-600-ZPrime-6000_2018'):
            paramsRange=paramZprime6000Tau600
        if(sample == 'tauPrime2e-600-ZPrime-7000_2018'):
            paramsRange=paramZprime7000Tau600
      
        if(sample == 'tauPrime2e-600-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprimeSSM3000Tau600
        if(sample == 'tauPrime2e-600-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprimeSSM4000Tau600
        if(sample == 'tauPrime2e-600-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprimeSSM5000Tau600
        if(sample == 'tauPrime2e-600-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprimeSSM6000Tau600
        if(sample == 'tauPrime2e-600-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprimeSSM7000Tau600



        if(sample == 'tauPrime2e-800-ZPrime-3000_2018' or sample == 'tauPrime2e-800-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime4000Tau800
        if(sample == 'tauPrime2e-800-ZPrime-4000_2018' or sample == 'tauPrime2e-800-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau800
        if(sample == 'tauPrime2e-800-ZPrime-5000_2018' or sample == 'tauPrime2e-800-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau800
        if(sample == 'tauPrime2e-800-ZPrime-6000_2018' or sample == 'tauPrime2e-800-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau800
        if(sample == 'tauPrime2e-800-ZPrime-7000_2018' or sample == 'tauPrime2e-800-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau800


        if(sample == 'tauPrime2e-1000-ZPrime-3000_2018' or sample == 'tauPrime2e-1000-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime3000Tau1000
        if(sample == 'tauPrime2e-1000-ZPrime-4000_2018' or sample == 'tauPrime2e-1000-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau1000
        if(sample == 'tauPrime2e-1000-ZPrime-5000_2018' or sample == 'tauPrime2e-1000-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau1000
        if(sample == 'tauPrime2e-1000-ZPrime-6000_2018' or sample == 'tauPrime2e-1000-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau1000
        if(sample == 'tauPrime2e-1000-ZPrime-7000_2018' or sample == 'tauPrime2e-1000-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau1000


        if(sample == 'tauPrime2e-1200-ZPrime-3000_2018' or sample == 'tauPrime2e-1200-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime3000Tau1200
        if(sample == 'tauPrime2e-1200-ZPrime-4000_2018' or sample == 'tauPrime2e-1200-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau1200
        if(sample == 'tauPrime2e-1200-ZPrime-5000_2018' or sample == 'tauPrime2e-1200-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau1200
        if(sample == 'tauPrime2e-1200-ZPrime-6000_2018' or sample == 'tauPrime2e-1200-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau1200
        if(sample == 'tauPrime2e-1200-ZPrime-7000_2018' or sample == 'tauPrime2e-1200-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau1200

        if(sample == 'tauPrime2e-1400-ZPrime-3000_2018' or sample == 'tauPrime2e-1400-ZPrimeSSM-3000_2018'):
            paramsRange=paramZprime3000Tau1400
        if(sample == 'tauPrime2e-1400-ZPrime-4000_2018' or sample == 'tauPrime2e-1400-ZPrimeSSM-4000_2018'):
            paramsRange=paramZprime4000Tau1400
        if(sample == 'tauPrime2e-1400-ZPrime-5000_2018' or sample == 'tauPrime2e-1400-ZPrimeSSM-5000_2018'):
            paramsRange=paramZprime5000Tau1400
        if(sample == 'tauPrime2e-1400-ZPrime-6000_2018' or sample == 'tauPrime2e-1400-ZPrimeSSM-6000_2018'):
            paramsRange=paramZprime6000Tau1400
        if(sample == 'tauPrime2e-1400-ZPrime-7000_2018' or sample == 'tauPrime2e-1400-ZPrimeSSM-7000_2018'):
            paramsRange=paramZprime7000Tau1400





        if(options.limits == "CLS"):
            expMedian = "0.5"
            expp1sig = "0.84"
            expp2sig = "0.975"
            expm1sig = "0.16"
            expm2sig = "0.025"
    
            nameMedian = name+"_"+expMedian.replace(".","p")
            namep1sig = name+"_"+expp1sig.replace(".","p")
            namep2sig = name+"_"+expp2sig.replace(".","p")
            namem1sig = name+"_"+expm1sig.replace(".","p")
            namem2sig = name+"_"+expm2sig.replace(".","p")
        
            run_combine_median = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --expectedFromGrid={} --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 --adaptiveToys 1 -T {} &".format(nice_priority,name, input_dir, name2,expMedian,toy_number)
            print run_combine_median
            os.system(run_combine_median)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.quant0.500.root {1}/".format(name, tree_dir))
   
            run_combine_observed = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 &".format(nice_priority,name, input_dir, name2)
            os.system(run_combine_observed)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.root {1}/higgsCombine.{2}.HybridNew.mH120.obs.root".format(name,tree_dir,name))

 
            run_combine_p1sig = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --expectedFromGrid={} --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 --adaptiveToys 1 -T {} &".format(nice_priority,name, input_dir, name2,expp1sig,toy_number)
            print run_combine_p1sig
            os.system(run_combine_p1sig)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.quant0.840.root {1}/".format(name, tree_dir))
     
            run_combine_p2sig = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --expectedFromGrid={} --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 --adaptiveToys 1 -T {} &".format(nice_priority,name, input_dir, name2,expp2sig,toy_number)
            print run_combine_p2sig
            os.system(run_combine_p2sig)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.quant0.975.root {1}/".format(name, tree_dir))
    
    
            run_combine_m1sig = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --expectedFromGrid={} --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 --adaptiveToys 1 -T {} &".format(nice_priority,name, input_dir, name2,expm1sig,toy_number)
            print run_combine_m1sig
            os.system(run_combine_m1sig)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.quant0.160.root {1}/".format(name, tree_dir))
            
            run_combine_m2sig = "nice -n {} combine -H AsymptoticLimits -M HybridNew  -n .{} -d {}/{}.txt --expectedFromGrid={} --saveWorkspace --LHCmode LHC-limits -v 1 --rRelAcc 0.000005 --rAbsAcc 0.000005 --adaptiveToys 1 -T {} &".format(nice_priority,name, input_dir, name2,expm2sig,toy_number)
            print run_combine_m2sig
            os.system(run_combine_m2sig)
            os.system("mv higgsCombine.{0}.HybridNew.mH120.quant0.025.root {1}/".format(name, tree_dir))

        if(options.limits == "Asymptotic"):
            run_combine = "combine -M AsymptoticLimits -n .{} -d {}/{}.txt --rRelAcc 0.000005 --rAbsAcc 0.000005 --rMin -1000.0 --rMax 1000.0".format(name, input_dir, name2)
            if(debug>0):
                print("Running command {}".format(run_combine))
            os.system(run_combine)
            os.system("mv higgsCombine.{0}.AsymptoticLimits.mH120.root {1}/".format(name, tree_dir))


        if(options.sig):
            run_combine = "combine -M Significance -n .{} {}/{}.txt -t -1 --expectSignal=1" .format(name, input_dir, name2)
            #run_combine = "combine -M Significance -n .{} {}/{}.txt" .format(name, input_dir, name2)
            print run_combine
            os.system(run_combine)
            os.system("mv higgsCombine.{0}.Significance.mH120.root {1}/".format(name, tree_dir))
    
    for sample in samples:
        ### For parallel running, use both following lines
        #t = Thread(target=task, args=(sample,))
        #t.start()
        
        ### use this line to run signal one after the other
        task(sample)
