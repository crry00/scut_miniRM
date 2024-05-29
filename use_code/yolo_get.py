import torch
import cv2

class Yologet:
    model=None
    def __init__(self,path='./best.pt'):#加载模型
        self.model = torch.hub.load('ultralytics/yolov5', "custom", path=path)

    def getresult(self,img):#推理
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.model(img)
        return results

    def getlocation(self,img,threshold=0.75):
        re=self.getresult(img)
        results=re.xyxy[0]
        results = results[results[:, 4] >= threshold]#保留置信度大于阈值的
        if results.size(0)==14:#总识别的个数
            # 取出第二个数据（y）最小的五个目标，即最上面的5个小色块
            sorted_results = results[results[:, 1].argsort()][:5]
            location_results = results[results[:, 1].argsort()][5:14]
            # 根据这五个目标的第一个元素大小（x）将最后一个元素按升序排列
            sorted_results = sorted_results[sorted_results[:, 0].argsort()]
            # 初始化一个空列表用于存放结果
            remaining_sorted_results = []
            # 遍历sorted_results中的每一行，按顺序在results中查找最后一个元素（类别）与该行相同的行，并提取出来
            for row in sorted_results:#按顺序保存坐标
                matching_rows = location_results[location_results[:, -1] == row[-1]]
                matchrow=matching_rows.tolist()[0]
                centerX=int((matchrow[0]+matchrow[2])/2)
                centerY=int((matchrow[1]+matchrow[3])/2)

                remaining_sorted_results.append([centerX,centerY])
            # print(remaining_sorted_results)
            return remaining_sorted_results
        else:
            return None