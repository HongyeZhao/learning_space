import matlab.engine
import time


def exec_csp(self):
    # 启动 MATLAB 引擎
    eng = matlab.engine.start_matlab()
    eng.cd("../bin/CSP/", nargout=0)

    # 创建一个列表用来捕获输出
    output = []

    # 启动 MATLAB 代码的执行
    eng.eval("disp('Starting DCS_ALL...');", nargout=0)

    # 定义一个 MATLAB 代码片段，该片段会循环输出信息
    eng.eval("""
        for i = 1:5
            disp(['Processing step ' num2str(i)]);
            pause(1);  % 模拟处理时间
        end
    """, nargout=0)

    # 实时获取输出
    while True:
        time.sleep(0.1)  # 等待一段时间
        # 在这里你可以从 MATLAB 获取输出
        # 例如使用一些特定的函数来检查状态
        # 这部分具体实现可能因 MATLAB 代码而异
        print()

        # 检查 MATLAB 是否还在运行
        if not eng.isrunning():
            break

    # 完成后，可以将输出保存到显示控件
    # self.out_show.append('\n'.join(output))

    # 关闭 MATLAB 引擎
    eng.quit()
