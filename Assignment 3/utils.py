import re
import sys
import textwrap


def extract_fields(text):
    # Regular expression patterns to extract fields
    question_pattern = r'\*\*Question\*\*\n(.*?)\n\*\*Model Answer\*\*'
    model_answer_pattern = r'\*\*Model Answer\*\*\n(.*?)\n\*\*Student Answer\*\*'
    student_answer_pattern = r'\*\*Student Answer\*\*\n(.*?)\n\*\*TA Rating for Question Usefulness'
    rating_pattern = r'\*\*TA Rating for Question Usefulness \(1 being very poor, 5 being excellent\)\*\*\n(.*?)\n\*\*TA Comments'
    comments_pattern = r'\*\*TA Comments for Question Usefulness\*\*\n(.*?)\n\*\*End of TA Comments\*\*'

    # Extracting fields using regular expressions
    question = re.search(question_pattern, text, re.DOTALL).group(1).strip()
    model_answer = re.search(model_answer_pattern, text, re.DOTALL).group(1).strip()
    student_answer = re.search(student_answer_pattern, text, re.DOTALL).group(1).strip()
    rating = re.search(rating_pattern, text, re.DOTALL).group(1).strip()
    comments = re.search(comments_pattern, text, re.DOTALL).group(1).strip()
    fields = {
        'question': question,
        'model_answer': model_answer,
        'student_answer': student_answer,
        'rating': rating,
        'comments': comments
    }
    return fields


# Function to read the file and extract fields for each block
def read_questions_file_into_dict(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Splitting text into blocks
    blocks = text.split('******************************************************************\n\n')

    # Extracting fields from each block
    extracted_blocks = []
    for block in blocks:
        if block.strip():  # Skipping empty blocks
            extracted_blocks.append(extract_fields(block))
    return extracted_blocks
