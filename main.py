# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Iranian': [{'name': 'RadioJavan',
                       'thumb': 'https://www.radiojavan.com/images/rj-touch-icon-144.png',
                       'video': 'https://stream.rjtv.tv/live/smil:rjtv.smil/playlist.m3u8',
                       'genre': 'Music'},
                      {'name': 'ManoTo',
                       'thumb': 'https://dwphh95xlnw84.cloudfront.net/images/shows/portrait/1060.jpeg',
                       'video': 'https://dow6lwapg8fa4.cloudfront.net/live.m3u8',
                       'genre': 'Entertainment'},
                      {'name': 'Tapesh',
                       'thumb': 'http://www.tapesh.tv/wp-content/uploads/2017/08/tapesh-new-logo-300x300.png',
                       'video': 'http://iptv.tapesh.tv/tapesh/playlist.m3u8',
                       'genre': 'Entertainment'},
                     {'name': 'Dreamland TV',
                      'thumb': 'http://dreamlandtvs.com/wp-content/uploads/2017/04/footer-logo.png',
                      'video': 'http://ad.mysisli.com/live/Dr13/index.m3u8',
                      'genre': 'Entertainment'},
                     {'name': 'Shabakeh 7',
                      'thumb': 'https://www.parsatv.com/index_files/channels/worldfashion.jpg',
                      'video': 'http://97.107.115.84:1935/live/myStream2/playlist.m3u8',
                      'genre': 'Entertainment'},
                      {'name': 'MTC',
                      'thumb': 'https://www.parsatv.com/index_files/channels/worldfashion.jpg',
                      'video': 'http://mellitv.tulix.tv:1935/mellitv/myStream.sdp/playlist.m3u8',
                      'genre': 'Entertainment'},
                      ],
            'IRIB': [{'name': 'Shabakeh 3 HD',
                      'thumb': 'https://newsmedia.tasnimnews.com/Tasnim/Uploaded/Image/1394/01/19/139401191152146655061533.jpg',
                      'video': 'https://cdn1live.irib.ir/live-channels/smil:tv3/playlist.m3u8?s=GltKzPFznPJPaxgojsbUFg&t=1576429107',
                      'genre': 'Cars'}
                     ,
                     {'name': 'Shabakeh Varzesh HD',
                      'thumb': 'https://2.bp.blogspot.com/-tZ1WJE7r5fw/WrXR2h15wCI/AAAAAAAAt_4/Bci3D-iNv9Y5GNDKvZ4XOf9kA5xJNP6FACLcBGAs/s1600/varzesh.jpg',
                      'video': 'https://livetv.persianleague.com/live/varzesh/playlist.m3u8',
                      'genre': 'Cars'}
                     ,
                     {'name': 'Khozestan',
                      'thumb': 'https://sepehr.irib.ir/uploads/channel/khozestan-min.png',
                      'video': 'https://cdn1live.irib.ir/live-channels/smil:khoozestan/playlist.m3u8?s=sE0N6v2CSNcczTi5g5OLww&t=1576429273',
                      'genre': 'Cars'}
                     ],
            'Radio': [{'name': 'Shemroon',
                      'thumb': 'https://cdn-profiles.tunein.com/s197608/images/logoq.jpg',
                      'video': 'http://usa7.fastcast4u.com:5919/',
                      'genre': 'Food'},
                     {'name': 'Javan IRIB',
                      'thumb': 'https://cdn-profiles.tunein.com/s20281/images/logoq.png',
                      'video': 'http://s1.cdn1.iranseda.ir:1935/liveedge/radio-javan/chunklist_w1833251740.m3u8',
                      'genre': 'Food'},
                     {'name': 'varzesh',
                      'thumb': 'https://cdn117-fs2.soroush-hamrah.ir/static_file/d1/1521842931410sjDR1HKCTdvqQiSB4MLgUJO52w7lyIze.jpg?',
                      'video': 'http://s3.cdn1.iranseda.ir:1935/liveedge/radio-varzesh/playlist.m3u8',
                      'genre': 'Food'}
                     ],
            'Fashion':[{'name': 'World Fashion',
                      'thumb': 'https://www.parsatv.com/index_files/channels/worldfashion.jpg',
                      'video': 'https://wfc.bonus-tv.ru/cdn/wfcint/index.m3u8',
                      'genre': 'Fashion'},
                     {'name': 'Travel TV Russia',
                      'thumb': 'https://pbs.twimg.com/profile_images/580681250429513729/ftiH-vHY_400x400.jpg',
                      'video': 'http://31.13.223.103:1935/travel/travel.stream/chunklist_w919550210.m3u8',
                      'genre': 'Fashion'},
                     {'name': 'FTV Paris',
                      'thumb': 'https://i.pinimg.com/originals/5f/c6/81/5fc681d442e17d2b493e6080695b64aa.png',
                      'video': 'https://fash1043.cloudycdn.services/slive/_definst_/ftv_paris_adaptive.smil/media.m3u8',
                      'genre': 'Fashion'},
                     {'name': 'FTV Bikini',
                      'thumb': 'https://www.parsatv.com/index_files/channels/worldfashion.jpg',
                      'video': 'https://fash1043.cloudycdn.services/slive/_definst_/ftv_ftv_midnite_k1y_27049_midnite_secr_108_hls.smil/media.m3u8',
                      'genre': 'Fashion'},
                     {'name': 'HD Fashion',
                      'thumb': 'https://www.parsatv.com/index_files/channels/worldfashion.jpg',
                      'video': 'http://95.67.47.115/hls/hdfashion_ua_hi/index.m3u8',
                      'genre': 'Fashion'},],
            'Turkish': [
                        {'name': 'TRT MUZIK 1',
                        'thumb': 'https://odatv.com/images/2016_08/2016_08_07/trt-takvimine-sorusturma-0708161200_l2.jpg',
                        'video': 'https://trtcanlitv-lh.akamaihd.net/i/TRTMUZIK_1@181845/master.m3u8',
                        'genre': 'Turkish'},
                        {'name': 'TRT TURK 1',
                        'thumb': 'https://www.wikidata.org/wiki/Q4628831#/media/File:TRT_T%C3%BCrk_logosu.png',
                        'video': 'https://trtcanlitv-lh.akamaihd.net/i/TRTTURK_1@182144/master.m3u8',
                        'genre': 'Turkish'},
                         {'name': 'TRT COCUK',
                          'thumb': 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/032013/trt_cocuk_logo.png',
                          'video': 'https://trtcanlitv-lh.akamaihd.net/i/TRTCOCUK_1@181844/master.m3u8',
                          'genre': 'Turkish'},
                         {'name': 'TRT1 HD',
                          'thumb': 'http://2.bp.blogspot.com/-lKXWDSYQSDM/T-buFHUJhDI/AAAAAAAAA7A/RHaEUqLF-nc/s320/trt1hd%2Byeni%2Bfrekans%25C4%25B1.png',
                          'video': 'https://trtcanlitv-lh.akamaihd.net/i/TRT1HD_1@181842/master.m3u8',
                          'genre': 'Turkish'},
                         {'name': 'TRT AVAZ 1',
                          'thumb': 'https://www.satlogo.com/hires/tt/trt_avaz_tr.png',
                          'video': 'https://trtcanlitv-lh.akamaihd.net/i/TRTAVAZ_1@182244/master.m3u8',
                          'genre': 'Turkish'},
         ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
