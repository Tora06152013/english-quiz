from flask import Flask, render_template, request, session
from questions import questions
import random

app = Flask(__name__)

app.secret_key = "english_quiz_secret"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start/<int:total>")
def start_quiz(total):

    if total not in [10, 100]:
        total = 10

    # 問題をランダムに選ぶ
    question_indices = random.sample(range(len(questions)), total)

    session["question_indices"] = question_indices
    session["question_number"] = 0
    session["score"] = 0
    session["total_questions"] = total

    return render_template(
        "index.html",
        question=questions[question_indices[0]],
        question_number=1,
        total_questions=total
    )


@app.route("/answer", methods=["POST"])
def answer():
    user_answer = request.form["answer"]

    question_number = session["question_number"]
    question_indices = session["question_indices"]

    correct_answer = questions[question_indices[question_number]]["answer"]

    if user_answer == correct_answer:
        result = "正解！🎉"
        result_type = "correct"
        session["score"] += 1
    else:
        result = "不正解！😢"
        result_type = "incorrect"

    question_number += 1
    session["question_number"] = question_number

    question_finished = question_number >= session["total_questions"]

    if question_finished:
        result = f"クイズ終了！ {session['score']} / {session['total_questions']}問正解！"
        result_type = "finished"

    return render_template(
        "result.html",
        result=result,
        result_type=result_type,
        correct_answer=correct_answer,
        question_finished=question_finished
    )


@app.route("/next")
def next_question():
    question_number = session["question_number"]

    if question_number >= session["total_questions"]:
        return render_template(
            "result.html",
            result=f"クイズ終了！ {session['score']} / {session['total_questions']}問正解！"
        )

    return render_template(
        "index.html",
        question=questions[session["question_indices"][question_number]],
        question_number=question_number + 1,
        total_questions=session["total_questions"]
    )


if __name__ == "__main__":
    app.run(debug=True)