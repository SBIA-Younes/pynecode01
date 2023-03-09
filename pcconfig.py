import pynecone as pc

config = pc.Config(
    app_name="pynecode01",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
