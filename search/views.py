from django.shortcuts import render

# Create your views here.
import cPickle as pickle

infor = pickle.load(open('data/infor.data','r'))
dic   = pickle.load(open('data/dic.data','r'))



def index(request):
    s = ''
    try:
        s = request.GET['keywords']
        print s
        if s == '':
            go_to_die
    except:
        result = []
    else:
        keys = s.split()
        for i,one_key in enumerate(keys):
            print '[',one_key,']'
            if dic.has_key(one_key):
                if i == 0:
                    find = dic[one_key]
                else:
                    find = find & dic[one_key]
            else:
                find = set()
        result = []
        if find:
            for date in find:
                result.append(infor[date])
        else:
            result = [['','Nothing','SAD STORY']]
        
        print len(result)
    #print result 
    return render(request,'search/index.html',{
        'result':result,
        'word'  :s,
        })
