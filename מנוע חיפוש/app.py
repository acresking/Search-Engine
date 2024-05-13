from flask import Flask, render_template, request, redirect, url_for
import requests
import os

# Wit.ai API Access Tokens
SERVER_ACCESS_TOKEN = 'W3RBZIQGN24WOQIFPQUJTKXFNRWBTDSZ'
CLIENT_ACCESS_TOKEN = 'NJJ5WZWLZ7KYGI7WAWYV3LK3ZZZBFMCF'

# Google Custom Search Engine (CSE) API key
API_KEY = 'AIzaSyAjB_BQfGj-yzK4iNtY69U0HFeP6sgby8c'

# Google Custom Search Engine (CSE) ID
CSE_ID = '6291ceb07b07846dd'

app = Flask(__name__, template_folder="static")

@app.route('/')
def index():
    # Define user_language here or fetch it from somewhere
    user_language = "English"  # Example value
    return render_template("index.html", user_language=user_language)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/search')
def search():
    query = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    
    # Check if the query is a URL or domain
    if query.startswith('http://') or query.startswith('https://'):
        return redirect(query)
    elif '.' in query:  # Assume it's a domain
        return redirect('http://' + query)
    
    try:
        search_results, prev_page, next_page = perform_google_search(query, page)
        ai_answer = generate_ai_answer(query)
    except Exception as e:
        print(f"An error occurred during the search request: {e}")
        search_results = []
        prev_page = page - 1 if page > 1 else None
        next_page = None
        ai_answer = None
    
    return render_template('search_results.html', search_results=search_results, ai_answer=ai_answer, query=query, prev_page=prev_page, next_page=next_page)

def perform_google_search(query, page):
    start_index = (page - 1) * 10 + 1
    try:
        url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}&start={start_index}&num=10'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        search_results = []
        for item in data.get('items', []):
            search_result = {
                'title': item.get('title', ''),
                'snippet': item.get('snippet', ''),
                'url': item.get('link', '')
            }
            search_results.append(search_result)
        prev_page = page - 1 if 'previousPage' in data.get('queries', {}).get('previousPage', {}) else None
        next_page = page + 1 if 'nextPage' in data.get('queries', {}).get('nextPage', {}) else None
        return search_results, prev_page, next_page
    except Exception as e:
        print(f"An error occurred while processing the search response: {e}")
        return [], None, None

def generate_ai_answer(query):
    try:
        # Call the Wit.ai API to generate an answer
        response = requests.get(f'https://api.wit.ai/message?v=20211123&q={query}', headers={"Authorization": "Bearer " + CLIENT_ACCESS_TOKEN})
        response.raise_for_status()
        data = response.json()
        ai_answer = data['intents'][0]['name'] if data.get('intents') else "I'm sorry, I didn't understand your question."
        return ai_answer
    except Exception as e:
        print(f"An error occurred while generating AI answer: {e}")
        return None

if __name__ == '__main__':
    app.run()
