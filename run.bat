@echo off

REM src 디렉토리로 이동
chcp 65001 > nul
cd srcs

REM 필요한 디렉토리 생성
mkdir data 2>nul

REM 도커 이미지 빌드
docker build -t web-link-extractor .

if %ERRORLEVEL% neq 0 (
    echo 도커 이미지 빌드 실패!
    goto :error
)

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

:error
echo.
echo 오류가 발생했습니다. 프로그램을 종료합니다.
exit /b 1
