# -*- coding: utf-8 -*-
from multiprocessing import Process, current_process
from multiprocessing import Manager


def func(name, m_list, m_dict):
    m_dict['name'] = '老杨'
    m_list.append('你好')


if __name__ == '__main__':
    with Manager() as mgr:  # with语句主要用于简化资源管理，确保在使用完资源后能够被正确地释放。这通常用于文件操作、数据库连接、网络连接等场景。
        m_list = mgr.list()
        m_dict = mgr.dict()
        m_list.append('Hello!!')
        # 两个进程不能直接相互使用对象，需要互相传递
        p1 = Process(target=func, args=('p1', m_list, m_dict))
        p2 = Process(target=func, args=('p2', m_list, m_dict))
        p1.start()
        p2.start()
        p1.join()  # 等待p1进程结束，主进程继续执行
        print(m_list)
        print(m_dict)
