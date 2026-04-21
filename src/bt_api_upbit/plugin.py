from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.plugins.metadata import PluginMetadata

metadata = PluginMetadata(
    name="bt_api_upbit",
    version="0.1.0",
    description="Upbit exchange plugin for bt_api",
    author="cloudQuant",
    author_email="yunjinqi@gmail.com",
    license="MIT",
)

plugin_info = PluginInfo(
    name="bt_api_upbit",
    version="0.1.0",
    metadata=metadata,
)
