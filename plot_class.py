import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.style.use('ggplot')
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class Figure_Canvas(FigureCanvas):
    def __init__(self,a,b,c,d,e,f,g,parent=None, width=6, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        super(Figure_Canvas,self).__init__(fig) # 初始化父类
        self.axes = fig.add_subplot(111,polar=True) # 调用figure下面的add_subplot方法
        #注意，self.a为作图假数据，self.g为显示真数据
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
    def draw_diagram(self):
        hexagon=[self.a,self.b,self.c,self.f,self.e,self.d]
        real=[self.g,self.b,self.c,self.f,self.e,self.d]
        label=['Hp','攻击','防御','速度','特防','特攻']
        N=len(hexagon)
        angles=np.linspace(0,2*np.pi,N,endpoint = False)
        hexagon=np.concatenate((hexagon,[hexagon[0]]))
        angles=np.concatenate((angles,[angles[0]]))
        real=np.concatenate((real,[real[0]]))
        # 绘制折线
        self.axes.plot(angles, hexagon, 'o-', linewidth=2)
        # 填充颜色
        self.axes.fill(angles, hexagon, alpha=0.25)
        # 添加每个特征的标签
        self.axes.set_thetagrids(angles * 180/np.pi, label,fontsize=20)
        #设置显示数值
        for i in range(0,len(hexagon)):
            self.axes.text(angles[i],hexagon[i],real[i],ha='center', va='bottom', fontsize=20)
        # 设置雷达图的范围
        self.axes.set_ylim(0,max(hexagon)*1.1)
        #设置极轴方向
        self.axes.set_theta_zero_location('N')
        #设置网格
        self.axes.grid(True)
        self.axes.tick_params('y',labelleft=False)
        
        




