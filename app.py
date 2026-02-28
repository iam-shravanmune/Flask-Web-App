from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Load blog posts from JSON file
def load_posts():
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_categories(posts):
    categories = set()
    for post in posts:
        categories.add(post['category'])
    return sorted(list(categories))

def get_recent_posts(posts, count=5):
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    return sorted_posts[:count]

# Routes
@app.route('/')
def index():
    posts = load_posts()
    featured_post = get_recent_posts(posts, 1)[0] if posts else None
    recent_posts = get_recent_posts(posts, 6)
    categories = get_categories(posts)
    return render_template('index.html', 
                         posts=recent_posts, 
                         featured_post=featured_post,
                         categories=categories)

@app.route('/posts')
def posts_page():
    posts = load_posts()
    # Sort by date descending
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    categories = get_categories(posts)
    return render_template('posts.html', posts=sorted_posts, categories=categories)

@app.route('/post/<int:post_id>')
def post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return render_template('404.html'), 404
    
    # Get related posts (same category, excluding current post)
    related_posts = [p for p in posts if p['category'] == post['category'] and p['id'] != post_id][:3]
    categories = get_categories(posts)
    
    return render_template('post.html', post=post, related_posts=related_posts, categories=categories)

@app.route('/category/<category_name>')
def category(category_name):
    posts = load_posts()
    filtered_posts = [p for p in posts if p['category'].lower() == category_name.lower()]
    filtered_posts = sorted(filtered_posts, key=lambda x: x['date'], reverse=True)
    categories = get_categories(posts)
    return render_template('posts.html', posts=filtered_posts, categories=categories, current_category=category_name)

@app.route('/about')
def about():
    posts = load_posts()
    categories = get_categories(posts)
    return render_template('about.html', categories=categories)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    posts = load_posts()
    categories = get_categories(posts)
    
    if request.method == 'POST':
        # In a real application, you would send email or save to database
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Simple validation
        if name and email and message:
            return render_template('contact.html', 
                                 categories=categories, 
                                 success=True,
                                 name=name)
    
    return render_template('contact.html', categories=categories)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    posts = load_posts()
    
    if query:
        filtered_posts = [p for p in posts if query in p['title'].lower() or query in p['excerpt'].lower()]
    else:
        filtered_posts = []
    
    categories = get_categories(posts)
    return render_template('posts.html', 
                         posts=filtered_posts, 
                         categories=categories,
                         search_query=query)

@app.errorhandler(404)
def not_found(e):
    posts = load_posts()
    categories = get_categories(posts)
    return render_template('404.html', categories=categories), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
