import webbrowser

def showEarnings( stockName):
	earningsLink = 'https://www.nasdaq.com/earnings/report/'
	#earningsLink.append( stockName)
	earningsLink += stockName
	webbrowser.open( earningsLink)
	

def showDividends( stockName):
	dividendLinkBegin = 'https://www.nasdaq.com/symbol/'
	dividendLinkEnd = 	'/dividend-history'
	dividendLinkBegin += stockName
	dividendLinkBegin += dividendLinkEnd
	webbrowser.open( dividendLinkBegin)

def showWeeklyEarnings():
	link = 'ttps://seekingalpha.com/earnings/earnings-calendar'
	webbrowser.open( link)

# Google Fiance
# Polling vic index
# S&P 500, Gold, Silver, Bonds, QQQ, Natural Gas