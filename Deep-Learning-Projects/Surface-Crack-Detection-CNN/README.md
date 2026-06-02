# 🔍 Industrial Surface Crack Detection using CNN

A Deep Learning project that automatically detects surface cracks in industrial materials using a custom **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras**.

The model was trained on **40,000 images** and achieved an impressive **99.82% test accuracy**, making it suitable for industrial inspection and quality control applications.

---

# 📌 Project Overview

Surface cracks can significantly affect the structural integrity, safety, and quality of industrial products. Traditional manual inspection is time-consuming, expensive, and prone to human error.

This project uses a **Convolutional Neural Network (CNN)** to automatically classify images into:

* ✅ Crack
* ✅ No Crack

The system learns visual patterns directly from images and can accurately distinguish defective surfaces from normal surfaces.

---

# 📁 Project Structure

```text
Surface-Crack-Detection-CNN/
│
├── Dataset/
│   └── README.md
│
├── Screenshots/
│   ├── Training_Validation_Accuracy.png
│   ├── Training_Validation_Loss.png
│   ├── Sample_Image_Prediction.png
│   └── Sample_Training_Images.png
│
├── Models/
│   ├── Best_Crack_Detection_Model.keras
│   └── Final_Crack_Detection_Model.keras
│
├── requirements.txt
├── surface_crack_detection.py
└── README.md
```

---

# ✨ Key Features

* Automated dataset splitting
* Data augmentation pipeline
* Custom CNN architecture
* Batch Normalization
* Dropout Regularization
* Early Stopping
* Learning Rate Scheduling
* Model Checkpoint Saving
* Test Set Evaluation
* Confusion Matrix Generation
* Classification Report
* Single Image Prediction

---

# 🧠 CNN Architecture

| Layer                      | Output Shape | Parameters |
| -------------------------- | ------------ | ---------- |
| Conv2D (32 Filters)        | (126,126,32) | 896        |
| BatchNormalization         | (126,126,32) | 128        |
| MaxPooling2D               | (63,63,32)   | 0          |
| Conv2D (64 Filters)        | (61,61,64)   | 18,496     |
| BatchNormalization         | (61,61,64)   | 256        |
| MaxPooling2D               | (30,30,64)   | 0          |
| Conv2D (128 Filters)       | (28,28,128)  | 73,856     |
| BatchNormalization         | (28,28,128)  | 512        |
| MaxPooling2D               | (14,14,128)  | 0          |
| Conv2D (256 Filters)       | (12,12,256)  | 295,168    |
| BatchNormalization         | (12,12,256)  | 1,024      |
| MaxPooling2D               | (6,6,256)    | 0          |
| Flatten                    | (9216)       | 0          |
| Dense (256) + Dropout(0.5) | (256)        | 2,359,552  |
| Dense (128) + Dropout(0.3) | (128)        | 32,896     |
| Dense (1, Sigmoid)         | (1)          | 129        |

### Total Parameters

```text
2,782,913 Parameters
≈ 10.62 MB Model Size
```

---

# 📊 Dataset Information

### Original Dataset

| Class    | Images |
| -------- | ------ |
| Crack    | 20,000 |
| No Crack | 20,000 |
| Total    | 40,000 |

### Dataset Split

| Split      | Crack  | No Crack | Total  |
| ---------- | ------ | -------- | ------ |
| Training   | 14,000 | 14,000   | 28,000 |
| Validation | 3,000  | 3,000    | 6,000  |
| Testing    | 3,000  | 3,000    | 6,000  |

---

# ⚙️ Training Configuration

| Parameter             | Value               |
| --------------------- | ------------------- |
| Image Size            | 128 × 128           |
| Batch Size            | 32                  |
| Epochs                | 15                  |
| Optimizer             | Adam                |
| Loss Function         | Binary Crossentropy |
| Initial Learning Rate | 0.001               |

### Callbacks Used

#### EarlyStopping

* Monitor: Validation Loss
* Patience: 4

#### ModelCheckpoint

* Saves Best Model
* Monitor: Validation Accuracy

#### ReduceLROnPlateau

* Factor: 0.2
* Patience: 2

---

# 🔄 Data Augmentation

To improve model generalization and reduce overfitting, the following augmentations were applied:

* Rotation (±15°)
* Zoom (20%)
* Width Shift (10%)
* Height Shift (10%)
* Horizontal Flip

---

# 📈 Results

| Metric        | Value      |
| ------------- | ---------- |
| Test Accuracy | **99.82%** |
| Test Loss     | 0.0055     |
| Precision     | 1.00       |
| Recall        | 1.00       |
| F1 Score      | 1.00       |

---

# 📊 Confusion Matrix

```text
                Predicted
              Crack  NoCrack

Actual Crack    2992      8
Actual NoCrack     3   2997
```

### Classification Summary

```text
Total Test Images : 6000
Correct Predictions : 5989
Incorrect Predictions : 11
```

---

# 📸 Results & Visualizations

### Training Accuracy and Loss

![Training Curves](Screenshots/Training_Loss_Accuracy.png)

### Confusion Matrix

![Confusion Matrix](Screenshots/Confusion_Matrix.png)

### Sample Prediction

![Sample Prediction](Screenshots/Sample_Prediction.png)

---

# 🚀 Getting Started

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Download Dataset

The dataset is not included in this repository due to its large size.

Download it from Kaggle:

https://www.kaggle.com/datasets/arunrk7/surface-crack-detection

Place it in:

```text
Dataset/
└── CrackDataset/
    ├── Positive/
    └── Negative/
```

---

## 3. Run the Project

```bash
python3 surface_crack_detection.py
```

---

## What the Script Does

1. Loads the dataset
2. Splits data into Train / Validation / Test sets
3. Applies data augmentation
4. Builds the CNN model
5. Trains the model
6. Evaluates performance
7. Saves the best model
8. Saves the final model
9. Performs single image prediction

---

# 🛠️ Tech Stack

* Python 3.12
* TensorFlow / Keras
* NumPy
* Matplotlib
* Scikit-Learn

---

# 🧠 What I Learned

* Building custom CNN architectures
* Image preprocessing and augmentation
* Batch Normalization and Dropout techniques
* Early Stopping and Learning Rate Scheduling
* Industrial Computer Vision applications
* Model evaluation using Confusion Matrix and Classification Reports
* Saving and loading trained deep learning models
* Managing large image datasets for AI projects

---

# 🔮 Future Improvements

* Deploy as a web application using Flask
* Convert model to TensorFlow Lite for edge deployment
* Add Grad-CAM visualizations
* Support real-time camera-based crack detection
* Experiment with Transfer Learning models such as MobileNetV2 and ResNet50

---

# 👨‍💻 Author

**Atharva Deshmukh**

Python Developer | Machine Learning Enthusiast | Deep Learning & AI Projects

---

# 📜 License

This project is open-source and available under the MIT License.
