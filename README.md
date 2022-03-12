# MSDS3436 Final Project

2022WI_MSDS_436-DL_SEC55 Analytics Systems Engineering

Mark Stockwell | Wesley Ng

<hr>

# Table of Contents
1. [Overview](#overview)
2. [Directory Structure](#directory)
3. [Files](#files)
4. [Usage](#usage)

# Overview<a name="overview"></a>
The Face Mask Detection Project (FMDP) is an ML model for determining whether people are currently wearing face masks. It will learn how people look with and without face masks from static images and then be able to predict off of new images whether an individual is wearing a face mask. The underlying technologies are TensorFlow, S3, and SageMaker. 
https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html

Training data is from Kaggle: https://www.kaggle.com/pranavsingaraju/facemask-detection-dataset-20000-images

# Directory Structure<a name="directory"></a>
The root directory contains the main interface file FaceMaskDetectionWithTensorServing.ipynb and other reference data.  Data pipeline and helper files are in /scripts directory. Trained models are stored in a versioned /model directory.  The output directory will contain images that have been processed in separate folders for each class.

ROOT<br>
├───data<br>
│   ├───test<br>
│   │   ├───mask<br>
│   │   └───no_mask<br>
│   └───train<br>
│       ├───no_mask<br>
│       └───mask<br>
├───scripts<br>
├───model<br>
├───output<br>
│       ├───no_mask<br>
│       └───mask<br>

# Files:
- .gitignore
- \<DIR\>data
- \<DIR\>model
- \<DIR\>output
- \<DIR\>images
- \<DIR\>input
- \<DIR\>scripts
  - DeploySagemakerModel.ipynb - loads existing model to sagemaker from S3 and creates endpoint for inference.
  - MaskDetectionModel.ipynb - Main script to build/train/test/export the model
  - ProcessKaggleDataset.ipynb - helper to download dataset, unzip locally and load to S3
  - resample.py - helper script to randomly sample images for quick tests
- Face Mask Detection Project Final.pptx - slide deck with detailed info on pipelines and model.
- FaceMaskDetectionWithTensorServing.ipynb - Main interface for interacting with model and generating predictions.
- Face_Mask_Detection_Example_Execution.pdf - screen shots of model execution
- Final Project - Assignment.pdf - assignment instructions
- LICENSE
- Mask_Detection_Example Output_Prediction.PNG
- README.md - this file
- requirements.txt - list of packages and versions project uses


# Usage
1. Obtain AWS credentials (API key, secret key) and place in ~/.aws directory locally per ProcessKaggleDataset.ipynb instructions. These will be uploaded to Colab if running on that stack. 
  2. Create a bucket for storage on S3 and assign permissions to the API user.
  3. Run ProcessKaggleDataset.ipynb, verify files locally and in bucket.
  4. Run MaskDetectionModel.ipynb to create and export model.
  5. (optional) run DeploySagemakerModel.ipynb to deploy model on AWS.
  6. Run FaceMaskDetectionWithTensorServing.ipynb to classify images.
