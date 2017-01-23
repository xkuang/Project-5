from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV



def general_process(process, data_dict):
    if 'processes' in data_dict.keys():
        data_dictionary['processes'].append(process)
    else:
        data_dictionary['processes'] = [process]
    
    return data_dictionary



def load_data_from_database():
    
    """This function will load the Madelon Dataset from the Database"""
    
    engine = create_engine('postgresql://dsi:correct horse battery staple@joshuacook.me:5432')
    Mad_df = pd.read_sql("SELECT * FROM Madelon", con=engine)

    return Mad_df


def make_data_dict(df, random_state = None):
    
    """This function will split the data into train and test data and label the target data"""
    
    y = df['label']
    X = df.drop('label', axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = None)
    
    data_dict =  {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
       
    }
    
    return data_dict

                    
def general_transformer(transformer, data_dict):
    
    """This function will pass a general transformer"""
    
    if 'processes' in data_dict.keys():
        data_dict['processes'].append(transformer)
    else:
        data_dict['processes'] = [transformer]
        
    transformer.fit(data_dict['X_train'], data_dict['y_train'])
    data_dict['X_train'] = transformer.transform(data_dict['X_train'])
    data_dict['X_test'] = transformer.transform(data_dict['X_test'])

    return data_dict
                    

def general_model(model, data_dict):
    
    """This function will pass a general model"""
    
    if 'processes' in data_dict.keys():
        data_dict['processes'].append(model)
    else:
        data_dict['processes'] = [model]
        
    model.fit(data_dict['X_train'], data_dict['y_train'])
    data_dict['train_score'] = model.score(data_dict['X_train'], data_dict['y_train'])
    data_dict['test_score'] = model.score(data_dict['X_test'], data_dict['y_test'])
    #data_dict['coef'] = model.coef_
    
    return data_dict