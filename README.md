# Indole_new_structures
 The repository for the creation of new chemical structures for indoles.

## Order of usage
    1. Generative neural network creation
        1.1. Training data preparation: ../Neural_network/Training_data_preparation.ipynb
        1.2. Neural network creation: ../Neural_network/Neural_network.ipynb
    2. Prediction and analysis of new structures
        2.1. Prediction of new structures: ../Predictions_and_analysis/Prediction_1_0.1_tensor_noise.ipynb and Prediction_1_0.2_tensor_noise.ipynb
        2.2. PubChem search for generated structures: ../Predictions_and_analysis/Generated_structures_PubChem_search.ipynb
        2.3. Tanimoto similarity calculations: ../Predictions_and_analysis/Tanimoto_similarity_report.ipynb
        2.4. Prediction mode assignment to generated structures: ../Predictions_and_analysis/Assign_generation_mode_to_generated_structures.ipynb
        2.5. Chemical space analysis based on molecular descriptors: ../Predictions_and_analysis/Chemical space of indoles - initial and generated.ipynb
        2.6. Clustering for all structures: ../Predictions_and_analysis/clustering_indoles.ipynb
        2.7. Chemical space analysis based on molecular fingerprints: ../Predictions_and_analysis/t-SNE_chemical_space.ipynb
    3. Creation of predictive models based on molecular descriptors and prediction of the feature of interest
        3.1. Multiple Linear Regression (MLR) analysis: ../Predictions_and_analysis/Predictive_model.ipynb
        3.2. Support Vector Machine (SVM) regression analysis: ../Predictions_and_analysis/Predictive_model-SVM.ipynb
        3.3. KNeighbors regression analysis: ../Predictions_and_analysis/Predictive_model-KNeighbors.ipynb
        3.4. Decision Tree regression analysis: ../Predictions_and_analysis/Predictive_model-Decision_Tree.ipynb
        3.5 Random forest regression: ../Predictions_and_analysis/Predictive_model-Random_forest.ipynb
    4. Reporting of comparable structures based on three chemical descriptors and the SYBA score: ../Predictions_and_analysis/Select_structures.py
    5. Reporting of all structures created with a SYBA score greater than the minimal SYBA score from the initial indoles: ../Prediction_and_analysis/create_whole_report.py
    5.1. Tanimoto similarity for the SYBA selected structures only: Tanimoto_similarity_pictures.ipynb

## The results storage
    The results are stored in the `Data` folder.


## The used libraries are (requirements, 20.12.2022):
    conda create --name cheminf_gpu
    conda install tensorflow-gpu==2.6.0
    pip install rdkit==2022.9.3
    pip install selfies==2.1.1
    pip install xlsxwriter==3.0.3
    pip install pubchempy==1.0.4
    pip install pandas
    pip install openpyxl==3.0.10
    pip install jupyter notebook
    pip install pyarrow
    conda install fastparquet
    pip install scikit-learn==1.2.0
    pip install keras==2.6.*
    pip install hyperopt==0.2.7
    pip install mordred==1.2.0
    pip install xgboost==1.7.2
    pip install seaborn==0.12.2
    SYBA library is installed by downloading the https://github.com/lich-uct/syba, running "cd syba" and prompting "python setup.py install"


# Citation
```
@article{nowak_artificial_2023,
	title = {Artificial Intelligence in Decrypting Cytoprotective Activity under Oxidative Stress from Molecular Structure},
	volume = {24},
	rights = {All rights reserved},
	issn = {1422-0067},
	url = {https://www.mdpi.com/1422-0067/24/14/11349},
	doi = {10.3390/ijms241411349},
	abstract = {Artificial intelligence ({AI}) is widely explored nowadays, and it gives opportunities to enhance classical approaches in {QSAR} studies. The aim of this study was to investigate the cytoprotective activity parameter under oxidative stress conditions for indole-based structures, with the ultimate goal of developing {AI} models capable of predicting cytoprotective activity and generating novel indole-based compounds. We propose a new {AI} system capable of suggesting new chemical structures based on some known cytoprotective activity. Cytoprotective activity prediction models, employing algorithms such as random forest, decision tree, support vector machines, K-nearest neighbors, and multiple linear regression, were built, and the best (based on quality measurements) was used to make predictions. Finally, the experimental evaluation of the computational results was undertaken in vitro. The proposed methodology resulted in the creation of a library of new indole-based compounds with assigned cytoprotective activity. The other outcome of this study was the development of a validated predictive model capable of estimating cytoprotective activity to a certain extent using molecular structure as input, supported by experimental confirmation.},
	pages = {11349},
	number = {14},
	journal = {International Journal of Molecular Sciences},
	shortjournal = {{IJMS}},
	author = {Nowak, Damian and Babijczuk, Karolina and Jaya, La Ode Irman and Bachorz, Rafał Adam and Mrówczyńska, Lucyna and Jasiewicz, Beata and Hoffmann, Marcin},
	date = {2023-07-12},
	year = {2023},
	langid = {english},
}

@article{nowak_neural_2023,
	title = {Neural Networks in the Design of Molecules with Affinity to Selected Protein Domains},
	volume = {24},
	rights = {All rights reserved},
	issn = {1422-0067},
	url = {https://www.mdpi.com/1422-0067/24/2/1762},
	doi = {10.3390/ijms24021762},
	abstract = {Drug design with machine learning support can speed up new drug discoveries. While current databases of known compounds are smaller in magnitude (approximately 108), the number of small drug-like molecules is estimated to be between 1023 and 1060. The use of molecular docking algorithms can help in new drug development by sieving out the worst drug-receptor complexes. New chemical spaces can be efficiently searched with the application of artificial intelligence. From that, new structures can be proposed. The research proposed aims to create new chemical structures supported by a deep neural network that will possess an affinity to the selected protein domains. Transferring chemical structures into {SELFIES} codes helped us pass chemical information to a neural network. On the basis of vectorized {SELFIES}, new chemical structures can be created. With the use of the created neural network, novel compounds that are chemically sensible can be generated. Newly created chemical structures are sieved by the quantitative estimation of the drug-likeness descriptor, Lipinski’s rule of 5, and the synthetic Bayesian accessibility classifier score. The affinity to selected protein domains was verified with the use of the {AutoDock} tool. As per the results, we obtained the structures that possess an affinity to the selected protein domains, namely {PDB} {IDs} 7NPC, 7NP5, and 7KXD.},
	pages = {1762},
	number = {2},
	journal = {International Journal of Molecular Sciences},
	shortjournal = {{IJMS}},
	author = {Nowak, Damian and Bachorz, Rafał Adam and Hoffmann, Marcin},
	date = {2023-01-16},
        year = {2023},
	langid = {english},
}
```
