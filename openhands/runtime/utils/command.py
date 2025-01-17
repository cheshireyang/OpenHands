def get_remote_startup_command(
    port: int,
    sandbox_workspace_dir: str,
    username: str,
    user_id: int,
    plugin_args: list[str],
    browsergym_args: list[str],
):
    return [
        '/openhands/micromamba/bin/micromamba',
        'run',
        '-n',
        'openhands',
        'poetry',
        'run',
        'python',
        '-u',
        '-m',
        'openhands.runtime.action_execution_server',
        str(port),
        '--working-dir',
        sandbox_workspace_dir,
        *plugin_args,
        '--username',
        username,
        '--user-id',
        str(user_id),
        *browsergym_args,
    ]
