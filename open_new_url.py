def Run_Sql_Excute(list_time,list_func_name,is_retry='0',routine_schema='dwd',is_param='0'):
    '''
    :param list_time: 时间列表 格式：'202001'
    :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
    :return: None
    '''
    # try:
    if is_retry == '0':
        if is_param == '0':
            for f_name in list_func_name:
                job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                try:
                    for t_time in list_time:
                        # print(list_time.index(t_time))
                        try:
                            with PgSQLContextManager() as db_cursor:
                                run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                start_time = dt.datetime.now()
                                sql = ''' select {routine_schema}."{f_name}"('{day_id}','{day_id}'); '''.format(routine_schema=routine_schema,day_id=t_time,f_name = f_name)
                                log.info("执行sql日期为：{}".format(t_time))
                                log.info(sql)
                                db_cursor.execute(sql)
                                end_date = dt.datetime.now()
                                log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=f_name,seconds=end_date-start_time))
                        except Exception as e :
                            # with PgSQLContextManager() as db_cursor:
                            #     failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            #     failed_use_time = (failed_end_date-run_start_date).seconds
                            #     sql_log = '''
                            #                                    insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                            #                         values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            #         routine_schema = routine_schema,
                            #         function_name=f_name, insert_time='now()', status_code='Failed',
                            #         start_date=t_time, end_date=t_time,retry_count = 'null',job_start_date=run_start_date,
                            #         job_end_date=failed_end_date,total_use_time = failed_use_time
                            #     )
                            #     db_cursor.execute(sql_log)
                            print(e)
                            # continue
                            raise ValueError('任务失败')
                            # continue
                    with PgSQLContextManager() as db_cursor:
                        job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        total_use_time = (job_end_date-job_start_date).seconds
                        sql_log = '''
                                   insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                        values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema = routine_schema,function_name=f_name, insert_time='now()', status_code='Successed',
                            start_date=list_time[0], end_date=list_time[-1],retry_count='null',job_start_date=job_start_date,job_end_date=job_end_date,
                            total_use_time = total_use_time
                        )
                        db_cursor.execute(sql_log)
                except Exception as e :
                            with PgSQLContextManager() as db_cursor:
                                failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                failed_use_time = (failed_end_date-run_start_date).seconds
                                sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                    routine_schema = routine_schema,
                                    function_name=f_name, insert_time='now()', status_code='Failed',
                                    start_date=t_time, end_date=t_time,retry_count = 'null',job_start_date=run_start_date,
                                    job_end_date=failed_end_date,total_use_time = failed_use_time
                                )
                                db_cursor.execute(sql_log)
        elif is_param == '1':
            try:
                with PgSQLContextManager() as db_cursor:
                    run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    start_time = dt.datetime.now()
                    sql = ''' select {routine_schema}."{f_name}"(); '''.format(
                        routine_schema=routine_schema, f_name=list_func_name[0])
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=list_func_name[0], seconds=end_date - start_time))
                    job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    total_use_time = (job_end_date - run_start_date).seconds
                    sql_log = '''
                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                        routine_schema=routine_schema, function_name=list_func_name[0], insert_time='now()',
                        status_code='Successed',
                        start_date='null', end_date='null', retry_count='null',
                        job_start_date=run_start_date, job_end_date=job_end_date,
                        total_use_time=total_use_time
                    )
                    db_cursor.execute(sql_log)
            except Exception as e:
                with PgSQLContextManager() as db_cursor:
                    failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    failed_use_time = (failed_end_date - run_start_date).seconds
                    sql_log = '''
                                                           insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                        routine_schema=routine_schema,
                        function_name=list_func_name[0], insert_time='now()', status_code='Failed',
                        start_date='null', end_date='null', retry_count='null', job_start_date=run_start_date,
                        job_end_date=failed_end_date, total_use_time=failed_use_time
                    )
                    db_cursor.execute(sql_log)
        else:
            print('参数输入错误，只能是0或1！')
    elif is_retry == '1':
        if is_param == '0':
            for f_name in list_func_name:
                job_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                try:
                    for t_time in list_time:
                        # print(list_time.index(t_time))
                        try:
                            with PgSQLContextManager() as db_cursor:
                                run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                start_time = dt.datetime.now()
                                sql = ''' select {routine_schema}."{f_name}"('{day_id}','{day_id}'); '''.format(routine_schema=routine_schema,day_id=t_time,f_name = f_name)
                                log.info("执行sql日期为：{}".format(t_time))
                                log.info(sql)
                                db_cursor.execute(sql)
                                end_date = dt.datetime.now()
                                log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=f_name,seconds=end_date-start_time))
                        except Exception as e :
                            # with PgSQLContextManager() as db_cursor:
                            #     failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            #     failed_use_time = (failed_end_date-run_start_date).seconds
                            #     sql_log = '''
                            #                                    insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                            #                         values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            #         routine_schema = routine_schema,
                            #         function_name=f_name, insert_time='now()', status_code='Failed',
                            #         start_date=t_time, end_date=t_time,retry_count = 'null',job_start_date=run_start_date,
                            #         job_end_date=failed_end_date,total_use_time = failed_use_time
                            #     )
                            #     db_cursor.execute(sql_log)
                            print(e)
                            # continue
                            raise ValueError('任务失败')
                            # continue
                    with PgSQLContextManager() as db_cursor:
                        job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        total_use_time = (job_end_date-job_start_date).seconds
                        sql_log = '''
                                   insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                        values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                            routine_schema = routine_schema,function_name=f_name, insert_time='now()', status_code='Successed',
                            start_date=list_time[0], end_date=list_time[-1],retry_count='1',job_start_date=job_start_date,job_end_date=job_end_date,
                            total_use_time = total_use_time
                        )
                        log.info("任务：{f_name}再次执行成功！".format(f_name))
                        db_cursor.execute(sql_log)
                except Exception as e :
                            Delete_log(routine_schema, f_name)
                            with PgSQLContextManager() as db_cursor:
                                failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                failed_use_time = (failed_end_date-run_start_date).seconds
                                sql_log = '''
                                                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                                    routine_schema = routine_schema,
                                    function_name=f_name, insert_time='now()', status_code='Failed',
                                    start_date=t_time, end_date=t_time,retry_count = '1',job_start_date=run_start_date,
                                    job_end_date=failed_end_date,total_use_time = failed_use_time
                                )
                                log.info("任务：{f_name}再次执行失败！".format(f_name))
                                db_cursor.execute(sql_log)

        elif  is_param == '1':
            try:
                with PgSQLContextManager() as db_cursor:
                    Delete_log(routine_schema, list_func_name[0])
                    run_start_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    start_time = dt.datetime.now()
                    sql = ''' select {routine_schema}."{f_name}"(); '''.format(
                        routine_schema=routine_schema, f_name=list_func_name[0])
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info('''执行任务名称：{name},执行完成时间为：{seconds}s'''.format(name=list_func_name[0],
                                                                           seconds=end_date - start_time))
                    job_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    total_use_time = (job_end_date - run_start_date).seconds
                    sql_log = '''
                               insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                    values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                        routine_schema=routine_schema, function_name=list_func_name[0], insert_time='now()',
                        status_code='Successed',
                        start_date='null', end_date='null', retry_count='1',
                        job_start_date=run_start_date, job_end_date=job_end_date,
                        total_use_time=total_use_time
                    )
                    db_cursor.execute(sql_log)
            except Exception as e:
                with PgSQLContextManager() as db_cursor:
                    failed_end_date = parse(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    failed_use_time = (failed_end_date - run_start_date).seconds
                    sql_log = '''
                                                           insert into dwd.run_table_log(routine_schema,function_name,insert_time,status,start_date,end_date,retry_count,job_start_date,job_end_date,total_use_time)
                                                values('{routine_schema}','{function_name}',{insert_time},'{status_code}','{start_date}','{end_date}','{retry_count}','{job_start_date}','{job_end_date}','{total_use_time}');'''.format(
                        routine_schema=routine_schema,
                        function_name=list_func_name[0], insert_time='now()', status_code='Failed',
                        start_date='null', end_date='null', retry_count='1', job_start_date=run_start_date,
                        job_end_date=failed_end_date, total_use_time=failed_use_time
                    )
                    db_cursor.execute(sql_log)
    else:
        print('is_retry参数输入错误，只能是0或1！')
