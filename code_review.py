import asyncio
import queue
from sydney import SydneyClient
import time
from datetime import datetime

# 测评 Prompt
SYSTEM_TEMPLATE = """\
你是一名世界顶级的软件工程师，你精通多种编程语言和编程框架。你的任务是要对一名候选人提交的代码进行评价和打分。你的评价结果将决定候选人是否通过测评，因此你的评价绝对要是专业的、精确的且合理的！
"""

# 题目要求
question = """\
###### 题目描述
我们正在开发一个订单管理系统，你需要编写一部分核心功能代码。系统应具有以下功能：
1. 创建订单：输入用户id、商品名称和数量，返回一个新的订单编号。
2. 修改订单：输入订单编号、修改的商品名称和数量，如果订单存在并且没有被发货，则修改订单，否则抛出异常。
3. 查询订单：输入订单编号，以字符串的形式返回订单的详细信息，包括用户id、商品名称、商品数量和发货状态。
4. 发货订单：输入订单编号，如果订单存在并且没有被发货，则更改订单的发货状态并返回成功，否则抛出异常。

具体需求如下：
- 对于每一个新的订单，系统必须生成一个唯一的订单编号
- 如果试图修改不存在的订单，或者已经被发货的订单，系统应抛出异常
- 如果试图查询不存在的订单，系统应抛出异常
- 如果试图发货不存在的订单，或者已经被发货的订单，系统应抛出异常
- 不存在的订单抛出 IllegalArgumentException异常，且异常信息为 "Order not found."
- 修改已经被发货的订单，抛出 IllegalStateException异常，且异常信息为 "Order has already been shipped."

现在，已经定义好了订单管理的相关接口 **OrderManager**，请你完成它的实现类 **Demo**。

###### 提示
你可以在 **SampleTest.java** 中看到本题的测试逻辑
点击左侧工具栏的 “文件” 按钮，你可以看到本题所使用的类
题目要求返回的字符串格式在 **OrderManager** 类中已经说明，不在赘述
"""

# 代码库中*已经存在*的主要源码文件
codebase_files = """\
public class Demo implements OrderManager {

    @Override
    public int createOrder(int userId, String productName, int quantity) {
        return -1;
    }

    @Override
    public void modifyOrder(int orderId, String newProductName, int newQuantity) {
        
    }

    @Override
    public String getOrder(int orderId) {
        return null;
    }

    @Override
    public void shipOrder(int orderId) {
       
    }
}
"""

# 语言类型
programming_env = """Java编程语言"""

# 候选人在已有代码基础上所作出的改动（以Diff格式给出）
codebase_diffs = """\
1a2,4
> import java.util.HashMap;
> import java.util.Map;
> 
5a9,13
>     private final Map<Integer, Order> orders;
> 
>     public Demo() {
>         this.orders = new HashMap<>();
>     }
8c16
<         return -1;
---
>         Order order = new Order(userId, productName, quantity);
>         orders.put(order.getOrderId(), order);
>         return order.getOrderId();
14,15c22,30
<         
<     }
---
>         Order order = orders.get(orderId);
>         if (order == null) {
>             throw new IllegalArgumentException("Order not found.");
>         }
> 
>         if (order.isShipped()) {
>             throw new IllegalStateException("Order has already been shipped and cannot be modified.");
>         }
> 
>         order.setProductName(newProductName);
>         order.setQuantity(newQuantity);
20c35,41
<         return null;
---
>         Order order = orders.get(orderId);
>         if (order == null) {
>             throw new IllegalArgumentException("Order not found.");
>         }
>         return order.toString();
26c47,57
<        
---
>         Order order = orders.get(orderId);
>         if (order == null) {
>             throw new IllegalArgumentException("Order not found.");
>         }
> 
>         if (order.isShipped()) {
>             throw new IllegalStateException("Order has already been shipped.");
>         }
> 
>         order.setShipped(true);
31a63,95
> 
>     public static class Order {
>         private static int nextOrderId = 1;
> 
>         private final int orderId;
>         private final int userId;
>         private String productName;
>         private int quantity;
>         private boolean isShipped;
> 
>         public Order(int userId, String productName, int quantity) {
>             this.orderId = nextOrderId++;
>             this.userId = userId;
>             this.productName = productName;
>             this.quantity = quantity;
>             this.isShipped = false;
>         }
> 
>         public int getOrderId() {
>             return orderId;
>         }
> 
>         public int getUserId() {
>             return userId;
>         }
> 
>         public String getProductName() {
>             return productName;
>         }
> 
>         public int getQuantity() {
>             return quantity;
>         }
> 
>         public void setProductName(String productName) {
>             this.productName = productName;
>         }
> 
>         public void setQuantity(int quantity) {
>             this.quantity = quantity;
>         }
> 
>         public boolean isShipped() {
>             return isShipped;
>         }
> 
>         public void setShipped(boolean isShipped) {
>             this.isShipped = isShipped;
>         }
> 
>         @Override
>         public String toString() {
>             return "userId: " + userId +
>                     ", name: " + productName +
>                     ", quantity: " + quantity +
>                     ", isShipped: " + isShipped;
>         }
>     }
"""

# 测试用例的个数：4
test_total_num = "4"

# 通过测试用例个数：4 （候选者的答案可以通过四个测试用例） 
test_pass_num = "4"

# 通过率为：100%
test_pass_rate = "100%"


HUMAN_TEMPLATE = f"""\
# 测试题信息

## 以下是测试题的详细要求（以Markdown格式给出）

```Markdown
{question}
```

## 以下是代码库中*已经存在*的主要源码文件

{codebase_files}

候选人需要在这些已有的源码文件上做改动，以完成测试题目。

## 以下编程环境相关信息

候选人所使用的【编程语言/编程框架】是 {programming_env}。

# 候选人的答案

以下是候选人在已有代码基础上所作出的改动（以Diff格式给出）：

```Diff
{codebase_diffs}
```

你必须要区分候选人的代码和码库中的已有代码，你*只需要*针对候选人的代码改动进行评价，*不要*评价代码库中的已有代码。

# 评价标准

## 评价指南

Evaluate  on a 0-10 scale, focusing on the code additions. Assign a 0 score only if the solution is entirely irrelevant or non-functional, reflecting the inability to solve the problem. Provide detailed explanations for each dimension, ensuring the evaluation considers both the problem and the code. Assess Code Redundancy in relation to other dimensions' observations and scores.

## 评价维度及等级描述

### 解题思路 (Problem-Solving Approach)

0: Code does not make sense, there is no actual logic or code within the function, and no solution is provided based on the problem.
1-2: Has difficulty understanding the problem. No clear strategy to solve.
3-4: Shows basic understanding but struggles with forming a complete solution.
5-6: Understands the problem and has a general approach, but misses some edge cases or details.
7-8: Has a solid approach to solving the problem and considers various scenarios.
9-10: Demonstrates a clear, optimized, and well-thought-out approach, capturing all nuances of the problem.

### 代码质量 (Code Quality)

0: The diff code is completely irrelevant to the problem and has no practical significance.
1-2: Code is disorganized, lacks clarity, and has multiple errors.
3-4: Code has some organization but contains errors or lacks readability.
5-6: Code is mostly organized and functional, with minor issues or inefficiencies.
7-8: Code is clean, follows best practices, and is mostly optimized.
9-10: Code is exemplary in terms of cleanliness, readability, and optimization.

### 代码冗余 (Code Redundancy)

0: Code does not solve the problem at all and redundancy cannot be assessed.
1-2: Code contains many repeated sections and lacks modularization.
3-4: Some parts of the code are unnecessarily repetitive.
5-6: Moderate level of redundancy but shows effort in reducing it.
7-8: Minimal redundancy with decent use of functions/methods to modularize.
9-10: Code is DRY (Don't Repeat Yourself) with optimal modularization and reuse.

### 代码设计 (Code Design)

0: Code does not solve the problem at all, lacks structure and design related to the problem.
1-2: Code lacks a coherent structure and design. Components seem disjointed.
3-4: Basic structure is present, but design principles are mostly ignored.
5-6: Demonstrates a fair understanding of code design but lacks in some areas of abstraction or modularization.
7-8: Good design practices are followed with appropriate abstractions and modular components.
9-10: Outstanding design, following best practices, and demonstrating a deep understanding of software design principles.

已知该题目包含 {test_total_num} 个测试用例，候选人的代码通过了 {test_pass_num} 个测试用例，即通过率为: {test_pass_rate}

你必须一步一步思考。

首先，你需要分析测试用例的通过情况，并据此信息对候选人代码准确性作出判断。
然后，你需要*一个维度一个维度地*对候选人的答案作出评价。在评价每个维度的时候你都要一步一步思考：
  1. 从该维度的视角出发，对候选人的代码改动进行整体分析。你的分析必须要聚焦于当前维度，必须要跟当前维度高度相关。
  2. 将候选人代码中的具体表现与评价标准中的等级描述进行对照，评判出候选人代码处于哪个等级。你需要引用候选人的代码以及评价标准中的描述内容来佐证你的判断，绝对不能凭主观意见做判断。
  3. 最后，给出一个合理的评分（0-10）。
最后，在所有维度都评价完成之后，你需要对评价结果进行总结，并使用JSON格式输出最终评价结果（包含中文版本和英文版本）。

[format_instructions]

要求：
* 你*只需要*针对候选人的代码改动进行评价，*不要*评价代码库中的已有代码。
* 你必须严格依照评价标准进行评分，不能有任何主观判断。
* 你必须对所有维度作出评价，*绝对不能*遗漏任何一个维度。
* 你必须一步一步思考，*绝对不能*直接输出评价结果，不能跳过任何步骤。
* 如果候选人的改动内容为空，表示候选人未对代码作出任何改动。这种情况下所有评价维度都可判为0分。

接下来，你将输出一条很长很长的回复。在这条回复中你必须完成所有的步骤，输出所有必须的内容，绝对不能中断，不能有任何省略。
"""


# 发送 Prompt 请求
async def ask_question_copilot(prompt: str, conversation_style: str) -> dict:
    start_time = time.time()
    start_formatted_time = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
    send_message = "Prompt request sending time"
    print(f"{start_formatted_time} - {send_message}")
    async with SydneyClient() as sydney:
        await sydney.reset_conversation(style=conversation_style)
        response = await sydney.ask(prompt)
        end_time = time.time()
        end_formatted_time = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
        spend_time = end_time - start_time
        data_dict = {
            "send_start_time" : start_formatted_time,
            "accept_over_time" : end_formatted_time,
            "spend_time": spend_time,
            "response": response
        }
        receive_message = "Data reception completion time"
        print(f"{end_formatted_time} - {receive_message}")
        spend_time_message = "Time spent on data requests"
        print(f"{spend_time_message}:  {spend_time}s")
        return data_dict


if __name__ == "__main__":
    combined_template = SYSTEM_TEMPLATE + "/n" + HUMAN_TEMPLATE
    data = asyncio.run(ask_question_copilot(combined_template,"precise"))
    print(data["response"])











