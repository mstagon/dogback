

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

# OpenAI GPT-3 API 키 설정
# api_key = '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'
api_key = "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"
openai.api_key = api_key


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
                engine="gpt-3.5-turbo",  # GPT-3 엔진 선택
                messages=[
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


@Chat.route('/crawl', methods=['GET'])
class GetExample(Resource):
    @Chat.response(200, '성공')
    def get(self):

        try:
            html_code = """
               <div className="ListTable-mobile__StyledWrapper-sc-1377b965-0 kFdvKq">
    <div className="AdRecruitInternMobile__StyledWrapper-sc-7c0db175-0 cuUNBC">
        <div className="inter-mo-ad-wrapper">
            <div className="MuiBox-root jss205 jss201">
                <div className="MuiBox-root jss206"><span
                    className="MuiSkeleton-root MuiSkeleton-rect MuiSkeleton-pulse"
                    style="width: 60px; height: 60px;"></span></div>
                <div className="MuiBox-root jss207">
                    <div className="MuiBox-root jss208">
                        <div className="MuiBox-root jss209"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                            style="width: 100px;"></span></div>
                        <div className="MuiBox-root jss210"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"></span></div>
                        <div className="MuiBox-root jss211">
                            <div className="MuiBox-root jss212"><span
                                className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                style="width: 40px;"></span></div>
                            <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                  style="width: 40px;"></span></div>
                    </div>
                    <div className="MuiBox-root jss213">
                        <button className="MuiButtonBase-root MuiIconButton-root jss202" tabIndex="0" type="button">
                            <span className="MuiIconButton-label"><svg className="MuiSvgIcon-root jss203"
                                                                       focusable="false" viewBox="0 0 12 16"
                                                                       aria-hidden="true"
                                                                       xmlns="http://www.w3.org/2000/svg" width="12"
                                                                       height="16" aria-label="스크랩"><title>스크랩</title><path
                                fill="currentColor"
                                d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg>,</span>
                        </button>
                        <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                              style="width: 20px; margin: auto;"></span></div>
                </div>
            </div>
            <hr className="MuiDivider-root jss204">
                <div id="linkareer-google-ad-manager-RECRUIT_MO_1"
                     className="main-banner-ad GoogleAdManagerSlot__StyledAdDiv-sc-db9040af-0 gXKKgM"
                     data-is-loaded="false"></div>
        </div>
        <hr className="MuiDivider-root divider">
    </div>
    <div className="AdRecruitInternMobile__StyledWrapper-sc-7c0db175-0 cuUNBC">
        <div className="inter-mo-ad-wrapper">
            <div className="MuiBox-root jss214 jss201">
                <div className="MuiBox-root jss215"><span
                    className="MuiSkeleton-root MuiSkeleton-rect MuiSkeleton-pulse"
                    style="width: 60px; height: 60px;"></span></div>
                <div className="MuiBox-root jss216">
                    <div className="MuiBox-root jss217">
                        <div className="MuiBox-root jss218"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                            style="width: 100px;"></span></div>
                        <div className="MuiBox-root jss219"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"></span></div>
                        <div className="MuiBox-root jss220">
                            <div className="MuiBox-root jss221"><span
                                className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                style="width: 40px;"></span></div>
                            <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                  style="width: 40px;"></span></div>
                    </div>
                    <div className="MuiBox-root jss222">
                        <button className="MuiButtonBase-root MuiIconButton-root jss202" tabIndex="0" type="button">
                            <span className="MuiIconButton-label"><svg className="MuiSvgIcon-root jss203"
                                                                       focusable="false" viewBox="0 0 12 16"
                                                                       aria-hidden="true"
                                                                       xmlns="http://www.w3.org/2000/svg" width="12"
                                                                       height="16" aria-label="스크랩"><title>스크랩</title><path
                                fill="currentColor"
                                d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg>,</span>
                        </button>
                        <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                              style="width: 20px; margin: auto;"></span></div>
                </div>
            </div>
            <hr className="MuiDivider-root jss204">
                <div id="linkareer-google-ad-manager-RECRUIT_MO_2"
                     className="main-banner-ad GoogleAdManagerSlot__StyledAdDiv-sc-db9040af-0 gXKKgM"
                     data-is-loaded="false"></div>
        </div>
        <hr className="MuiDivider-root divider">
    </div>
    <div className="AdRecruitInternMobile__StyledWrapper-sc-7c0db175-0 cuUNBC">
        <div className="inter-mo-ad-wrapper">
            <div id="linkareer-google-ad-manager-RECRUIT_MO_3"
                 className="main-banner-ad GoogleAdManagerSlot__StyledAdDiv-sc-db9040af-0 gXKKgM" data-is-loaded="true"
                 data-google-query-id="CMCS_u2DwIEDFRXXFgUdo7wHhg">
                <div id="google_ads_iframe_/22903531815/prod_mo_web_recruit_3_20230531_0__container__"
                     style="border: 0pt none; display: inline-block; width: 790px; height: 94px;">
                    <iframe frameBorder="0"
                            src="https://fce61c574cef13d73edf774eb1b7b5fe.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html"
                            id="google_ads_iframe_/22903531815/prod_mo_web_recruit_3_20230531_0"
                            title="3rd party ad content" name="" scrolling="no" marginWidth="0" marginHeight="0"
                            width="790" height="94" data-is-safeframe="true"
                            sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation"
                            allow="attribution-reporting" role="region" aria-label="Advertisement" tabIndex="0"
                            data-google-container-id="7" style="border: 0px; vertical-align: bottom;"
                            data-load-complete="true"></iframe>
                </div>
            </div>
            <div className="bookmark">
                <button className="MuiButtonBase-root MuiIconButton-root scrap-button" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">46</p>
            </div>
        </div>
        <hr className="MuiDivider-root divider">
    </div>
    <div className="AdRecruitInternMobile__StyledWrapper-sc-7c0db175-0 cuUNBC">
        <div className="inter-mo-ad-wrapper">
            <div className="MuiBox-root jss232 jss201">
                <div className="MuiBox-root jss233"><span
                    className="MuiSkeleton-root MuiSkeleton-rect MuiSkeleton-pulse"
                    style="width: 60px; height: 60px;"></span></div>
                <div className="MuiBox-root jss234">
                    <div className="MuiBox-root jss235">
                        <div className="MuiBox-root jss236"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                            style="width: 100px;"></span></div>
                        <div className="MuiBox-root jss237"><span
                            className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"></span></div>
                        <div className="MuiBox-root jss238">
                            <div className="MuiBox-root jss239"><span
                                className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                style="width: 40px;"></span></div>
                            <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                                  style="width: 40px;"></span></div>
                    </div>
                    <div className="MuiBox-root jss240">
                        <button className="MuiButtonBase-root MuiIconButton-root jss202" tabIndex="0" type="button">
                            <span className="MuiIconButton-label"><svg className="MuiSvgIcon-root jss203"
                                                                       focusable="false" viewBox="0 0 12 16"
                                                                       aria-hidden="true"
                                                                       xmlns="http://www.w3.org/2000/svg" width="12"
                                                                       height="16" aria-label="스크랩"><title>스크랩</title><path
                                fill="currentColor"
                                d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg>,</span>
                        </button>
                        <span className="MuiSkeleton-root MuiSkeleton-text MuiSkeleton-pulse"
                              style="width: 20px; margin: auto;"></span></div>
                </div>
            </div>
            <hr className="MuiDivider-root jss204">
                <div id="linkareer-google-ad-manager-RECRUIT_MO_4"
                     className="main-banner-ad GoogleAdManagerSlot__StyledAdDiv-sc-db9040af-0 gXKKgM"
                     data-is-loaded="false"></div>
        </div>
        <hr className="MuiDivider-root divider">
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152727">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[AIA생명] 특별계정팀 인턴"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278651"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">AIA생명</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152727"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[AIA생명]
                    특별계정팀 인턴</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">인턴</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">채용시마감</p>
                        <p className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                            133</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">5</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152726">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[SIA] 인공지능연구소 인턴"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278649"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">SIA</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152726"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[SIA]
                    인공지능연구소 인턴</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">인턴</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        09.29</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        121</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152725">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[㈜희성화학] 재경팀 회계/기획, 구매영업팀 구매담당 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278648"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">희성화학</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152725"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[㈜희성화학] 재경팀
                    회계/기획, 구매영업팀 구매담당 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        11.12</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        26</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152724">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[스템코] 2023년 9월 환경부문 신입 채용 (환경시설운영, 고졸)"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278647"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">스템코</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152724"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[스템코] 2023년
                    9월 환경부문 신입 채용 (환경시설운영, 고졸)</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.09</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        35</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152723">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[단군소프트] 2023년 9월 각 분야별 신입 및 경력사원 수시채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278646"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">단군소프트</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152723"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[단군소프트]
                    2023년 9월 각 분야별 신입 및 경력사원 수시채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.02</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        33</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152721">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[씨젠의료재단] 2023년도 하반기 (재)씨젠의료재단 사업부문 우수인재 공채(추가 모집)"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278636"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">씨젠의료재단</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152721"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[씨젠의료재단]
                    2023년도 하반기 (재)씨젠의료재단 사업부문 우수인재 공채(추가 모집)</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">인턴</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.03</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        89</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152720">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[앱솔브랩] 글로벌팀 미국 마케팅 채용우대형 인턴 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278635"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">앱솔브랩</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152720"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[앱솔브랩] 글로벌팀
                    미국 마케팅 채용우대형 인턴 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">인턴</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.19</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        114</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">6</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152719">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[앱솔브랩] 글로벌팀 일본 마케팅 체험형 인턴 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278631"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">앱솔브랩</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152719"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[앱솔브랩] 글로벌팀
                    일본 마케팅 체험형 인턴 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">인턴</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.19</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        35</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152718">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[(주)코리아나화장품] 생산관리(신입/경력-고졸/초대졸-천안) 모집"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278630"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">코리아나화장품</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152718"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[(주)코리아나화장품]
                    생산관리(신입/경력-고졸/초대졸-천안) 모집</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.05</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        22</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152717">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[(주)코리아나화장품] 공무기술직(신입/경력-고졸이상-천안) 모집"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278629"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">코리아나화장품</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152717"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[(주)코리아나화장품]
                    공무기술직(신입/경력-고졸이상-천안) 모집</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.05</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        13</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152712">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[HD현대이엔티] 2023년 3/4분기 3차 신입 및 경력사원 모집"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278614"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">HD현대이엔티</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152712"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[HD현대이엔티]
                    2023년 3/4분기 3차 신입 및 경력사원 모집</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        09.26</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        193</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152711">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[SSG.COM] 냉동제조시설 안전관리자 모집"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278613"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">SSG</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152711"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[SSG.COM]
                    냉동제조시설 안전관리자 모집</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        09.29</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        42</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152710">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[㈜천재교육] 부문별 인재 모집"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278612"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">천재교육</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152710"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[㈜천재교육] 부문별
                    인재 모집</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.05</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        65</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152709">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[㈜태룡건설] 2023년 개발사업 신입 및 경력사원 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278611"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">태룡건설</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152709"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[㈜태룡건설]
                    2023년 개발사업 신입 및 경력사원 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.03</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        29</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152708">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[한림제약] 재경팀 신입사원 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278610"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">한림제약</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152708"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[한림제약] 재경팀
                    신입사원 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.06</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        26</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152706">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[SK네트웍스] 워커힐 기계설비 유지보수 및 고압가스 냉동제조시설 관리 신입사원 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278601"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">SK네트웍스</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152706"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[SK네트웍스] 워커힐
                    기계설비 유지보수 및 고압가스 냉동제조시설 관리 신입사원 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.12</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        41</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">1</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152705">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[한진] (주)한진 물류전문직(초대졸) 신입 안전/보건관리자 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278600"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">한진</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152705"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[한진] (주)한진
                    물류전문직(초대졸) 신입 안전/보건관리자 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.15</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        64</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152704">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[한국전자금융] 2023년 한국전자금융(주) 신입사원 공개채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278599"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">한국전자금융</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152704"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[한국전자금융]
                    2023년 한국전자금융(주) 신입사원 공개채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.06</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        89</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">2</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152703">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[에어코리아] 여객운송직 채용(부산)"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278598"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">에어코리아</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152703"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[에어코리아]
                    여객운송직 채용(부산)</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">상시채용</p>
                        <p className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                            55</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
    <div className="activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD"
         data-activityid="152702">
        <div className="img-wrapper">
            <div className="img-thumbnail SimpleImg__StyledWrapper-sc-48c08f3a-0 fseepS"><img data-is-ratio-equal="true"
                                                                                              width="60px" height="60px"
                                                                                              placeholder="white"
                                                                                              alt="[에이비엠] 2023년 하반기 신입 및 경력 채용"
                                                                                              src="https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50,w_60/https://api.linkareer.com/attachments/278597"
                                                                                              srcSet=""
                                                                                              style="opacity: 1;"></div>
        </div>
        <div className="recruit-content">
            <div className="content-wrapper">
                <div className="organization-wrapper">
                    <div>
                        <div className="container"><p
                            className="MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary"
                            style="cursor: default;">에이비엠</p></div>
                    </div>
                </div>
                <div className="recruit-title"><a className="link" href="/activity/152702"><p
                    className="MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary">[에이비엠] 2023년
                    하반기 신입 및 경력 채용</p></a></div>
                <div className="info-wrapper-recruit">
                    <div className="first-container">
                        <div className="job-type-container"><p
                            className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">신입</p>
                        </div>
                        <div className="category-container"><p
                            className="MuiTypography-root category MuiTypography-body1 MuiTypography-colorTextPrimary">각
                            부문</p></div>
                    </div>
                    <div className="second-container"><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">~
                        10.15</p><p
                        className="MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary">조회
                        38</p></div>
                </div>
            </div>
            <div className="scrap-container">
                <button className="MuiButtonBase-root MuiIconButton-root button-scrap" tabIndex="0" type="button"><span
                    className="MuiIconButton-label"><svg className="MuiSvgIcon-root icon-bookmark" focusable="false"
                                                         viewBox="0 0 12 16" aria-hidden="true"
                                                         xmlns="http://www.w3.org/2000/svg" width="12" height="16"
                                                         aria-label="스크랩"><title>스크랩</title><path fill="currentColor"
                                                                                                  d="M9.006 0H2.994A2.994 2.994 0 000 2.994V16l6-2.368L12 16V2.994A2.994 2.994 0 009.006 0z"></path></svg></span>
                </button>
                <p className="MuiTypography-root scrap-count MuiTypography-body1 MuiTypography-colorTextSecondary">0</p>
            </div>
        </div>
    </div>
</div>
            """
            soup = BeautifulSoup(html_code, 'html.parser')

            # 빈 리스트를 생성하여 데이터를 저장할 준비를 합니다.
            data = []

            # 모든 활동 항목을 찾습니다.
            activity_items = soup.find_all('div',
                                           class_='activity-list-item ActivityListItem-mobile__StyledWrapper-sc-88d1228a-0 kuskyD')

            # 각각의 활동에 대한 정보를 추출합니다.
            for item in activity_items:
                # 기업명 추출
                company_name = item.find('p',
                                         class_='MuiTypography-root organization-name MuiTypography-body1 MuiTypography-colorTextPrimary').text

                # 공고명 추출
                job_title = item.find('p',
                                      class_='MuiTypography-root title MuiTypography-body1 MuiTypography-colorTextPrimary').text

                # 마감 기한 추출
                deadline = item.find('p',
                                     class_='MuiTypography-root short-info-typo MuiTypography-body1 MuiTypography-colorTextPrimary',
                                     text='채용시마감').text

                # 추출한 데이터를 딕셔너리로 저장
                data.append({
                    '기업명': company_name,
                    '공고명': job_title,
                    '마감기한': deadline
                })

            # 추출한 데이터로 DataFrame 생성
            df = pd.DataFrame(data)
            result = df.to_json(orient='records', lines=True)
            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
