#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup 
from time import time, localtime, strftime
import pandas as pd
import re
import os
import urllib.parse
import requests
import argparse

def extract_links(file_path, base_url=None):
    """
    HTML 파일에서 모든 링크를 추출하는 함수
    
    Parameters:
    file_path (str): HTML 파일 경로
    base_url (str, optional): 상대 URL을 절대 URL로 변환할 때 사용할 기본 URL
    
    Returns:
    list: 추출된 유효한 링크 목록
    """
    try:
        # HTML 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            page = file.read()
        
        # BeautifulSoup으로 파싱
        soup = BeautifulSoup(page, 'html.parser')
        
        # 모든 a 태그에서 href 속성 추출
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href'].strip()
            
            # javascript:void(0) 링크 제외
            if href.startswith('javascript:void'):
                continue
                
            # 빈 링크 제외
            if not href or href == '#':
                continue
                
            # 내부 링크 확인 (절대 경로가 아닌 상대 경로이면서 #으로 시작하는 경우)
            if href.startswith('#'):
                continue
                
            # 상대 URL을 절대 URL로 변환
            if base_url and not (href.startswith('http://') or href.startswith('https://')):
                href = urllib.parse.urljoin(base_url, href)
                
            links.append(href)
        
        # 스크립트 태그에서도 URL 추출 (선택적)
        for script in soup.find_all('script'):
            script_text = script.get_text()
            # URL 추출 패턴 (http 또는 https로 시작하는 URL)
            urls = re.findall(r'https?://[^\s\'"\)\}]+', script_text)
            for url in urls:
                if url not in links:
                    links.append(url)
        
        # 중복 제거 및 정렬
        unique_links = sorted(list(set(links)))
        
        return unique_links
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return []

def process_directory(directory_path, base_url=None):
    """
    디렉토리 내 모든 HTML 파일에서 링크를 추출하여 DataFrame으로 반환
    
    Parameters:
    directory_path (str): HTML 파일이 있는 디렉토리 경로
    base_url (str, optional): 상대 URL을 절대 URL로 변환할 때 사용할 기본 URL
    
    Returns:
    pandas.DataFrame: 파일명과 추출된 링크를 포함하는 DataFrame
    """
    results = []
    
    # 디렉토리 내 파일 목록 가져오기
    file_list = os.listdir(directory_path)
    
    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        
        # HTML 파일만 처리
        if file_name.lower().endswith(('.html', '.htm')):
            print(f"Processing: {file_name}")
            
            # 링크 추출
            links = extract_links(file_path, base_url)
            
            # 결과에 추가
            for link in links:
                results.append({
                    'file_name': file_name,
                    'url': link
                })
    
    # DataFrame 생성
    if results:
        df = pd.DataFrame(results)
        return df
    else:
        return pd.DataFrame(columns=['file_name', 'url'])

def extract_links_from_url(url):
    """
    웹 URL에서 직접 링크를 추출하는 함수
    
    Parameters:
    url (str): 링크를 추출할 웹페이지 URL
    
    Returns:
    list: 추출된 유효한 링크 목록
    """
    import requests
    from urllib.parse import urlparse
    
    try:
        # URL에서 기본 도메인 추출
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        # 웹페이지 가져오기
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # HTTP 에러 발생시 예외 발생
        
        # BeautifulSoup으로 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 모든 a 태그에서 href 속성 추출
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href'].strip()
            
            # javascript:void(0) 링크 제외
            if href.startswith('javascript:void'):
                continue
                
            # 빈 링크 제외
            if not href or href == '#':
                continue
                
            # 내부 링크 확인 (절대 경로가 아닌 상대 경로이면서 #으로 시작하는 경우)
            if href.startswith('#'):
                continue
                
            # 상대 URL을 절대 URL로 변환
            if (href.startswith('http://') or href.startswith('https://')):
                links.append(href)
        
        # 스크립트 태그에서도 URL 추출 (선택적)
        for script in soup.find_all('script'):
            script_text = script.get_text()
            # URL 추출 패턴 (http 또는 https로 시작하는 URL)
            urls = re.findall(r'https?://[^\s\'"\)\}]+', script_text)
            for url in urls:
                if url not in links:
                    links.append(url)
        
        # 중복 제거 및 정렬
        unique_links = sorted(list(set(links)))
        
        return unique_links
    
    except Exception as e:
        print(f"Error processing URL {url}: {str(e)}")
        return []

def main():
    import argparse
    
    # 명령행 인자 파싱
    parser = argparse.ArgumentParser(description='웹페이지에서 링크를 추출하는 도구')
    parser.add_argument('--url', help='링크를 추출할 웹페이지 URL')
    parser.add_argument('--directory', help='HTML 파일이 있는 디렉토리 경로')
    parser.add_argument('--base-url', help='상대 URL을 절대 URL로 변환할 때 사용할 기본 URL')
    parser.add_argument('--output', help='결과를 저장할 CSV 파일명 (기본값: 타임스탬프 포함 자동 생성)')
    
    args = parser.parse_args()
    
    # 결과를 저장할 DataFrame 초기화
    df = pd.DataFrame(columns=['source', 'url'])
    
    # URL에서 링크 추출
    if args.url:
        print(f"URL에서 링크 추출 중: {args.url}")
        links = extract_links_from_url(args.url)
        
        if links:
            url_df = pd.DataFrame({
                'source': [args.url] * len(links),
                'url': links
            })
            df = pd.concat([df, url_df], ignore_index=True)
    
    # 디렉토리에서 링크 추출
    if args.directory:
        print(f"디렉토리에서 링크 추출 중: {args.directory}")
        directory_path = args.directory
        base_url = args.base_url
        
        # 디렉토리 내 모든 HTML 파일에서 링크 추출
        file_list = os.listdir(directory_path)
        
        for file_name in file_list:
            file_path = os.path.join(directory_path, file_name)
            
            # HTML 파일만 처리
            if file_name.lower().endswith(('.html', '.htm')):
                print(f"  처리 중: {file_name}")
                
                # 링크 추출
                links = extract_links(file_path, base_url)
                
                # 결과에 추가
                if links:
                    file_df = pd.DataFrame({
                        'source': [file_name] * len(links),
                        'url': links
                    })
                    df = pd.concat([df, file_df], ignore_index=True)
    
    # URL이나 디렉토리 중 하나는 제공해야 함
    if not args.url and not args.directory:
        parser.print_help()
        print("\n에러: URL이나 디렉토리 중 하나는 제공해야 합니다.")
        return
    
    # 결과 저장
    if not df.empty:
        if args.output:
            csv_filename = args.output
        else:
            timestamp = strftime('%Y%m%d_%H%M%S', localtime(time()))
            csv_filename = f'/app/data/extracted_links_{timestamp}.csv'
        
        df.to_csv(csv_filename, index=False)
        print(f"링크 추출 완료: {len(df)} 개의 링크를 '{csv_filename}'에 저장했습니다.")
    else:
        print("추출된 링크가 없습니다.")

if __name__ == "__main__":
    main()
