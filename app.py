from imports import *
from graph import *
from predict_UI import *
from process import *
import json
from streamlit_lottie import st_lottie
from contact_us import *
import warnings
warnings.filterwarnings('ignore')



#loading files for animations
def load_lottiefiles(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

lottie_graph = load_lottiefiles('animations/data-analysis-gif.json')
lottie_car = load_lottiefiles('animations/car.json')
lottie_car2 = load_lottiefiles('animations/car2.json')

st.sidebar.title('Navigation Panel')
nav = st.sidebar.radio(' ',['Analyze', 'Prediction'])

if nav == 'Analyze':
    st.title('Used Car Data Analysis and Visualisation')
    st_lottie(
    lottie_graph,
    quality= 'medium',
    width= '40rem',
    height= '20rem',
    )
    graphs()

if nav == 'Prediction':
    st.title('Price Prediction using Machine Learning Algorithms')
    st_lottie(
    lottie_car,
    quality= 'medium',
    width= '40rem',
    height= '15rem',
    )
    predict_data()
        
    
