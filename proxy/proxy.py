from abc import ABC, abstractmethod

# The interface of a remote service.
class ThirdPartyYouTubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, id):
        pass

    @abstractmethod
    def download_video(self, id):
        pass


# The concrete implementation of a service connector.
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self):
        # Send an API request to YouTube.
        pass

    def get_video_info(self, id):
        # Get metadata about some video.
        pass

    def download_video(self, id):
        # Download a video file from YouTube.
        pass

# Proxy class to cache request results.
class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service):
        self.service = service
        self.list_cache = None
        self.video_cache = None
        self.need_reset = False

    def download_exists(self, id):
        # Check if the video is already downloaded.
        pass

    def list_videos(self):
        if self.list_cache is None or self.need_reset:
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, id):
        if self.video_cache is None or self.need_reset:
            self.video_cache = self.service.get_video_info(id)
        return self.video_cache

    def download_video(self, id):
        if not self.download_exists(id) or self.need_reset:
            self.service.download_video(id)


# The GUI class, which works with a service object through an interface.
class YouTubeManager:
    def __init__(self, service):
        self.service = service

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        # Render the video page.

    def render_list_panel(self):
        video_list = self.service.list_videos()
        # Render the list of video thumbnails.

    def react_on_user_input(self):
        self.render_video_page()
        self.render_list_panel()

# The application can configure proxies on the fly.
class Application:
    def init(self):
        youtube_service = ThirdPartyYouTubeClass()
        youtube_proxy = CachedYouTubeClass(youtube_service)
        manager = YouTubeManager(youtube_proxy)
        manager.react_on_user_input()
