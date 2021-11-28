#MyDevelopmentDiary
----------------------------------------------
##OneDay                     2021/11/28
----------------------------------------------
<p>网页信息爬取
<p>导入包：import requests

<p>先要进行网站页面数据分析

<li>第一步
<p>F12进入开发者模式后，点击网路，选择Fetch/XHR,或者文档。</p>
<p>过滤多余干扰项</p>
<p><img src="Resource/Image/DD_1_01.jpg" /></p>
<li>第二步
<p>点击预览或者相应，确认其中的内容。</p>
<p>判断该请求路径是否为需要的路径</p>
<p><img src="Resource/Image/DD_1_02.jpg" /></p>
<li>第三步
<p>确定请求URL</p>
<p>确定请求方法</p>
<p>确定请求方法</p>
<p>确定Content-Type</p>
<p><img src="Resource/Image/DD_1_03.jpg" /></p>
<li>第四步
<p>确定User-Agent</p>
<p><img src="Resource/Image/DD_1_04.jpg" /></p>

<p>Response通信
<p>url：请求URL
<p>params：？后面的参数，可以在上述的第三步中选择PayLoad选项卡查看
<p>headers：连接头，要设置'User-Agent'进行UA伪装
<p>如果返回是html格式的话
<p>response = requests.get(url=url,params=parm, headers=header)
<p>如果返回是json格式的话
<p>response = requests.get(url=url,params=parm, headers=header).json()
<p>上述 requests.get可以换成 requests.post
