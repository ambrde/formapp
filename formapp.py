from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods=['GET', 'POST'])
def render_main():
    return render_template('formhome.html')
    
@app.route("/results", methods=['GET', 'POST'])
def render_results():
    r = int(request.form['redamt'])
    g = int(request.form['greenamt'])
    b = int(request.form['blueamt'])
    if r > g and r > b:
        summary = "Your color is mostly red."
    elif g > r and g > b:
        summary = "Your color is mostly green."
    elif b > r and b > g:
        summary = "Your color is mostly blue."
    else:
        summary = "Your color is not mostly anything! Two or more of your values were equal."
    answers = "Red: " + str(r) + "Green: " + str(g) + "Blue: " + str(b)
    
    return render_template('formresponse.html', answers = answers, summary = summary, r = r, g = g, b = b)
    
if __name__=="__main__":
    app.run(debug=False)