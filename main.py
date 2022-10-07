from flask import Flask,request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def template():
 return render_template("index.html")

@app.route('/operacion',methods=['POST'])
def operacion():
  ope=int(request.form['select'])
  num1=int(request.form['num1'])
  num2=int(request.form['num2'])

  if ope==1:
   op="+"
   res=num1+num2
  if ope==2:
   op="-"
   res=num1-num2
  if ope==3:
   op="x"
   res=num1*num2
  if ope==4:
    if num2==0:
      op="/"
      res="No se puede dividir por cero"
    if num2!=0:
       op="/"
       res=float(num1 /num2 )

  if ope<1 or ope>4:
     res="Fuera de rango la operación"
   
  return (f'{num1} {op} {num2} = {res}')
if __name__=='__main__':
   app.run(debug=True)