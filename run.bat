@echo off

REM src 디렉토리로 이동
cd src

REM 필요한 디렉토리 생성
mkdir data 2>nul

REM 도커 이미지 빌드
docker build -t web-link-extractor .

REM 스크립트 실행 도움말
echo 웹 링크 추출기 실행 준비가 완료되었습니다.
echo.
echo 사용 예시:
echo 1. 웹 URL에서 링크 추출:
echo    docker run -v .\data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv
echo.
echo 2. 로컬 HTML 파일에서 링크 추출 (src/data/samples 디렉토리 내 파일):
echo    docker run -v .\data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv
echo.
echo 도움말 보기:
echo    docker run web-link-extractor --help

REM 메인 디렉토리로 돌아가기 (필요한 경우)
cd ..
