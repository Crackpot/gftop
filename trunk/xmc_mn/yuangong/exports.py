#coding=utf8
from data_exporter.base import Export
from models import Gongzhong

class GongzhongExport(Export):
    filename = 'gongzhong'
    columns = ('id', 'gongzhong')
    headers = ('id', 'gongzhong')
    directory = 'gongzhong'
    def get_query(self, offset=None, limit=None):
        qs = Gongzhong.objects.all()

        if offset and limit:
            return qs[offset:limit]

        if limit:
            return qs[:limit]

        if offset:
            return qs[offset:]

        return qs

    def get_count(self):
        return Gongzhong.objects.count()