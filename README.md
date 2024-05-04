#### 什么是 Prompt Engineering？
解释这个词之前，首先需要解释 prompt 这个词。   

简单的理解它是给 AI 模型的指令。   

它可以是一个问题、一段文字描述，甚至可以是带有一堆参数的文字描述。AI 模型会基于 prompt 所提供的信息，生成对应的文本，亦或者图片。   

比如，我们在 ChatGPT 里输入 What is the capital of China? (中国的首都是什么？)，这个问题就是 prompt。   

**而 Prompt Engineering （中文意思为提示工程，后缩写为 PE）则是：**

Prompt Engineering 是一种人工智能（AI）技术，它通过设计和改进 AI 的 prompt 来提高 AI 的表现。   

Prompt Engineering 的目标是创建高度有效和可控的 AI 系统，使其能够准确、可靠地执行特定任务。   

#### Prompt Engineering 基本原则 & 建议

在和大语言模型对话时，亦或者在使用和设计 prompt 时，有以下几个原则与建议。记住这几个原则，能让你写出更好的 prompt   

1. Prompt 里最好包含完整的信息  

这个是对结果影响最大的因素。比如如果你想让 AI 写一首关于 OpenAI 的诗。   

**示例**       
效果较差的提示词Prompt：   
```
Write a poem about OpenAI.
// 写一首关于 OpenAI 的诗。(中文也可，用英文的效果更好)
```  
上述提示词它生成的答案可能就会很宽泛，而更好的方式是增加更多的信息。     


效果较好的提示词Prompt：   
```
Write a short inspiring poem about OpenAI, focusing on the recent DALL-E product launch (DALL-E is a text to image ML model) in the style of a {famous poet}
// 以{著名诗人}的风格写一首关于OpenAI的励志短诗，重点是最近发布的DALL-E产品（DALL-E是一种文本到图像的ML模型）。
```

2. Prompt 最好简洁易懂，并减少歧义

这个比较好理解，即使你跟人说话，说一些简单的短句，对方也会更容易听懂，AI 也是这样。另外，在 prompt 里也需要减少一些歧义，少用模棱两可的词语。   

**就例如下面这个示例:**
```    
The description for this product should be fairly short, a few sentences only, and not too much more.  
// 该产品的描述应相当简短，只需几句话，不宜过多。
```
比如像这个就很不明确，什么叫 not too much more (不宜过多)？   


**更好的 prompt 是这样的，明确告知要写多少句话，就比较明确：**   
```
Use a 3 to 5 sentence paragraph to describe this product.
// 用 3 至 5 句话描述该产品。
```

另外需要注意的是，简单并不代表简短。你的 prompt 也可以很长，只要你的 prompt 描述更充分就可以，即使长一点也没有关系。    


3. Prompt 要使用正确的语法、拼写，以及标点

**特别是在使用英语的 prompt 的时候，一定要注意语法和拼写。**


#### 技巧篇
1. To Do and Not To Do （做于不做） <br> 
明确的告知 ChatGPT 它需要做什么，同时你如果想缩小返回内容的输出范围，就告知 ChatGPT 它不允许做什么。   

**示例**    
```
场景：推荐香港值得游玩的地方

Please recommend me some places to visit in Hong Kong including amusement parks.
// 请向我推荐香港的一些旅游景点，包括游乐园。

Please recommend me some places to visit in Hong Kong. Do not recommend museums.
// 请向我推荐一些香港的旅游景点。不要推荐博物馆。
```

2. 增加示例 <br> 
在某些场景下，我们能比较简单地向 AI 描述出什么能做，什么不能做。但有些场景，有些需求很难通过文字指令传递给 AI，即使描述出来了，AI 也不能很好地理解。    

**示例** 
```
场景：起英文名

Suggest three English names for a boy.
// 推荐三个男孩的英文名字。

Suggest three English names for a boy.
Here are some examples: Jimmy、Jason、James
// 推荐三个男孩的英文名字。
// 下面是一些例子：Jimmy、Jason、James
```

3. 使用引导词，引导模型输出特定内容 <br> 
在代码生成场景里，有一个小技巧，在 prompt 最后，增加一个代码的引导，告知 AI 我已经将条件描述完了，你可以写代码了。   

**示例**
```
Create a MySQL query for all students in the Computer Science Department:
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
SELECT

// 
为计算机科学系的所有学生创建 MySQL 查询：
表系，列 = [系Id，系名］
表 students，列 = [DepartmentId、StudentId、StudentName］
SELECT
```
在 prompt 的最后增加 SELECT 可以很好地提示 AI 可以写 SQL 代码了。    


在吴恩达的 ChatGPT Prompt Engineering 课程中，也提到这个技巧，只是在课程中，引导词并不是放在最后，而是在 prompt 里直接说明，让 AI 生成一个 JSON 格式的内容。课程中的例子是这样的（注意这个是 python 代码）：

```
prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""

// 
prompt = f"""
生成一个包含三个编造的书名及其作者和流派的列表。
及其作者和流派。
以 JSON 格式提供它们，键值如下：
book_id、标题、作者、流派。
"""
```
简单解释下，其关键是在 prompt 里跟 AI 说明，需要 AI 按照 JSON 格式输出内容。    


4. 增加 Role（角色）或人物 <br> 
再介绍一个更有效的技巧，就是在 prompt 里增加一些 role（角色）相关的内容，让 AI 生成的内容更符合你的需求。  

**示例**
```
In order to be able to explain complexity to a seven or eight year old. Rewrite the following sentence to make it easier to understand:...
// 为了能够向七八岁的孩子解释复杂性。改写下面的句子，使其更容易理解：...


You are a primary school teacher who can explain complex content to a level that a 7 or 8 year old child can understand. Please rewrite the following sentences to make them easier to understand: ...
// 你是一名小学教师，能够向七八岁的孩子解释复杂的内容。请改写下面的句子，使其更容易理解：...
```

5. 使用特殊符号指令和需要处理的文本分开 <br> 
不管是信息总结，还是信息提取，你一定会输入大段文字，甚至多段文字，此时有个小技巧。   

可以用"""将指令和文本分开。根据我的测试，如果你的文本有多段，增加"""会提升 AI 反馈的准确性（这个技巧来自于 OpenAI 的 API 最佳实践文档）    

**示例**
未使用指令将文本进行区分：
```
Please summarize the following sentences to make them easier to understand.
OpenAI is an American artificial intelligence (AI) research laboratory consisting of the non-profit OpenAI Incorporated (OpenAI Inc.) and its for-profit subsidiary corporation OpenAI Limited Partnership (OpenAI LP). OpenAI conducts AI research with the declared intention of promoting and developing a friendly AI. OpenAI systems run on the fifth most powerful supercomputer in the world.[5][6][7] The organization was founded in San Francisco in 2015 by Sam Altman, Reid Hoffman, Jessica Livingston, Elon Musk, Ilya Sutskever, Peter Thiel and others,[8][1][9] who collectively pledged US$1 billion. Musk resigned from the board in 2018 but remained a donor. Microsoft provided OpenAI LP with a $1 billion investment in 2019 and a second multi-year investment in January 2023, reported to be $10 billion.[10]

//
请概括以下句子，使其更易于理解。
OpenAI是美国的一家人工智能（AI）研究实验室，由非营利性的OpenAI Incorporated（OpenAI Inc.）及其营利性子公司OpenAI Limited Partnership（OpenAI LP）组成。OpenAI 开展人工智能研究的公开意图是推广和开发友好的人工智能。OpenAI 系统运行在世界排名第五的超级计算机上。[5][6][7] 该组织于 2015 年在旧金山成立，由 Sam Altman、Reid Hoffman、Jessica Livingston、Elon Musk、Ilya Sutskever、Peter Thiel 等人创立，[8][1][9] 他们共同认捐了 10 亿美元。马斯克于 2018 年从董事会辞职，但仍是捐赠者之一。微软在 2019 年向 OpenAI LP 提供了 10 亿美元的投资，并在 2023 年 1 月提供了第二笔多年期投资，据说高达 100 亿美元[10]。
```

使用指令将文本进行区分：
```
Please summarize the following sentences to make them easier to understand.

Text: """
OpenAI is an American artificial intelligence (AI) research laboratory consisting of the non-profit OpenAI Incorporated (OpenAI Inc.) and its for-profit subsidiary corporation OpenAI Limited Partnership (OpenAI LP). OpenAI conducts AI research with the declared intention of promoting and developing a friendly AI. OpenAI systems run on the fifth most powerful supercomputer in the world.[5][6][7] The organization was founded in San Francisco in 2015 by Sam Altman, Reid Hoffman, Jessica Livingston, Elon Musk, Ilya Sutskever, Peter Thiel and others,[8][1][9] who collectively pledged US$1 billion. Musk resigned from the board in 2018 but remained a donor. Microsoft provided OpenAI LP with a $1 billion investment in 2019 and a second multi-year investment in January 2023, reported to be $10 billion.[10]
"""

//
请概括以下句子，使其更易于理解。

文本： """
OpenAI 是美国一家人工智能（AI）研究实验室，由非营利性的 OpenAI Incorporated（OpenAI 公司）及其营利性子公司 OpenAI Limited Partnership（OpenAI LP）组成。OpenAI 开展人工智能研究的公开意图是推广和开发友好的人工智能。OpenAI 系统运行在世界排名第五的超级计算机上。[5][6][7] 该组织于 2015 年在旧金山成立，由 Sam Altman、Reid Hoffman、Jessica Livingston、Elon Musk、Ilya Sutskever、Peter Thiel 等人创立，[8][1][9] 他们共同认捐了 10 亿美元。马斯克于 2018 年从董事会辞职，但仍是捐赠者之一。微软在 2019 年向 OpenAI LP 提供了 10 亿美元的投资，并在 2023 年 1 月提供了第二笔多年期投资，据说高达 100 亿美元[10]。
"""
```

6. 通过格式词阐述需要输出的格式 <br> 
这个技巧是技巧 2 的变种，比较常用于生成文本场景。   

假设你想让 AI 总结一篇非常非常长的文章，并且按照特定格式给你总结，那你可以在文章前面明确输出的格式。它的意思其实是让 ChatGPT 按 Topic 总结，每个 Topic 里按照无序列表（就是里面那个 -）将每个 Topic 的主要观点罗列出来。

**示例**
```
Summarize the main points of the following speech
Use the following format:
Topic 1: <topic_name_1>
- <point_1>
..
Topic 2: <topic_name_2>
- <point_1>
..
Topic 10: ..

Text: """
Thank you so much, Fred, for that lovely introduction. And thanks to the Atlantic Council for hosting me today.

The course of the global economy over the past two years has been shaped by COVID-19 and our efforts to fight the pandemic. It’s now evident, though, that the war between Russia and Ukraine has redrawn the contours of the world economic outlook. Vladimir Putin’s unprovoked attack on Ukraine and its people is taking a devastating human toll, with lives tragically lost, families internally displaced or becoming refugees, and communities and cities destroyed.
...
"""

//
概括以下演讲的要点
使用以下格式：
主题 1：<主题_名称_1
- <观点_1
..
题目 2：<题目名称_2
- <观点_1
..
主题 10: .

文本： """
非常感谢弗雷德的精彩介绍。也感谢大西洋理事会今天接待我。

在过去的两年里，COVID-19 和我们抗击大流行病的努力影响了全球经济的进程。但现在显而易见的是，俄罗斯和乌克兰之间的战争重新勾勒了世界经济前景的轮廓。弗拉基米尔-普京（Vladimir Putin）对乌克兰及其人民的无端攻击正在造成毁灭性的人员伤亡，许多人不幸丧生，一些家庭在境内流离失所或沦为难民，一些社区和城市遭到破坏。
...
"""
```

输出的内容是这样子的:   
```
Topic 1: The war in Ukraine
- The war is taking a human toll with lives lost, families displaced, and communities destroyed
- The Biden administration is committed to holding Russia accountable
- The war has violated international law and is a challenge to the international order

Topic 2: The global economy
- The war is having negative impacts on the global economy, including higher commodity prices and inflation
- The IMF and World Bank will be focused on helping developing countries weather the impacts of the war
- The ultimate outcome for the global economy depends on the path of the war

//
主题 1：乌克兰战争
- 战争造成人员伤亡、家庭流离失所、社区被毁
- 拜登政府致力于追究俄罗斯的责任
- 战争违反了国际法，是对国际秩序的挑战

议题 2：全球经济
- 战争正在对全球经济产生负面影响，包括商品价格上涨和通货膨胀
- 国际货币基金组织（IMF）和世界银行将致力于帮助发展中国家抵御战争的影响
- 全球经济的最终结果取决于战争的走向
```


**示例2**
使用此技巧可以使输出更结构化。比如针对一篇文章进行问答，你不仅想要得到一个答案，也希望 ChatGPT 的答案符合特定的格式，方便你下一步进行自动化。   

比如问 "这里的债券 duration 是多少？". 正常 GPT 模型的答案可能是 "债券 duration 是 4 年" 或 "duration 4 年"。 ChatGPT 的回答不稳定，且不方便继续处理。   

解法： 我们可以通过这个技巧，让模型理解我们预期的格式。并在此基础上，为了方便自动化，让模型输出特定的结构化答案 (比如 JSON/Markdown 等)。 也可以方便集成更多的额外要求，比如增加一个"confidence level", 并通过 prompt 的形式指定这些数值的格式。   

```
{context}
Question: What is bond duration mentioned here.
Answer template (Valid JSON format):
{{
"duration": $duration_numeric_value_in_year,
"confidence_level": $answer_confidence_level_high_modrate_or_low,
}}
Answer:


//
{上下文｝
问题 这里提到的债券期限是什么。
答案模板（有效 JSON 格式）：
{{
“持续时间”： $duration_numeric_value_in_year、
“置信度”：$answer_confidence_level_high_modrate_or_low、
}}
答案：
```


7. Zero-Shot Chain of Thought (思维链) <br> 
这个技巧使用起来非常简单，只需要在问题的结尾里放一句 Let‘s think step by step （让我们一步步地思考），模型输出的答案会更加准确。   

在吴恩达的 ChatGPT Prompt Engineering 课程中，有提到一个这个技巧的另一种用法，不仅仅只是让 AI 按步骤行事，还会告知 AI 每一步要做什么。比如这个案例（注意这个是 python 代码）：

```
prompt_2 = f"""
Your task is to perform the following actions:
1 - Summarize the following text delimited by
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""

//
prompt_2 = f"""
您的任务是执行以下操作：
1 - 用 1 个句子概括以下以
  <> 分隔的文本总结为 1 个句子。
2 - 将摘要翻译成法文。
3 - 列出法语摘要中的每个名称。
4 - 输出一个 json 对象，其中包含
  以下键：french_summary、num_names。

使用以下格式：
文本： <摘要文本
摘要： <摘要
翻译： <摘要译文
名称： <意大利语摘要中的名称列表>。
输出 JSON：<json，包含摘要和名称数>。

文本： <{text}> 文本
"""
```

简单解释下这个代码：  
- 开头是让 AI 按照 1 ～ 4 步运行
- 然后再让 AI 根据特定格式输出内容

最后 AI 的输出是这样的：  
```
Summary: Jack and Jill go on a quest to fetch water, but misfortune strikes and they tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.
Translation: Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.
Names: Jack, Jill
Output JSON: {"french_summary": "Jack et Jill partent en quête d'eau, mais la malchance frappe et ils dégringolent la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.", "num_names": 2}

//
摘要：杰克和吉尔去打水，但不幸发生了，他们从山上摔了下来，回到家时虽然受了点伤，但冒险精神丝毫未减。
译文：杰克和吉尔去打水，但不幸发生了，他们从山上摔了下来，回到家时虽然受了点伤，但冒险精神丝毫未减。
名称： 杰克、吉尔
输出 JSON：{“english_summary”: “杰克和吉尔出发去找水，但厄运降临了，他们从山上摔了下来，虽然摔得鼻青脸肿，但冒险精神丝毫未减。”, “num_names”: 2}
```

上述的案例只是将任务拆解，能让 AI 生成的结果更加符合要求，这个方法同样能提升 AI 的回答准确性，比如这个案例：   

```
Determine if the student's solution is correct or not.

Question:
I'm building a solar power installation and I need help working out the financials.

Land costs $100 / square foot

I can buy solar panels for $250 / square foot

I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square foot
What is the total cost for the first year of operations
as a function of the number of square feet.

Student's Solution:
Let x be the size of the installation in square feet.
Costs:

Land cost: 100x

Solar panel cost: 250x

Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000

//
判断学生的解答是否正确。

问题
我正在建造一个太阳能发电装置，我需要帮助计算财务费用。

土地成本为 100 美元/平方英尺

我可以以每平方英尺 250 美元的价格购买太阳能电池板

我通过谈判签订了一份维护合同，每年的维护费用为 10 万美元。
每年 10 万美元，每平方英尺另加 10 美元
运营第一年的总成本是多少？
作为平方英尺数的函数。

学生的解答：
设 x 为安装面积（平方英尺）。
成本：

土地成本：100x

太阳能电池板成本：250x

维护成本：100,000 + 100x
总成本：100x + 250x + 100,000 + 100x = 450x + 100,000
```

AI 的回答是「The student's solution is correct」。但其实学生的答案是错误的，应该 360x + 100,000，我们将 prompt 调整成这样：   

```
prompt = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.
Use the following format:
Question:
###
question here
###
Student's solution:
###
student's solution here
###
Actual solution:
###
steps to work out the solution and your solution here
###
Is the student's solution the same as actual solution \
just calculated:
###
yes or no
###
Student grade:
###
correct or incorrect
###
Question:
###
I'm building a solar power installation and I need help \
working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
  me a flat $100k per year, and an additional $10 / square \
  foot
  What is the total cost for the first year of operations \
  as a function of the number of square feet.
###
Student's solution:
###
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
   Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
###
Actual solution:
"""

//
prompt = f"""
你的任务是判断该学生的解（ ）是否正确。
是否正确。
解题步骤如下：
- 首先，计算出你自己的解。
- 然后将你的解法与学生的解法进行比较
并评估学生的解法是否正确。
在您自己完成问题之前，不要决定学生的解法是否正确。
在您自己做完这道题之前，不要决定学生的解法是否正确。
使用以下格式：
问题：
###
这里的问题
###
学生的解决方案：
###
学生的解决方案
###
实际解法
###
求解步骤和你的解在这里
###
学生的解法是否与实际解法相同？
刚刚计算的：
###
是或否
###
学生成绩：
###
正确或不正确
###
问题
###
我正在建造一个太阳能发电装置，我需要帮助
算出财务账目。
- 土地成本为 100 美元/平方英尺
- 我可以买到 250 美元/平方英尺的太阳能电池板
- I negotiated a contract for maintenance that will cost\ me a flat $100k per year
  每年固定花费 10 万美元，每平方英尺额外花费 10 美元。
  平方英尺
  运营第一年的总成本是多少？
  作为平方英尺数的函数。
###
学生的解决方案：
###
设 x 为安装面积（平方英尺）。
成本：
1. 土地成本：100x
2. 太阳能电池板成本：250x
3. 维护成本：100,000 + 100x
   总成本：100x + 250x + 100,000 + 100x = 450x + 100,000
###
实际解决方案：
"""
```

本质上，也是将任务分拆成多步，这次 AI 输出的结果是这样的（结果就是正确的了）：   
```
Let x be the size of the installation in square feet.

Costs:

1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 10x

Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000

Is the student's solution the same as actual solution just calculated:
No

Student grade:
Incorrect

//
设 x 为安装面积（平方英尺）。

成本

1. 土地成本： 100x
2. 太阳能电池板成本：250x
3. 维护成本：100,000 + 10x

总成本：100x + 250x + 100,000 + 10x = 360x + 100,000

学生的解决方案与刚才计算的实际解决方案是否相同？
不一样

学生成绩：
不正确
```


8. Few-Shot Chain of Thought (一针见血的思维链) <br> 

要解决这个缺陷，就要使用到新的技巧，Few-Shot Chain of Thought。   
根据 Wei 他们团队在 2022 年的研究表明：通过向大语言模型展示一些少量的样例，并在样例中解释推理过程，大语言模型在回答提示时也会显示推理过程。这种推理的解释往往会引导出更准确的结果。   

思维链有以下特点：   
- "the label space and the distribution of the input text specified by the demonstrations are both key (regardless of whether the labels are correct for individual inputs)" 标签空间和输入文本的分布都是关键因素（无论这些标签是否正确）。
- the format you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all. 即使只是使用随机标签，使用适当的格式也能提高性能。

**示例**
```
I loved the new Batman movie!  // Negative
This is bad // Positive
This is good // Negative
What a good show! //


我喜欢新的《蝙蝠侠》电影！ // 消极
这很糟糕 // 积极
这很好 // 消极
多好的节目啊 //
```
Output 是这样的：   
```
Positive

// 积极
```

在上述的案例里，每一行，我都写了一句话和一个情感词，并用 // 分开，但我给这些句子都标记了错误的答案，比如第一句其实应该是 Positive 才对。但：   
- 即使我给内容打的标签是错误的（比如第一句话，其实应该是 Positive），对于模型来说，它仍然会知道需要输出什么东西。换句话说，模型知道 // 划线后要输出一个衡量该句子表达何种感情的词（Positive or Negative）。这就是前面论文里 #1 提到的，即使我给的标签是错误的，或者换句话说，是否基于事实，并不重要。标签和输入的文本，以及格式才是关键因素。
- 只要给了示例，即使随机的标签，对于模型生成结果来说，都是有帮助的。这就是前面论文里 #2 提到的内容。

最后，需要记住，思维链仅在使用大于等于 100B 参数的模型时，才会生效。

9. 在示例里加入特定符号，让模型知道如何处理特殊情况 <br> 

**示例**
这个解释起来有点复杂，以下是 OpenAI 的官方 prompt，在一些奇怪的问题上比如 What is Devz9 的回答，你可以用 ？ 代替答案，让模型知道当遇到超出回答范围时，需要如何处理？

```
Q: Who is Batman?
A: Batman is a fictional comic book character.

Q: What is torsalplexity?
A: ?

Q: What is Devz9?
A: ?

Q: Who is George Lucas?
A: George Lucas is American film director and producer famous for creating Star Wars.

Q: What is the capital of California?
A: Sacramento.

Q: What is Kozar-09?
A: 

//
问：蝙蝠侠是谁？
答：蝙蝠侠是一个虚构的漫画人物。

问：什么是背痛？
A: ?

问：什么是 Devz9？
A: ?

问：乔治-卢卡斯是谁？
答：乔治-卢卡斯是美国电影导演和制片人，因创作《星球大战》而闻名。

问：加利福尼亚州首府是哪里？
答：萨克拉门托。

问：Kozar-09 是什么？
A:
```


