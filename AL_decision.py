import pandas as pd 

df = pd.read_csv("D:/Photos & Videos/Colledge Life/Automated Labor ppt/Machine Learning model/automated_turn.csv")
df.columns = df.columns.str.lower()

indep = df.drop('decision',axis='columns')
independent = indep.drop('moving_distance_mm',axis='columns')

d =df.drop('stop_distance_mm',axis='columns')
de = d.drop('right_distance_mm',axis='columns')
dept = de.drop('left_distance_mm',axis='columns')
dependent = dept.drop('moving_distance_mm',axis='columns')

from sklearn.preprocessing import LabelEncoder
la_decision=LabelEncoder()

dependent['decision_n']=la_decision.fit_transform(dependent['decision'])
dependent_n = dependent.drop('decision',axis='columns')

from sklearn import tree
model=tree.DecisionTreeClassifier()

model.fit(independent,dependent_n)
model.score(independent,dependent_n)

from sklearn import tree
import matplotlib.pyplot as plt
fig = fig = plt.figure(figsize=(100,50))
print(tree.plot_tree((model),filled=1))
movement = True
while movement:
    stop = float(input("Enter your stop Distance: "))
    right = float(input("Enter your Right side distance: "))
    left = float(input("Enter your Left Distance: "))
    decision = model.predict([[stop,right,left]])
    if decision == 1:
        print("Decision 1:- Take left")
        print("Decision 2:- Moves by 10 mm")
        print("Decision 3:- Stops")
    if decision == 0:
        print("Decision 1:- Move forward")
        print("Decision 2:- Moves by 10 mm")
        print("Decision 3:- Stops")
    if decision == 2:
        print("Decision 1:- Take right")
        print("Decision 2:- Moves by 10 mm")
        print("Decision 3:- Stops")
    end = input("Do you want to contiue Y/N ? ")
    if end == "N":
        movement = False
    



