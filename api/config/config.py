import os
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data/config.yaml")

def get_config():
    if not os.path.exists(config_path):
        logging.warning("config.yaml未建立，准备初始化")
        with open(config_path, "w") as f:
            f.write("""# 超级管理员设置
super_admin: 
super_admin_password:
# jwt设置
jwt:
    secret_key:
    expire_minutes:
# oidc设置
oidc:
    issuer:
    client_id:
    client_secret:
    callback_url:
    scope:
    token_url:
    userinfo_url:
# smtp设置
smtp:
    host:
    port:
    user:
    password:
    sender:
# 数据库设置
database:
    print_sql: False
# logging设置
logging:
    level: INFO
""")
        exit(1)
    with open(config_path, "r") as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    return config


class Config:
    def __init__(self):
        # SuperAdmin
        self.SUPER_ADMIN = get_config()["super_admin"]
        self.SUPER_ADMIN_PASSWORD = get_config()["super_admin_password"]
        # jwt
        self.JWT_SECRET_KEY = get_config()["jwt"]["secret_key"]
        self.JWT_EXPIRE_MINUTES = get_config()["jwt"]["expire_minutes"]
        # oidc设置
        self.ENABLE_OIDC = get_config()["oidc"]["enable"]
        self.OIDC_ISSUER = get_config()["oidc"]["issuer"]
        self.OIDC_CLIENT_ID = get_config()["oidc"]["client_id"]
        self.OIDC_CLIENT_SECRET = get_config()["oidc"]["client_secret"]
        self.OIDC_CALLBACK_URL = get_config()["oidc"]["callback_url"]
        self.OIDC_SCOPE = get_config()["oidc"]["scope"]
        self.OIDC_TOKEN_URL = get_config()["oidc"]["token_url"]
        self.OIDC_USERINFO_URL = get_config()["oidc"]["userinfo_url"]
        # SMTP设置
        self.SMTP_HOST = get_config()["smtp"]["host"]
        self.SMTP_PORT = get_config()["smtp"]["port"]
        self.SMTP_USER = get_config()["smtp"]["user"]
        self.SMTP_PASSWORD = get_config()["smtp"]["password"]
        self.SMTP_SENDER = get_config()["smtp"]["sender"]
        # 数据库设置
        self.PRINT_SQL = get_config()["database"]["print_sql"]
        # logging设置
        self.LOG_LEVEL = get_config()["logging"]["level"]

    def modify_config(self):
        #创建config.yaml备份
        with open(config_path, "r") as f:
            config = f.read()
        with open(config_path + ".bak", "w") as f:
            f.write(config)
        #修改config.yaml
        with open(config_path, "w") as f:
            config = f.read()
            config = yaml.load(config, Loader=yaml.FullLoader)








if __name__ == '__main__':
    get_config()