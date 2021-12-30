import News.GetNews
import News.AddImages
import News.CreateNewsHtml
import News.SearchNews

class MaestroNews:
    def __init__(self):
        for url in News.SearchNews.SearchNews().urls:
            try:
                NewsPayload = News.GetNews.GetNews([url]).response
                NewsPayload[1] = News.AddImages.AddImages(str(NewsPayload[3]), str(NewsPayload[1])).response
                News.CreateNewsHtml.CreateNewsHtml(NewsPayload[1], NewsPayload[4], str(NewsPayload[3]))
            except Exception:
                pass