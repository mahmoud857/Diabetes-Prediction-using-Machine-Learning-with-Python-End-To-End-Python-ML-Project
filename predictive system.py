import numpy as np 
import pickle

# Load the model 

loding_model=pickle.load(open("F:\ماشين ليرنج\مشاريع ماشين ليرنج end to end\Project 2 Diabetes Prediction using Machine Learning with Python  End To End Python ML Project\diabetes_model","rb"))

input_data=(6,148,72,35,0,33.6,0.627,50)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


print("---------------------------------------------------")

prediction=loding_model.predict(input_data_reshaped)

print(prediction)
print("---------------------------------------------------")

if[prediction]==0:
    print("the person is not diabetic")
else:
    print("the person is diabetic")
print("---------------------------------------------------")


