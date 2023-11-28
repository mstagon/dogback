from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from flask_restx import Api, Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Diary, Calendar
from datetime import datetime
from openai import OpenAI
import os
from flasgger import Swagger
from pytz import timezone
DB_URL = 'sqlite:///diary.db'
datetime.now(timezone('Asia/Seoul'))
app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
Chat = api.namespace('chat', description='조회 API')
CORS(app)
swagger = Swagger(app)
# 파라미터 파서 정의
parser = reqparse.RequestParser()
parser.add_argument('prompt', type=str, required=True, help='사용자 입력 문장')

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(
    api_key = "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",
)



# @Chat.route('/diary/', methods=['POST'])
# class diary(Resource):
#     @Chat.doc(params={'prompt': '사용자 입력 문장'})
#     @Chat.response(200, '성공')
#     @Chat.response(400, '잘못된 요청')
#     def post(self):
#         try:
#             args = parser.parse_args()
#             content = args['prompt']
#             response = openai.Completion.create(
#                 engine="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": '''너는 지금부터 사용자가 입력한 일기에서 건강과 관련한 키워드를 인식하고 해당 데이터를 추출할거야
#                                 예를들어 "2023년 10월 16일 오늘은 콩이와 병원을 갔다. 가는길은 30분정도라 산책도 할겸 걸어갔다.
#                                 병원에 도착해서 체중을 재보니 2.4kg이였다 저번보다 100g증가 했다. 병원에 온 이유는 심장 사상충 예방 약을 복용하기 위함 이였다"
#                                 이러한 일기를 입력 받을경우
#                                 날짜 : 20231016, 몸무게 : 2.4kg, 산책 : 30분, 기타 : 심장사상충 예방약 복용
#                                 위 처럼 추출해주면되 지금부터 일기를 입력할게'''},
#                     {"role": "user", "content": content},
#                 ],
#                 temperature=0,
#                 max_tokens=2048
#             )
#
#             chatbot_response = response.choices[0].text.strip()
#
#             result = {
#                 'content': chatbot_response
#             }
#
#             return jsonify(result)
#
#         except Exception as e:
#             return jsonify({'error': str(e)})

@Chat.route('/solution/', methods=['POST'])
class solution(Resource):
    @Chat.doc(params={'prompt': '사용자 입력 문장'})
    @Chat.response(200, '성공')
    @Chat.response(400, '잘못된 요청')
    def post(self):
        try:
            args = parser.parse_args()
            content = args['prompt']
            response = client.chat.completions.create(
                messages=[
                    {"role": "system",
                     "content": '''너는 지금부터 사용자가 입력한 반려견 건강 상태를 확인하고 그에 따른 솔루션을 제공해줘 그리고 좀 간단하게 말해줘'''},
                    {"role": "user", "content": content},
                ],
                model="gpt-3.5-turbo",
            )

            chatbot_response = response.choices[0].message.content

            result = {
                'content': chatbot_response
            }
            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)})

@app.route("/posts/", methods=["POST"])
def create_post():
    if request.method == "POST":
        post_data = request.form
        title = post_data.get("title")
        content = post_data.get("content")
        current_time = datetime.now(timezone('Asia/Seoul'))
        session = Session()
        new_post = Diary(title=title, content=content, create_date=current_time)
        session.add(new_post)
        session.commit()
        session.close()

        return jsonify({"message": "Post created successfully"})

# Endpoint for retrieving diary data
@app.route("/get_list/", methods=["GET"])
def get_diary_data():
    if request.method == "GET":
        db = Session()
        diary_data = db.query(Diary).all()
        db.close()

        # Convert to a list of dictionaries for JSON serialization
        diary_list = []
        for entry in diary_data:
            entry_dict = {
                "id": entry.id,
                "title": entry.title,
                "content": entry.content,
                "create_date": entry.create_date.strftime("%Y-%m-%d %H:%M:%S.%f")
            }
            diary_list.append(entry_dict)

        return jsonify(diary_list)


@app.route("/calendar/", methods=["POST"])
def create_calendar_event():
    if request.method == "POST":
        post_data = request.form
        event_name = post_data.get("event_name")
        event_date = post_data.get("event_date")
        dt = datetime.strptime(event_date, "%Y-%m-%dT%H:%M:%S.%f")

        session = Session()
        new_event = Calendar(event_name=event_name, event_date=dt)
        session.add(new_event)
        session.commit()
        session.close()

        return jsonify({"message": "Calendar event created successfully"})

@app.route("/get_calendar_events/", methods=["GET"])
def get_calendar_events():
    if request.method == "GET":
        db = Session()
        calendar_events = db.query(Calendar).all()
        db.close()

        # Convert to a list of dictionaries for JSON serialization
        events_list = []
        for event in calendar_events:
            event_dict = {
                "id": event.id,
                "event_name": event.event_name,
                "event_date": event.event_date.strftime("%Y-%m-%d %H:%M:%S"),
            }
            events_list.append(event_dict)

        return jsonify(events_list)

if __name__ == "__app__":
    app.run(host="0.0.0.0", port=5000, debug=True)
