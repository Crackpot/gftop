from django.contrib.sitemaps import Sitemap
from mysite.items.models import Item

class ItemsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Item.objects.filter()

    def lastmod(self, obj):
        return obj.pub_date

sitemaps = {
    'items': ItemsSitemap,
}
