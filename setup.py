# -*- coding: utf-8 -*-

def setup_tileviews(filepath):
    with open(filepath) as sqlcode:
        sql = sqlcode.read()
    db.executesql(sql)
    db.commit()


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description = """
        To be run with command line (add -h for help):

        <you>:~/<path>/<to>/apps$ python -m <app>.itile.setup -h

        """,
        formatter_class = argparse.RawTextHelpFormatter
    )

    try:
        from ..planetstore.common import db
    except Exception as err:
        message = """You are running this script without the necessary environment.
        Please read the documentation here below."""
        print(err)
        parser.print_help()
        raise Exception(message)
    else:
        import os
        import inspect

    here = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    parser.add_argument("-p", "--path",
        help = 'Path to sql file resources',
        default = os.path.join(here, 'resources')
    )

    parser.add_argument("-f", "--file",
        help = 'The sql file resource name',
        default = "views.sql"
    )

    args = parser.parse_args()

    filepath = os.path.join(args.path, args.file or '').rstrip('/')
    setup_tileviews(filepath)
