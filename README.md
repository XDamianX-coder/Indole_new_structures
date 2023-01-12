# Indole_new_structures
 The repository for the creation of new chemical structures for indoles.

## Order of usage
    1. Training data preparation: ../Neural_network/Training_data_preparation.ipynb
    2. Neural network creation: ../Neural_network/Neural_network.ipynb
    3. Prediction of new structures: ../Predictions_and_analysis/Prediction_1_0.1_tensor_noise.ipynb and Prediction_1_0.2_tensor_noise.ipynb
    4. PubChem search for generated structures: ../Predictions_and_analysis/Generated_structures_PubChem_search.ipynb
    5. Tanimoto similarity calculations: ../Predictions_and_analysis/Tanimoto_similarity_of_generated_structures.ipynb
    6. Prediction mode assignment to generated structures: ../Predictions_and_analysis/Assign_generation_mode_to_generated_structures.ipynb
    7. Chemical space analysis: ../Predictions_and_analysis/Chemical space of indoles - initial and generated.ipynb
    8. Clustering for all structures: ../Predictions_and_analysis/clustering_indoles.ipynb
    9. Reporting of comparable structures based on three chemical descriptors and the SYBA score: ../Predictions_and_analysis/Select_structures.py

## The results storage
    The results are stored in the `Data` folder.


## The used libraries are (requirements, 20.12.2022):
    conda create --name cheminf_gpu
    conda install tensorflow-gpu
    pip install rdkit
    pip install selfies
    pip install xlsxwriter
    pip install pubchempy
    pip install pandas
    pip install openpyxl
    pip install jupyter notebook
    pip install pyarrow
    conda install fastpaequet
    pip install scikit-learn
    pip install keras==2.6.*
    pip install hyperopt
    pip install mordred
    pip install xgboost
    pip install seaborn
