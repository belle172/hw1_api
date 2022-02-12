# Jasper Bellefeuille 3081 hw1 part A 
# Okay heres what were doing: im gonna make it like a planner, 
# so you can add a category, add a specific task to a category, 
# mark a task as complete (get rid of it), see tasks in a 
# specific category, or see all tasks  

# imports 
from flask import Flask, request, jsonify

# initialize variables 
app = Flask(__name__)
categories = [] # list 
tasks = []      # list of lists  

@app.route('/planner/getCategories',methods = ['GET'])
def getCategories():
   return jsonify({"categories":categories});

@app.route('/planner/getTasks',methods = ['GET'])
def getTasks():
   return jsonify({"tasks":tasks});

@app.route('/planner/addCategory',methods = ['POST'])
def addCategory():
   global categories 
   category = request.get_json() 
   categories.append(category)
   return jsonify({"categories":category});

@app.route('/planner/addTask',methods = ['POST'])
def addTask():
   global tasks 
   task = request.get_json() 
   tasks.append(task)
   return jsonify({"tasks":task});

@app.route('/planner/removeTask',methods = ['POST'])
def removeTask():
   global tasks 
   task = request.get_json() 
   tasks.remove(task) 
   return jsonify({"tasks":task});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8081, debug = True)
