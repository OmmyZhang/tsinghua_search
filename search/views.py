from django.shortcuts import render

# Create your views here.
import cPickle as pickle
import jieba

infor = pickle.load(open('data/infor.data','r'))
dic   = pickle.load(open('data/dic.data','r'))



def index(request):
    s = ''
    ONE_PAGE = 1000
    try:
        s = request.GET['keywords']
        print s
        if s == '':
            go_to_die
    except:
        result = []
        p_num = 1
        cur_p = 1
    else:
        sp = s.split()
        keys =[]
        
        for one_part in sp:
            keys +=  jieba.lcut(one_part,cut_all=False)
        
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
            result = [['?keyword=','Nothing','SAD STORY']]
        
        print len(result)
        p_num = (len(result) -1) / ONE_PAGE + 1;
        
        if request.GET.has_key('page'):
            cur_p = int(request.GET['page'])
        else:
            cur_p = 1
        
        st = (cur_p-1) * ONE_PAGE
        en = min( cur_p * ONE_PAGE - 1,len(result) )
        result = result[st:en]
    #print result 
    
    if p_num == 1:
        p_num = 0
    return render(request,'search/index.html',{
        'result':result,
        'word'  :s,
        'pages' : range(1,p_num+1),
        'cur_p' : cur_p
        })
