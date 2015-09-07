from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from parse.models import Entry
from rest.serializers import EntrySerializer


class EntryList(ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer