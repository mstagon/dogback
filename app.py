from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from flask_restx import Api, Resource, reqparse
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)
api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
Chat = api.namespace('chat', description='조회 API')
CORS(app)

# 파라미터 파서 정의
parser = reqparse.RequestParser()
parser.add_argument('prompt', type=str, required=True, help='사용자 입력 문장')

api_key = "sk-JafbVlxwrOV0omSRqtUkT3BlbkFJKRMsktenjno3CJqxpuM5S"
openai.api_key = api_key

keyword_responses = {
    '네이버커넥트재단': '네이버 커넥트재단의 채용공고 정보를 캘린터에 등록하였습니다.  기간 ~10-13',
    'LG전자': 'LG전자의 채용공고 정보를 캘린터에 등록하였습니다.  기간 ~10-23',
}

nc = {
    'title': '네이버 커넥트재단', 'start': '2023-09-23', 'end': '2023-10-13', 'color': '#111111', 'url': 'https://apply.connect.or.kr/connect/applyDetail?annoId=20009534',
}

lg = {
    'title': 'LG전자', 'start': '2023-09-23', 'end': '2023-10-23', 'color': '#111111', 'url': 'https://www.lge.co.kr"',
}

keyword_responsesdetial = {
    '네이버커넥트재단': nc,
    'LG전자': lg,
}


@Chat.route('/', methods=['POST'])
class Chatbot(Resource):
    @Chat.doc(params={'prompt': '사용자 입력 문장'})
    @Chat.response(200, '성공')
    @Chat.response(400, '잘못된 요청')
    def post(self):
        try:
            args = parser.parse_args()
            content = args['prompt']
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "너는 지금부터 입력한 취업 자소서에 첨삭을 해줘"},
                    {"role": "user", "content": content},
                ],
                temperature=0,
                max_tokens=2048
            )

            chatbot_response = response.choices[0].text.strip()

            result = {
                'content': chatbot_response
            }

            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)})


@Chat.route('/modify/', methods=['GET', 'POST'])
class Modify(Resource):
    @Chat.doc(params={'prompt': '사용자 입력 문장'})
    @Chat.response(200, '성공')
    @Chat.response(400, '잘못된 요청')
    def post(self):
        try:
            args = parser.parse_args()
            content = args['prompt']
            # 사용자 입력에서 키워드 추출
            matched_keyword = content

            matched_keywords = [keyword for keyword in keyword_responses.keys() if keyword in content]

            if matched_keywords:
                # 가장 먼저 매칭된 키워드를 사용하여 답변 및 이벤트 검색
                matched_keyword = matched_keywords[0]
                response = keyword_responses[matched_keyword]
                responsedate = keyword_responsesdetial.get(matched_keyword, "null")
            else:
                # 매칭된 키워드가 없을 경우 기본 응답 반환
                response = '죄송합니다. 이해하지 못했습니다.'
                responsedate = "null"

            result = {
                'content': response,
                'event': responsedate
            }
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=False)
