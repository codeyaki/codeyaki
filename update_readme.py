import feedparser

somjang_blog_rss_url = "https://teching.tistory.com/rss"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"|{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday}|[{feed['title']}]({feed['link']})|\n"
    
markdown_text = f"""
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=300&section=header&text=Hello%20I'm%20Son" style="width:100%;">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F5onchangwoo&count_bg=%2379C83D&title_bg=%23000000&icon=octopusdeploy.svg&icon_color=%2350B218&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

안녕하세요. 백엔드 개발자 손창우입니다

#### **Contact Me**
  
  <img src="https://img.shields.io/badge/Gmail-EA4335?style=round-square&logo=Gmail&logoColor=white"/> <a> scw9410@gmail.com </a> <br/>
#### Blog
  <img src="https://img.shields.io/badge/Tistory-000000?style=round-square&logo=Tistory&logoColor=white"/> <a>https://teching.tistory.com</a> <br/>

<br/>
<br/>
  
### :hammer_and_wrench: **Used Tool & Skill**   
  
#### Skill
  
Language: 
<img src="https://img.shields.io/badge/JAVA-007396?style=round-square&logo=java&logoColor=white"> 
<img src="https://img.shields.io/badge/Python-3776AB?style=round-square&logo=Python&logoColor=white"> 
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=round-square&logo=JavaScript&logoColor=white"> <br/>

Database: 
<img src="https://img.shields.io/badge/oracle-F80000?style=round-square&logo=oracle&logoColor=white"> 
<img src="https://img.shields.io/badge/mysql-4479A1?style=round-square&logo=mysql&logoColor=white"> 
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=round-square&logo=PostgreSQL&logoColor=white"> <br/>
  
Persistence API:
<img src="https://img.shields.io/badge/mybatis-212121?style=round-square&logo=Mybatis&logoColor=white">
<img src="https://img.shields.io/badge/JPA(Hibernate)-59666C?style=round-square&logo=Hibernate&logoColor=white"> <br/>

Back-end: 
<img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=round-square&logo=Spring Boot&logoColor=white"> <br/>

Front-end: 
<img src="https://img.shields.io/badge/React-61DAFB?style=round-square&logo=React&logoColor=white"> <br/>

#### Tools
<img src="https://img.shields.io/badge/github-181717?style=round-square&logo=github&logoColor=white"> 
<img src="https://img.shields.io/badge/notion-000000?style=round-square&logo=Notion&logoColor=white"> 
<img src="https://img.shields.io/badge/IntelliJ IDEA-000000?style=round-square&logo=IntelliJ IDEA&logoColor=white"> 
<img src="https://img.shields.io/badge/Slack-4A154B?style=round-square&logo=Slack&logoColor=white"> <br/>


<br/>
<br/>

### :metal: **Blog Post**

|날짜|제목|
|---|---|
{latest_blog_post_list}

<br/>
<br/>
  
### :memo: **Algorithm Test**
  [![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=son99)](https://solved.ac/son99/)

<br/>
<br/>

  
### :octocat: Github stats
[![GitHub Streak](https://streak-stats.demolab.com?user=5onchangwoo&theme=java-dark&locale=en&date_format=%5BY.%5Dn.j&background=45%2C4A12EB%2CEB5454&dates=EBEBEB&border=000000)](https://git.io/streak-stats)  
  
<br/>
<br/>



  
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=250&section=footer" style="width:100%;">
</div>


"""

readme_text = f"{markdown_text}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
