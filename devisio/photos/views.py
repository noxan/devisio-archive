from django.utils import simplejson as json
from django.views.generic import DetailView, ListView, RedirectView
from django.core.urlresolvers import reverse

from devisio.common.pjax import PJAXResponseMixin
from models import Album


class PhotoShareView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return reverse('photos:detail', args=[self.kwargs['slug']]) + '#' + self.kwargs['photoid']


class AlbumDetailView(PJAXResponseMixin, DetailView):
    model = Album

    def serialize_album(self, album):
        def _serialize_photo(photo):
            version = photo.image.version_generate('album_gallery')
            return {
                "src": version.url,
                "width": version.width,
                "height": version.height
            }

        res = [_serialize_photo(photo) for photo in album.photos.all()]

        return json.dumps(res)

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(*args, **kwargs)
        context['json'] = self.serialize_album(context['object'])
        return context


class AlbumListView(PJAXResponseMixin, ListView):
    def get_queryset(self):
        return Album.objects.visible()[:6]


class AlbumOverviewView(PJAXResponseMixin, ListView):
    template_name = 'photos/album_overview.html'

    def get_queryset(self):
        return Album.objects.visible()
