import streamlit as st
import matplotlib.pyplot as plt

st.title("Student Study Analyzer")
st.write("Analyze how your study and sleep habits affect your academic performance.")

# ===================== SUBJECT SETUP =====================

st.sidebar.header("Subject Setup")

num_subjects = st.sidebar.number_input(
    "Enter number of subjects (max 8)",
    min_value=1,
    max_value=8,
    value=5
)

# Initialize session state for subjects
if "subjects" not in st.session_state or len(st.session_state.subjects) != num_subjects:
    st.session_state.subjects = [f"Subject {i+1}" for i in range(num_subjects)]

st.sidebar.subheader("Enter Subject Names")

for i in range(num_subjects):
    st.session_state.subjects[i] = st.sidebar.text_input(
        f"Name of subject {i+1}",
        st.session_state.subjects[i]
    )

subjects = st.session_state.subjects

# ===================== DATA INPUT =====================

marks = []
study_hours = []
sleep_hours = []

st.sidebar.header("Enter Performance Data")

for subject in subjects:
    st.sidebar.markdown(f"### {subject}")
    marks.append(st.sidebar.slider(f"Marks in {subject}", 0, 100, 70))
    study_hours.append(st.sidebar.slider(f"Study hours for {subject}", 0.0, 10.0, 2.0))
    sleep_hours.append(st.sidebar.slider(f"Sleep hours before {subject}", 0.0, 10.0, 7.0))

# ===================== VISUALIZATIONS =====================

st.subheader("Subject-wise Marks")
fig1, ax1 = plt.subplots()
ax1.bar(subjects, marks)
ax1.set_ylabel("Marks")
st.pyplot(fig1)

st.subheader("Study Hours vs Marks")
fig2, ax2 = plt.subplots()
ax2.scatter(study_hours, marks)
ax2.set_xlabel("Study Hours")
ax2.set_ylabel("Marks")
st.pyplot(fig2)

st.subheader("Sleep Hours vs Marks")
fig3, ax3 = plt.subplots()
ax3.scatter(sleep_hours, marks)
ax3.set_xlabel("Sleep Hours")
ax3.set_ylabel("Marks")
st.pyplot(fig3)

# ===================== INSIGHTS =====================

st.subheader("Insights")

avg_marks = sum(marks) / len(marks)
avg_sleep = sum(sleep_hours) / len(sleep_hours)
avg_study = sum(study_hours) / len(study_hours)

if avg_sleep < 6:
    st.warning("Your average sleep is low. This may negatively affect academic performance.")
else:
    st.success("Your average sleep duration looks healthy.")

if avg_study < 2:
    st.warning("Your average study time is low. Consider increasing focused study hours.")
else:
    st.success("Your study time appears consistent.")

st.info(f"Average Marks Across Subjects: {avg_marks:.2f}")
