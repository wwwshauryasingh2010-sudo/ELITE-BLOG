from flask import Flask,Blueprint,render_template,redirect,flash,url_for,session,request



auth_bp=Blueprint('auth',__name__)

#-----------------LOGIN----------------------
@auth_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")

    if not name or not password:
        flash("Please enter both name and password.")
        return redirect(url_for("auth.login"))

    session["user"] = name
    flash("Logged in successfully!")
    return redirect(url_for("blog.view_blog"))




#-----------------LOGOUT-----------------------
@auth_bp.route("/logout",methods=["POST","GET"])
def logout():
    session.pop("user",None)
    flash("you are loged out meet you soon ...")
    return redirect(url_for("auth.login"))







     
