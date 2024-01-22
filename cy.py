from flask import Flask
a=Flask(__name__)
@a.route("/")
def fun1():
  return"<h1><a href = https://iittp.codetantra.com></a></h1>"
@a.route("/one")
def fun2():
  return"<h1>bits csw</h1>"
@a.route("/two")
def fun3():
  return"<h1>bits cse</h1>"
a.run()