# Jasper Bellefeuille 3081 hw1 part A 
# Okay heres what were doing: im gonna make it like a planner, 
# so you can add a category, add a specific task to a category, 
# mark a task as complete (get rid of it), see tasks in a 
# specific category, or see all tasks  

# imports 
from flask import Flask, request, jsonify
from datatime import datetime 

# initialize variables 
app = Flask(__name__)
categories = [] # list 
tasks = {"csci3081": "hw1"}      # dictionary  

# returns the list of categories 
@app.route('/planner/getCategories',methods = ['GET'])
def getCategories():
   return jsonify({"categories":categories});

# returns the dictionary of all tasks 
@app.route('/planner/getTasks',methods = ['GET'])
def getTasks():
   return jsonify({"tasks":tasks});

# returns the tasks in the requested category  
@app.route('/planner/getCategory',methods = ['GET'])
def getCategory(): 
   global tasks 
   categoryTasks = [] 
   currentCategory = request.get_json(force=True) 
   if currentCategory in tasks: 
      categoryTasks = tasks(currentCategory)

   # for (category, task) in tasks 
   #    if category == currentCategory: 
   #       categoryTasks.append(task)

   return jsonify({"tasks":categoryTasks});

@app.route('/planner/addCategory',methods = ['POST'])
def addCategory():
   global categories 
   category = request.get_json(force=True) 
   categories.append(category) 
   return jsonify({"categories":category});

@app.route('/planner/addTask',methods = ['POST'])
def addTask():
   global tasks 
   global categories 
   task = request.get_json() 
   (category, currentTask) = task 
   tasks[category].append(currentTask)
   # check if category is already in list of categories, if not add it 
   if category not in categories: 
      categories.append(category) 
   return jsonify({"tasks":task});

@app.route('/planner/removeTask',methods = ['POST'])
def removeTask():
   global tasks 
   task = request.get_json(force=True) 
   (category, currentTask) = task 
   tasks[category].remove(currentCategory) 
   return jsonify({"tasks":task});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=7651, debug = True)
