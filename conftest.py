# conftest.py文件
# coding:utf-8

import pytest
import time
import allure
from common.basedriver import BaseDriver


driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中\
    :param item:
    """
    print("item", item)

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot_base64()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:300px;height:600px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
            print("到这里了吗")
            with allure.step('添加失败截图...'):
                print("yahahah")
                allure.attach(_capture_screenshot(), "失败截图", allure.attachment_type.PNG)
            print("allure截图了吗")
        report.extra = extra


def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    # 页面稳定后截图
    time.sleep(1)
    # print(driver.get_screenshot_as_png())
    # return driver.get_screenshot_as_base64()
    return driver.get_screenshot_as_png()


def _capture_screenshot_base64():
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    # 这是单例模式吗？？？全局范围内只生成一个session
    global driver
    if driver is None:
        driver = BaseDriver().get_android_driver()
        time.sleep(5)
    # yield driver
    # driver.quit()
    # print("执行了关闭driver的动作")

    print("实例化driver", driver)
    return driver


# @pytest.fixture(scope='session', autouse=True)
# def close_driver():
#     yield driver
#     driver.quit()
#     print(driver, "driver的关闭操作")


@pytest.fixture(autouse=True)
def operal_app(request):
    driver.launch_app()

    def fin():
        driver.close_app()

    request.addfinalizer(fin)



