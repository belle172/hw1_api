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
      categoryTasks = tasks[currentCategory]
   else: 
      categoryTasks = ["no tasks in the requested category"]
   return jsonify({"tasks":categoryTasks});

# adds a category to the list of categories 
@app.route('/planner/addCategory',methods = ['POST'])
def addCategory():
   global categories 
   category = request.get_json(force=True) 
   categories.append(category) 
   return jsonify({"categories":category});

# add one task to the dictionary of tasks 
@app.route('/planner/addTask',methods = ['POST'])
def addTask():
   global tasks 
   global categories 
   newTask = request.get_json(force=True) 
   for (key, value) in newTask.items(): 
      tasks[key].append(value)
      newCategory = key 
   # check if category is already in list of categories, if not add it 
   if newCategory not in categories: 
      categories.append(newCategory) 
   return jsonify({"tasks":task});

# remove a task from the dictionary of tasks 
@app.route('/planner/removeTask',methods = ['POST'])
def removeTask():
   global tasks 
   task = request.get_json(force=True) 
   for (key, value) in task.items(): 
      tasks[category].remove(currentCategory) 
   return jsonify({"tasks":task});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=7998, debug = True)
