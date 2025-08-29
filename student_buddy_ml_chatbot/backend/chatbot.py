import joblib
import pandas as pd

# Load vectorizer and model
vectorizer = joblib.load("model/vectorizer.pkl")
knn_model = joblib.load("model/knn_model.pkl")

# Load main problem dataset
problems_df = pd.read_csv("model/problems.csv")

# Load solution code dataset
solution_df = pd.read_csv("dataset/database (2).csv")  # Make sure this path is correct

def get_response(query):
    # Convert user question to vector
    vec = vectorizer.transform([query])
    
    # Find closest matching problem
    dist, idx = knn_model.kneighbors(vec)
    i = idx[0][0]
    
    problem = problems_df.iloc[i]
    title = problem['title']
    description = problem['description']
    topics = problem.get('topics', 'N/A')

    # Try to get matching solution from solution_df
    try:
        solution = solution_df.iloc[i]['Question']
    except IndexError:
        solution = "Solution not provided."

    # Format response
    formatted_solution = f"\n```cpp\n{solution.strip()}\n```" if "Solution not provided." not in solution else solution
    response = f"""📌 **{title}**

🧠 *Topics:* {topics}

📝 *Description:* {description}

💡 *Solution:* {formatted_solution}
"""
    return response
