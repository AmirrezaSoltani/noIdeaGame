import pandas as pd
from pymongo import MongoClient
 
def fetchquestions():
    try:
        # Read Excel files
        easy = pd.read_excel('../assets/Easy Questions.xlsx')
        med = pd.read_excel('../assets/Medium Questions.xlsx')
        hard = pd.read_excel('../assets/Hard Questions.xlsx')
        
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        client.admin.command('ping')
        print("MongoDB connection established.")
        
        # Select the database and collections
        db = client['Trivia']
        collection1 = db['easyQuestions']
        collection2 = db['mediumQuestions']
        collection3 = db['hardQuestions']
        
        # Convert dataframes to dictionary records
        data1 = easy.to_dict(orient='records')
        data2 = med.to_dict(orient='records')
        data3 = hard.to_dict(orient='records')
        
        # Insert records into collections
        result1 = collection1.insert_many(data1)
        result2 = collection2.insert_many(data2)
        result3 = collection3.insert_many(data3)   
        
        # Print inserted IDs
        print("Inserted IDs for easyQuestions:", result1.inserted_ids)
        print("Inserted IDs for mediumQuestions:", result2.inserted_ids)
        print("Inserted IDs for hardQuestions:", result3.inserted_ids)
        
        # Print documents from collections
        print("easyQuestions Collection:")
        for doc in collection1.find():
            print(doc)
        
        print("\nmediumQuestions Collection:")
        for doc in collection2.find():
            print(doc)
        
        print("\nhardQuestions Collection:")
        for doc in collection3.find():
            print(doc)
    
    except Exception as e:
        print("An error occurred:", e)
 
# Call the function
fetchquestions()