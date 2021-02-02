from argparse import ArgumentParser
from bug_api import BugAPI



if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument(
        'command',
        choices=['list','add','del'])
    parser.add_argument('text',nargs='?')
    args=parser.parse_args()
    server,db,port='localhost','mypostgres',8069
    user,pwd='admin','admin'
    api=BugAPI(server,port,db,user,pwd)

    if args.command=='list':
        bugs=api.read()
        for bug in bugs:
            print('%(id)d[%(is_closed)s]%(name)s'%bug)

    if args.command=='add':
        bug_id=api.write(args.text)
        print('bug%d created.'%bug_id)

    if args.command=='del':
        api.unlink(int(args.text))
        print('bug%s deleted.'%args.text)
