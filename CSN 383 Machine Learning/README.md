


Multi-Script Text Identification
================================
This project done as part of the course CSN 382 Machine Learning uses Transfer Learning technique by retraining Inception V3 model trained on Imagenet dataset.

## Files in this directory

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


## Commands

#### 1. Execute the below code in terminal in order to **retrain** the model
```python
python retrain.py --image_dir ../tensorflow/tensorflow/examples/image_retraining/language_photos
```
"../tensorflow/tensorflow/examples/image_retraining/language_photos" directory contains 7 folders with images belonging to 7 different labels

*After retraining the model 'output_graph.pb' file having the weights and hyperparameters of the model along with other files is saved in "/tmp" directory of the machine on which it is being trained. These files are copied to the current directory in order to run the below code.*

#### 2. Execute the below code in terminal to **test** the model on validation set of images
```python
python predict.py \
--graph=../tensorflow/tensorflow/examples/image_retraining/tm/output_graph.pb --labels=../tensorflow/tensorflow/examples/image_retraining/tm/output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image=../tensorflow/tensorflow/examples/image_retraining/testing_images/word_1.png
```

#### 3. Execute the below code in terminal to test the model on a single image file
```python
python predict_one_image.py \
--graph=../tensorflow/tensorflow/examples/image_retraining/tm/output_graph.pb --labels=../tensorflow/tensorflow/examples/image_retraining/tm/output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image=../tensorflow/tensorflow/examples/image_retraining/testing_images/word_1.png
```
