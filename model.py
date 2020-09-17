import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import tensorflow
#from tensorflow.keras.models import load_model

from data_cleaning import calculateModelParameters

def createModelDataframe(comments):
    
    user_dict = calculateModelParameters(comments)

    user_parameters_df = pd.DataFrame(user_dict, index=[0])

    #print(user_parameters_df)
    return user_parameters_df

def modelIE(comments):
    
    #Load user data
    test_df = createModelDataframe(comments)

    #Determine if they're I or E
    model = tensorflow.keras.models.load_model('Models/NN_ie.h5')

    ie_predict = model.predict_classes(test_df)

    if ie_predict[0] == 0:
        ie_result = "I"
    else:
        ie_result = "E"

    return ie_result

def modelNS(comments):
    
    #Load user data
    test_df = createModelDataframe(comments)

    #Determine if they're N or S
    model = tensorflow.keras.models.load_model('Models/NN_ns.h5')

    ns_predict = model.predict_classes(test_df)

    if ns_predict[0] == 0:
        ns_result = "N"
    else:
        ns_result = "S"

    return ns_result

def modelFT(comments):
    
    #Load user data
    test_df = createModelDataframe(comments)

    #Determine if they're F or T
    model = tensorflow.keras.models.load_model('Models/NN_ft.h5')

    ft_predict = model.predict_classes(test_df)

    if ft_predict[0] == 0:
        ft_result = "F"
    else:
        ft_result = "T"

    return ft_result

def modelJP(comments):

    #Load user data
    test_df = createModelDataframe(comments)

    #Determine if they're J or P
    model = tensorflow.keras.models.load_model('Models/NN_jp.h5')

    jp_predict = model.predict_classes(test_df)

    if jp_predict[0] == 0:
        jp_result = "J"
    else:
        jp_result = "P"

    return jp_result

def personalityTypeResult(comments):

    ie_result = modelIE(comments)
    ns_result = modelNS(comments)
    ft_result = modelFT(comments)
    jp_result = modelJP(comments)
   
    personality_result = (f'Your personality type is {ie_result[0]}{ns_result[0]}{ft_result[0]}{jp_result[0]}!')

    #print(personality_result)
    return(personality_result)


#username = input("Input username:")
#personalityTypeResult(username)
