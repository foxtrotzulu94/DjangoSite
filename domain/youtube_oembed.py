import json
import re
from urllib import request as urllib_request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request

from wagtail.embeds.exceptions import EmbedNotFoundException
from wagtail.embeds.oembed_providers import all_providers

from wagtail.embeds.finders.oembed import OEmbedFinder

class YoutubeOEmbedFinder(OEmbedFinder):
    def find_embed(self, url, max_width=None):
        result = super().find_embed(url, max_width)

        # HACK: do some magic to make our embed bigger!
        width_string = "width=\"{}\"".format(result['width'])
        height_string = "height=\"{}\"".format(result['height'])

        html_content = result['html']
        result['html'] = html_content.replace(width_string, 'width="100%"').replace(height_string, 'height="512px"')

        result['width'] = '100%'
        result['height'] = '512px'

        return result