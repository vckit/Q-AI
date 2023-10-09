from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

easy_computer_science_test = {
    "question1": {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Technology Modern Language", "Hyperlink and Text Markup Language"],
        "correct_answer_index": 0
    },
    "question2": {
        "question": "Which programming language is known for its use in web development and is often used on the client-side?",
        "options": ["Python", "JavaScript", "C++"],
        "correct_answer_index": 1
    },
    "question3": {
        "question": "What is the main function of an operating system?",
        "options": ["To format hard drives", "To provide a user interface", "To manage computer hardware and software resources"],
        "correct_answer_index": 2
    },
    "question4": {
        "question": "What is a database used for?",
        "options": ["Storing and retrieving data", "Playing video games", "Sending emails"],
        "correct_answer_index": 0
    },
    "question5": {
        "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "options": ["Queue", "Stack", "Linked List"],
        "correct_answer_index": 1
    },
    "question6": {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Control Processing Unit"],
        "correct_answer_index": 0
    },
    "question7": {
        "question": "Which of the following is a high-level programming language?",
        "options": ["Assembly language", "Java", "Machine language"],
        "correct_answer_index": 1
    },
    "question8": {
        "question": "What does URL stand for?",
        "options": ["Uniform Resource Locator", "Universal Reference Language", "United Resource Library"],
        "correct_answer_index": 0
    },
    "question9": {
        "question": "Which protocol is used for secure communication over the Internet?",
        "options": ["HTTP", "FTP", "HTTPS"],
        "correct_answer_index": 2
    },
    "question10": {
        "question": "What does IDE stand for in the context of software development?",
        "options": ["Integrated Development Environment", "Interactive Design Environment", "Internet Development Engine"],
        "correct_answer_index": 0
    },
}

def shuffle_options_and_update_index(question_data):
    options = question_data["options"][:]
    correct_answer_index = question_data["correct_answer_index"]

    # Store the correct answer
    correct_answer = options[correct_answer_index]

    # Shuffle the options
    random.shuffle(options)

    # Update the correct answer index to the new position of the correct answer
    updated_correct_answer_index = options.index(correct_answer)

    return options, updated_correct_answer_index

shuffled_easy_test = {
    key: {
        "question": question_data["question"],
        "options": shuffled_options[0],
        "correct_answer_index": shuffled_options[1],
        "difficulty": "easy"
    }
    for key, question_data in easy_computer_science_test.items()
    for shuffled_options in [shuffle_options_and_update_index(question_data)]  # Use a for loop to bind variable
}

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process the quiz and calculate the score
        score = 0
        for key, question_data in shuffled_easy_test.items():
            selected_answer = request.form.get(key)
            if selected_answer is not None:
                try:
                    selected_answer = int(selected_answer)
                    if selected_answer == question_data['correct_answer_index']:
                        score += 1
                except ValueError:
                    pass

        # Calculate the percentage score
        percentage_score = (score / len(shuffled_easy_test)) * 100

        # Create a results dictionary to pass to the template
        results_data = {
            'score': score,
            'total': len(shuffled_easy_test),
            'percentage_score': percentage_score
        }

        return render_template('result.html', results_data=results_data)

    return render_template('quiz.html', test=shuffled_easy_test)

@app.route('/result')
def result():
    results_data = request.args.get('results_data')
    return render_template('result.html', results_data=results_data)

if __name__ == "__main__":
    app.run(debug=True)