from django.conf.urls import url
from calaccess_website import views, sitemaps
from django.views.generic.base import RedirectView


urlpatterns = [
    # The homepage
    url(
        r'^$',
        RedirectView.as_view(url='https://www.californiacivicdata.org/'),
        name="home",
    ),

    #
    # Downloads
    #

    # Version archive views
    url(
        r'^downloads/$',
        views.VersionArchiveIndex.as_view(),
        name="version_archive_index",
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/$',
        views.VersionYearArchiveList.as_view(),
        name="version_archive_year"
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
        views.VersionMonthArchiveList.as_view(),
        name="version_archive_month"
    ),
    url(
        r'^downloads/latest/$',
        views.LatestVersion.as_view(),
        name='version_latest'
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<time>[0-9]{6})/$',
        views.VersionDetail.as_view(),
        name="version_detail"
    ),

    #
    # Documentation
    #

    # Index
    url(
        r'^documentation/$',
        views.DocumentationIndex.as_view(),
        name='docs_index'
    ),

    # CAL-ACCESS file views
    url(
        r'^documentation/raw-files/$',
        views.CalAccessFileList.as_view(),
        name='calaccess_file_list'
    ),
    url(
        r'^documentation/raw-files/(?P<slug>[-\w]+)/$',
        views.CalAccessFileDetail.as_view(),
        name='calaccess_file_detail',
    ),
    url(
        r'^documentation/raw-files/(?P<slug>[-\w]+)/downloads/$',
        views.CalAccessFileDownloadsList.as_view(),
        name='calaccess_file_downloads_list',
    ),

    # CCDC file views
    url(
        r'^documentation/processed-files/$',
        views.CcdcFileList.as_view(),
        name='ccdc_file_list'
    ),
    url(
        r'^documentation/processed-files/(?P<slug>[-\w]+)/$',
        views.CcdcFileDetail.as_view(),
        name='ccdc_file_detail',
    ),
    url(
        r'^documentation/processed-files/(?P<slug>[-\w]+)/downloads/$',
        views.CcdcFileDownloadsList.as_view(),
        name='ccdc_file_downloads_list',
    ),

    # Form views
    url(
        r'^documentation/calaccess-forms/$',
        views.FormList.as_view(),
        name='form_list'
    ),
    url(
        r'^documentation/calaccess-forms/(?P<id>\w+)/$',
        views.FormDetail.as_view(),
        name='form_detail',
    ),

    # Official documentation
    url(
        r'^documentation/calaccess-official-documentation/$',
        views.OfficialDocumentation.as_view(),
        name='official_documentation'
    ),

    # Frequently asked questions
    url(
        r'^documentation/frequently-asked-questions/$',
        views.FAQ.as_view(),
        name='faq'
    ),

    #
    # Redirects
    #

    url(
        r'^redirect/latest/processed/(?P<slug>[-\w\_\.]+)/$',
        views.redirect_latest_processed,
        name='redirect_latest_processed'
    ),

    url(
        r'^redirect/latest/raw/(?P<slug>[-\w\_\.]+)/$',
        views.redirect_latest_raw,
        name='redirect_latest_raw'
    ),

    #
    # Machine-readable stuff
    #

    url(
        r'^robots.txt$',
        views.CalAccessRobotsTxt.as_view(),
        name='robots_txt'
    ),
    url(
        r'^raw-file-sitemap.xml$',
        sitemaps.CalAccessFileSitemap.as_view(),
        name='calaccess_file_sitemap'
    ),
    url(
        r'^raw-file-downloads-sitemap.xml$',
        sitemaps.CalAccessFileDownloadsSitemap.as_view(),
        name='calaccess_file_downloads_sitemap'
    ),
    url(
        r'^processed-file-sitemap.xml$',
        sitemaps.CcdcFileSitemap.as_view(),
        name='ccdc_file_sitemap'
    ),
    url(
        r'^processed-file-downloads-sitemap.xml$',
        sitemaps.CcdcFileDownloadsSitemap.as_view(),
        name='ccdc_file_downloads_sitemap'
    ),
    url(
        r'^form-sitemap.xml$',
        sitemaps.FormSitemap.as_view(),
        name='form_sitemap'
    ),
    url(
        r'^downloads-sitemap.xml$',
        sitemaps.VersionSitemap.as_view(),
        name='version_sitemap'
    ),
    url(
        r'^downloads-year-sitemap.xml$',
        sitemaps.VersionYearSitemap.as_view(),
        name='version_archive_year_sitemap'
    ),
    url(
        r'^downloads-month-sitemap.xml$',
        sitemaps.VersionMonthSitemap.as_view(),
        name='version_archive_month_sitemap'
    ),
    url(
        r'^other-sitemap.xml$',
        sitemaps.OtherSitemap.as_view(),
        name='other_sitemap'
    ),
]
