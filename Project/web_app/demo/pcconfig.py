import pynecone as pc

class DemoConfig(pc.Config):
    pass

config = DemoConfig(
    app_name="demo",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)