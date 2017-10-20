# coding=utf8
from pymongo import MongoClient
import time

host = '172.16.10.130'
port = 22000
"""
陪我测试mongo
"""

class Statistics():

    def __init__(self,port=22000, host='172.16.10.130'):
        self.clint = MongoClient(host, port)
        self.db = self.clint.sneaky
        # self.collection = self.db.pw_live_room
        self.collection = self.db.pw_live_guest

    def statistics(self, start_time, end_time):

        start_stamp = time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))
        end_stamp = time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S'))
        if start_stamp > end_stamp:
            return 0
        online_room_sum = self.collection.find({'$or': [{'$or':[{'create_time':
                                                {'$gte': start_stamp, '$lte': end_stamp}},
                                                {'close_time': {'$gte': start_stamp, '$lte': end_stamp}}]},
                                                {'create_time':{'$lte':start_stamp},'close_time':{'$gte':end_stamp}}]}).count()
        owner_voice_score_sum =self.collection.find({'owner_voice_score':0}).count()
        # data = self.collection.find().sort([('create_time', -1)])
        # for item in data:
        #     try:
        #         create_time = item['create_time']
        #         close_time = item['close_time']
        #         if start_stamp < create_time < end_stamp or start_stamp < close_time < end_stamp:
        #             online_room_sum += 1
        #         elif create_time < start_stamp < end_stamp < close_time:
        #             online_room_sum += 1
        #     except Exception as e:
        #         pass
        #
        #
        #
        #     try:
        #         if int(item['owner_voice_score']) == 0:
        #             owner_voice_score_sum += 1
        #     except Exception as e:
        #         pass
        print online_room_sum
        print owner_voice_score_sum


# timestamp = time.time()
# time_local = time.localtime(timestamp)
# current = time.strftime("%Y-%m-%d 00:00:00",time_local)
# print current
# timestamp = time.mktime(time.strptime(current,'%Y-%m-%d %H:%M:%S')) + 3600
# add_hour = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
# print add_hour
# print add_hour - current
#
# print time.mktime(time.strptime(current,'%Y-%m-%d %H:%M:%S'))
#

ins =Statistics()
#ins.statistics('2017-08-28 00:00:00', '2017-08-28 21:00:00')
data = ins.collection.find({"live_id": "555_1507891572_live"})
for item in data:
    print item