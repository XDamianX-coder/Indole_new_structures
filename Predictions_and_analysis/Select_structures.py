#Libraries import
import pandas as pd
import numpy as np
from rdkit import Chem
from syba.syba import SybaClassifier
from mordred import Calculator, descriptors, Lipinski
import mordred
from rdkit.DataStructs.cDataStructs import TanimotoSimilarity

def prepare_data(File_with_generated_structures):
    
    #Initial structures load
    initial = pd.read_excel(File_with_generated_structures)
    initial = initial.columns.values.tolist()
    initial = initial[4:]
    
    #Generated structures load
    generated_smiles = pd.read_excel(File_with_generated_structures)
    generated_smiles = generated_smiles['new_SMILES']
    
    #MOL object creation
    mol_objs_ini = [Chem.MolFromSmiles(smi) for smi in initial]
    mol_objs_gen = [Chem.MolFromSmiles(smi) for smi in generated_smiles]

    #Molecular descriptors calculation
    calc = Calculator(descriptors, ignore_3D=True)
    molecular_descriptors_initials = calc.pandas(mol_objs_ini)
    molecular_descriptors_generated = calc.pandas(mol_objs_gen)
    
    return molecular_descriptors_initials, molecular_descriptors_generated, initial, generated_smiles

#Deletion of invalid data
def is_morder_missing(x):
    return np.nan if type(x) == mordred.error.Missing or type(x) == mordred.error.Error else x 

def deletion_of_invalid_data(molecular_descriptors_initials_, molecular_descriptors_generated_):
    molecular_descriptors_initials = molecular_descriptors_initials_.applymap(is_morder_missing)
    molecular_descriptors_generated = molecular_descriptors_generated_.applymap(is_morder_missing)
    
    simple_preprocessing = True

    if simple_preprocessing:
        molecular_descriptors_initials = molecular_descriptors_initials.dropna(axis=1, how='any')
        molecular_descriptors_generated = molecular_descriptors_generated.dropna(axis=1, how='any')
    
    molecular_descriptors_initials = molecular_descriptors_initials.loc[:, (molecular_descriptors_initials != 0).any(axis=0)]
    molecular_descriptors_generated = molecular_descriptors_generated.loc[:, (molecular_descriptors_generated != 0).any(axis=0)]
    return molecular_descriptors_initials, molecular_descriptors_generated


#Create useful dataframes
def create_df_with_molecular_descriptors(molecular_descriptors_initials_, molecular_descriptors_generated_, initial_, generated_smiles_):
    initial_strcutures = pd.DataFrame(data=molecular_descriptors_initials_[descriptor1], columns=[descriptor1])
    initial_strcutures[descriptor2] = molecular_descriptors_initials_[descriptor2]
    initial_strcutures[descriptor3] = molecular_descriptors_initials_[descriptor3]
    initial_strcutures['smiles'] = initial_

    generated_strcutures = pd.DataFrame(data=molecular_descriptors_generated_[descriptor1], columns=[descriptor1])

    generated_strcutures[descriptor2] = molecular_descriptors_generated_[descriptor2]
    generated_strcutures[descriptor3] = molecular_descriptors_generated[descriptor3]
    generated_strcutures['smiles'] = generated_smiles_

    return initial_strcutures, generated_strcutures


#Selection of the closest structures based on average score
def takeClosest(descriptor_1, descriptor_1_collection, descriptor_2, descriptor_2_collection, descriptor_3, descriptor_3_collection):
    average_picked = (descriptor_1+descriptor_2+descriptor_3)/3
    val = range(len(generated_strcutures[descriptor1]))
    dfc = pd.DataFrame(data=val, columns=['Number'])
    val_ = []
    for i in range(len(descriptor_1_collection)):
        average_ = (descriptor_1_collection[i]+descriptor_2_collection[i]+descriptor_3_collection[i])/3
        val_.append(average_)
    dfc['Average'] = val_
    
    closest_val = min(dfc['Average'], key=lambda x:abs(x-average_picked))
    
    closest_value_df =  dfc.loc[(dfc['Average'] == closest_val)]
    
    dfc = dfc.loc[dfc['Average'] != closest_val]
    
    closest_val_ = min(dfc['Average'], key=lambda x:abs(x-average_picked))
    
    closest_value_df_ =  dfc.loc[(dfc['Average'] == closest_val_)]
    
    dfc = dfc.loc[dfc['Average'] != closest_val_]
    
    closest_val__ = min(dfc['Average'], key=lambda x:abs(x-average_picked))
    
    closest_value_df__ =  dfc.loc[(dfc['Average'] == closest_val__)]
    
    closest_value_df_combined = pd.concat([closest_value_df, closest_value_df_, closest_value_df__], ignore_index=True)
    
    return closest_value_df_combined


#Search space
def create_a_box_to_search_within(center_of_a_box, size_of_a_box):
    chemical_space_descriptor_1 = [center_of_a_box[0]-size_of_a_box[0], center_of_a_box[0]+size_of_a_box[0]]
    chemical_space_descriptor_2 = [center_of_a_box[1]-size_of_a_box[1], center_of_a_box[1]+size_of_a_box[1]]
    chemical_space_descriptor_3 = [center_of_a_box[2]-size_of_a_box[2], center_of_a_box[2]+size_of_a_box[2]]
    return chemical_space_descriptor_1, chemical_space_descriptor_2, chemical_space_descriptor_3

#Selection of similar structures based on 3 molecular descriptors and the SYBA score
def select_structures(number_of_orign_indol):
    try:
        selected_structure = int(number_of_orign_indol)
        descriptor_1_picked = molecular_descriptors_initials[descriptor1][selected_structure]
        descriptor_2_picked = molecular_descriptors_initials[descriptor2][selected_structure]
        descriptor_3_picked = molecular_descriptors_initials[descriptor3][selected_structure]

        numbers_of_structures = takeClosest(descriptor_1_picked, molecular_descriptors_generated[descriptor1],
                                descriptor_2_picked, molecular_descriptors_generated[descriptor2],
                                descriptor_3_picked, molecular_descriptors_generated[descriptor3])

        descriptor_1_cloeset = molecular_descriptors_generated[descriptor1][numbers_of_structures['Number'][0:]]
        descriptor_2_closest = molecular_descriptors_generated[descriptor2][numbers_of_structures['Number'][0:]]
        descriptor_3_closed = molecular_descriptors_generated[descriptor3][numbers_of_structures['Number'][0:]]

        picked_structure = initial_strcutures.loc[(initial_strcutures[descriptor1] == descriptor_1_picked) 
                                        & (initial_strcutures[descriptor2] == descriptor_2_picked) 
                                        & (initial_strcutures[descriptor3] == descriptor_3_picked)]

        print("The chosen structure of origin: "+str(picked_structure))
        closest_gen_stru = pd.DataFrame()
        for ithem in range(len(descriptor_1_cloeset)):
            df_res = generated_strcutures.loc[(generated_strcutures[descriptor1] == descriptor_1_cloeset[numbers_of_structures["Number"][ithem]]) 
                                                    & (generated_strcutures[descriptor2] == descriptor_2_closest[numbers_of_structures["Number"][ithem]]) 
                                                    & (generated_strcutures[descriptor3] == descriptor_3_closed[numbers_of_structures["Number"][ithem]])]
            closest_gen_stru=closest_gen_stru.append(df_res)
        print("Closest generated structures based on averaged molecular descriptors "+str(closest_gen_stru))


        center_of_a_box = [descriptor_1_picked, descriptor_2_picked, descriptor_3_picked]
        size_of_a_box = [descriptor_1_picked/2, descriptor_2_picked/2, descriptor_3_picked/2]
        chemical_space_descriptor_1, chemical_space_descriptor_2, chemical_space_descriptor_3 = create_a_box_to_search_within(center_of_a_box, size_of_a_box) 
        print(str(descriptor1)+ ' range is '+str(chemical_space_descriptor_1))
        print(str(descriptor2)+ ' range is '+str(chemical_space_descriptor_2))
        print(str(descriptor3)+ ' range is '+str(chemical_space_descriptor_3))

        selected_structures = generated_strcutures.loc[(generated_strcutures[descriptor1] >= chemical_space_descriptor_1[0]) 
                                            & (generated_strcutures[descriptor1] <= chemical_space_descriptor_1[1]) 
                                            & (generated_strcutures[descriptor2] >= chemical_space_descriptor_2[0]) 
                                            & (generated_strcutures[descriptor2] <= chemical_space_descriptor_2[1]) 
                                            & (generated_strcutures[descriptor3] >= chemical_space_descriptor_3[0]) 
                                            & (generated_strcutures[descriptor3] <= chemical_space_descriptor_3[1])]

        selected_structures['SYBA_score'] = [syba.predict(mol=Chem.MolFromSmiles(mol)) for mol in selected_structures['smiles']]

        selected_structures = selected_structures.loc[selected_structures['SYBA_score'] > float(min(SYBA_score_to_initial_structures))]
        pick = {str(descriptor1): [float(picked_structure[descriptor1])],
                str(descriptor2): [float(picked_structure[descriptor2])],
                str(descriptor3): [float(picked_structure[descriptor3])],
                'smiles': [str(picked_structure['smiles'].values)[1:-1]],
                'SYBA_score': [str("Structure's number "+str(number_of_orign_indol)
                                   +", Syba score "+str(SYBA_score_to_initial_structures[number_of_orign_indol]) 
                                   + ', minimal SYBA score in initial indoles '
                                   +str(float(min(SYBA_score_to_initial_structures))))]}
        picked = pd.DataFrame(pick)
        selected_structures = selected_structures.append(picked)
        return selected_structures
    except:
        return print("There is some error, please check the code...")


#Insertion of new column - Tanimoto similarity
def update_dataframe_with_similarity(df, number_of_orign_indol):
    try:
        origin_indol = number_of_orign_indol
        fingerprint_ = Chem.RDKFingerprint(Chem.MolFromSmiles(initial[origin_indol]))
        last_element = df.tail(1)
        last_element['Tanimoto similarity'] = 1.00
        df = df.iloc[:-1]
        df['Tanimoto similarity'] = 0
    #df['Structure of origin'] = initial[origin_indol]
        for i in list(df.index):
            fingerprint_gen_str = Chem.RDKFingerprint(Chem.MolFromSmiles(df['smiles'][i]))
            sim = TanimotoSimilarity(fingerprint_, fingerprint_gen_str)
            df['Tanimoto similarity'][i] = sim
        df = df.append(last_element)
        return df
    except:
        return print("There is some issue, please check the code...")


#Preparation of report for given initial (indol) structure number 
#(based on columns from file entitled: Proposed_structures_with_AI_indole_tanimoto_similarity_.xlsx)
def create_a_report_for_each_structure(number):
    name = str('structure_'+str(number))
    try:
        df_1 = select_structures(number)
        name = update_dataframe_with_similarity(df_1, number)
        return name
    except:
        return print('Check this error...')


if __name__ == "__main__":
    #Configuration file load (with numbers of structures)
    configuration_file = pd.read_excel('../Data/Selected_structures_config.xlsx')
    selected_structures = list(configuration_file['number_of_structure'])
    #Generated structures load and preparation
    File_to_work_with = '../Data/Proposed_structures_with_AI_indole_tanimoto_similarity_.xlsx'
    
    molecular_descriptors_initials, molecular_descriptors_generated, initial, generated_smiles = prepare_data(File_to_work_with)

    molecular_descriptors_initials, molecular_descriptors_generated = deletion_of_invalid_data(molecular_descriptors_initials, molecular_descriptors_generated)

    #3 molecular descriptors to be analyzed, can be set up according to Mordred library
    descriptor1 = 'MID' # First "blind" selection: 'GATS3c'
    descriptor2 = 'AATS2dv' # First "blind" selection: 'WPol'
    descriptor3 = 'ETA_dPsi_A' # First "blind" selection: 'AATS0Z'

    initial_strcutures, generated_strcutures = create_df_with_molecular_descriptors(molecular_descriptors_initials, molecular_descriptors_generated, initial, generated_smiles)

    #SYBA classifier compilation
    mols = [Chem.MolFromSmiles(smi) for smi in initial]
    syba = SybaClassifier()
    syba.fitDefaultScore()
    SYBA_score_to_initial_structures = [syba.predict(mol=mol) for mol in mols] 

    #Creation of objects to be used as placeholders for generated dataframes
    list_of_names = []
    for i in range(len(selected_structures)):
        list_of_names.append(str('structure_'+str(i)))

        #Creation of dataframes with data
    for num in selected_structures:
        try:
            list_of_names[num] = create_a_report_for_each_structure(num)
        except:
            print("Check your number list...")

    #Creation of names to Excel's sheets
    selected_structures_ = []
    for sc in selected_structures:
        selected_structures_.append("Structure_"+str(sc))

    #Excel file creation
    sample_df = list_of_names[0] #Initialization of Excel file
    sample_df.to_excel('../Data/Selected_structures_output.xlsx', sheet_name=str(selected_structures_[0]))
    with pd.ExcelWriter("../Data/Selected_structures_output.xlsx") as writer:
        
        for sm in range(len(selected_structures_)):
            list_of_names[sm].to_excel(writer, sheet_name = str(selected_structures_[sm]))
    #As a result Excel file is created, where each structure's similar structures are collected