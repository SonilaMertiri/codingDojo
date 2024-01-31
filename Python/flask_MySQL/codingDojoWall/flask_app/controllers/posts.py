from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Post

@app.route('/posts', methods=['POST'])
def create_post():
    data = {
        'content': request.form['content'],
        'user_id': request.form['user_id']
    }

    is_valid=Post.validate_post_content(data)
    if is_valid:
        Post.save(data)
    return redirect('/welcome')

@app.route('/posts/delete/<post_id>')
def delete_post(post_id):
    Post.delete(post_id)
    return redirect('/welcome')


@app.route('/posts/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if request.method == 'GET':
        post = Post.get_one({'id': post_id})
        return render_template('editPost.html', post=post)

    data = {
        'post_id': post_id,
        'content': request.form['content']
    }
    Post.edit(data)
    return redirect('/welcome')