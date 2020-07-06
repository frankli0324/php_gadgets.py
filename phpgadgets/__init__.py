import phpgadgets.payloads as payloads
import phpgadgets.sources as sources
import sys
import click
from tabulate import tabulate
from textwrap import wrap
import shutil


@click.group()
def main():
    pass


@main.command('chain')
def full_chain():
    raise NotImplementedError()


def _get_table(module):
    cols, lines = shutil.get_terminal_size((1000, 20))
    if cols < 74:
        print('please use a shell that could contain at least 75 chracters in a line')
        exit(-1)
    META_KEYS = ['name', 'params', 'description', 'version']
    META = {k: [] for k in META_KEYS}
    for m in module.__all__:
        for k in META_KEYS:
            val = getattr(module, m).META[k]
            if k == 'name':
                val = "\n".join(wrap(val, int(cols * 0.1)))
            elif k == 'params':
                val = "\n".join(wrap(', '.join(val), int(cols * 0.2)))
            elif k == 'description':
                val = "\n".join(wrap(val, int(cols * 0.5)))
            elif k == 'version':
                val = "\n".join(wrap(', '.join(val), int(cols * 0.2)))
            META[k].append(val)
    return tabulate(META, headers="keys", tablefmt="grid")


def list_payloads():
    print('Available Payloads:', _get_table(payloads), sep='\n')


def list_sources():
    print('Available Sources:', _get_table(sources), sep='\n')


@main.command('list')
def list_all():
    list_payloads()
    list_sources()


@main.command('serialize')
def serialize_only():
    pass
