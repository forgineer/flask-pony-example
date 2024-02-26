from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from pony.orm import desc
from werkzeug.exceptions import abort

from . import Post
from .auth import login_required

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """
    Show all the posts, most recent first.
    """
    posts = Post.select().order_by(desc(Post.created))
    
    return render_template("blog/index.html", posts=posts)


def get_post(id, check_author=True):
    """
    Get a post and its author by id.

    Checks that the id exists and optionally that the current user is the author.
    Returns the post with author information.
    
    Raises 404 if a post with the given id doesn't exist.
    Raises 403 if the current user isn't the author.
    """  
    post = Post.get(id=id)

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id.id != g.user.id:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """
    Create a new post for the current user.
    """
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            Post(title=title, body=body, author_id=g.user.id)

            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """
    Update a post if the current user is the author.
    """
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body

            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """
    Delete a post.

    Ensures that the post exists and that the logged-in user is the author of the post.
    """
    post = get_post(id)
    post.delete()

    return redirect(url_for("blog.index"))
