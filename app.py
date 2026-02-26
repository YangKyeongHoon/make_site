from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    projects = [
        {
            'title': 'Gemini CLI와 함께 만든 포트폴리오 사이트 🤖',
            'description': 'Gemini CLI와 대화하며 단계별로 구축한 파이썬 Flask 기반의 개인 포트폴리오 웹사이트입니다. 프로젝트 요구사항 분석부터 파일 생성, 코드 작성, 동적 데이터 바인딩, 그리고 기본적인 디자인 적용까지 전 과정을 함께 진행했습니다.',
            'tech_stack': ['Python', 'Flask', 'HTML', 'CSS', 'Jinja2'],
            'image_url': 'https://via.placeholder.com/300x180?text=Gemini+CLI+Project', # 이 프로젝트의 스크린샷 등으로 변경해주세요!
            'link': '#' # 나중에 이 포트폴리오 사이트의 GitHub 저장소 링크로 변경해주세요!
        },
        {
            'title': '프로젝트 1 제목 🌟',
            'description': '이 프로젝트는 제가 [해결하고자 했던 문제]를 [사용한 기술]을 활용하여 해결한 경험을 담고 있습니다. 사용자 경험 개선에 중점을 두었으며, [구체적인 성과나 기능]을 달성했습니다!',
            'tech_stack': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript'],
            'image_url': 'https://via.placeholder.com/300x180?text=Project+1+Image', # 실제 프로젝트 이미지 URL로 변경해주세요!
            'link': 'https://github.com/yourusername/project1' # 실제 프로젝트 GitHub 또는 데모 링크로 변경해주세요!
        },
        {
            'title': '프로젝트 2 제목 🚀',
            'description': '두 번째 프로젝트는 [아이디어]를 기반으로 [사용 기술]을 적용하여 개발했습니다. 특히 [어려웠던 점이나 도전]을 극복하며 [배운 점]이 많습니다. [주요 기능]을 구현하여 [결과]를 얻었습니다.',
            'tech_stack': ['Python', 'Django', 'PostgreSQL', 'Docker'],
            'image_url': 'https://via.placeholder.com/300x180?text=Project+2+Image', # 실제 프로젝트 이미지 URL로 변경해주세요!
            'link': 'https://github.com/yourusername/project2' # 실제 프로젝트 GitHub 또는 데모 링크로 변경해주세요!
        },
        # 여기에 더 많은 프로젝트를 추가할 수 있어요! 😊
        {
            'title': '프로젝트 3 제목 💡',
            'description': '이 프로젝트는 [주제]에 대한 깊은 탐구와 [새로운 기술] 적용의 결과물입니다. [차별점]을 통해 [어떤 가치]를 제공하고자 했습니다. 코드를 통해 [구현 디테일]을 확인해보세요.',
            'tech_stack': ['JavaScript', 'React', 'Node.js', 'MongoDB'],
            'image_url': 'https://via.placeholder.com/300x180?text=Project+3+Image', # 실제 프로젝트 이미지 URL로 변경해주세요!
            'link': 'https://github.com/yourusername/project3' # 실제 프로젝트 GitHub 또는 데모 링크로 변경해주세요!
        }
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
