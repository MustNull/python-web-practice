import click
from lib.commands.database import initdb, create, \
    run, drop_tables, rollback as rollback_func


@click.group()
def cli():
    pass

# ToDo: 把这些命令移到commands下,然后用register_command注册,避免该文件臃肿


@cli.command()
@click.option('--name', help='migrate name', required=True)
def create_migrate(name):
    create(name)


@cli.command()
@click.option('--name', help='migrate name', default=None)
def migrate(name):
    # ToDo: 使用click补全自动填充migrate name
    run(name)


@cli.command()
def drop_all_tables():
    drop_tables()


@cli.command()
@click.option('--name', required=True)
def rollback(name):
    # ToDo: 使用click补全自动填充migrate name
    rollback_func(name)


def register_command(cli):
    cli.add_command(click.command()(initdb))


register_command(cli)


if __name__ == '__main__':
    cli()
