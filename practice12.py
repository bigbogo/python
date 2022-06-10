# https://pypi.org/search/
# pypi classifier
# Python 패키지 색인(PyPI)은 Python 프로그래밍 언어용 소프트웨어 저장소입니다.
# PyPI는 Python 커뮤니티에서 개발 및 공유하는 소프트웨어를 찾고 설치하는 데 도움이 됩니다
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())