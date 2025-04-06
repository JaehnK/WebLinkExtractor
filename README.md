# WebLinkExtractor

WebLinkExtractor는 웹페이지나 로컬 HTML 파일에서 외부 링크를 추출하는 도구입니다. Docker 이미지로 패키징되어 Python 환경 설정 없이도 어떤 시스템에서든 쉽게 실행할 수 있습니다.

## 특징

- **다양한 소스 지원**: 웹 URL 또는 로컬 HTML 파일에서 링크 추출
- **필터링 기능**: `javascript:void(0)` 링크와 내부 앵커 링크(#)는 자동으로 제외
- **상대 URL 변환**: 상대 경로를 자동으로 절대 URL로 변환
- **스크립트 태그 검색**: `<a>` 태그뿐만 아니라 스크립트 내의 URL도 추출
- **CSV 출력**: 모든 링크를 구조화된 CSV 형식으로 저장
- **Docker 기반**: Python 설치 없이 어디서나 실행 가능

## 설치 및 실행

### 사전 요구사항

- [Docker](https://www.docker.com/get-started) 설치

### 빠른 시작

1. **저장소 복제**

```bash
git clone https://github.com/yourusername/WebLinkExtractor.git
cd WebLinkExtractor
```

2. **도커 이미지 빌드**

```bash
docker build -t web-link-extractor .
```

3. **데이터 디렉토리 생성**

```bash
mkdir -p data
```

## 사용 방법

### Linux/macOS에서 실행

#### 웹 URL에서 링크 추출

```bash
docker run -v ./data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv
```

#### 로컬 HTML 파일에서 링크 추출
먼저 HTML 파일을 `data` 디렉토리에 복사한 후:

```bash
docker run -v ./data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv
```

### Windows에서 실행

#### 명령 프롬프트(CMD)

```cmd
# 웹 URL에서 링크 추출
docker run -v .\data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv

# 로컬 HTML 파일에서 링크 추출
docker run -v .\data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv
```

#### PowerShell

```powershell
# 웹 URL에서 링크 추출
docker run -v ${PWD}/data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv

# 로컬 HTML 파일에서 링크 추출
docker run -v ${PWD}/data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv
```

### 명령행 옵션

```
usage: link-extractor.py [-h] [--url URL] [--directory DIRECTORY] [--base-url BASE_URL] [--output OUTPUT]

웹페이지에서 링크를 추출하는 도구

options:
  -h, --help            도움말 표시
  --url URL             링크를 추출할 웹페이지 URL
  --directory DIRECTORY HTML 파일이 있는 디렉토리 경로
  --base-url BASE_URL   상대 URL을 절대 URL로 변환할 때 사용할 기본 URL
  --output OUTPUT       결과를 저장할 CSV 파일명 (기본값: 타임스탬프 포함 자동 생성)
```

## Docker Compose 사용하기

더 간편한 사용을 위해 Docker Compose를 활용할 수 있습니다.

1. **docker-compose.yml 수정**

```yaml
version: '3'

services:
  web-link-extractor:
    build: .
    volumes:
      - ./data:/app/data
    command: --url https://example.com --output /app/data/links.csv
```

2. **실행**

```bash
docker-compose up
```

## 출력 형식

스크립트는 다음 열이 포함된 CSV 파일을 생성합니다:

- `source`: 링크의 출처 (URL 또는 파일명)
- `url`: 추출된 URL

예시 출력:
```
source,url
https://example.com,https://example.org/page1
https://example.com,https://example.org/page2
sample.html,https://example.org/page3
```

## 문제 해결

### Docker 관련 일반적인 문제

1. **대문자 경로 문제**
   
   Docker 볼륨 마운트 시 경로에 대문자가 포함되어 있으면 오류가 발생할 수 있습니다.
   ```
   docker: invalid reference format: repository name must be lowercase.
   ```
   
   해결책: 상대 경로 사용
   ```bash
   # 이렇게 사용
   docker run -v ./data:/app/data web-link-extractor ...
   
   # 이렇게 사용하지 마세요
   docker run -v $(pwd)/data:/app/data web-link-extractor ...
   ```

2. **권한 문제**
   
   Linux/macOS에서 결과 파일 권한 문제가 발생할 수 있습니다.
   
   해결책:
   ```bash
   mkdir -p data
   chmod 777 data
   ```

3. **Docker 명령이 인식되지 않는 경우**
   
   Docker가 설치되어 있고 올바르게 실행되고 있는지 확인하세요:
   ```bash
   docker --version
   ```

## 주의 사항

- 너무 많은 요청을 빠르게 보내면 일부 웹사이트에서 IP가 차단될 수 있습니다.
- 모든 웹사이트의 이용약관을 준수하세요.
- 대규모 크롤링 작업에는 적절한 딜레이를 추가하는 것을 고려하세요.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 제공됩니다.