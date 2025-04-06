#!/bin/bash

# 필요한 디렉토리 생성
mkdir -p data

# 도커 이미지 빌드
docker build -t web-link-extractor .

# 스크립트 실행 도움말
echo "웹 링크 추출기 실행 준비가 완료되었습니다."
echo ""
echo "사용 예시:"
echo "1. 웹 URL에서 링크 추출:"
echo "   docker run -v \$(pwd)/data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv"
echo ""
echo "2. 로컬 HTML 파일에서 링크 추출 (data/samples 디렉토리 내 파일):"
echo "   docker run -v \$(pwd)/data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv"
echo ""
echo "도움말 보기:"
echo "   docker run web-link-extractor --help"
