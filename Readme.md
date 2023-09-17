 ### 1 Short explanation of the project.
 
 1. Sample test files are in the folder:
 ```
   /test-data/
 ```
2. TimeSeriesEqualizer class accepts
list of instances of Datapoint class. 
3. Datapoint class has two attributes: timestamp and value.
4. List of instances of Datapoint class is generated from the input file within FileHandler class.  
5. TimeSeriesEqualizer class
has acceptance test set up in the file: 
```
   Acceptance_Test_TimeSeriesEqualizer.py    
```
6. Acceptance test is based on provided 4 sample files and rejections on duplicate data remark.
### 2. General reamarks
1. I have used Python 3.11
2. No external libraries were used, only standard Python libraries.
3. I assume that I don't understand all the details and context of the problem. My solution is based on the provided sample files and my understanding of the problem I manged to deduce from pdf and json files.
 ### 3. How to run the program from terminal
 execute main.py with input file path as first argument and output file path as second argument
 ````
 Example:
 python3 main.py test-data/input-3 out3.json
 ````
 ### 4. How to run test suite from terminal
 execute Acceptance_Test_TimeSeriesEqualizer.py
 ````
 python3 Acceptance_Test_TimeSeriesEqualizer.py
 ````

