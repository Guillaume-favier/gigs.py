import sys
import os
size = os.get_terminal_size() 
w=int(str(size).split(',')[0].split('=')[1])
class bar:
	def __init__(self, index, total, title='Please wait'):
		self.index = index
		self.total = total
		self.title = title

	def disp(self, index='null'):
		if index != 'null':
			self.index = index
		index = self.index
		'''
		index is expected to be 0 based index. 
		0 <= index < total
		'''
		bar_len=w-(30)-len(self.title)
		percent_done = (index+1)/self.total*100
		percent_done = round(percent_done, 1)

		done = round(percent_done/(100/bar_len))
		togo = bar_len-done

		done_str = '█'*int(done)
		togo_str = '░'*int(togo)

		print(f'\t⏳{self.title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')

		if percent_done == 100:
			print('\t✅',end='\r')
		return