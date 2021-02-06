name: str = ...
pkg_name: str = ...
version: str = ...
dist_info: str = ...
content: dict[str, str] = ...

def build_wheel(
    wheel_directory: str,
    metadata_directory: str | None = ...,
    config_settings: dict[str, str] | None = ...,
) -> str: ...
def get_requires_for_build_wheel(
    config_settings: dict[str, str] | None = ...
) -> list[str]: ...
def build_sdist(
    sdist_directory: str, config_settings: dict[str, str] | None = ...
) -> str: ...
def get_requires_for_build_sdist(
    config_settings: dict[str, str] | None = ...
) -> list[str]: ...
