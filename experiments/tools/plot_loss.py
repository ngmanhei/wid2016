#!/usr/bin/python
import sys
import re
import matplotlib.pyplot as pl
# filename = '/home/wenxi/wenxi/reid-multi-task/experiments/tools/sample.log'
def main(argv):
	total_loss_pattern = re.compile('(.*)solver.cpp:228] Iteration (.*), loss = (.*)')
	loss_bbox_pattern = re.compile('(.*)solver.cpp:244]     Train net output #0: loss_bbox = (.*) \((.*)\)')
	loss_cls_pattern = re.compile('(.*)solver.cpp:244]     Train net output #1: loss_cls = (.*) \((.*)\)')
	rpn_cls_loss_pattern = re.compile('(.*)solver.cpp:244]     Train net output #2: rpn_cls_loss = (.*) \((.*)\)')
	rpn_loss_bbox_pattern = re.compile('(.*)solver.cpp:244]     Train net output #3: rpn_loss_bbox = (.*) \((.*)\)')
	iters = []
	total_loss = []
	loss_bbox = []
	loss_cls = []
	rpn_cls_loss = []
	rpn_loss_bbox = []
	IsSavePlot = False
	IsShowPlot = True
	f = open(argv[1], 'r')
	line = f.readline().strip()
	while line != '':
		searchObj1 = total_loss_pattern.search(line)
		if searchObj1 is None:
			line = f.readline().strip()
		else:
			iters.append(float(searchObj1.group(2)))
			total_loss.append(float(searchObj1.group(3)))
			
			line = f.readline().strip()
			searchObj2 = loss_bbox_pattern.search(line)
			loss_bbox.append(float(searchObj2.group(2)))

			line = f.readline().strip()
			searchObj2 = loss_cls_pattern.search(line)
			loss_cls.append(float(searchObj2.group(2)))

			line = f.readline().strip()
			searchObj2 = rpn_cls_loss_pattern.search(line)
			rpn_cls_loss.append(float(searchObj2.group(2)))

			line = f.readline().strip()
			searchObj2 = rpn_loss_bbox_pattern.search(line)
			rpn_loss_bbox.append(float(searchObj2.group(2)))

			# print '%d\t%f\t%f\t%f\t%f\t%f' % (iters, total_loss, loss_bbox, loss_cls, rpn_cls_loss, rpn_loss_bbox)
			line = f.readline().strip()

	pl.figure(1)
	pl.ylim([0,0.4])
	pl.plot(iters, total_loss, color = 'black')
	pl.title('total_loss')
	if IsSavePlot:
		pl.figure(1).savefig('total_loss.jpg')

	pl.figure(2)
	pl.ylim([0,0.2])
	pl.plot(iters, loss_bbox, color = 'green')
	pl.title('loss_bbox')
	if IsSavePlot:
		pl.figure(2).savefig('loss_bbox.jpg')	

	pl.figure(3)
	pl.ylim([0,0.3])
	pl.plot(iters, loss_cls, color = 'yellow')
	pl.title('loss_cls')
	if IsSavePlot:
		pl.figure(3).savefig('loss_cls.jpg')

	pl.figure(4)
	pl.ylim([0,0.005])
	pl.plot(iters, rpn_cls_loss, color = 'blue')
	pl.title('rpn_cls_loss')
	if IsSavePlot:
		pl.figure(4).savefig('rpn_cls_loss.jpg')

	pl.figure(5)
	pl.ylim([0,0.05])
	pl.plot(iters, rpn_loss_bbox, color = 'red')
	pl.title('rpn_loss_bbox')
	if IsSavePlot:
		pl.figure(5).savefig('rpn_loss_bbox.jpg')
	if IsShowPlot:
		pl.show()
if __name__ == '__main__':
	main(sys.argv)
