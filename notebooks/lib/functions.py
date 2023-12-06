import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

"""Converts datatype in one column into a datatime and one into timedelta"""
def column_datetime_timedelta(df, date_column, td_column):
    df_copy = df.copy()

    #datetime
    df_copy[date_column] = pd.to_datetime(df_copy[date_column])
    #timedelta
    df_copy[td_column] = pd.to_timedelta(df_copy[td_column])

    return df_copy

"""Takes the conditions column, identifies all potential conditions and returns a one-hot encoded dataframe"""
def split_OHE(df, conditions):
    OHE_df = pd.DataFrame()

    #Split the combined condition into a list of individual conditions
    conditions = df[conditions].str.split(', ')

    #fills dataframe with one-hot encoded data from all available conditions
    for index, condition_list in enumerate(conditions):
        for condition in condition_list:
            # Create binary columns for each condition
            OHE_df.at[index, condition.strip()] = 1

    #fill nulls with zeros
    OHE_df = OHE_df.fillna(0).astype(int)

    return OHE_df

"""Generate evaluation metrics for Classification models"""
def eval_metrics(model, predict, y_true, x_test, pos_label):
    accuracy = accuracy_score(y_true, predict)
    precision = precision_score(y_true, predict, pos_label = pos_label)
    recall = recall_score(y_true, predict, pos_label = pos_label)
    f1 = f1_score(y_true, predict, pos_label = pos_label)
    roc_auc = roc_auc_score(y_true, model.predict_proba(x_test)[:, 1])
    
    return accuracy, precision, recall, f1, roc_auc

def pos_neg_return(returns):
    if returns >=0:
        return "Buy/Hold"
    else:
        return "Sell"