# WebLinkExtractor

WebLinkExtractor는 웹페이지나 로컬 HTML 파일에서 외부 링크를 추출하는 파이썬 도구입니다. 이 도구는 다양한 소스에서 링크를 수집하여 CSV 형식으로 저장합니다.

## 특징

- **다양한 소스 지원**: 웹 URL 또는 로컬 HTML 파일에서 링크 추출
- **필터링 기능**: `javascript:void(0)` 링크와 내부 앵커 링크(#)는 자동으로 제외
- **상대 URL 변환**: 상대 경로를 자동으로 절대 URL로 변환
- **스크립트 태그 검색**: `<a>` 태그뿐만 아니라 스크립트 내의 URL도 추출
- **CSV 출력**: 모든 링크를 구조화된 CSV 형식으로 저장

## 설치

```bash
# 저장소 복제
git clone https://github.com/yourusername/WebLinkExtractor.git
cd WebLinkExtractor

# 필요한 라이브러리 설치
pip install -r requirements.txt
```

## 사용법

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

### 사용 예시

#### 웹 URL에서 링크 추출

```bash
python link-extractor.py --url https://example.com
```

#### 로컬 HTML 파일에서 링크 추출

```bash
python link-extractor.py --directory ./samples/ --base-url https://example.com
```

#### 출력 파일 지정

```bash
python link-extractor.py --url https://example.com --output links.csv
```

#### 웹 URL과 로컬 파일 모두에서 추출

```bash
python link-extractor.py --url https://example.com --directory ./samples/ --output combined_links.csv
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

## 요구 사항

- Python 3.6 이상
- BeautifulSoup4
- Pandas
- Requests

## 주의 사항

- 너무 많은 요청을 빠르게 보내면 일부 웹사이트에서 IP가 차단될 수 있습니다.
- 모든 웹사이트의 이용약관을 준수하세요.
- 대규모 크롤링 작업에는 적절한 딜레이를 추가하는 것을 고려하세요.

## 라이선스

MIT License
