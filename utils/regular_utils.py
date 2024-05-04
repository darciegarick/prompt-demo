import re

# 根据标签类型 分割文件
def label_splitting(file_content):
    pattern = r'##+\s[\w\W]*?(?=##|$)'
    matches = re.findall(pattern, file_content)
    process_dict = {}
    for matche in matches:
        process_dict[get_label(matche)] = get_question(matche)
    return process_dict

# 获取 标签类型
def get_label(part_content):
    lable_pattern = r'(?<=## )[\w\W]*?(?=\d)'
    lable_matches = re.findall(lable_pattern, part_content)
    return lable_matches[0].strip()

# 获取标签类型下的所有题目
def get_question(part_content):
    question_pattern = r'\d+\.[\w\W]*'
    question_matches = re.findall(question_pattern,part_content)
    # 去除每个字符串前后的空白字符
    # cleaned_questions = [question.strip() for question in question_matches]
    return question_matches


# 获取标签类型下的所有题目（不包括答案部分）
def get_every_question_noans(content):
    pattern = r'\d+\.[\w\W]*?(?=答)'
    matches = re.findall(pattern,content)
    return matches

