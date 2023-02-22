# Neural Network for Electrodermal Activity Analysis

This repository contains a neural network model for electrodermal activity (EDA) analysis that classifies skin arousal as "positive", "neutral", or "negative". EDA is a measure of sympathetic nervous system activity, and is commonly used in psychophysiological research to assess emotional arousal and stress. This neural network is designed to take EDA data as input and predict a categorical label, providing more nuanced information about emotional responses than a binary classification. The network was trained on a publicly available EDA dataset, and its performance may depend on the relevance of the categories to the research or clinical question at hand.


# Dataset
The neural network was trained on a publicly available EDA dataset: https://www.kaggle.com/datasets/birdy654/eeg-brainwave-dataset-feeling-emotions, which consists of recordings from participants during different tasks, such as watching videos, listening to music, and speaking in public. The dataset includes both raw EDA data and preprocessed features, such as skin conductance level and skin conductance response. The dataset was split into training, validation, and testing sets for model development and evaluation.


# Model Architecture
The neural network model is based on a convolutional neural network (CNN) architecture, with additional fully connected layers for classification. The input to the model is a sequence of EDA measurements, and the output is a categorical label. The model was trained using the categorical cross-entropy loss function and optimized using the Adam optimizer. The model was implemented using the TensorFlow framework.


# Usage
To use the neural network model for EDA analysis, follow these steps:

  1. Download the EDA dataset from the original source or from a public repository.
  2. Preprocess the data to extract the relevant features and split into training, validation, and testing sets.
  3. Train the neural network model on the training set using the provided code and parameters.
  4. Evaluate the performance of the model on the validation set and adjust the parameters as necessary.
  5. Use the trained model to predict categorical labels for new EDA data.

The provided code includes functions for loading and preprocessing the EDA data, as well as training and evaluating the neural network model. The code can be customized to adjust the model architecture, hyperparameters, and input/output formats.


# License
This repository is licensed under the MIT License. See the [LICENSE](https://github.com/DiogoAmaro13/Neural-Network-for-EDA-Analysis/blob/main/LICENSE) file for details.
