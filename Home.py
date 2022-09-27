import matplotlib.pyplot as plt
import streamlit as st
from reversible_first_order import ReversibleFirstOrder
from src.helpers import text_from_markdown, load_css, find_me_buttons

st.set_page_config(
    layout="centered", page_title="Reversible Kinetics", page_icon=":racing_car"
)

load_css("pages/styles.css")
PAGE_TEXT_FILE = "pages/01_Home.md"
content = text_from_markdown(PAGE_TEXT_FILE)

st.title("Reversible first-order reactions")

st.markdown(
    """
    :warning: Check the sidebar to access the sliders to interact with the plots! 
    If you are on a mobile device, click on the arrow on the top left of the screen to 
    show the sidebar. :warning:
    """
)

with st.sidebar:
    kf = st.slider("Rate constant - forward reaction - Kf", 1, 10, 1, 1)
    kb = st.slider("Rate constant - backward reaction - Kb", 1, 10, 1, 1)
    A0 = st.slider("Initial concentration A - [A0]", 0, 10, 1, 1)
    B0 = st.slider("Initial concentration B - [B0]", 0, 10, 0, 1)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
example = ReversibleFirstOrder(kf, kb, A0, B0, 5)

example.plot_reaction_time(ax=ax1)
st.pyplot(fig1)

example.plot_reaction_quotient_time(ax=ax2)
st.pyplot(fig2)

st.markdown("".join(content[0]))

columns = st.columns([1, 1, 1.2, 1, 1])

sites = ("linkedin", "portfolio", "github", "github_sponsors")
links = (
    "flsbustamante",
    "https://franciscobustamante.com.br",
    "chicolucio",
    "chicolucio",
)

with columns[2]:
    st.write("Developed by: Francisco Bustamante")
    for site, link in zip(sites, links):
        find_me_buttons(site, link)
