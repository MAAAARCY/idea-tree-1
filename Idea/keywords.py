from IdeaTree.settings import MODEL_FILE_PATH
from . import views
from . import same
import gensim

def word(word: str):
    api_datas = []
    obj = same.keep()
    flag = obj.get_flag()
    check_flag = obj.get_check_flag()

    model = gensim.models.Word2Vec.load(MODEL_FILE_PATH)
    result = model.wv.most_similar(word)
    ans = []
    judge = []

    for i in range(3):
        ans.append(result[i][0])

    if len(flag) == 0:
        api_datas.append(word)
        for i in range(3):
            api_datas.append(ans[i])
        obj.flag_changer()
        return api_datas
    if len(flag) > 0:
        if word in obj.get_ptr():
            obj.point_append(obj.get_ptr().index(word)+1)
        else:
            if len(check_flag) > 0:
                obj.allclear()
                api_datas.append(word)
                obj.check_flag_reset()
            else:
                obj.point_append(obj.get_ptr().index(word)+1)
            
        for i in range(3):
            if(ans[i] not in obj.get_ptr()):
                judge.append(ans[i])
                api_datas.append(ans[i])
        if len(judge) < 3:
            for i in range(3,9):
                if result[i][0] not in api_datas and result[i][0] not in obj.get_ptr():
                    judge.append(result[i][0])
                    api_datas.append(result[i][0])
                    if(len(judge) >= 3):
                        break

        return api_datas