import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="kinematics visualiser", page_icon="A", layout="wide")

st.markdown("""
<style>
h1 {color: Aqua;}
.stApp {background-color: #f8f9fa;}
</style>
""", unsafe_allow_html=True)

st.title("Kinematics Visualizer")

u=st.sidebar.slider("Initial velocity (m/s)",0,50, 20)
a=st.sidebar.slider("Acceleartion (m/s2)",0, 20, 10)
T= st.sidebar.slider("Total time (s)", 1, 30, 10)

t= np.linspace(0, T, 200)
v= u+ a*t
X= u*t + 0.5*a*t**2

fig= go.Figure(go.Scatter(x=t, y=v, mode="lines"))
fig.update_layout(title="Velocity vs Time", xaxis_ttitle="Time(s)",yaxis_title="Velocity (m/s)", template="plotly_white")
fig.update_trace(line_color="#3B5BDB", line_width=3)

fig2= go.Figure(go.Scatter(x=t, y=X, mode="lines"))
fig2.update_layout(title="Position vs Time", xaxis_ttitle="Time(s)",yaxis_title="Position(m)", template="plotly_white")
fig2.update_trace(line_color="#E8590C", line_width=3)

tab1, tab2 = st.tabs(["Velocity-Time", "Position-Time"])
with tab1:
  st.plotly_chart(fig, use_container_width=True)
with tab2:
  st.plotly_chart(fig2, use_container_width=True)


