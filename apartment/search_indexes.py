from haystack import indexes
from apartment.models import Apartment,Garden
from order.models import Article
from customAuth.models import Location

class GardenIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Garden

    def index_queryset(self, using=None):
        return self.get_model().objects.all()