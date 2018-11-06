from flask import Flask,json,render_template
'''5Nov2018AndrewCumming'''
app = Flask(__name__)
w =  json.load(open('worldl.json'))
@app.route('/')
def index():
	return render_template("index.html",w=w)

# @app.route('/country/<i>')
# def country(i):
# 	return "{0} {1}  {2}".format(w[int(i)]['name'],w[int(i)]['continent'],str(w[int(i)]['population']))

@app.route('/country/<i>')
def country(i):
	return render_template ("country.html",c =w[int(i)])

#if __name__=="main":
app.run(host='0.0.0.0',debug=True)

