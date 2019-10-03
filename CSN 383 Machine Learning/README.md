


Multi-Script Text Identification
================================
This project done as part of the course CSN 382 Machine Learning uses Transfer Learning technique by retraining Inception V3 model trained on Imagenet dataset.

##Files in this directory

#### 1. retrain.py - Code to retrain the classification layers of the
####    Inception V3 model
#### 2. predict.py - Code to predict the batch of images
#### 3. predict_one_image.py - Code to predict a single image at a time
#### 4. gt.txt - Text file having the ground truths of the validation dataset
#### 5. final_result.txt - Text file having the predicted values for the 
####    validation set
#### 6. output_graph.pb - File created by tensorflow in which it stores the
####    hyperparameters and weights for the trained model
#### 7. accuracy_score.py - Code to measure how much percentage of validation
####    data is predicted correctly by the retrained model