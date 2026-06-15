import re
from llm_engine import ask_llm
from report_generator import save_report

class MockInterviewAgent:
    def __init__(self, student_name):
        self.student_name = student_name
        self.history = []
        self.total_score = 0
        self.total_questions = 0

    def evaluate_answer(self, topic, question, answer):
        prompt = f"""You are an expert technical interviewer evaluating a student's answer.
        
Topic: {topic}
Question: {question}
Student's Answer: {answer}

Please evaluate the answer and provide your response strictly in the following format:
Score: <Score out of 10>
Evaluation: <Your detailed evaluation>
Missing Points: <What the student missed>
Improved Answer: <How to answer perfectly>
Interview Suggestion: <Tips for the student>
"""
        response = ask_llm(prompt)
        
        if response.startswith("Error:"):
            return response
            
        score = self.extract_score(response)
        
        self.history.append({
            "topic": topic,
            "question": question,
            "answer": answer,
            "score": score,
            "feedback": response
        })
        
        if score is not None:
            self.total_score += score
        self.total_questions += 1
        
        return response

    def extract_score(self, evaluation):
        match = re.search(r"Score:\s*(\d+(?:\.\d+)?)(?:/10|\s+out\s+of\s+10)?", evaluation, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return None
        return None

    def generate_final_report(self):
        if self.total_questions == 0:
            return "No questions were answered."
            
        avg_score = self.total_score / self.total_questions
        
        report_lines = [
            f"=== Final Interview Report ===",
            f"Student Name: {self.student_name}",
            f"Total Questions Answered: {self.total_questions}",
            f"Total Score: {self.total_score}/{self.total_questions * 10}",
            f"Average Score: {avg_score:.2f}/10",
            f"Overall Performance: {'Excellent' if avg_score >= 8 else 'Good' if avg_score >= 6 else 'Needs Improvement'}",
            f"\n=== Question-wise Analysis ==="
        ]
        
        for i, item in enumerate(self.history, 1):
            report_lines.append(f"\n--- Question {i} ---")
            report_lines.append(f"Topic: {item['topic']}")
            report_lines.append(f"Question: {item['question']}")
            report_lines.append(f"Student Answer: {item['answer']}")
            report_lines.append(f"Feedback:\n{item['feedback']}")
            
        report_content = "\n".join(report_lines)
        return report_content

    def finish_interview(self):
        report = self.generate_final_report()
        filepath = save_report(self.student_name, report)
        return filepath
