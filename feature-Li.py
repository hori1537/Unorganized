from pymatgen import MPRester
import itertools
import time
import sys
import pandas as pd




file = open('feature-Li-2.csv', 'w')
file.write('pretty_formula,volume,density,nsites,spacegroup,total_magnetization,formation_energy_per_atom,band_gap\n')

API_KEY = '3abOTovzlAhHNJME' # Materials Project の API をここに入れる

# pymatgen は 103 元素扱えるので、binary は C(103,2) = 5253 パターンありえる
symbol_1 =["Li"]
symbol_2 = ["O"]

other_symbols =["H", "He", "Be", "B", "C", "N", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

other_symbols_ = itertools.combinations(other_symbols, 3) 

allBinaries = itertools.product(symbol_1,symbol_2,other_symbols_) 

print(allBinaries)
#print(all_symbols)
#print(other_symbols)

z=1
x=1

with MPRester(API_KEY) as m:
    for system in allBinaries:
        results = m.get_data(system[0] + '-' + system[1], data_type='vasp') # 計算データ（VASP）を入手
        
        print('system- ',system)
        print('results- ', results)
        

        time.sleep(2)
        
        for material in results:
            if material['e_above_hull'] < 1e-6: # 熱力学的安定性のチェック。凸包上にデータがあればその物質は安定（分解しない）。
                output = material['pretty_formula'] + ','  \
                       + str(material['volume']) + ','  \
                       + str(material['density']) + ','  \
                       + str(material['nsites']) + ','  \
                       + str(material['spacegroup']['number']) + ', ' \
                       + str(material['total_magnetization']) + ',' \
                       + str(material['formation_energy_per_atom']) + ',' \
					   + str(material['band_gap'])
                
                #print(material)
                #output = pd.Series(material)
                #print(output)
                #output.to_csv('Feature-.csv')
                #sys.exit()

                file.write(output + '\n')
                
                #print('output- ',output)
                #print(system)
                z+=1
                print(z)
                
                if z >= 1000000000:
                    file.close()
                    sys.exit()
            else:
                print('material e_above_hull- ', material['e_above_hull'] )
                
                x+=1
                print(x)
file.close()