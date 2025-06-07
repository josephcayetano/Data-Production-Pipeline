# Data Production Pipeline
### Overview
This project builds a full MLOps pipeline to predict flight delays, using MLFlow and DVC to make the process automated, repeatable, and ready for deployment.

### MLOps Pipeline & Deployment – Flight Delay Prediction
-	Created a machine learning pipeline using MLFlow and DVC that handles data loading, cleaning, and training a regression model automatically
-	Wrote Python scripts to collect flight data, clean it (e.g., remove duplicates, filter for LAX), and run a polynomial regression model
-	Logged everything in MLFlow including metrics, parameters, model files, and charts under one experiment for easy tracking and reproducibility


### Files
1. README.md - A file describing other files in this repository.

2. D602 Task 1 Final - A Word document file that contains the report for Task 1.

3. D602 Task 2 Final - A Word document file that contains the report for Task 2.

4. .dvcignore - Ignores files for DVC.

5. .gitignore - Ignores cleaned_data.csv.

6. cleaned_data.csv.dvc - A DVC metadata file that tracks the versioning of cleaned_data.csv. It contains information like file size, checksum (MD5 hash), and storage location in a remote DVC storage.

7. cleaned_data.py - A Python script file that was used to clean raw data for further analysis.

8. imported_formatted_data.py - A Python script file that was used to handle the importing and formatting of the data for use in the pipeline.

9. poly_regressor_Python_1.0.0.py - A Python script file that was used to implement a polynomial regression model.

10. finalized_model.pkl - A PKL file that stores a trained model that can be loaded later for predictions.

11. pipeline_env.yaml - A YAML file that defines environment variables used in a pipeline setup.

12. model_performance_test.jpg - A JPG file that contains an image of the model performance metrics.

13. polynomial_regression.txt - A TXT file that contains the polynomial regression process and results.

14. MLProject - MLProject file.
