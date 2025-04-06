FROM python:3.9-slim

WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 복사
COPY link-extractor.py .

# 볼륨 마운트 포인트 생성 (출력 CSV 파일 및 입력 HTML 파일용)
VOLUME /app/data

# 컨테이너 실행 시 기본 명령어 설정
ENTRYPOINT ["python", "link-extractor.py"]

# 기본 인자 (도움말 표시)
CMD ["--help"]
