import os
from datetime import datetime

def save_report(student_name, report):
    folder_name = "reports"
    # Get the directory of the current script to create reports folder next to it
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(base_dir, folder_name)
    
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    safe_name = student_name.replace(" ", "_")
    filename = f"AI_Agent_{safe_name}_Interview_Report_{timestamp}.txt"
    filepath = os.path.join(reports_dir, filename)
    
    with open(filepath, "w") as f:
        f.write(report)
        
    return filepath
