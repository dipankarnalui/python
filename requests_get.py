import requests
URL="https://vbn.crashportal.ccp.xcal.tv/direct/getAllMiniDumpDetails?mac=D40AA91BB102&ng_startTime=11/23/2018%2000:00&ng_endTime=11/23/2018%2023:00"
content=requests.get(URL)
print(content.text)
