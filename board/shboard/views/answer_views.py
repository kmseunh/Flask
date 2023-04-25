from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from shboard import db
from shboard.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']               #--- POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 content인 값
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)              #--- 질문에 달린 답변들
    db.session.commit()
    return redirect(url_for('question/detail', question_id=question_id))
