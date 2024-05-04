#### 结合AI 实现实战编程题的智能判题

**示例：**
```markdown
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
```

###### 提供Java基础环境
实现类  **Demo**
```java
// TODO
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
```

接口 **OrderManager**

```java
public interface OrderManager {
    /**
     * 根据用户id、商品名称和数量生成一个新的订单
     *
     * @param userId      用户 id
     * @param productName 商品名称
     * @param quantity    商品数量
     * @return 新的订单编号
     */
    int createOrder(int userId, String productName, int quantity);

    /**
     * 输入订单编号和修改的商品名称和数量，如果订单存在并且没有被发货，则修改订单，否则抛出异常。
     *
     * @param orderId        订单编号
     * @param newProductName 商品名称
     * @param newQuantity    商品数量
     */
    void modifyOrder(int orderId, String newProductName, int newQuantity);

    /**
     * 输入订单编号，以字符串的形式返回订单的详细信息
     *
     * @param orderId 订单编号
     * @return 订单的详细信息，形如："userId: 1, name: Apple, quantity: 10, isShipped: false"，注意分割符是英文逗号及一个空格
     */
    String getOrder(int orderId);

    /**
     * 输入订单编号，如果订单存在并且没有被发货，则更改订单的发货状态并返回成功，否则抛出异常。
     *
     * @param orderId 订单编号
     */
    void shipOrder(int orderId);
}
```


**测试用例：**
```java
// 将使⽤ JUnit5 执⾏测试
// Tests will be executed using JUnit5

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class SampleTest {
    private OrderManager orderManager;

    @BeforeEach
    public void setup() {
        orderManager = new Demo();
    }

    @Test
    @DisplayName("测试创建订单")
    public void testCreateOrder() {
        int orderId = orderManager.createOrder(1, "Product 1", 5);
        String expected = "userId: 1, name: Product 1, quantity: 5, isShipped: false";
        assertEquals(expected, orderManager.getOrder(orderId));
    }

    @Test
    @DisplayName("测试修改已经发货的订单")
    public void testModifyShippedOrder() {
        int orderId = orderManager.createOrder(1, "Product 1", 5);
        orderManager.shipOrder(orderId);

        assertThrows(IllegalStateException.class, () -> orderManager.modifyOrder(orderId, "Product 2", 10));
    }

    @Test
    @DisplayName("测试获取不存在的订单")
    public void testGetNonexistentOrder() {
        assertThrows(IllegalArgumentException.class, () -> orderManager.getOrder(100));
    }

    @Test
    @DisplayName("测试发货订单")
    public void testShipOrder() {
        int orderId = orderManager.createOrder(1, "Product 1", 5);
        orderManager.shipOrder(orderId);
        String expected = "userId: 1, name: Product 1, quantity: 5, isShipped: true";
        assertEquals(expected, orderManager.getOrder(orderId));
    }
}
```

####  假设候选者该题的代码实现如下：
```java
// 以下为候选者答案
import java.util.HashMap;
import java.util.Map;

public class Demo implements OrderManager {

    private final Map<Integer, Order> orders;

    public Demo() {
        this.orders = new HashMap<>();
    }

    @Override
    public int createOrder(int userId, String productName, int quantity) {
        Order order = new Order(userId, productName, quantity);
        orders.put(order.getOrderId(), order);
        return order.getOrderId();
    }

    @Override
    public void modifyOrder(int orderId, String newProductName, int newQuantity) {
        Order order = orders.get(orderId);
        if (order == null) {
            throw new IllegalArgumentException("Order not found.");
        }

        if (order.isShipped()) {
            throw new IllegalStateException("Order has already been shipped and cannot be modified.");
        }

        order.setProductName(newProductName);
        order.setQuantity(newQuantity);
    }

    @Override
    public String getOrder(int orderId) {
        Order order = orders.get(orderId);
        if (order == null) {
            throw new IllegalArgumentException("Order not found.");
        }
        return order.toString();
    }

    @Override
    public void shipOrder(int orderId) {
        Order order = orders.get(orderId);
        if (order == null) {
            throw new IllegalArgumentException("Order not found.");
        }

        if (order.isShipped()) {
            throw new IllegalStateException("Order has already been shipped.");
        }

        order.setShipped(true);
    }

    public static class Order {
        private static int nextOrderId = 1;

        private final int orderId;
        private final int userId;
        private String productName;
        private int quantity;
        private boolean isShipped;

        public Order(int userId, String productName, int quantity) {
            this.orderId = nextOrderId++;
            this.userId = userId;
            this.productName = productName;
            this.quantity = quantity;
            this.isShipped = false;
        }

        public int getOrderId() {
            return orderId;
        }

        public int getUserId() {
            return userId;
        }

        public String getProductName() {
            return productName;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setProductName(String productName) {
            this.productName = productName;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        public boolean isShipped() {
            return isShipped;
        }

        public void setShipped(boolean isShipped) {
            this.isShipped = isShipped;
        }

        @Override
        public String toString() {
            return "userId: " + userId +
                    ", name: " + productName +
                    ", quantity: " + quantity +
                    ", isShipped: " + isShipped;
        }
    }
}
```

候选者做答后，我们需要根据候选者的解题思路、代码设计、代码质量等维度去评测候选者的代码  

```python
# code_review.py
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
```


**执行代码控制台返回输出如下：**
```
2024-05-04 18:02:15 - Prompt request sending time
2024-05-04 18:04:14 - Data reception completion time
Time spent on data requests:  118.96024823188782s

首先，我们来看一下测试用例的通过情况。已知该题目包含 4 个测试用例，候选人的代码通过了 4 个测试用例，即通过率为: 100%。这说明候选人的代码在功能上是正确的，能够满足题目的要求。

接下来，我们将从四个维度对候选人的代码进行评价：解题思路、代码质量、代码冗余和代码设计。

### 解题思路 (Problem-Solving Approach)

候选人的解题思路非常清晰。他首先创建了一个 `Order` 类来存储订单的信息，包括订单编号、用户id、商品名称、商品数量和发货状态。然后，他在 `Demo` 类中使用了一个 `HashMap` 来存储所有的订单，订单编号作为键，`Order` 对象作为值。这样，他就可以通过订单编号快速地找到对应的订单。在处理创建订单、修改订单、查询订单和发货订单的操作时，他都首先检查了订单是否存在，如果不存在则抛出异常。在修改订单和发货订单的操作中，他还检查了订单是否已经被发货，如果已经被发货则抛出异常。这些都符合题目的要求。因此，我认为他的解题思路处于9-10的等级，他展示了一种清晰、优化且深思熟虑的解题思路，捕获了问题的所有细节。所以，我给解题思路打分为：10分。

### 代码质量 (Code Quality)

候选人的代码质量非常高。他的代码组织得很好，易于阅读。他正确地使用了 Java 的异常处理机制来处理订单不存在或已经被发货的情况。他还正确地使用了 `HashMap` 来存储订单，使得通过订单编号查找订单的操作的时间复杂度为 O(1)。因此，我认为他的代码质量处于9-10的等级，他的代码在清洁度、可读性和优化方面都是模范。所以，我给代码质量打分为：10分。

### 代码冗余 (Code Redundancy)

候选人的代码没有冗余。他没有重复的代码，每个功能都只实现了一次。他使用了函数/方法来模块化代码，使得代码更加清晰和易于维护。因此，我认为他的代码冗余处于9-10的等级，他的代码是 DRY (Don't Repeat Yourself) 的，模块化和重用做得很好。所以，我给代码冗余打分为：10分。

### 代码设计 (Code Design)

候选人的代码设计非常好。他创建了一个 `Order` 类来封装订单的信息和操作，这是一种很好的面向对象的设计。他还在 `Demo` 类中使用了一个 `HashMap` 来存储所有的订单，这是一种很好的数据结构的选择。他的代码遵循了良好的设计原则，有适当的抽象和模块化的组件。因此，我认为他的代码设计处于9-10的等级，他的设计遵循了最佳实践，展示了对软件设计原则的深入理解。所以，我给代码设计打分为：10分。

总结一下，候选人的代码在所有维度上都表现得非常好。他的解题思路清晰，代码质量高，没有冗余，设计合理。他的代码不仅能够正确地解决问题，而且易于阅读和维护。因此，我认为他的代码是非常优秀的。

以下是我对候选人代码的评价结果（以JSON格式给出）：

```json
{
    "Problem-Solving Approach": 10,
    "Code Quality": 10,
    "Code Redundancy": 10,
    "Code Design": 10,
    "Test Case Pass Rate": "100%",
    "Summary (Chinese)": "候选人的代码在所有维度上都表现得非常好。他的解题思路清晰，代码质量高，没有冗余，设计合理。他的代码不仅能够正确地解决问题，而且易于阅读和维护。因此，我认为他的代码是非常优秀的。",
    "Summary (English)": "The candidate's code performs very well in all dimensions. His problem-solving approach is clear, the code quality is high, there is no redundancy, and the design is reasonable. His code can not only solve the problem correctly, but also easy to read and maintain. Therefore, I think his code is excellent."
}
```
```

#### 怎么设计 Prompt 

#### 首先先了解 什么是 Prompt Engineering？
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


