from flask import Flask,render_template
import urllib2, json
app=Flask(__name__)

@app.route('/')
def root():
    u=urllib2.urlopen("http://quotes.rest/qod.json")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                           info = data['contents']['quotes'][0]
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
