from flask import Flask, jsonify
from werkzeug.routing import BaseConverter

import logic

app = Flask(__name__)




def to_python_number( value):
    v = value.split("[")[1]
    value = v.split("]")[0]
    return [float(x) for x in value.split(',')]

def to_python_relation(value, n):
    h =[]
    res=[]
    count=0
    v = value.split("[")[1]
    value = v.split("]")[0]
    for i in value.split(','):
        if count==n:
            res.append(h)
            print(h)
            h=[]
            count=1
        else:
            count+=1
        h.append(float(i))
    res.append(h)
    print(res)
    return res

@app.route("/fuzzyNumberRelationComposition/<number>/<relation>/<n>",methods=['GET'])
def f1(number, relation,n):
    n = int(n)
    number = to_python_number(number)
    relation=to_python_relation(relation, n)
    return jsonify({"result": logic.fuzzyNumberRelationComposition(number, relation)})

@app.route("/fuzzyOutput/<condition>/<effect>/<a>",methods=['GET'])
def f2(condition, effect, a):
    condition = to_python_number(condition)
    effect = to_python_number(effect)
    a = to_python_number(a)
    return jsonify({"result": logic.fuzzyOutput(condition, effect, a)})


@app.route("/fuzzyOutputSystem/<condition>/<effect>/<a>/<n>")
def f3(condition, effect, a, n):
    import logic1
    condition = to_python_number(condition)
    effect = to_python_number(effect)
    n = int(n)
    a = to_python_relation(a, n)
    return jsonify({"result": logic1.fuzzyOutputSystem(condition, effect, a)})

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
