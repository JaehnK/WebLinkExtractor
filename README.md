# Docker로 WebLinkExtractor 실행하기

이 가이드는 Python 환경이 설치되어 있지 않은 시스템에서도 Docker를 사용하여 WebLinkExtractor를 실행하는 방법을 설명합니다.

## 사전 요구사항

- Docker 설치 ([Docker 설치 가이드](https://docs.docker.com/get-docker/))
- Docker Compose 설치 (선택 사항, [Docker Compose 설치 가이드](https://docs.docker.com/compose/install/))

## 빠른 시작

### 1. 도커 이미지 빌드

```bash
docker build -t web-link-extractor .
```

### 2. 도커 컨테이너 실행

#### 웹 URL에서 링크 추출

```bash
docker run -v $(pwd)/data:/app/data web-link-extractor --url https://example.com --output /app/data/links.csv
```

#### 로컬 HTML 파일에서 링크 추출
먼저 HTML 파일을 `data` 디렉토리에 복사한 후 다음 명령어를 실행합니다:

```bash
docker run -v $(pwd)/data:/app/data web-link-extractor --directory /app/data/samples --output /app/data/links.csv
```

## Docker Compose 사용하기

더 간편한 사용을 위해 Docker Compose를 활용할 수 있습니다.

### docker-compose.yml 수정

`docker-compose.yml` 파일의 `command` 부분을 필요에 맞게 수정하세요:

```yaml
command: --url https://example.com --output /app/data/links.csv
```

### 실행

```bash
docker-compose up
```

## 팁과 주의사항

1. **데이터 디렉토리 관리**
   - `data` 디렉토리는 컨테이너와 호스트 시스템 간에 공유됩니다.
   - 결과물인 CSV 파일은 `data` 디렉토리에 저장됩니다.
   - HTML 파일을 분석하려면 `data` 디렉토리 내에 배치해야 합니다.

2. **경로 참조**
   - 컨테이너 내에서 모든 경로는 `/app/data/`로 시작합니다.
   - 예: 호스트의 `./data/samples` 디렉토리는 컨테이너 내에서 `/app/data/samples`입니다.

3. **권한 문제**
   - 권한 문제가 발생하면 다음 명령어로 데이터 디렉토리의 권한을 조정하세요:
     ```bash
     mkdir -p data
     chmod 777 data
     ```

## 명령어 예시

### 단일 웹페이지 분석

```bash
docker run -v $(pwd)/data:/app/data web-link-extractor --url https://example.com --output /app/data/example_links.csv
```

### 여러 HTML 파일 분석

```bash
docker run -v $(pwd)/data:/app/data web-link-extractor --directory /app/data/html_files --base-url https://example.com --output /app/data/batch_links.csv
```

### 웹페이지와 로컬 파일 모두 분석

```bash
docker run -v $(pwd)/data:/app/data web-link-extractor --url https://example.com --directory /app/data/html_files --output /app/data/combined_links.csv
```