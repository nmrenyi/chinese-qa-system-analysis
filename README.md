# Chinese QA System
Computational Linguistics, 2022Fall, Tsinghua University, Homework 1

## Requirements
20 questions, with two distinct descriptions of each question, composed of 5 kinds of questions, 4 questions in each kind.

问题分为如下5个类别，请同学们对每个类别提4个问题。
1. “是什么(What)”型问题，如“光合作用的产物是什么?”
2. “什么时候(When)”型问题，如“中华人⺠共和国是什么时候建立的?”
3. “什么地点(Where)”型问题，如“爱因斯坦是在哪里出生的?”
4. “是谁(Who)型问题”，如“中国历史上第一个皇帝是谁?”
5. “哪一个(Which)型问题”，如“哪座山是中国最高的?”“二氧化碳和氧气中哪一个能令澄清石灰水变浑浊?”

为了保证问题的难度，每个问题应保证在系统测试中，至少有2个系统在该问题的至少一个问法上答错。

将问题输入给如下中文问答系统中进行测试，得到系统回答。系统的输出与标准答案意思一致即可认为正确，不必
文字上与标准答案完全一样。需要测试的代表性问答系统包括:

1. 百度文心:https://wenxin.baidu.com/moduleApi/ernie3 中的自由问答
2. 智源悟道:https://open.wudaoai.com/ 需要进行注册，注册后在“体验中心”中选择“智能问答”即可
3. 源1.0:需要先访问https://air.inspur.com/home ，注册用户并点击首⻚的“申请API”，填写相关信息后等待批
准通过。批准通过后访问http://221.194.179.88:11016/?question=中国第一位女皇帝是谁&usrname=xx&phone=xxx ，将自己的用户名，电话和问题填入其中，即可得到答案。据测试， 源1.0只在工作日批准申请且需要数个工作日，为避免赶不上作业截止日期，请同学们提前申请。

Analyze the accuracy and consistency of each QA system. Analyze the answering capability on different kinds of questions for each QA system. Do case study and analyze.

## Submission
`qa_submission.xlsx` includes:
1. 问题编号
2. 问法编号
3. 问题类别
4. 问题
5. 标准答案
6. 标准答案来源1(网址)
7. 标准答案来源1(具体段落)
8. 标准答案来源2(网址)
9. 标准答案来源2(具体段落)
10. 各个模型的回答及其正确与否

Besides the `qa_submission.xlsx`, submit report containing the required analysis in pdf format to the web school.

## Steps
1. reformat `SQuAD2.0` dataset to required format in `qa_submission.numbers`, with ground truth answer from `SQuAD2.0` dataset (answer text, answer position, quesition id, etc., enough for locating the answer).
2. translate the questions into Chinese with opensource translators
    - [Google Translation](https://cloud.google.com/translate)
    - [Microsoft Translation](https://www.microsoft.com/en-us/translator/business/trial/)
3. test the questions on the QA systems
4. evaluate the correctness
5. analyze and write report

## Resources
1. [SQuAD2.0: The Stanford Question Answering Dataset](https://rajpurkar.github.io/SQuAD-explorer/), [Dev Set v2.0](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json)
