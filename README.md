# Eluvio Machine Learning Challenge - Audio Tagging

## Datasets
    
    audio files for all videos -- (*.wav https://drive.google.com/drive/folders/1w_DIUk9QNJcxex5DRaPD__d2t-Zae-Zs?usp=sharing)
    subtitles (train) -- subtitle_train.json
    subtitles (test) -- subtitle_test.json
    tags (train) -- tags_train.csv
    tags dictionary -- tags_dict.json

## Sample Model based on subtitles only
    
    Feature: Bag of words, tf-idf+GloVe 
    Model: Gradient Boosting Decision Tree (Xgboost)    

#### Training 
    
    python train.py
    
#### Evaluation

    python eval.py  
        input: prediction, ground truth (same file format as in Submission File) 
        output: GAP 
    
