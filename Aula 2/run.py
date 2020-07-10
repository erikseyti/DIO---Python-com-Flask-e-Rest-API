from flask import Flask
app = Flask(__name__)

@app.route("/<int:numero>", methods=['GET','POST'])
def ola(numero):
    return f"Ola Mundo! {numero}"

if __name__ == "__main__":
    app.run(debug=True)
