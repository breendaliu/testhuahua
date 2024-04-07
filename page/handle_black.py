import logging

from selenium.webdriver.common.by import By
# import allure

def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        # todo “以后再说”报错，当前提示无法弹出，待再次验证
        # _black_list = [
        #     # 同意用户协议
        #     (By.ID, "com.kejian.huahua:id/tv_positive"),
        #     # 跳过启动页
        #     (By.ID, "com.kejian.huahua:id/iv_into"),
        #     # 同意隐私协议
        #     (By.ID, "com.kejian.huahua:id/iv_chose_state"),
        #     # 选择登录方式页面，同意用户协议
        #     (By.ID, "com.kejian.huahua:id/iv_chose_state"),
        #     # 获取位置权限
        #    # (By.ID, "com.android.permissioncontroller:id/permission_allow_always_button"),
        #     #(By.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button"),
        #     # 关闭首页弹窗，添加黑名单失败
        #     (By.ID, "com.kejian.huahua:id/iv_del_img")
        #
        # ]
        from page.base_page import BasePage
        instance: BasePage = args[0]  # 接入self
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            # 清空错误次数
            _error_num = 0
            instance.set_implicitly_wait(20)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
                #.attach(content, attachment_type=.attachment_type.PNG)
            logging.error("element not found, handle black list")
            instance.set_implicitly_wait(10)
            # 如果次数太多，就退出异常逻辑，直接报错
            if instance._error_num > instance._max_err_num:
                instance._error_num = 0
                raise e
            # 记录一直异常的次数
            instance._error_num += 1
            # 对黑名单里的弹框进行处理
            for ele in instance._black_list:
                logging.info(ele)
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    # 继续寻找原来的正常控件
                    return wrapper(*args, **kwargs)
            # 如果黑名单也没有，就报错
            logging.warning("black list no one foound")
            raise ValueError("元素未找到，且不在黑名单中")

    return wrapper
