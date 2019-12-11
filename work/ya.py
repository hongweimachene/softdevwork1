from flask import Flask, render_template,request
import cgi

app= Flask(__name__)

@app.route("/")

def form():
    print(app)
    print(request)
    print(request.args)
    print(request.form)
    return render_template('form.html')

@app.route('/output')

def out():
    print(request.args['username'])
    return render_template('out_html',
                           username= request.args["username"],
                           method = request.method
                           )

if __name__ == "__main__":
    app.debug=True
    app.run()
    
    
    
