from Page.page_login import PageLogin


class LoginBusiness(PageLogin):

    # 登录好生源
    def pwd_login(self, username, pwd):
        self.select_pwd_login()
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login()
        info_list = list()
        info_list.append(self.get_current_url())
        info_list.append(self.get_title_info())
        return info_list
