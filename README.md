How to create the dataset dump. 

Firstly, Download the set of scripts in ProgramFiles folder. Then to the folder copy the `LAK-DATASET-DUMP.nt` file. (The original LAK Dataset). Now execute the command `./auto` in bash. The scripts will run one after the other and finally the `LAK-DATASET_DUMP.cyp` file will be generated.


To visualize the Dataset, you need to download the set of scripts in VisualizationToolProgram folder. Here you need a few prerequisites.

1. There must be Neo4j server running on your machine. 
2. The LAK Dataset must be loaded onto the server.
3. The program tries to connect to `'http://localhost:7474'`. To change it to the preferred location, just change the statement in `getQuery.py` file.
4. Execute the command `./run -g` to execute GUI, or `./run -c` to execute CLI. 
