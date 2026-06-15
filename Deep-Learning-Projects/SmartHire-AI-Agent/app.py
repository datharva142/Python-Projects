import streamlit as st
from questions import questions_bank
from interview_agent import MockInterviewAgent

# ----------------- Configuration -----------------
st.set_page_config(
    page_title="SmartHire AI Agent",
    page_icon="🤖",
    layout="wide"
)

# ----------------- Helper Functions -----------------
def initialize_session_state():
    if "agent" not in st.session_state:
        st.session_state.agent = None
    if "selected_questions" not in st.session_state:
        st.session_state.selected_questions = []
    if "current_q_index" not in st.session_state:
        st.session_state.current_q_index = 0
    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False
    if "interview_finished" not in st.session_state:
        st.session_state.interview_finished = False
    if "current_evaluation" not in st.session_state:
        st.session_state.current_evaluation = None
    if "final_report" not in st.session_state:
        st.session_state.final_report = None
    if "report_filepath" not in st.session_state:
        st.session_state.report_filepath = None

def get_available_topics():
    return list(set(q["topic"] for q in questions_bank))

def start_interview(name, mode, topic=None):
    st.session_state.agent = MockInterviewAgent(name)
    if mode == "Full Interview":
        st.session_state.selected_questions = questions_bank
    else:
        st.session_state.selected_questions = [q for q in questions_bank if q["topic"] == topic]
    
    st.session_state.current_q_index = 0
    st.session_state.interview_started = True
    st.session_state.interview_finished = False
    st.session_state.current_evaluation = None
    st.session_state.final_report = None
    st.session_state.report_filepath = None

def finish_interview():
    st.session_state.interview_finished = True
    st.session_state.final_report = st.session_state.agent.generate_final_report()
    st.session_state.report_filepath = st.session_state.agent.finish_interview()

def next_question():
    st.session_state.current_q_index += 1
    st.session_state.current_evaluation = None

# ----------------- Main App UI -----------------
initialize_session_state()

st.title("🤖 SmartHire AI Agent")
st.markdown("Practice technical interviews with an AI-based system powered by Llama3.")
st.divider()

# Sidebar for Setup
with st.sidebar:
    st.header("Setup Interview")
    student_name = st.text_input("Enter your name:", placeholder="Name")
    
    mode = st.radio("Select Interview Mode:", ["Full Interview", "Topic-wise Interview"])
    
    selected_topic = None
    if mode == "Topic-wise Interview":
        topics = get_available_topics()
        selected_topic = st.selectbox("Select a topic:", topics)
        
    start_btn = st.button("Start Interview", type="primary", use_container_width=True)
    
    if start_btn:
        if not student_name.strip():
            st.error("Please enter your name to begin.")
        else:
            start_interview(student_name, mode, selected_topic)
            st.rerun()

# Main Area content
if not st.session_state.interview_started:
    st.info("👈 Please enter your details in the sidebar and click 'Start Interview' to begin.")

elif st.session_state.interview_finished:
    st.header("🎉 Interview Complete!")
    st.success(f"Great job, {st.session_state.agent.student_name}! Here is your final report:")
    
    # Display the final report cleanly
    report_text = st.session_state.final_report
    st.code(report_text, language="markdown")
    
    # Provide a download button
    with open(st.session_state.report_filepath, "r") as f:
        st.download_button(
            label="📄 Download Report File (.txt)",
            data=f,
            file_name=st.session_state.report_filepath.split("/")[-1],
            mime="text/plain",
            type="primary"
        )
    
    if st.button("Start New Interview"):
        st.session_state.interview_started = False
        st.rerun()

else:
    # Display current question
    q_idx = st.session_state.current_q_index
    total_q = len(st.session_state.selected_questions)
    current_q = st.session_state.selected_questions[q_idx]
    
    st.subheader(f"Question {q_idx + 1} of {total_q} [{current_q['topic']}]")
    st.markdown(f"**{current_q['question']}**")
    
    # Input answer
    if st.session_state.current_evaluation is None:
        answer = st.text_area("Your Answer:", height=150, placeholder="Type your answer here...")
        if st.button("Submit Answer", type="primary"):
            if not answer.strip():
                st.warning("Please provide an answer before submitting.")
            else:
                with st.spinner("AI is evaluating your answer..."):
                    eval_result = st.session_state.agent.evaluate_answer(current_q["topic"], current_q["question"], answer)
                    st.session_state.current_evaluation = eval_result
                st.rerun()
    else:
        st.text_area("Your Answer:", value=st.session_state.agent.history[-1]["answer"], height=150, disabled=True)
        
        st.divider()
        st.subheader("🤖 AI Evaluation")
        
        # Determine if it's an error message
        if st.session_state.current_evaluation.startswith("Error:"):
            st.error(st.session_state.current_evaluation)
        else:
            st.info(st.session_state.current_evaluation)
            
        # Navigation buttons
        col1, col2 = st.columns([1, 4])
        with col1:
            if q_idx < total_q - 1:
                if st.button("Next Question", type="primary"):
                    next_question()
                    st.rerun()
            else:
                if st.button("Finish Interview", type="primary"):
                    finish_interview()
                    st.rerun()
        with col2:
            if st.button("End Interview Early", type="secondary"):
                finish_interview()
                st.rerun()
