# pip install lxml
# pip install wget

### 下载文件

import wget
url = 'https://epg.pw/xmltv/epg.xml'  
path = './'
wget.download(url,path)

### 设置
file_name = "epg.xml" # 下载文件名
filter_tvgroup = ['民視','民視台灣台', '中視' ,'台視','華視','三立財經新聞台','ViuTV'] # 需要下载的电视台名
result_file_name = "epg_filtered.xml" # 生成的结果文件名

### 读取原始文件

import pandas
xml = pandas.read_xml(file_name)

xml_programme = xml.query('id.isnull()')
xml_p_new = xml_programme[['channel', 'start', 'stop', 'title', 'date','audio']]
xml_p_new = xml_p_new.rename(columns={'channel': 'id'})

xml_tvstation = xml.query('channel.isnull()')
xml_t_new = xml_tvstation[['id','display-name']]

xml_total = xml_t_new.merge(xml_p_new, on='id')

filtered_xml_total = xml_total.loc[xml_total['display-name'].isin(filter_tvgroup)]

# 电视频道总表filtered_tv，电视节目总表filtered_xml_total
filtered_xml_total = filtered_xml_total.drop(['display-name'], axis=1)
filtered_tv = xml_t_new.loc[xml_t_new['display-name'].isin(filter_tvgroup)]

# 获取原始文件前两行

f=open(file_name,'r')
str_head = ""
for i in range(2):
    str_head += f.readline().strip() + '\n'
print(str_head)

# 输出文件（channel部分）
with open(result_file_name,"w") as file:
    file.write(str_head)

    for row in filtered_tv.itertuples():
        file.write("\t<channel id=\"" + str(int(row.id)) + "\">\n")
        file.write("\t\t<display-name lang=\"TW\">" + row._2 +"</display-name>\n")
        file.write("\t</channel>\n")

# 输出文件（epg部分）
with open(result_file_name,"a") as file:
    for row in filtered_xml_total.itertuples():
        file.write("\t<programme channel=\"" + str(int(row.id)) + "\" start=\"" + str(row.start) + "\" stop=\"" + str(row.stop) + "\">\n")
        file.write("\t\t<title lang=\"zh\">" + str(row.title) + "</title>\n")   
        file.write("\t\t<date>" + str(int(row.date)) + "</date>\n" )
        file.write("\t\t<audio>\n")
        file.write("\t\t\t<stereo>stereo</stereo>\n")
        file.write("\t\t</audio>\n")
        file.write("\t</programme>\n")

