#!/usr/bin/env/python3
import sys, os, markdown
count = 0
buf = ""
ofilename = sys.argv[2]
ifilename = sys.argv[1]
outfile = open(ofilename, "w")
head = open("template/head.html", "r").read()
foot = open("template/foot.html", "r").read()
slides = open(ifilename, "r").read().split("~~~")

outfile.write(head)
k=0
md=markdown.Markdown()
for slide in slides:
	if k != 0: outfile.write("<br id=\"break-"+str(k)+"\">")
	outfile.write("<div id=\"page-"+str(k)+"\" class=\"child\">")
	outfile.write(md.reset().convert(slide).replace("\n", "<br>"))
	outfile.write("</div>")
	k+=1
outfile.write(foot)