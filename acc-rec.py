from docx import Document
document = Document('./test.docx')
real_title_list = []
for p in document.paragraphs:
    string = p.text
    if (string.endswith('label_1')):
        real_title_list.append(string)
        print(p.text)


def cal_pre_recall(pre_title_list, real_title_list): 
    turePre_title_list = []
    for title in pre_title_list:
        if (title.endswith('label_1')):
            turePre_title_list.append(title)
    real_title_count = len(real_title_list)
    pre_title_count = len(pre_title_list)
    turePre_title_count = len(turePre_title_list)
    if (real_title_count > 0 and pre_title_count > 0):
        presision = turePre_title_count/pre_title_count
        recall = turePre_title_count/real_title_count
        return presision, recall
    else:
        return 0, 0

