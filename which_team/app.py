from flask import Flask, render_template, request
from team_recommendation import get_team_recommendation  # Import your custom function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        # Extract data from form
        history = request.form.get("history")
        passionate = request.form.get("passionate")
        iq = request.form.get("iq")
        public = request.form.get("public")

        # Call your recommendation function
        recommended_team = get_team_recommendation(history, passionate, iq, public)

        # Show the result (you might want to render a template instead)
        return f"Based on your answers, you might enjoy rooting for {recommended_team}!"
    return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug=True)
