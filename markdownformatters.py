import pyperclip
import requests
import re
import dataset
import string as S
from itertools import cycle


def make_youtube_inline(videoid,iframewidth=560,iframeheight=315):
    """Takes a videoid and returns markdown formatted iframe to embed the video"""
    return '<iframe  title="YouTube video player" width="{}" height="{}" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>'.format(iframewidth,iframeheight,videoid)

def youtube_videoid(url):
    " youtube video url -> youtube videoid "
    return re.findall(r'v=([a-zA-Z0-9\-]+)', url)[0]


class MarkdownTable(object):
    """docstring for MarkdownTable"""
    def __init__(self, column_headers,justifications=None):
        super(MarkdownTable, self).__init__()
        self.column_headers = column_headers
        self.formatstr = "|"+"{}|"*len(column_headers) # |{}|{}|{}|
        if justifications is None:
        	self.justifications = ['l' for col in self.column_headers]
        self.rowcontents = []
        # add the column headers to the contents
        # self.rowcontents.append([h for h in column_headers])
        # add the pipe formatting to the contents
        # self.rowcontents.append([self.make_pipe_formatting(len(h)) for h in column_headers])

    def make_pipe_formatting(self,width,justification='l'):
        if justification == 'l':
            return ':'+ '-'*(width-1)
        elif justification == 'r':
            return '-'*(width-1) + ':' 
        elif justification == 'c': 
            return ':'+ '-'*(width-2) + ':'

    def add_row(self,columns):
        self.rowcontents.append([str(x) for x in columns])

    def get_max_column_widths(self):
        """ Returns the width of the widest row of each column """
        max_widths = [0 for x in range(len(self.column_headers))]
        all_rows = [self.column_headers]
        for r in self.rowcontents:
        	all_rows.append(r)
        for row in all_rows:
            for i,contents in enumerate(row):
                if len(contents) > max_widths[i]:
                    max_widths[i] = len(contents)
        return max_widths

    def make_table(self):
        max_widths = self.get_max_column_widths()
        rows = []
        # add the column headers
        column_headers = [h.ljust(width) for (h,width) in zip(self.column_headers,max_widths)]
        rows.append(self.formatstr.format(*column_headers))
        # add the pipe formatters
        pipes = [self.make_pipe_formatting(width) for width in max_widths]
        rows.append(self.formatstr.format(*pipes))
        # add the rowcontents
        for row in self.rowcontents:
            rows.append(self.formatstr.format(*[col.ljust(width) for (col,width) in zip(row,max_widths)]))
        return "\n".join(rows)

    def __repr__(self):
        return self.make_table()

# if __name__ == '__main__':
#     foo = MarkdownTable(['Header 1','Header 2'])
#     foo.add_row(['a','b'])
#     print(foo)
