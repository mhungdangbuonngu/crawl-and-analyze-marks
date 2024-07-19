import requests
import csv
import time
csv_headers=['sbd','Toan','Van','NgoaiNgu','VatLy','HoaHoc','SinhHoc','TBKHTN', 'LichSu', 'DiaLy', 'GDCD', 'TBKHXH']
with open('diemThiHaNoi.csv','w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(csv_headers)
    for x in range(1000001 , 1108573):
        formatted_x = str(x).zfill(8)
        scraping_url='https://dantri.com.vn/thpt/1/0/99/'+ str(formatted_x) +'/2024/0.2/search-gradle.htm'
        payload={}
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response=requests.request("GET",scraping_url,headers=headers,data=payload)
        success = False
        for attempt in range(3):
            try:
                info = response.json()['student']
                if info:
                    diem = [info['sbd'],info['toan'],info['van'],info['ngoaiNgu'],info['vatLy'],info['hoaHoc'],info['sinhHoc'],info['diemTBTuNhien'],info['lichSu'],info['diaLy'],info['gdcd'],info['diemTBXaHoi']]
                    writer.writerow(diem)
                    print(f'insert mark for {formatted_x}')
                    success = True
                    break
                else:
                    print(f'no student found {formatted_x}')
                    success = True  # No retry needed if no data is found
                    break
            except (requests.RequestException, ValueError) as e:
                print(f"Attempt {attempt + 1} failed for SBD {formatted_x}: {e}")
                time.sleep(2)  # Wait before retrying
        if not success:
            print(f"Failed to retrieve data for SBD {formatted_x} after 3 attempts")
        time.sleep(0.05)  # Add a delay between requests to avoid rate limiting
f.close()