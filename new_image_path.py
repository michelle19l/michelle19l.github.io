import os
import os.path
import re

def get_image_name():
	rootdir = "E:/blog/hexo/source/images/"
	images_list=""
	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			images_list.append(filename)



def replace_1():
	#input_str=input("原图片路径") # eg. E:\study\大二下\漏洞测试\作业\作业一\
	#output_str='/images'+input("现图片路径") # eg. /漏洞测试作业一/,若在根目录下则输入/

	input_str="E:\blog\hexo\source\_posts\\".split(" ")
	output_str="/images/power-designer入门/"

	style="zoom：50%;"
	input_file='E:\\blog\hexo\source\_posts\power-designer入门.md'
	output_file="E:\\blog\hexo\source\_posts\output.txt"

	file_data = ""
	with open(input_file, "r", encoding="utf-8") as f:
		for line in f:
			for i_str in input_str:
				if i_str in line:
					line = line.replace(i_str,output_str)
			file_data += line
	with open(output_file,"w",encoding="utf-8") as f:
		f.write(file_data)



replace_1()
	
	
	
	
	
