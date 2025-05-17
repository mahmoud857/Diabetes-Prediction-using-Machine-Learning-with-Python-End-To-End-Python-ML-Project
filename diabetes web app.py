import numpy as np 
import pickle
import streamlit 

loading_model=pickle.load(open("F:\ماشين ليرنج\مشاريع ماشين ليرنج end to end\Project 2 Diabetes Prediction using Machine Learning with Python  End To End Python ML Project\diabetes_model","rb"))


def diabetes_prediction(input_data):

    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)


    print("---------------------------------------------------")

    prediction=loading_model.predict(input_data_reshaped)

    print(prediction)
    print("---------------------------------------------------")

    if[prediction]==0:
        return "the person is not diabetic"
    else:
        return "the person is diabetic"
print("---------------------------------------------------")

   


def main():
    streamlit.title("Diabetes Prediction Web App")

    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age

    Pregnancies=streamlit.text_input("Number of Pregnancies")
    Glucose=streamlit.text_input("Glucose Level")
    BloodPressure=streamlit.text_input("Blood Pressure value")
    SkinThickness=streamlit.text_input("Skin Thickness value")
    Insulin=streamlit.text_input("Insulin Level")
    BMI=streamlit.text_input("BMI value")
    DiabetesPedigreeFunction=streamlit.text_input("Diabetes Pedigree Function value")
    Age=streamlit.text_input("Age of the Person")

    diagnosis=""

    if streamlit.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    

    streamlit.success(diagnosis)




    if __name__=="__main__":
        main()
        