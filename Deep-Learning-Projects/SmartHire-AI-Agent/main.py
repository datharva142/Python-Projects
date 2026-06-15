from questions import questions_bank
from interview_agent import MockInterviewAgent

def print_header():
    print("="*50)
    print(" "*12 + "SmartHire AI Agent")
    print("="*50)

def show_menu():
    print("\n--- Main Menu ---")
    print("1. Start Full Interview")
    print("2. Start Topic-wise Interview")
    print("3. Exit")
    return input("Select an option: ")

def get_available_topics():
    topics = set(q["topic"] for q in questions_bank)
    return list(topics)

def start_interview(agent, selected_questions):
    for i, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {i} [{q['topic']}]: {q['question']}")
        answer = input("Your Answer: ")
        
        print("\n[AI is evaluating your answer...]")
        evaluation = agent.evaluate_answer(q["topic"], q["question"], answer)
        
        print("\n--- AI Evaluation ---")
        print(evaluation)
        print("-" * 21)
        
        if i < len(selected_questions):
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont != 'yes' and cont != 'y':
                print("Ending interview early.")
                break

def main():
    print_header()
    student_name = input("Enter your name: ")
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            agent = MockInterviewAgent(student_name)
            print("\nStarting Full Interview...")
            start_interview(agent, questions_bank)
            filepath = agent.finish_interview()
            print(f"\nInterview finished. Final report saved to: {filepath}")
            break
            
        elif choice == '2':
            topics = get_available_topics()
            print("\nAvailable Topics:")
            for i, topic in enumerate(topics, 1):
                print(f"{i}. {topic}")
                
            topic_choice = input("Select a topic number: ")
            try:
                topic_idx = int(topic_choice) - 1
                if 0 <= topic_idx < len(topics):
                    selected_topic = topics[topic_idx]
                    selected_questions = [q for q in questions_bank if q["topic"] == selected_topic]
                    agent = MockInterviewAgent(student_name)
                    print(f"\nStarting Topic-wise Interview for {selected_topic}...")
                    start_interview(agent, selected_questions)
                    filepath = agent.finish_interview()
                    print(f"\nInterview finished. Final report saved to: {filepath}")
                    break
                else:
                    print("Invalid topic choice.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '3':
            print("Exiting SmartHire AI Agent. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
