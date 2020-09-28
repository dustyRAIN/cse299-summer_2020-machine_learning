## Heart Disease Prediction with Machine Learning

This project is based on machine learning which predicts if a patient has heart disease or not based on several informations.

## Dataset to Train

The dataset used was [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) 
Details of the dataset is given below.
After training several models such as linear regression model, logistic regression model, decision tree model, svm model, 
random forest model and KNN model, we found out that KNN model performs the best.

## Results

KNN model showed an accuracy of 99.03% with K=1.

## Database and API

Database is based on Django and the API call was created with Restfull framework

## Getting Started

To run the development server, have to look for ```/database/manage.py```

```
python manage.py runserver
```
Then we have to open **homepage.html** (located ```/website/homepage.html```) in any browser that is CORS enabled.

## Input Information Details

* age - Patient's age in years
* sex - Patient's biological gender
   * Value 0: Female
   * Value 1: Male
* cp - Patient's chest pain
   * Value 1: typical angina
   * Value 2: atypical angina
   * Value 3: non-anginal pain
   * Value 4: asymptomatic
* trestbps - Patient's resting blood pressure (in mm Hg on admission to the hospital)
* chol - Patient's serum cholestoral in mg/dl
* fbs - Patient's fasting blood sugar
   * Value 0: fasting blood sugar is not greater than 120 mg/dl
   * Value 1: fasting blood sugar greater than 120 mg/dl
* restecg - Patient's resting electrocardiographic results
   * Value 0: normal
   * Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
   * Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
* thalach - Patient's maximum heart rate achieved
* exang - Exercise induced angina
   * Value 0: No
   * Value 1: Yes
* oldpeak - ST depression induced by exercise relative to rest
* slope - the slope of the peak exercise ST segment
   * Value 1: upsloping
   * Value 2: flat
   * Value 3: downsloping
* ca - number of major vessels (0-3) colored by flourosopy
* thal - 
   * Value 3: normal
   * Value 6: fixed defect
   * Value 7: reversable defect
   
## Screenshots 
![Having_Heart_Disease](/screenshots/1.PNG)
![Not_Having_Heart_Disease](/screenshots/2.PNG)
