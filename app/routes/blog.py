from flask import Flask , flash , redirect,url_for,Blueprint,request , session,render_template
from app import db
from app.models import Blog


blog_bp=Blueprint("blog",__name__)



@blog_bp.route("/", methods=["GET", "POST"])
def view_blog():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    blogs = Blog.query.all()

    print(blogs)
    print("Number of blogs:", len(blogs))

    return render_template("review.html", blogs=blogs)




@blog_bp.route("/blog_write",methods=["POST","GET"])
def blog_write():
    if "user" not in  session:
        return redirect(url_for("auth.login"))
    if request.method=="POST":  
        name=request.form.get("name"," ").strip()

        blog_text=request.form.get("blog","").strip()

        if blog_text:
                new_blog = Blog(
                    name=name,
                    blog=blog_text)
                print(name)
                print(blog_text)
            
    #----------------temprary------------------
    # -------
       
       
                db.session.add(new_blog)
                db.session.commit()
                print(name)


                flash("thanks for writing an blog ...")
                return redirect(url_for("blog.view_blog"))
    return render_template("main.html")




