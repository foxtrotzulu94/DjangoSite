from django.conf.urls import include, url

# This URL file includes all the URLs that map to functions in this directory

# Imports for REST API, nicknamed as shorthand
import personal_site.rest.work_experience as we
import personal_site.rest.extracurricular_experience as ece
import personal_site.rest.volunteer_experience as ve
import personal_site.rest.personal_project as pp
import personal_site.rest.game_title as gt
import personal_site.rest.personal_interest as pi


urlpatterns = [
    # url(r'', include('.extracurricular_experience'))    # Map to main site

    # 'Experience' REST API URLs
    # TODO: PENDING REFACTOR
    # There's a way to do this where less code is written and is easier to maintain. I'll do it tomorrow
    # Work Experience (we)
    url(r'^data/work_exp/', we.list_all),
    url(r'^data/work_exp/?P<pk>[0-9]*$', we.specific),
    url(r'^data/work_exp/?P<pk>[0-9]*/images/', we.specific_image_list),
    url(r'^data/work_exp/?P<pk>[0-9]*/thumbnail/', we.specific_thumbnail),

    # Extra-Curricular Experience (ece)
    url(r'^data/extra_exp/', ece.list_all),
    url(r'^data/extra_exp/?P<pk>[0-9]*$', ece.specific),
    url(r'^data/extra_exp/?P<pk>[0-9]*/images/', ece.specific_image_list),
    url(r'^data/extra_exp/?P<pk>[0-9]*/thumbnail/', ece.specific_thumbnail),

    # Volunteer Experience (ve)
    url(r'^data/volunteer/', ve.list_all),
    url(r'^data/volunteer/?P<pk>[0-9]*$', ve.specific),
    url(r'^data/volunteer/?P<pk>[0-9]*/images/', ve.specific_image_list),
    url(r'^data/volunteer/?P<pk>[0-9]*/thumbnail/', ve.specific_thumbnail),

    # Personal Projects (pp)
    url(r'^data/projects/', pp.list_all),
    url(r'^data/projects/?P<pk>[0-9]*$', pp.specific),
    url(r'^data/projects/?P<pk>[0-9]*/images/', pp.specific_image_list),
    url(r'^data/projects/?P<pk>[0-9]*/thumbnail/', pp.specific_thumbnail),

    # Shipped Titles (gt)
    url(r'^data/titles/', gt.list_all),
    url(r'^data/titles/?P<pk>[0-9]*$', gt.specific),
    url(r'^data/titles/?P<pk>[0-9]*/images/', gt.specific_image_list),
    url(r'^data/titles/?P<pk>[0-9]*/thumbnail/', gt.specific_thumbnail),

    # Interests & hobbies
    url(r'^data/interests/', pi.list_all),
    url(r'^data/interests/?P<pk>[0-9]*$', pi.specific),
    url(r'^data/interests/?P<pk>[0-9]*/images/', pi.specific_image_list),
    url(r'^data/interests/?P<pk>[0-9]*/thumbnail/', pi.specific_thumbnail),
]
