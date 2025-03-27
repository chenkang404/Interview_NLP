核保评点系统：

当前部署环境：
   IP：221.231.13.230:45620
   目录：/apps/dev/Underwriting_Sys
   Git：git clone ssh://git@172.16.2.90:222/workspace/Underwriting_Sys/Underwriting_Sys.git

部署：
        启动服务
        bash start_user_xu_server.sh start
        重启服务
        bash start_user_xu_server.sh restart
        关闭服务
        bash start_user_xu_server.sh stop

注意事项：
	中再疾病函数对照表.xlsx 被很多服务调用，改动需谨慎。
	改动原则：
		对照表 由一个人统筹管理。
		对照表中，相似疾病的 匹配规则(列表和关键字)  要保持相似。

    	字段注释：
		def_name      # 函数名
		HBZS_def      # 小见空间核保助手-函数名
		HBZS_did      # 小见空间核保助手-疾病ID
		disease_n      # 自定义的疾病名
		disease_list    # 疾病匹配列表
		kwords          # 疾病匹配关键字
		# 阳光-除外话术
		CI
		MI
		ADB
		Life
		# 匹配手册
		ZZ_match_disease
		RZ_match_disease
		MZ_match_disease
		KL_match_disease

	在诸多其他服务中，该项目的核保手册代码 和 疾病函数对照表 是正统。
