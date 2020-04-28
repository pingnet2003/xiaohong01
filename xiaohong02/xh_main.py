# -*- coding:utf-8 -*-
import wordcloud

# 1、准备文本
sentence = 'Do not go gentle into that good night!'

# 2、创建词云对象
wc = wordcloud.WordCloud()

# 3、通过文本数据生成词云
wc.generate(sentence)

# 4、保存图片
wc.to_file("test_wc.png")
