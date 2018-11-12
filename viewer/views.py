import csv

import simplejson
from django.core.files.storage import default_storage
from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST
import json
import requests
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import File
import os
from .forms import FileForm
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext
# from django.views import View
from django.views.decorators.csrf import csrf_protect
import pandas

# Create your views here.
# ToDo: Clean the file


def home(request):
    return render(request, 'home.html')


def demo(request):
    return render(request, 'demo.html')


class View(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        # data = {'id': '1', 'first_name': 'Tyrone', 'last_name': 'Ellicott', 'email': 'tellicott0@slideshare.net', 'gender': 'Male', 'Credit card number': '3534248523324444', 'city': 'Zhaodong'}, {'id': '2', 'first_name': 'Jarid', 'last_name': 'Lyburn', 'email': 'jlyburn1@dailymotion.com', 'gender': 'Male', 'Credit card number': '4903816866819211', 'city': 'Gręboszów'}, {'id': '3', 'first_name': 'Lauri', 'last_name': 'Munkley', 'email': 'lmunkley2@google.ca', 'gender': 'Female', 'Credit card number': '5048372103317935', 'city': 'Sumbergebang'}, {'id': '4', 'first_name': 'Ilyse', 'last_name': 'Stathers', 'email': 'istathers3@thetimes.co.uk', 'gender': 'Female', 'Credit card number': '5100147295075458', 'city': 'Udobnaya'}, {'id': '5', 'first_name': 'Barbette', 'last_name': 'Flemyng', 'email': 'bflemyng4@plala.or.jp', 'gender': 'Female', 'Credit card number': '56022102955417787', 'city': 'Louisville'}, {'id': '6', 'first_name': 'Merrily', 'last_name': 'Depper', 'email': 'mdepper5@buzzfeed.com', 'gender': 'Female', 'Credit card number': '3576060205053475', 'city': 'Kuantan'}, {'id': '7', 'first_name': 'Dedra', 'last_name': 'Clausson', 'email': 'dclausson6@mapy.cz', 'gender': 'Female', 'Credit card number': '5038387435990398758', 'city': 'Gagah'}, {'id': '8', 'first_name': 'Sephira', 'last_name': 'Hans', 'email': 'shans7@google.cn', 'gender': 'Female', 'Credit card number': '630431409264856945', 'city': 'Sōja'}, {'id': '9', 'first_name': 'Timmy', 'last_name': 'Jesper', 'email': 'tjesper8@ft.com', 'gender': 'Male', 'Credit card number': '564182426873163432', 'city': 'Tall Rif‘at'}, {'id': '10', 'first_name': 'Dita', 'last_name': 'Barca', 'email': 'dbarca9@geocities.com', 'gender': 'Female', 'Credit card number': '3542123079696380', 'city': 'Davyd-Haradok'}, {'id': '11', 'first_name': 'Irving', 'last_name': 'Deinert', 'email': 'ideinerta@umich.edu', 'gender': 'Male', 'Credit card number': '3529350132098661', 'city': 'Kadupayung'}, {'id': '12', 'first_name': 'Konstanze', 'last_name': 'Fursse', 'email': 'kfursseb@walmart.com', 'gender': 'Female', 'Credit card number': '30162839432533', 'city': 'Borisova Griva'}, {'id': '13', 'first_name': 'Roseann', 'last_name': 'Bernette', 'email': 'rbernettec@arizona.edu', 'gender': 'Female', 'Credit card number': '4026976715660752', 'city': 'Kastsyukovichy'}, {'id': '14', 'first_name': 'Garwin', 'last_name': 'Gaishson', 'email': 'ggaishsond@networksolutions.com', 'gender': 'Male', 'Credit card number': '5179218196685681', 'city': 'El Carmen'}, {'id': '15', 'first_name': 'Jourdain', 'last_name': 'Younie', 'email': 'jyouniee@unblog.fr', 'gender': 'Male', 'Credit card number': '5154024144572453', 'city': 'Horodnya'}, {'id': '16', 'first_name': 'Othilie', 'last_name': 'Arthars', 'email': 'oartharsf@alexa.com', 'gender': 'Female', 'Credit card number': '3561277436727522', 'city': 'Chãos'}, {'id': '17', 'first_name': 'Korey', 'last_name': 'Babon', 'email': 'kbabong@netvibes.com', 'gender': 'Male', 'Credit card number': '3555879488976515', 'city': 'Tulsa'}, {'id': '18', 'first_name': 'Cherilynn', 'last_name': 'Zecchi', 'email': 'czecchih@twitter.com', 'gender': 'Female', 'Credit card number': '201808480179442', 'city': 'Douala'}, {'id': '19', 'first_name': 'Sybille', 'last_name': 'Glasheen', 'email': 'sglasheeni@etsy.com', 'gender': 'Female', 'Credit card number': '5610714838380142', 'city': 'Kotatengah'}, {'id': '20', 'first_name': 'Wendell', 'last_name': 'Margiotta', 'email': 'wmargiottaj@dagondesign.com', 'gender': 'Male', 'Credit card number': '3578659219972139', 'city': 'Shuangchahe'}, {'id': '21', 'first_name': 'Joshuah', 'last_name': 'Campany', 'email': 'jcampanyk@goo.gl', 'gender': 'Male', 'Credit card number': '3576557939754872', 'city': 'Pirassununga'}, {'id': '22', 'first_name': 'Gualterio', 'last_name': 'Eltringham', 'email': 'geltringhaml@networkadvertising.org', 'gender': 'Male', 'Credit card number': '3547415879914582', 'city': 'Veracruz'}, {'id': '23', 'first_name': 'Dion', 'last_name': 'Pepall', 'email': 'dpepallm@nifty.com', 'gender': 'Male', 'Credit card number': '5007668360530402', 'city': 'Stockholm'}, {'id': '24', 'first_name': 'Jodie', 'last_name': 'Killwick', 'email': 'jkillwickn@yahoo.co.jp', 'gender': 'Male', 'Credit card number': '502044652231655045', 'city': 'Ganquan'}, {'id': '25', 'first_name': 'Caron', 'last_name': 'Klasing', 'email': 'cklasingo@alibaba.com', 'gender': 'Female', 'Credit card number': '3531381809119361', 'city': 'Yinghai'}, {'id': '26', 'first_name': 'Farleigh', 'last_name': 'Klausewitz', 'email': 'fklausewitzp@last.fm', 'gender': 'Male', 'Credit card number': '3586921122012720', 'city': 'Paços de Ferreira'}, {'id': '27', 'first_name': 'Ferdy', 'last_name': 'Rycraft', 'email': 'frycraftq@icq.com', 'gender': 'Male', 'Credit card number': '3561141563076873', 'city': 'Grand Forks'}, {'id': '28', 'first_name': 'Winona', 'last_name': 'Cropp', 'email': 'wcroppr@huffingtonpost.com', 'gender': 'Female', 'Credit card number': '633110689885927967', 'city': 'Taoyuan'}, {'id': '29', 'first_name': 'Allister', 'last_name': 'Flello', 'email': 'aflellos@tumblr.com', 'gender': 'Male', 'Credit card number': '36611003352368', 'city': 'Mayong'}, {'id': '30', 'first_name': 'Adamo', 'last_name': 'Ghest', 'email': 'aghestt@networksolutions.com', 'gender': 'Male', 'Credit card number': '5602225819767041', 'city': 'Philadelphia'}, {'id': '31', 'first_name': 'Annnora', 'last_name': 'Olerenshaw', 'email': 'aolerenshawu@businessinsider.com', 'gender': 'Female', 'Credit card number': '3536693411209801', 'city': 'Pancoran'}, {'id': '32', 'first_name': 'Nicky', 'last_name': 'Petett', 'email': 'npetettv@ed.gov', 'gender': 'Female', 'Credit card number': '5108759490893949', 'city': 'Norfolk'}, {'id': '33', 'first_name': 'Thomasin', 'last_name': 'Colombier', 'email': 'tcolombierw@berkeley.edu', 'gender': 'Female', 'Credit card number': '5100176652316767', 'city': 'Lochovice'}, {'id': '34', 'first_name': 'Wilbur', 'last_name': 'Galier', 'email': 'wgalierx@list-manage.com', 'gender': 'Male', 'Credit card number': '3570436137686523', 'city': 'Karátoulas'}, {'id': '35', 'first_name': 'Christian', 'last_name': 'Vaugham', 'email': 'cvaughamy@histats.com', 'gender': 'Female', 'Credit card number': '201828215939332', 'city': 'Paris La Défense'}, {'id': '36', 'first_name': 'Packston', 'last_name': 'Caton', 'email': 'pcatonz@youku.com', 'gender': 'Male', 'Credit card number': '3575034180359406', 'city': 'Svyetlahorsk'}, {'id': '37', 'first_name': 'Micky', 'last_name': 'Sivyour', 'email': 'msivyour10@newyorker.com', 'gender': 'Male', 'Credit card number': '6709331915203688394', 'city': 'Khartsyz’k'}, {'id': '38', 'first_name': 'Cybill', 'last_name': 'Boniface', 'email': 'cboniface11@marketwatch.com', 'gender': 'Female', 'Credit card number': '3563658804549572', 'city': 'New York City'}, {'id': '39', 'first_name': 'Jodee', 'last_name': 'Asker', 'email': 'jasker12@soup.io', 'gender': 'Female', 'Credit card number': '3533042847512995', 'city': 'Shimen'}, {'id': '40', 'first_name': 'Lynnette', 'last_name': 'Lindeboom', 'email': 'llindeboom13@cyberchimps.com', 'gender': 'Female', 'Credit card number': '3542890316077661', 'city': 'Madura'}, {'id': '41', 'first_name': 'Ches', 'last_name': 'Slemmonds', 'email': 'cslemmonds14@reverbnation.com', 'gender': 'Male', 'Credit card number': '4508458198050444', 'city': 'Vyškov'}, {'id': '42', 'first_name': 'Katerina', 'last_name': 'Allday', 'email': 'kallday15@baidu.com', 'gender': 'Female', 'Credit card number': '67620859147887374', 'city': 'Ābdānān'}, {'id': '43', 'first_name': 'Mirelle', 'last_name': 'Blitz', 'email': 'mblitz16@uol.com.br', 'gender': 'Female', 'Credit card number': '3585834246688427', 'city': 'Văn Giang'}, {'id': '44', 'first_name': 'Derk', 'last_name': 'Hawkey', 'email': 'dhawkey17@harvard.edu', 'gender': 'Male', 'Credit card number': '3588963856962041', 'city': 'Verkhnevilyuysk'}, {'id': '45', 'first_name': 'Davie', 'last_name': 'Rostron', 'email': 'drostron18@oracle.com', 'gender': 'Male', 'Credit card number': '3582241486363658', 'city': 'Reina Mercedes'}, {'id': '46', 'first_name': 'Graig', 'last_name': 'Fanthome', 'email': 'gfanthome19@samsung.com', 'gender': 'Male', 'Credit card number': '4041376922357', 'city': 'Baie-Saint-Paul'}, {'id': '47', 'first_name': 'Meredithe', 'last_name': 'Eastup', 'email': 'meastup1a@buzzfeed.com', 'gender': 'Female', 'Credit card number': '58935710866446596', 'city': 'Atlantis'}, {'id': '48', 'first_name': 'Edmon', 'last_name': 'Barby', 'email': 'ebarby1b@bluehost.com', 'gender': 'Male', 'Credit card number': '201625764290699', 'city': 'Baghlān'}, {'id': '49', 'first_name': 'Yalonda', 'last_name': 'McGinty', 'email': 'ymcginty1c@barnesandnoble.com', 'gender': 'Female', 'Credit card number': '372301070841012', 'city': 'Blarney'}, {'id': '50', 'first_name': 'Llewellyn', 'last_name': 'Larman', 'email': 'llarman1d@typepad.com', 'gender': 'Male', 'Credit card number': '3569160611821090', 'city': 'Mlandizi'}, {'id': '51', 'first_name': 'Irvin', 'last_name': 'Domesday', 'email': 'idomesday1e@constantcontact.com', 'gender': 'Male', 'Credit card number': '3537495433789011', 'city': 'Zhatay'}, {'id': '52', 'first_name': 'Harri', 'last_name': 'Edgington', 'email': 'hedgington1f@sfgate.com', 'gender': 'Female', 'Credit card number': '6375715883058502', 'city': 'Zhutang'}, {'id': '53', 'first_name': 'Isidro', 'last_name': 'Cadding', 'email': 'icadding1g@msu.edu', 'gender': 'Male', 'Credit card number': '374283609047493', 'city': 'Mamuša'}, {'id': '54', 'first_name': 'Cristie', 'last_name': 'Mussalli', 'email': 'cmussalli1h@ask.com', 'gender': 'Female', 'Credit card number': '3572769844519654', 'city': 'Stąporków'}, {'id': '55', 'first_name': 'Preston', 'last_name': 'Austwick', 'email': 'paustwick1i@techcrunch.com', 'gender': 'Male', 'Credit card number': '564182883643124849', 'city': 'Ponta do Sol'}, {'id': '56', 'first_name': 'Rosalinda', 'last_name': 'Gane', 'email': 'rgane1j@umn.edu', 'gender': 'Female', 'Credit card number': '3554845335982155', 'city': 'Denver'}, {'id': '57', 'first_name': 'Madlin', 'last_name': 'Nance', 'email': 'mnance1k@soup.io', 'gender': 'Female', 'Credit card number': '3579840766271419', 'city': 'Zhumadian'}, {'id': '58', 'first_name': 'Lindsey', 'last_name': 'Caffery', 'email': 'lcaffery1l@ca.gov', 'gender': 'Male', 'Credit card number': '3559281176721897', 'city': 'Penha'}, {'id': '59', 'first_name': 'Northrup', 'last_name': 'Thynne', 'email': 'nthynne1m@ebay.com', 'gender': 'Male', 'Credit card number': '5602228389932950307', 'city': 'Suban'}, {'id': '60', 'first_name': 'Saxe', 'last_name': 'Rubrow', 'email': 'srubrow1n@imageshack.us', 'gender': 'Male', 'Credit card number': '30298479433918', 'city': 'Kuncen'}, {'id': '61', 'first_name': 'Sunshine', 'last_name': 'Aish', 'email': 'saish1o@cisco.com', 'gender': 'Female', 'Credit card number': '201929833205229', 'city': 'Garango'}, {'id': '62', 'first_name': 'Gannon', 'last_name': 'Peschke', 'email': 'gpeschke1p@virginia.edu', 'gender': 'Male', 'Credit card number': '3538793209328934', 'city': 'Berlin'}, {'id': '63', 'first_name': 'Tally', 'last_name': 'Clowser', 'email': 'tclowser1q@springer.com', 'gender': 'Male', 'Credit card number': '3556349816651767', 'city': 'Livramento do Brumado'}, {'id': '64', 'first_name': 'Che', 'last_name': 'Iacofo', 'email': 'ciacofo1r@stanford.edu', 'gender': 'Male', 'Credit card number': '3541775692154914', 'city': 'Mouzourás'}, {'id': '65', 'first_name': 'Suzy', 'last_name': 'Chestnutt', 'email': 'schestnutt1s@joomla.org', 'gender': 'Female', 'Credit card number': '3555989684765990', 'city': 'Klyuchevsk'}, {'id': '66', 'first_name': 'Pascale', 'last_name': 'Richin', 'email': 'prichin1t@howstuffworks.com', 'gender': 'Male', 'Credit card number': '3584219632947143', 'city': 'Thai Charoen'}, {'id': '67', 'first_name': 'Basilio', 'last_name': 'Benedite', 'email': 'bbenedite1u@joomla.org', 'gender': 'Male', 'Credit card number': '3579365900974595', 'city': 'Kŭrdzhali'}, {'id': '68', 'first_name': 'Grace', 'last_name': 'Gallyhaock', 'email': 'ggallyhaock1v@artisteer.com', 'gender': 'Female', 'Credit card number': '060430154235061875', 'city': 'Živinice'}, {'id': '69', 'first_name': 'Stan', 'last_name': 'Braitling', 'email': 'sbraitling1w@icq.com', 'gender': 'Male', 'Credit card number': '201671250576951', 'city': 'Portsmouth'}, {'id': '70', 'first_name': 'Far', 'last_name': 'Revey', 'email': 'frevey1x@wsj.com', 'gender': 'Male', 'Credit card number': '5568557057534002', 'city': 'Nyima'}, {'id': '71', 'first_name': 'Rasla', 'last_name': 'Thursfield', 'email': 'rthursfield1y@ihg.com', 'gender': 'Female', 'Credit card number': '30263223497064', 'city': 'Vapnyarka'}, {'id': '72', 'first_name': 'Sindee', 'last_name': 'Cafferty', 'email': 'scafferty1z@bigcartel.com', 'gender': 'Female', 'Credit card number': '4405821694728421', 'city': 'Leeuwarden'}, {'id': '73', 'first_name': 'Zuzana', 'last_name': 'Daveren', 'email': 'zdaveren20@linkedin.com', 'gender': 'Female', 'Credit card number': '5100137865517260', 'city': 'Konotop'}, {'id': '74', 'first_name': 'Atalanta', 'last_name': 'Pink', 'email': 'apink21@ucoz.ru', 'gender': 'Female', 'Credit card number': '4911200834476947712', 'city': 'Stará Ves nad Ondřejnicí'}, {'id': '75', 'first_name': 'Lark', 'last_name': 'Dumphry', 'email': 'ldumphry22@slashdot.org', 'gender': 'Female', 'Credit card number': '4057575942632', 'city': 'Vicuña'}, {'id': '76', 'first_name': 'Shawn', 'last_name': 'Sawdon', 'email': 'ssawdon23@arizona.edu', 'gender': 'Male', 'Credit card number': '3542971295100052', 'city': 'Palue'}, {'id': '77', 'first_name': 'Janessa', 'last_name': 'Adelman', 'email': 'jadelman24@elegantthemes.com', 'gender': 'Female', 'Credit card number': '56104202350431283', 'city': 'Hongqi'}, {'id': '78', 'first_name': 'Emmott', 'last_name': 'Sowthcote', 'email': 'esowthcote25@jimdo.com', 'gender': 'Male', 'Credit card number': '3538698514831144', 'city': 'Bylym'}, {'id': '79', 'first_name': 'Boy', 'last_name': 'Seater', 'email': 'bseater26@elpais.com', 'gender': 'Male', 'Credit card number': '3579336416835687', 'city': 'Farah'}, {'id': '80', 'first_name': 'Addia', 'last_name': 'MacColgan', 'email': 'amaccolgan27@kickstarter.com', 'gender': 'Female', 'Credit card number': '3528014538744572', 'city': 'Cabimas'}, {'id': '81', 'first_name': 'Hana', 'last_name': 'Rigmond', 'email': 'hrigmond28@nps.gov', 'gender': 'Female', 'Credit card number': '5213023544345543', 'city': 'Tours'}, {'id': '82', 'first_name': 'Nikita', 'last_name': 'Lyfe', 'email': 'nlyfe29@mapquest.com', 'gender': 'Male', 'Credit card number': '3537370494527198', 'city': 'Tiepu'}, {'id': '83', 'first_name': 'Wynne', 'last_name': 'Willgress', 'email': 'wwillgress2a@answers.com', 'gender': 'Female', 'Credit card number': '3547490283006382', 'city': 'Palopo'}, {'id': '84', 'first_name': 'Auroora', 'last_name': 'Ambrosini', 'email': 'aambrosini2b@icio.us', 'gender': 'Female', 'Credit card number': '6398587414872658', 'city': 'Charneca da Cotovia'}, {'id': '85', 'first_name': 'Jerry', 'last_name': 'Albertson', 'email': 'jalbertson2c@marketwatch.com', 'gender': 'Female', 'Credit card number': '372301859687149', 'city': 'Viçosa'}, {'id': '86', 'first_name': 'Michaella', 'last_name': 'Chifney', 'email': 'mchifney2d@telegraph.co.uk', 'gender': 'Female', 'Credit card number': '6334578686051678089', 'city': 'Ulapes'}, {'id': '87', 'first_name': 'Fredrika', 'last_name': 'Mallinar', 'email': 'fmallinar2e@bluehost.com', 'gender': 'Female', 'Credit card number': '3577632556071493', 'city': 'Colesberg'}, {'id': '88', 'first_name': 'Fania', 'last_name': 'Geerling', 'email': 'fgeerling2f@eepurl.com', 'gender': 'Female', 'Credit card number': '5602254572459349', 'city': 'Banjar Banyuning Barat'}, {'id': '89', 'first_name': 'Deonne', 'last_name': 'Dewey', 'email': 'ddewey2g@geocities.jp', 'gender': 'Female', 'Credit card number': '5100178741647590', 'city': 'Monte-Carlo'}, {'id': '90', 'first_name': 'Felipe', 'last_name': 'Bartley', 'email': 'fbartley2h@ameblo.jp', 'gender': 'Male', 'Credit card number': '3548263451249079', 'city': 'Raków'}, {'id': '91', 'first_name': 'Jolyn', 'last_name': 'Barhems', 'email': 'jbarhems2i@ebay.co.uk', 'gender': 'Female', 'Credit card number': '4175665617496311', 'city': 'Carolina'}, {'id': '92', 'first_name': 'Adah', 'last_name': 'Griffitts', 'email': 'agriffitts2j@clickbank.net', 'gender': 'Female', 'Credit card number': '30263190212843', 'city': 'Kalamáta'}, {'id': '93', 'first_name': 'Yalonda', 'last_name': 'Crayden', 'email': 'ycrayden2k@edublogs.org', 'gender': 'Female', 'Credit card number': '3567664875382535', 'city': 'Xiongbei'}, {'id': '94', 'first_name': 'Milena', 'last_name': 'MacElholm', 'email': 'mmacelholm2l@archive.org', 'gender': 'Female', 'Credit card number': '3534583271129078', 'city': 'Ban Pong'}, {'id': '95', 'first_name': 'Janice', 'last_name': 'Halgarth', 'email': 'jhalgarth2m@weather.com', 'gender': 'Female', 'Credit card number': '6373080014527475', 'city': 'Boac'}, {'id': '96', 'first_name': 'Dolores', 'last_name': 'Shapter', 'email': 'dshapter2n@so-net.ne.jp', 'gender': 'Female', 'Credit card number': '4508621668916721', 'city': 'Los Frentones'}, {'id': '97', 'first_name': 'James', 'last_name': 'Balling', 'email': 'jballing2o@ning.com', 'gender': 'Male', 'Credit card number': '4405456984823317', 'city': 'Jalanbaru'}, {'id': '98', 'first_name': 'Morgen', 'last_name': 'Stritton', 'email': 'mstritton2p@virginia.edu', 'gender': 'Male', 'Credit card number': '30048014738630', 'city': 'Mahaba'}, {'id': '99', 'first_name': 'Alfy', 'last_name': 'Corradino', 'email': 'acorradino2q@arstechnica.com', 'gender': 'Male', 'Credit card number': '3570973408091298', 'city': 'Francisco Villa'}, {'id': '100', 'first_name': 'Jard', 'last_name': 'Gledstane', 'email': 'jgledstane2r@huffingtonpost.com', 'gender': 'Male', 'Credit card number': '3552627842615623', 'city': 'Yengimahalla'}, {'id': '101', 'first_name': 'Gina', 'last_name': 'Warboys', 'email': 'gwarboys2s@reverbnation.com', 'gender': 'Female', 'Credit card number': '3529534457403487', 'city': 'Dalu'}, {'id': '102', 'first_name': 'Mathew', 'last_name': 'Coey', 'email': 'mcoey2t@eepurl.com', 'gender': 'Male', 'Credit card number': '491185566476178775', 'city': 'Motupe'}, {'id': '103', 'first_name': 'Christiano', 'last_name': 'Entwistle', 'email': 'centwistle2u@nhs.uk', 'gender': 'Male', 'Credit card number': '3567124787757795', 'city': 'Kampungtengah'}, {'id': '104', 'first_name': 'Kermie', 'last_name': 'Hurll', 'email': 'khurll2v@amazon.com', 'gender': 'Male', 'Credit card number': '56022539918816854', 'city': 'Tembol'}, {'id': '105', 'first_name': 'Beckie', 'last_name': 'Treker', 'email': 'btreker2w@china.com.cn', 'gender': 'Female', 'Credit card number': '3586655915278540', 'city': 'Hadapu Zhen'}, {'id': '106', 'first_name': 'Deloria', 'last_name': 'Tythacott', 'email': 'dtythacott2x@live.com', 'gender': 'Female', 'Credit card number': '3580839753555534', 'city': 'Ilongero'}, {'id': '107', 'first_name': 'Lock', 'last_name': 'Felmingham', 'email': 'lfelmingham2y@github.io', 'gender': 'Male', 'Credit card number': '5610726156250855', 'city': 'Las Tunas'}, {'id': '108', 'first_name': 'Johnathon', 'last_name': 'Hentze', 'email': 'jhentze2z@admin.ch', 'gender': 'Male', 'Credit card number': '30387543389881', 'city': 'Taling Chan'}, {'id': '109', 'first_name': 'Charmane', 'last_name': 'Wrigglesworth', 'email': 'cwrigglesworth30@macromedia.com', 'gender': 'Female', 'Credit card number': '3535600964784644', 'city': 'Hitiaa'}, {'id': '110', 'first_name': 'Concettina', 'last_name': 'Kikke', 'email': 'ckikke31@google.com', 'gender': 'Female', 'Credit card number': '3554786728513035', 'city': 'Smoky Lake'}, {'id': '111', 'first_name': 'Fayina', 'last_name': 'Backe', 'email': 'fbacke32@time.com', 'gender': 'Female', 'Credit card number': '374622726618415', 'city': 'Melati'}, {'id': '112', 'first_name': 'Horacio', 'last_name': 'Crust', 'email': 'hcrust33@rambler.ru', 'gender': 'Male', 'Credit card number': '3537951601659840', 'city': 'Biting'}, {'id': '113', 'first_name': 'Sid', 'last_name': 'Crickett', 'email': 'scrickett34@thetimes.co.uk', 'gender': 'Male', 'Credit card number': '201607650048191', 'city': 'Garawati'}, {'id': '114', 'first_name': 'Katee', 'last_name': 'Hearl', 'email': 'khearl35@nsw.gov.au', 'gender': 'Female', 'Credit card number': '5108758959462410', 'city': 'Yaté-Barrage'}, {'id': '115', 'first_name': 'Fionna', 'last_name': 'Gillespey', 'email': 'fgillespey36@linkedin.com', 'gender': 'Female', 'Credit card number': '6334914868843510324', 'city': 'Chinameca'}, {'id': '116', 'first_name': 'Dan', 'last_name': 'Naughton', 'email': 'dnaughton37@infoseek.co.jp', 'gender': 'Male', 'Credit card number': '3548665778180771', 'city': 'Cikarang'}, {'id': '117', 'first_name': 'Spenser', 'last_name': 'Tenman', 'email': 'stenman38@google.com.br', 'gender': 'Male', 'Credit card number': '3583405114466659', 'city': 'Quarteira'}, {'id': '118', 'first_name': 'Thain', 'last_name': 'Yeskin', 'email': 'tyeskin39@woothemes.com', 'gender': 'Male', 'Credit card number': '4017957582097246', 'city': 'Nürnberg'}, {'id': '119', 'first_name': 'Maxine', 'last_name': 'Rizzo', 'email': 'mrizzo3a@aol.com', 'gender': 'Female', 'Credit card number': '67061171719299616', 'city': 'Huacapampa'}, {'id': '120', 'first_name': 'Karlotta', 'last_name': 'Tathacott', 'email': 'ktathacott3b@dailymotion.com', 'gender': 'Female', 'Credit card number': '346690461071749', 'city': 'Beizhouzi'}, {'id': '121', 'first_name': 'Klemens', 'last_name': 'Bindin', 'email': 'kbindin3c@cpanel.net', 'gender': 'Male', 'Credit card number': '3556738400616725', 'city': 'Hanlin'}, {'id': '122', 'first_name': 'Addi', 'last_name': 'Davydychev', 'email': 'adavydychev3d@posterous.com', 'gender': 'Female', 'Credit card number': '36371717378049', 'city': 'Yinglan'}, {'id': '123', 'first_name': 'Roxi', 'last_name': 'Switland', 'email': 'rswitland3e@alexa.com', 'gender': 'Female', 'Credit card number': '670982498703852044', 'city': 'Ziguinchor'}, {'id': '124', 'first_name': 'Kennedy', 'last_name': 'Pembry', 'email': 'kpembry3f@com.com', 'gender': 'Male', 'Credit card number': '4917341684971742', 'city': 'Ndago'}, {'id': '125', 'first_name': 'Harlin', 'last_name': 'Camplen', 'email': 'hcamplen3g@netscape.com', 'gender': 'Male', 'Credit card number': '3562090840496967', 'city': 'Granja'}, {'id': '126', 'first_name': 'Justis', 'last_name': 'Hendricks', 'email': 'jhendricks3h@cnet.com', 'gender': 'Male', 'Credit card number': '3547320517802357', 'city': 'Villiers'}, {'id': '127', 'first_name': 'Cirilo', 'last_name': 'Lindner', 'email': 'clindner3i@gizmodo.com', 'gender': 'Male', 'Credit card number': '3555989864643488', 'city': 'Vilarinho das Cambas'}, {'id': '128', 'first_name': 'Mable', 'last_name': 'Ivimey', 'email': 'mivimey3j@icq.com', 'gender': 'Female', 'Credit card number': '30434480309892', 'city': 'Đắk Glei'}, {'id': '129', 'first_name': 'Sherlocke', 'last_name': 'Baise', 'email': 'sbaise3k@nyu.edu', 'gender': 'Male', 'Credit card number': '6390293782234351', 'city': 'Oibioin'}, {'id': '130', 'first_name': 'Suzie', 'last_name': "O'Donegan", 'email': 'sodonegan3l@tamu.edu', 'gender': 'Female', 'Credit card number': '4917307873075173', 'city': 'Murom'}, {'id': '131', 'first_name': 'Elie', 'last_name': 'Potapczuk', 'email': 'epotapczuk3m@yahoo.co.jp', 'gender': 'Female', 'Credit card number': '5602238092726816', 'city': 'Saldanha'}, {'id': '132', 'first_name': 'Sander', 'last_name': 'Troup', 'email': 'stroup3n@weebly.com', 'gender': 'Male', 'Credit card number': '3573496837370544', 'city': 'Alagoa Grande'}, {'id': '133', 'first_name': 'Brigida', 'last_name': 'Selbie', 'email': 'bselbie3o@cnet.com', 'gender': 'Female', 'Credit card number': '346899635885278', 'city': 'Cigoong'}, {'id': '134', 'first_name': 'Belinda', 'last_name': 'McElrea', 'email': 'bmcelrea3p@usda.gov', 'gender': 'Female', 'Credit card number': '5002357168995190', 'city': 'Xinglongjie'}, {'id': '135', 'first_name': 'Agata', 'last_name': 'Lochrie', 'email': 'alochrie3q@blogspot.com', 'gender': 'Female', 'Credit card number': '201702008448266', 'city': 'Chamlykskaya'}, {'id': '136', 'first_name': 'Delphinia', 'last_name': 'Claremont', 'email': 'dclaremont3r@dedecms.com', 'gender': 'Female', 'Credit card number': '3530844967551825', 'city': 'Jiupu'}, {'id': '137', 'first_name': 'Adah', 'last_name': 'Cominello', 'email': 'acominello3s@sina.com.cn', 'gender': 'Female', 'Credit card number': '3532566607143709', 'city': 'Surazh'}, {'id': '138', 'first_name': 'Freeman', 'last_name': 'Earsman', 'email': 'fearsman3t@psu.edu', 'gender': 'Male', 'Credit card number': '30010013806008', 'city': 'Knyazhichi'}, {'id': '139', 'first_name': 'Jeddy', 'last_name': 'Hollyland', 'email': 'jhollyland3u@addtoany.com', 'gender': 'Male', 'Credit card number': '3548864104401601', 'city': 'Néa Palátia'}, {'id': '140', 'first_name': 'Loy', 'last_name': 'Worsall', 'email': 'lworsall3v@yahoo.com', 'gender': 'Male', 'Credit card number': '5007663775687913', 'city': 'Węgliniec'}, {'id': '141', 'first_name': 'Kylie', 'last_name': 'Warrack', 'email': 'kwarrack3w@washington.edu', 'gender': 'Male', 'Credit card number': '4041377118018527', 'city': 'Namballe'}, {'id': '142', 'first_name': 'Jennee', 'last_name': 'Hazart', 'email': 'jhazart3x@senate.gov', 'gender': 'Female', 'Credit card number': '3572449154728217', 'city': 'Spas-Klepiki'}, {'id': '143', 'first_name': 'Mathe', 'last_name': 'Durtnell', 'email': 'mdurtnell3y@gizmodo.com', 'gender': 'Male', 'Credit card number': '374288923920234', 'city': 'Sidi Yahia el Gharb'}, {'id': '144', 'first_name': 'Jessa', 'last_name': 'Grimm', 'email': 'jgrimm3z@oracle.com', 'gender': 'Female', 'Credit card number': '4508802398576411', 'city': 'Goris'}, {'id': '145', 'first_name': 'Faith', 'last_name': 'Haughton', 'email': 'fhaughton40@amazon.de', 'gender': 'Female', 'Credit card number': '3573992813548061', 'city': 'Batang'}, {'id': '146', 'first_name': 'Aeriela', 'last_name': 'Jebb', 'email': 'ajebb41@scientificamerican.com', 'gender': 'Female', 'Credit card number': '3572286581316574', 'city': 'Rongelap'}, {'id': '147', 'first_name': 'Dani', 'last_name': 'Carrington', 'email': 'dcarrington42@ucoz.com', 'gender': 'Female', 'Credit card number': '3564963408722503', 'city': 'Zhangzhu'}, {'id': '148', 'first_name': 'Adams', 'last_name': 'Pietesch', 'email': 'apietesch43@networkadvertising.org', 'gender': 'Male', 'Credit card number': '3544601220867297', 'city': 'Cibeuti'}, {'id': '149', 'first_name': 'Ilaire', 'last_name': 'Cardenas', 'email': 'icardenas44@hubpages.com', 'gender': 'Male', 'Credit card number': '5451484151039699', 'city': 'Diepsloot'}, {'id': '150', 'first_name': 'Nicolais', 'last_name': 'Rodgman', 'email': 'nrodgman45@desdev.cn', 'gender': 'Male', 'Credit card number': '3588362515696092', 'city': 'Aomori Shi'}
        obj = File.objects.get(pk=1)  # ToDo: get the latest file upload's pk
        path = os.path.join(settings.MEDIA_ROOT, obj.file_field.path)
        data = csvtojson(path)
        data = json.dumps(data)
        data = json.loads(data)
        type(data)
        return Response({'data': data}, template_name = 'viewer.html')


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = File(file_field=request.FILES['file'])
            file.save()
            return HttpResponseRedirect(reverse('upload'))
    else:
        form = FileForm()  # A empty, unbound form
    obj = File.objects.get(pk=1)
    dir = obj.file_field.path
    # Render list page with the documents and the form
    return render(request, 'upload.html', {'form': form, 'path': dir})


#Note that json.dumps only works with dictionaries containing simple data types. Django has support for serializing model objects to json, using:
# from django.core import serializers
# obj_as_json = serializers.serialize("json", my_model_object)


# def save(f):
#     PATH = settings.MEDIA_ROOT
#     with open(PATH, 'wb+') as destination:
#         for chunk in f.chunks():
#              destination.write(chunk)


def csvtojson(f):
    csvfile = open(f, 'r')
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        data.append(row)

    data = json.loads(json.dumps(data))
    return data

# def file_upload():
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)