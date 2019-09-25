from flask import Flask, render_template,request
import cgi

app= Flask(__name__)

@app.route("/")

def form():
    print(app)
    print(request)
    print(request.args)
    return render_template('form.html')

if __name__ == "__main__":
    app.debug=True
    app.run()
    
    
    
