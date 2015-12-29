from time import strftime

# import mysql
import pytest

import MySQLdb
from time import gmtime, strftime


def pytest_addoption(parser):
    parser.addoption(
        '--bedrock',
        action='store',
        dest='bedrock',
        metavar='bedrock',
        help='marks tests so they use Bedrock branch')
    parser.addoption(
        '--skipsprod',
        action='store',
        dest='skipsprod',
        metavar='skip',
        help='marks tests as staging only and skips them on production')


def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        'bedrock: marks tests so they use Bedrock branch')


def pytest_runtest_setup(item):
    if hasattr(item.obj, 'bedrock') and '/b' not in item.config.option.base_url:
        item.config.option.base_url = item.config.option.base_url + '/b'
    else:
        item.config.option.base_url = item.config.option.base_url.replace('/b', '')
    if hasattr(item.obj, 'skipsprod') and 'allizom.org' not in item.config.option.base_url:
        pytest.skip("skipping tests marked staging only")

@pytest.fixture(autouse=True)
def session_id(mozwebqa):
    print 'Session ID: {}'.format(mozwebqa.selenium.session_id)
    str = '{}\n'.format(mozwebqa.selenium.session_id)
    str_session_id = '{}'.format(mozwebqa.selenium.session_id)

    with open ("/home/adi/python.txt", "a") as myfile:
        myfile.write(str)

    current_time = strftime("%Y-%m-%d %H:%M")
    print('Current time is: {}'.format(current_time))

    """ Connect to MySQL database """
    try:
        conn = MySQLdb.connect(host='localhost',
                                ser='root',
                                passwd='',
                                db='bedrock_sessionIDs')
        # if conn.is_connected():
        #     print('Connected to MySQL database')

        c = conn.cursor()
        tblQuery = """CREATE TABLE IF NOT EXISTS test_session_ids (id int unsigned auto_increment not NULL,
        session_id VARCHAR(60) not NULL,
        date_created VARCHAR(100) not NULL,
        primary key(id))"""
        c.execute(tblQuery)
        print('............Successfully created table .......')
        insQuery = """insert into test_session_ids (session_id, date_created) values ('%s', '%s')"""
        # insQuery = """insert into test_session_ids (session_id, date_created) values ('whatever', 'whatever')"""
        c = conn.cursor()
        c.execute("insert into test_session_ids (session_id, date_created) values (%s, %s)", (str_session_id, current_time))
        # c.execute(insQuery)
        print('............Successfully ADDED to table .......')
        conn.commit()

    except:
        print ('UNABLE TO PERFORM DATABASE OPERATION')

    finally:
        conn.close()


