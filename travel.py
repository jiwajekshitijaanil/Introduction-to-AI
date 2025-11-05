import streamlit as st
DESTINATIONS = [
    {"name": "Goa", "climate": "Hot", "interest": "Beach", "budget": "Medium", "season": "Winter",
     "description": "Beaches, water sports and relaxed holiday vibe."},
    {"name": "Manali", "climate": "Cold", "interest": "Mountains", "budget": "Medium", "season": "Summer",
     "description": "Himalayan hill station with trekking and snow activities (seasonal)."},
    {"name": "Jaipur", "climate": "Hot", "interest": "History", "budget": "Low", "season": "Winter",
     "description": "Rich cultural heritage, palaces, forts and local markets."},
    {"name": "Kerala", "climate": "Humid", "interest": "Nature", "budget": "Medium", "season": "Monsoon",
     "description": "Backwaters, houseboats, and lush green landscapes."},
    {"name": "Kashmir", "climate": "Cold", "interest": "Mountains", "budget": "High", "season": "Summer",
     "description": "Scenic valleys, lakes, and cooler weather in summer."},
    {"name": "Ooty", "climate": "Cold", "interest": "Nature", "budget": "Low", "season": "Summer",
     "description": "Tea gardens, mild climate, and calm hill station atmosphere."},
    {"name": "Andaman Islands", "climate": "Humid", "interest": "Beach", "budget": "High", "season": "Winter",
     "description": "Clear waters, snorkeling, and island resorts."},
    {"name": "Darjeeling", "climate": "Cold", "interest": "Nature", "budget": "Medium", "season": "Summer",
     "description": "Tea gardens, views of Kanchenjunga, and pleasant weather."}
]
def score_destination(dest, prefs):
    score = 0
    if dest["season"] == prefs["season"]:
        score += 2
    if dest["climate"] == prefs["climate"]:
        score += 2
    if dest["interest"] == prefs["interest"]:
        score += 3 
    if dest["budget"] == prefs["budget"]:
        score += 1
    return score

st.set_page_config(page_title="Travel Destination Advisor", layout="centered")
st.title("Travel Destination Advisor Expert System")
st.write("Select your preferences and get recommended destinations.")

# input area
with st.form("prefs_form"):
    col1, col2 = st.columns(2)
    with col1:
        season = st.selectbox("Preferred season to travel", ["Summer", "Winter", "Monsoon"], index=0)
        climate = st.selectbox("Preferred climate", ["Hot", "Cold", "Humid"], index=0)
    with col2:
        interest = st.selectbox("Type of place you like", ["Beach", "Mountains", "History", "Nature"], index=0)
        budget = st.selectbox("Budget level", ["Low", "Medium", "High"], index=1)

    submit = st.form_submit_button("Find destinations")

if submit:
    prefs = {"season": season, "climate": climate, "interest": interest, "budget": budget}
    scored = []
    for d in DESTINATIONS:
        s = score_destination(d, prefs)
        scored.append((s, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    top_score = scored[0][0]
    if top_score == 0:
        st.warning("No strong exact matches found — showing best partial matches.")
    st.subheader("Recommended destinations (best matches first):")
    shown = 0
    for score, dest in scored:
        if shown >= 3 and score < top_score:
            break
        st.markdown(f"**{dest['name']}**")
        st.write(dest["description"])
        st.write(f"- Best season: {dest['season']}  |  Climate: {dest['climate']}  |  Budget: {dest['budget']}  |  Interest: {dest['interest']}")
        st.write(f"- Match score: {score}")
        st.write("")  # spacing
        shown += 1