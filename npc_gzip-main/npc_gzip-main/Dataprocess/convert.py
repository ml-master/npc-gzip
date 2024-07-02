import json
import random

if __name__ == '__main__':
    file_Convert = "/public/zs/npc/convert_dataset/"
    file_path = "/public/zs/npc/fakenews/gossipcop_v3-1_style_based_fake.json"
    file1_path = "/public/zs/npc/fakenews/gossipcop_v3-2_content_based_fake.json"
    file2_path = "/public/zs/npc/fakenews/gossipcop_v3-3_integration_based_fake_tn200.json"
    file3_path = "/public/zs/npc/fakenews/gossipcop_v3-4_story_based_fake.json"
    file4_path = "/public/zs/npc/fakenews/gossipcop_v3-5_style_based_legitimate.json"
    file5_path = "/public/zs/npc/fakenews/gossipcop_v3-7_integration_based_legitimate_tn300.json"
    # file_path = "/public/zs/npc/fakenews/gossipcop_v3-1_style_based_fake.json"
    file_train_convert = file_Convert+file_path.split(".")[0].split('/')[-1]+"_"+"train_convert.txt"
    file1_train_convert = "/public/zs/npc/custom_dataset/train1.txt"
    file2_train_convert = "/public/zs/npc/custom_dataset/train2.txt"
    file3_train_convert = "/public/zs/npc/custom_dataset/train3.txt"
    file4_train_convert = "/public/zs/npc/custom_dataset/train4.txt"
    file5_train_convert = "/public/zs/npc/custom_dataset/train5.txt"
    file_test_convert = file_Convert+file_path.split(".")[0].split('/')[-1]+"_"+"test_convert.txt"
    file1_test_convert = "/public/zs/npc/custom_dataset/test1.txt"
    file2_test_convert = "/public/zs/npc/custom_dataset/test2.txt"
    file3_test_convert = "/public/zs/npc/custom_dataset/test3.txt"
    file4_test_convert = "/public/zs/npc/custom_dataset/test4.txt"
    file5_test_convert = "/public/zs/npc/custom_dataset/test5.txt"
    with open(file5_path, 'r', encoding='utf-8') as file:
        # 使用json.load()方法解析JSON数据
        ids = json.load(file)
    count = 0
    print(len(ids))
    list_number = range(0,len(ids)-1)
    print(list_number)
    test_number = int(len(ids)*0.3)
    train_number = len(ids) - test_number
    print(test_number)
    print(train_number)
    # print(random.sample(list_number,int(len(ids)*0.3)))
    print(type(ids))
    id_tests = random.sample(list(ids),test_number)
    # id_trains = random.sample(list(ids),train_number)
    # id_trains = list_number[id_tests,:]
    print(id_tests)
    count =0
    origin_text1=""
    origin_label1=""
    origin_text2=""
    origin_label2=""
    origin_text=""
    origin_label=""
    for id in ids:
        if file2_path == "/public/zs/npc/fakenews/gossipcop_v3-3_integration_based_fake_tn200.json" or file5_path == "/public/zs/npc/fakenews/gossipcop_v3-7_integration_based_legitimate_tn300.json":
            origin_text1 = "{"+ids[id]['doc_1_text']+"}"
            origin_label1 = "{"+ids[id]['doc_1_label']+"}"
            origin_text2 = "{"+ids[id]['doc_2_text']+"}"
            origin_label2 = "{"+ids[id]['doc_2_label']+"}"

        else:
            origin_text = "{"+ids[id]['origin_text']+"}"
            origin_label = "{"+ids[id]['origin_label']+"}"

        flag = True
        for name in id_tests:
            if name==id:
                with open(file5_test_convert, 'a', encoding='utf-8') as file:
                    file.write(origin_label1+"\t" + origin_text1.replace("\n", " "))
                    file.write("\n")
                    file.write(origin_label2+"\t" + origin_text2.replace("\n", " "))
                    # file.write(origin_label + "\t" + origin_text.replace("\n", " "))
                    file.write("\n")
                count= count+1
                flag = False
                break
        if flag == True:
            with open(file5_train_convert,'a',encoding = 'utf-8') as file:
                file.write(origin_label1+"\t" + origin_text1.replace("\n", " "))
                file.write("\n")
                file.write(origin_label2+"\t" + origin_text2.replace("\n", " "))
                # file.write(origin_label+"\t"+origin_text.replace("\n"," "))
                file.write("\n")
    print(count)
        # print(id)
    # print(id_trains)

    # 打印解析后的Python对象
    # for id in ids:
    #     origin_text = "{"+ids[id]['origin_text']+"}"
    #     origin_label = "{"+ids[id]['origin_label']+"}"
    #     print(origin_text+"\n"+origin_label)
    #     if count < 3000:
    #         with open(file1_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     # break
    #     if count<15000and count >= 13000:
    #         with open(file1_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     else:
    #         with open(file1_train_convert, 'a', encoding='utf-8') as file:
    #             file.write(origin_label + "\t" + origin_text.replace("\n", " "))
    #             file.write("\n")
    #     count= count + 1


    # print(file_test_convert)
    # print(file_train_convert)
    # print(file_convert)
    # 打开文件并读取内容
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     # 使用json.load()方法解析JSON数据
    #     ids = json.load(file)
    # count = 0
    # print(len(ids))
    # # 打印解析后的Python对象
    # for id in ids:
    #     origin_text = "{"+ids[id]['origin_text']+"}"
    #     origin_label = "{"+ids[id]['origin_label']+"}"
    #     print(origin_text+"\n"+origin_label)
    #     if count < 3000:
    #         with open(file_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     # break
    #     if count<15000and count >= 13000:
    #         with open(file_test_convert,'a',encoding = 'utf-8') as file:
    #             file.write(origin_label+"\t"+origin_text.replace("\n"," "))
    #             file.write("\n")
    #     else:
    #         with open(file_train_convert, 'a', encoding='utf-8') as file:
    #             file.write(origin_label + "\t" + origin_text.replace("\n", " "))
    #             file.write("\n")
    #     count= count + 1
        # if count == 10000:
        # break


    # print(data[1])
    # print(data['name'])  # 提取name字段的值
    # print(data['age'])  # 提取age字段的值

