# -*- coding: utf-8 -*-
import io, os, re, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))
SLUG = "2026nin-en-iyi-10-monitoru-oyun-ofis-yaratici-isler"
DATE_HUMAN = "5 Ekim 2026"
DATE_ISO = "2026-10-05"
CAT = "Donanım"
READ = "9 dk okuma"
HERO = 37698747

def px(i):
    return "https://images.pexels.com/photos/%d/pexels-photo-%d.jpeg?auto=compress&cs=tinysrgb&w=1200" % (i, i)

def fig(pid, alt, cap):
    return (
        '<figure style="margin: 24px 0; text-align: center;">\n'
        '  <img src="%s" alt="%s" style="width:100%%; border-radius: 12px;" loading="lazy">\n'
        '  <figcaption style="font-size: 0.85rem; color: #94a3b8; margin-top: 8px;">%s</figcaption>\n'
        '</figure>\n'
    ) % (px(pid), alt, cap)

TITLE = "2026'nın En İyi 10 Monitörü: Oyun, Ofis ve Yaratıcı İşler İçin"
DESC = ("2026'nın en iyi 10 monitörü: Samsung Odyssey OLED, LG UltraGear, ASUS ROG Swift, "
        "Dell UltraSharp, BenQ, LG UltraWide, AOC, Xiaomi, Philips ve iiyama; OLED/IPS/VA/Mini LED "
        "panel rehberi, çözünürlük-yenileme tablosu, boyut-mesafe hesabı, amaç karşılaştırma tablosu ve SSS.")

B = []
A = B.append

A('<h2>2026\'da Monitör Pazarı Nereye Geldi?</h2>')
A('<p>2026, monitör pazarında üç eğilimin aynı anda olgunlaştığı yıl oldu. Birincisi <strong>OLED gaming '
  'monitörlerin</strong> ana akıma geçmesi: 240 Hz ve 360 Hz OLED paneller, bir yıl öncesinin fiyatının '
  'yarısına inerek rekabetçi FPS oyuncularının standart tercihi hâline geldi. İkincisi <strong>4K + yüksek '
  'yenileme</strong> kombinasyonunun masaüstünde gerçekçi olması: DisplayPort 2.1 ve HDMI 2.1 sayesinde '
  '3840x2160 çözünürlükte 144 Hz artık tek kablo ile çalışıyor ve orta segment ekran kartları bile AI tabanlı '
  'kare üretimiyle bu yükün altından kalkabiliyor. Üçüncüsü ise ofis tarafında: <strong>USB-C hub\'lı ekranlar</strong> '
  'tek kablo ile güç, görüntü, veri ve ethernet taşıyerek dizüstü bilgisayarla çalışan herkesin masa düzenini '
  'tek kabloya indirdi.</p>')
A('<p>Bu üç eğilim, "hangi monitörü alayım" sorusunu eskisinden çok daha net bir sınıflandırmaya '
  'ihtiyaç duyar hâle getirdi. Artık soru yalnızca "kaç inç" değil; <strong>panel tipi, çözünürlük, yenileme '
  'hızı, bağlantı standardı ve kullanım amacı</strong> birlikte değerlendirilmeli. 165 Hz bir IPS ekran, '
  'aynı fiyat bandındaki 240 Hz OLED karşısında oyuncu için farklı, video editörü için bambaşka bir doğru '
  'tercih. Bu rehber, on modeli tek bir sıralamada değil, <strong>farklı ihtiyaçlara karşılık gelen on '
  'ayrı cevap</strong> olarak sunuyor; ardından panel, çözünürlük ve boyut kararlarını netleştiren '
  'karşılaştırma tabloları geliyor.</p>')
A(fig(39178044,
      "Boş iş istasyonları sıralanmış modern bir bilgisayar laboratuvarı",
      "2026'da kurumsal alımlarda bile tek kriter kalmadı: aynı masada gaming, ofis ve yaratıcı ekranlar yan yana değerlendiriliyor."))

A('<h2>1. Samsung Odyssey OLED G6 / G8 - OLED\'in Fiyat/Performans Zirvesi</h2>')
A('<p>Samsung\'un Odyssey OLED ailesi, 2026\'da OLED\'i ana akım yapan modellerin başında geliyor. '
  '<strong>OLED G6</strong> (27 inç, 1440p, 240 Hz) rekabetçi oyuncular için dengeli bir noktada dururken, '
  '<strong>OLED G8</strong> (32 inç, 4K, 240 Hz) hem oyuncu hem de içerik üreticisi olan kullanıcıların '
  'ilk tercihi hâline geldi. QD-OLED tabanlı panel, %99 DCI-P3 kapsama ve 1.000 nit tepe parlaklığıyla '
  'HDR içerikte farkı ilk bakışta belli ediyor. Samsung\'un oyuncular için eklediği 0.03 ms tepki süresi, '
  'hareketli sahnelerde gölge bırakma (ghosting) sorununu neredeyse tamamen ortadan kaldırıyor.</p>')
A('<p>Yazılım tarafı da olgun: Tizen tabanlı arayüz, oyun modlarını kaydetmeye, KVM anahtarını yönetmeye '
  've renk profillerini uygulama bazında hatırlamaya izin veriyor. HDMI 2.1 ve DisplayPort 2.1 bağlantıları '
  'sayesinde hem PC hem de PlayStation 5 / Xbox Series X ile 4K 240 Hz kullanılabiliyor. <strong>Kime gøre:</strong> '
  'siyah derinliği yüksek bir görüntüde oynayıp, aynı monitörle film ve renkli içerik de tüketmek isteyenler.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> QD-OLED, kavisli olmayan düz yüzey</li>')
A('  <li><strong>Çözünürlük:</strong> 2560x1440 (G6) / 3840x2160 (G8)</li>')
A('  <li><strong>Yenileme:</strong> 240 Hz, 0.03 ms tepki, FreeSync Premium Pro / G-Sync uyumlu</li>')
A('  <li><strong>Bağlantı:</strong> DisplayPort 2.1, HDMI 2.1 x2, USB-C hub, 90W güç aktarımı, KVM</li>')
A('  <li><strong>Fiyat:</strong> G6 yaklaşık 24.000-27.000 TL, G8 yaklaşık 39.000-45.000 TL</li>')
A('</ul>')

A('<h2>2. LG UltraGear OLED - Yenileme Hızı Rekorunun Sahibi</h2>')
A('<p>LG UltraGear ailesi, 2026\'da <strong>480 Hz OLED</strong> seçeneğiyle rekabetçi FPS tarafında '
  'standartları yukarı çekti. 27 inçlik 1440p model, CS2 ve Valorant turnuvalarında sahne arkasında en '
  'çok görülen ekranlardan biri; 45 inçlik kavisli UltraWide OLED ise sim-racing ve uçuş simülatörü '
  'kullanıcılarının vazgeçilmezi. Her iki modelde de LG\'nin anti-refleks kaplaması, parlak bir odada '
  ' bile görüş alanını koruyor - OLED monitörlerin geleneksel "ayna" sorununu ciddi ölçüde azaltıyor.</p>')
A('<p>USB-C hub desteği, LG\'yi oyunculuk dışında da kullanılabilir kılıyor: tek kablo ile 90W şarj, '
  'görüntü ve veri. Renk tarafında fabrika kalibrasyonu Delta E &lt; 2 ile geliyor; yani kutudan çıkar çıkmaz '
  'fotoğraf ve video işleri için yeterince doğru. <strong>Kime gøre:</strong> refleks ve kare hızını her '
  'şeyin üstünde tutan rekabetçi oyuncular ile geniş ekran seven sim-racing kullanıcıları.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> WOLED, 27 inç düz / 45 inç kavisli (1800R) seçenekleri</li>')
A('  <li><strong>Çözünürlük:</strong> 2560x1440 (27") veya 3440x1440 / 5120x2160 (UltraWide)</li>')
A('  <li><strong>Yenileme:</strong> 240 Hz - 480 Hz arası modele göre</li>')
A('  <li><strong>Bağlantı:</strong> DisplayPort 2.1, HDMI 2.1, USB-C (90W), USB hub, DTS Headphone:X</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 27.000 - 55.000 TL (boyut ve yenilemeye göre)</li>')
A('</ul>')
A(fig(18966440,
      "Modern ekipmanlarla kurulmuş RGB aydınlatmalı oyun masası",
      "480 Hz'e çıkan yenileme hızları, rekabetçi FPS'te artık ekranın kendisi bir avantaj kalemi."))

A('<h2>3. ASUS ROG Swift PG32UCDM - 4K OLED\'in Referansı</h2>')
A('<p>ASUS ROG Swift PG32UCDM, 32 inç 4K QD-OLED paneliyle 2026\'nın en dengeli premium monitörü '
  ' sayılıyor. 240 Hz yenileme, 1.000 nit HDR tepe parlaklığı ve G-Sync uyumluluğu; buna karşılık '
  'yanma (burn-in) önleme paketi olarak hareketli araç çubuğu, piksel yenileme ve statik parlaklık '
  'sınırlama özellikleri ekleniyor. ASUS\'un "OLED Care" paneli, monitörü masa üstünde bıraktığınızda bile '
  'arka planda dinlenme döngüsü çalıştırıyor - bu, ofiste 8-10 saat açık kalan bir ekran için kritik bir detay.</p>')
A('<p>Renk tarafında %99 DCI-P3 ve fabrika kalibrasyonu, onu oyunculuğun yanında video kurgu için de '
  'geçerli bir seçenek hâline getiriyor. KVM ve USB-C hub desteği tek kablo düzenini sağlarken, dahili '
  'hoparlörler acil durumlar için yeterli seviyede. <strong>Kime gøre:</strong> 4K keskinliğinde oyun oynayıp '
  'aynı ekranda 4K video kurgulayan, ikisini ayrı monitör almak istemeyen profesyoneller.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> QD-OLED, 32 inç düz</li>')
A('  <li><strong>Çözünürlük:</strong> 3840x2160 (4K UHD)</li>')
A('  <li><strong>Yenileme:</strong> 240 Hz, 0.03 ms, G-Sync / FreeSync Premium Pro</li>')
A('  <li><strong>Bağlantı:</strong> DisplayPort 2.1, HDMI 2.1 x2, USB-C (90W), USB hub, KVM, kulaklık girişi</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 46.000 - 52.000 TL</li>')
A('</ul>')

A('<h2>4. Dell UltraSharp U2725QE - Ofis ve Kod Yazmanın Güvenli Cevabı</h2>')
A('<p>Dell UltraSharp serisi, ofis ve yazılım dünyasında on yıllardır olduğu gibi 2026\'da da '
  'varsayılan tercih. <strong>U2725QE</strong>, 27 inç 4K IPS Black paneliyle 2.000:1 statik kontrast '
  'sunuyor - klasik IPS\'in 1.000:1 seviyesinin iki katı; yani koyu temalı kod editöründe satır araları '
  'daha net okunuyor. Jak DSC desteğiyle tek kablo üzerinden 4K 120 Hz, Thunderbolt 4 ile ise '
  '90W güç aktarımı ve 10 Gbps veri aynı anda taşınıyor.</p>')
A('<p>Ofis tarafında belirleyici olan ek detaylar: RJ-45 ethernet portu (dizüstü-docking karmaşasını '
  'bitiriyor), low blue light sertifikası, Pb-free ve Energy Star sertifikaları ve 3 yıl Next Business Day '
  'garanti. Panel, 178 derece izleme açısıyla toplantı paylaşımında da renk kaybı yaşatmıyor. '
  '<strong>Kime gøre:</strong> günde 8+ saat ekrana bakan, renk doğruluğundan ödün vermek istemeyen '
  'yazılımcılar, analistler ve ofis kullanıcıları.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> IPS Black, 27 inç düz, mat kaplama</li>')
A('  <li><strong>Çözünürlük:</strong> 3840x2160 (4K), %99 sRGB, %98 DCI-P3</li>')
A('  <li><strong>Yenileme:</strong> 120 Hz (DC - Dynamic Dimming desteğiyle)</li>')
A('  <li><strong>Bağlantı:</strong> Thunderbolt 4 (90W), HDMI 2.1, DP 1.4, RJ-45, USB hub x4, KVM</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 26.000 - 30.000 TL</li>')
A('</ul>')
A(fig(20213729,
      "Ofis sandalyesiyle birlikte bilgisayar kurulumu bulunan çalışma masası",
      "Tek kablo düzeni ofiste artık lüks değil: USB-C hub'lı ekran, dizüstü + ethernet + güç bağlantısını tek hatto indiriyor."))

A('<h2>5. BenQ PD3226G - Yaratıcı İşler İçin Kalibrasyon Standartı</h2>')
A('<p>BenQ PD serisi, fotoğraf ve video profesyonelleri için tasarlanmış bir ekran ailesi. '
  '<strong>PD3226G</strong>, 32 inç 4K IPS paneli ve kutudan çıkmış kalibrasyon raporuyla geliyor; '
  'Delta E &lt; 2 garantisi, kör bir teslim süreci istemeyen serbest çalışanlar için kritik. '
  'BenQ\'nun CAD/CAM, animasyon, ekipman ve düşük mavi ışık ön ayarları, tek tuşla farklı iş akışlarına '
  'geçiş sağlıyor. Hardware Calibration desteği sayesinde renk profili monitörün kendi belleğinde '
  'saklanıyor; bilgisayar değiştirdiğinizde kalibrasyonu yeniden yapmanız gerekmiyor.</p>')
A('<p>KVM ve USB-C (90W) desteği, iki bilgisayar arasında tek klavye-fare ile geçişi mümkün kılıyor. '
  'Paper Color Sync özelliği ise ekranda baskı provası simülasyonu yaparak, basılı çıkacak işin '
  'ekrandaki hâline yakın görünmesini sağlıyor. <strong>Kime gøre:</strong> renk doğruluğu pazarlık '
  'konusu olmayan fotoğrafçılar, video editörleri, grafik tasarımcılar ve ajans ekipleri.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> IPS, 32 inç düz, 10 bit (8 bit + FRC)</li>')
A('  <li><strong>Çözünürlük:</strong> 3840x2160 (4K), %99 sRGB, %95 DCI-P3, factory calibration</li>')
A('  <li><strong>Yenileme:</strong> 60 Hz (renk öncelikli kullanım)</li>')
A('  <li><strong>Bağlantı:</strong> USB-C (90W), HDMI 2.1 x2, DP 1.4, KVM, hub, headphone jack</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 28.000 - 33.000 TL</li>')
A('</ul>')
A(fig(39694504,
      "Kurulu bir profesyonel video kurgu stüdyosu ve monitörler",
      "Renk yönetimi iş akışında ekran, dekor değil ölçü aletidir: kalibrasyon raporu gelmeyen ekranda iş teslim edilmez."))

A('<h2>6. LG UltraWide Curved - Tek Ekranla İki Ekran Etkisi</h2>')
A('<p>21:9 ve 32:9 en-boy oranlı kavisli ekranlar, 2026\'da masa düzenini yeniden düşündüren '
  'bir kategori. <strong>LG UltraWide</strong> ailesinin 34 inçlik modeli (3440x1440) iki adet 16:9 '
  'ekranın yerini alırken kavis sayesinde görüş açısının kenarlarını da kullanıma katıyor; '
  '45 inçlik model ise neredeyse üç ekranlık alan sunuyor. Ultrawide\'ın asıl gücü, video zaman '
  'çizelgesi, çoklu kod penceresi ve tablo + rapor yan yana kullanım gibi yatay alanda genişlik '
  'isteyen işlerde.</p>')
A('<p>Kavis yarıçapı (1000R - 1800R arası) masa mesafenize göre seçilmeli: 60-70 cm mesafede '
  '1000R daha doğal, 80 cm üzeri mesafede 1800R daha rahat. Panel tarafında VA ve IPS OLED seçenekleri '
  'mevcut; ofis ağırlıklı kullanımda IPS, film ve oyun ağırlıklı kullanımda OLED tercih ediliyor. '
  '<strong>Kime gøre:</strong> çoklu pencereyle çalışan yazılımcı, finans uzmanı, video editörü ve '
  'sim-racing sevenler.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> VA veya IPS OLED, 34" / 38" / 45" / 49" seçenekleri</li>')
A('  <li><strong>Çözünürlük:</strong> 3440x1440 (21:9) veya 5120x1440 (32:9)</li>')
A('  <li><strong>Yenileme:</strong> 75 Hz - 240 Hz (model ve panele göre)</li>')
A('  <li><strong>Bağlantı:</strong> USB-C (90W), Thunderbolt, HDMI, DP, KVM, Picture-by-Picture</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 15.000 - 50.000 TL</li>')
A('</ul>')
A(fig(37848030,
      "Birden fazla monitörden oluşan fotoğraf düzenleme masaüstü kurulumu",
      "Ultrawide, zaman çizelgesi ve katman panellerini aynı karede tutar: dar ekranda iki kez sekme değiştirmek yerine tek bakış."))

A('<h2>7. AOC Gaming (Q27G4 / CQ27G3) - Bütçe Dostu Performans</h2>')
A('<p>Bütçe sınıfında 2026\'nın en akıllıca dağıtımını AOC yapıyor. <strong>Q27G4</strong> serisi, '
  '27 inç 1440p 180 Hz IPS paneliyle orta segment bir GPU\'dan maksimum verimi almanızı sağlıyor; '
  '1080p 240 Hz yerine 1440p 180 Hz tercihi, hem keskinlik hem kare hızı açısından daha dengeli '
  'bir uzlaşma. Şasi sade, ayak küçük, VESA uyumlu; yani kol tarafına geçtiğinde duvar montajına da hazır.</p>')
A('<p>Gaming tarafında 1 ms MPRT tepki, Adaptive-Sync ve düşük gecikme modu standart. Ofis kullanımına '
  'da açık olan ekran; yükseklik ayarı, pivot ve tilt özellikleriyle dikey konumda kod okumaya imkân tanıyor. '
  'Bu sınıfın en büyük dezavantajı HDR performansı: 300-400 nit seviyesinde kaldığı için HDR\'ı aktif '
  'etmenin pek bir anlamı yok. <strong>Kime gøre:</strong> 10.000-14.000 TL bandında ilk ciddi '
  'oyun monitörünü alacaklar ve öğrenciler.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> Fast IPS (Q27G4) veya VA kavisli (CQ27G3)</li>')
A('  <li><strong>Çözünürlük:</strong> 2560x1440 (1440p QHD)</li>')
A('  <li><strong>Yenileme:</strong> 165 - 180 Hz, 1 ms MPRT, Adaptive-Sync</li>')
A('  <li><strong>Bağlantı:</strong> HDMI 2.0 x2, DP 1.4, kulaklık çıkışı, VESA 100x100</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 9.500 - 14.000 TL</li>')
A('</ul>')

A('<h2>8. Xiaomi Mi Monitor (G27Qi / A27Qi) - Ucuz Ama Ucuz Hissettirmeyen</h2>')
A('<p>Xiaomi, monitör pazarına girdiği günden beri aynı formülü uyguluyor: <strong>iyi paneli '
  'küçük bir şasi ve düşük fiyatla</strong> birleştirmek. <strong>G27Qi</strong>, 27 inç 1440p '
  '180 Hz IPS paneli ve %95 DCI-P3 kapsamasıyla 10.000 TL altındaki en yetenekli ekranlardan biri. '
  'Mi Gaming Monitor serisi, fabrika kalibrasyonu ve renk profillerini de standart getirerek '
  '"bütçe = kötü renk" önyargısını kırıyor.</p>')
A('<p>Bağlantı tarafında HDMI 2.0 ve DP 1.4 yeterli; ancak USB-C hub ve KVM bu fiyatta yok - '
  'bütçeniz ofis bağlantılarına da ihtiyaç duyuyorsa bu eksikliği hesaba katın. Piksel garantisi '
  've yerel servis ağı, Türkiye\'de garanti sürecini sorunsuz hâle getiriyor. <strong>Kime gøre:</strong> '
  'ilk sistemini kuran, 1440p deneyimini ucuza yaşamak isteyen öğrenciler ve ofis/oyun karışık '
  'kullanım yapanlar.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> Fast IPS, 27 inç düz</li>')
A('  <li><strong>Çözünürlük:</strong> 2560x1440 (1440p), %95 DCI-P3, HDR400</li>')
A('  <li><strong>Yenileme:</strong> 165 - 180 Hz, Adaptive-Sync</li>')
A('  <li><strong>Bağlantı:</strong> HDMI 2.0 x2, DP 1.4, kulaklık girişi, VESA</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 8.500 - 12.000 TL</li>')
A('</ul>')

A('<h2>9. Philips Ev/Ofis Serisi (27E1N / Evnia) - Konfor Önceliği</h2>')
A('<p>Philips, monitör tarafında iki farklı kimlikle birden konuşuyor. <strong>Ev/Ofis serisi</strong> '
  '(27E1N5600 gibi modeller) 27 inç 4K IPS panelleri, PowerSensor ile otomatik enerji tasarrufu ve '
  'LightSensor ile ortam ışığına göre parlaklık ayarını bir araya getiriyor; yani ekran açık unutulduğunda '
  'bile faturaya ve göze dost davranıyor. <strong>Evnia</strong> alt markası ise oyunculara 180-240 Hz '
  'arası paneller sunuyor ve Ambiglow etkisiyle duvara yansıyan ambiyans aydınlatması ekliyor.</p>')
A('<p>Kulaklık askısı, geleneksel VGA çıkışı ve dahili hoparlör gibi "küçük" detaylar, bu seriyi '
  'ev-ofis karışık kullanım için pratik kılıyor. Ergonomi tarafında yükseklik, tilt, pivot ve swivel '
  'tam dört eksende destekli - uzun masa sürelerinde en çok göz ardı edilen konu olan boyun konforu '
  'için belirleyici. <strong>Kime gøre:</strong> ekranını gün boyu açık tutan, film de izleyen, '
  'oyun da oynayan ev-ofis kullanıcıları.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> IPS (Ev/Ofis) veya Fast LCD / VA (Evnia)</li>')
A('  <li><strong>Çözünürlük:</strong> 3840x2160 (4K) veya 2560x1440</li>')
A('  <li><strong>Yenileme:</strong> 60 - 240 Hz modele göre</li>')
A('  <li><strong>Bağlantı:</strong> USB-C (65W), HDMI, DP, SmartImage, PowerSensor, Ambiglow</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 11.000 - 25.000 TL</li>')
A('</ul>')
A(fig(17136613,
      "Yatak odasında masaya kurulmuş bilgisayar ve ekran",
      "Ev-ofis karışık kullanımında sessizlik ve göz konforu, kağıt üstündeki teknik özelliklerden daha hızlı fark ediliyor."))

A('<h2>10. iiyama ProLite (XUB2792UHSU) - Profesyonel Bütçe Seçeneği</h2>')
A('<p>Listeyi, kurumsal alımlarda ve butik ofislerde sıkça tercih edilen <strong>iiyama ProLite</strong> '
  'kapatıyor. XUB2792UHSU, 27 inç 4K IPS paneli, Blue Light Reducer ve Flicker Free teknolojileriyle '
  'uzun mesai saatleri için tasarlanmış bir ekran. iiyama\'nın 3 yıl yerinde garanti ve profesyonel '
  'kullanıcıya yönelik "pro" segment yaklaşımı, fiyatı 15.000 TL bandında tutarken kurumsal güvenilirliği '
  'koruyor.</p>')
A('<p>Hız tarafında 60 Hz ile sınırlı; ancak ofis, muhasebe, tasarım ve üretim işlerinde yenileme '
  'hızı yerine <strong>ergonomi, göz konforu ve bağlantı çeşitliliği</strong> belirleyici. Ayak, '
  'yükseklik/pivot/tilt destekli; VESA delikleri sayesinde kol sistemlerine takılabiliyor. '
  '<strong>Kime gøre:</strong> uygun fiyata 4K keskinliği, sağlam garanti ve rahat ergonomi isteyen '
  'ofisler, eğitim kurumları ve ekranını ikinci/üçüncü monitör olarak ekleyenler.</p>')
A('<ul>')
A('  <li><strong>Panel tipi:</strong> IPS, 27 inç düz, mat kaplama</li>')
A('  <li><strong>Çözünürlük:</strong> 3840x2160 (4K UHD), %99 sRGB</li>')
A('  <li><strong>Yenileme:</strong> 60 Hz, 4 ms tepki</li>')
A('  <li><strong>Bağlantı:</strong> HDMI x2, DP 1.2, USB hub, kulaklık girişi, VESA 100x100</li>')
A('  <li><strong>Fiyat:</strong> Yaklaşık 13.000 - 16.500 TL, 3 yıl yerinde garanti</li>')
A('</ul>')

A('<h2>Panel Rehberi: IPS vs OLED vs VA vs Mini LED</h2>')
A('<p>Yukarıdaki on modelin hepsi aynı görüntüyü üretmiyor; fark, panel teknolojisinde saklı. '
  'Aşağıdaki tablo, dört ana panel tipini koyu-siyah performansı, parlaklık, yanma riski ve fiyat '
  'açısından yan yana koyuyor:</p>')
A('<table>')
A('  <tr><th>Panel</th><th>Siyah / kontrast</th><th>Parlaklık</th><th>Yanma riski</th><th>Gecikme</th><th>Fiyat</th><th>Kim için</th></tr>')
A('  <tr><td><strong>IPS</strong></td><td>1.000:1 - vasat siyah</td><td>350-600 nit</td><td>Yok</td><td>Çok iyi (1 ms)</td><td>En uygun</td><td>Ofis, kod, genel kullanım</td></tr>')
A('  <tr><td><strong>OLED / QD-OLED</strong></td><td>Mükemmel siyah, sonsuz kontrast</td><td>250-1.000 nit (HDR)</td><td>Düşük - yazılımla yönetilir</td><td>0.03 ms</td><td>Yüksek</td><td>Rekabetçi oyun, film, hibrit iş</td></tr>')
A('  <tr><td><strong>VA</strong></td><td>3.000:1 - güçlü siyah</td><td>300-500 nit</td><td>Yok</td><td>Orta (ghosting olabilir)</td><td>Uygun</td><td>Film, ofis, kavisli ultrawide</td></tr>')
A('  <tr><td><strong>Mini LED</strong></td><td>Yerel karartma ile 100.000:1</td><td>1.000-1.600 nit</td><td>Yok</td><td>İyi</td><td>Orta-yüksek</td><td>HDR film, parlak ortam, video</td></tr>')
A('</table>')
A('<p><strong>Kısa kural:</strong> karanlık odada oyun ve film ise <strong>OLED</strong>; parlak '
  'bir odada HDR içerik üretimi ise <strong>Mini LED</strong>; gün boyu metin ve kod ise '
  '<strong>IPS</strong>; bütçe sınırlıysa ve koyu sahneler önemliyse <strong>VA</strong>.</p>')

A('<h2>Amaç Tablosu: Neyi, Neden Almalısınız?</h2>')
A('<table>')
A('  <tr><th>Amaç</th><th>Önerilen panel</th><th>Çözünürlük / yenileme</th><th>Bu listedeki model</th><th>Bütçe aralığı</th></tr>')
A('  <tr><td><strong>Rekabetçi oyun</strong></td><td>OLED veya Fast IPS</td><td>1440p, 240-480 Hz</td><td>LG UltraGear OLED, Samsung Odyssey OLED G6</td><td>24.000 - 45.000 TL</td></tr>')
A('  <tr><td><strong>Ofis / kod</strong></td><td>IPS / IPS Black</td><td>4K, 60-120 Hz</td><td>Dell UltraSharp U2725QE, iiyama ProLite</td><td>13.000 - 30.000 TL</td></tr>')
A('  <tr><td><strong>Video / fotoğraf</strong></td><td>IPS (kalibre) veya Mini LED</td><td>4K, %95+ DCI-P3</td><td>BenQ PD3226G, ASUS ROG Swift PG32UCDM</td><td>28.000 - 52.000 TL</td></tr>')
A('  <tr><td><strong>Bütçe / öğrenci</strong></td><td>Fast IPS veya VA</td><td>1440p, 165-180 Hz</td><td>AOC Q27G4, Xiaomi G27Qi</td><td>8.500 - 14.000 TL</td></tr>')
A('  <tr><td><strong>Çoklu pencere / sim</strong></td><td>VA veya OLED ultrawide</td><td>3440x1440 veya 5120x1440</td><td>LG UltraWide Curved</td><td>15.000 - 50.000 TL</td></tr>')
A('</table>')

A('<h2>Çözünürlük ve Yenileme Rehberi: Doğru Eşleşmeyi Bulmak</h2>')
A('<p>Çözünürlük ile yenileme hızını GPU kapasitenize göre eşleştirmek, en sık yapılan hatayı '
  'önler. Yanlış eşleşme, ya pahalı donanımın boşa çalışması ya da beklenen akıcılığın '
  'gelmemesi demek:</p>')
A('<ul>')
A('  <li><strong>1080p 144-165 Hz:</strong> Orta segment ekran kartları ve rekabetçi FPS için '
  'en verimli başlangıç. 24 inç ve altı boyutlarda piksel yoğunluğu yeterli; 27 inçte '
  'piksel aralığı göze çarpmaya başlar.</li>')
A('  <li><strong>1440p 165-240 Hz:</strong> 2026\'nın en popüler dengesi. 27 inç boyutunda '
  'keskinlik ve kare hızını birlikte sunar; orta-üst segment bir GPU ile rahatça sürdürülebilir.</li>')
A('  <li><strong>4K 144-240 Hz:</strong> Hem oyun hem kurgu için üst nokta. DisplayPort 2.1 / '
  'HDMI 2.1 zorunlu; DLSS ve FSR benzeri AI kare üretimi olmadan 4K 144 Hz tam performans '
  'veremez. Güncel kart karşılaştırması için <a href="2026nin-en-iyi-10-ekran-karti-oyun-yaraticilik-yapay-zeka.html">2026\'nın en iyi 10 ekran kartı</a> listemize bakın.</li>')
A('  <li><strong>Ultrawide (21:9 / 32:9):</strong> 3440x1440, 4K\'dan daha az piksel işler; '
  'bu yüzden kare hızını korumak daha kolay. 32:9 ise 5120x1440 ile 4K ile aynı yükü taşır.</li>')
A('</ul>')
A('<p><strong>Boyut-mesafe hesabı:</strong> Genel kabul, ekranın göz mesafesinin yaklaşık '
  'yarısı kadar seçilmesidir. 27 inç için 55-70 cm, 32 inç için 65-85 cm, 34 inç ultrawide için '
  '70-90 cm ve 45 inç kavisli için 90-110 cm öneriliyor. Kavisli ekranlarda yarıçap, bu mesafeye '
  'eşit olmalı: 1000R panel yaklaşık 100 cm, 1800R panel yaklaşık 180 cm teorik odak mesafesine '
  'sahiptir. 4K\'da 27 inç kullanıyorsanız ölçek %150\'ye alın; 32 inçte %125 çoğu kullanıcı için '
  'en rahat okunur.</p>')
A(fig(16129705,
      "Birden fazla bilgisayar ekranı karşısında çalışan bir kişi",
      "Mesafe, boyut ve çözünürlük üçlüsü doğru kurulduğunda göz yorgunluğu ciddi ölçüde azalıyor."))

A(fig(31726545,
      "Minimalist tasarımlı modern ev ofisi kurulumu",
      "Ergonomi dört eksende çalışır: ekran yüksekliği, izleme mesafesi, panel parlaklığı ve ortam ışığı."))

A('<h2>Sıkça Sorulan Sorular (SSS)</h2>')
A('<h3>OLED monitör yanma (burn-in) riski ofis kullanımı için sorun olur mu?</h3>')
A('Günlük 8-10 saatlik sabit arayüzlü kullanımda risk artık oldukça düşük; ancak sıfır değil. 2026 '
  'modellerinde piksel yenileme, hareketli araç çubuğu, statik parlaklık sınırlama ve otomatik dinlenme '
  'döngüleri standart. Kod editörü ve tablo gibi sabit beyaz arayüzlerdeyseniz <strong>IPS Black '
  '(Dell UltraSharp)</strong> yine de daha güvenli bir tercih; oyun ve film ağırlıklıysanız OLED\'i '
  'gönül rahatlığıyla seçebilirsiniz.')
A('<h3>4K monitör mü, 1440p yüksek yenileme mi?</h3>')
A('İki ayrı ihtiyaç. <strong>Kare hızı</strong> refleks ve akıcılık gerektiren oyunlarda belirleyicidir; '
  '<strong>çözünürlük</strong> ise metin keskinliği, piksel yoğunluğu ve kurgu hassasiyetinde. Eğer '
  'oyunun %70\'inden fazlası rekabetçi FPS ise 1440p 240 Hz, kurgu / hikâye oyunu / genel kullanım '
  'ağırlıklıysa 4K 144 Hz daha doğru. Tek monitörle ikisini birden istiyorsanız 32 inç 4K 240 Hz OLED '
  'bandına bakın.')
A('<h3>USB-C hub\'lı ekran alırken nelere dikkat etmeli?</h3>')
A('Üç kritik değer var: <strong>güç aktarımı (W)</strong> - dizüstü bilgisayarınızın şarjını '
  'karşılamalı (30W küçük, 65W orta, 90W üst segment için yeterli); <strong>video protokolü</strong> - '
  'DisplayPort Alt Modu ile 4K 60 Hz, Thunderbolt ile 4K 120 Hz ve üstü mümkün; ve <strong>veri '
  'hızı</strong> - 5 Gbps mi 10 Gbps mi. Ethernet portu ve KVM desteği, çift makine kullananlar için '
  'ayrı bir kazanç.')
A('<h3>60 Hz ofis monitörü hâlâ yeterli mi?</h3>')
A('Metin, tablo ve kod için evet; ancak 120 Hz ve üzeri, kaydırma ve pencere hareketlerinde göz '
  'yorgunluğunu belirgin biçimde azaltıyor. Ofiste 120 Hz bir IPS ekran ile renk öncelikli 60 Hz '
  'bir ekran arasında kaldıysanız, uzun soluklu kullanımda <strong>120 Hz + iyi panel</strong> '
  'kombinasyonu genellikle daha konforlu. Bütçeniz izin veriyorsa 4K 120 Hz USB-C modeller '
  'artık orta segmente indi.')
A(fig(28896170,
      "Modern teknoloji cihazlarıyla düzenli bir çalışma alanı",
      "Doğru monitör, masadaki en hızlı geri dönüşü sağlayan yatırımdır: her oturumda fark edilir."))

A('<h2>Sonuç: Doğru Ekran, Doğru İş İçin</h2>')
A('Listeyi tek bir "en iyi" sıralaması olarak değil, on farklı ihtiyacın karşılığı olarak okumak '
  'gerekiyor. <strong>Samsung Odyssey OLED</strong> ve <strong>LG UltraGear OLED</strong> oyun ve HDR '
  'tarafının zirvesi; <strong>ASUS ROG Swift PG32UCDM</strong> 4K\'da hibrit bir çözüm; '
  '<strong>Dell UltraSharp</strong> ve <strong>iiyama ProLite</strong> ofisin güvenli cevapları; '
  '<strong>BenQ PD3226G</strong> renk doğruluğunu pazarlık dışı yapanlar için; <strong>LG UltraWide</strong> '
  'geniş alan ihtiyacı olanlara; <strong>AOC</strong> ve <strong>Xiaomi</strong> bütçeyi zorlamadan '
  'yüksek yenileme vaat ediyor; <strong>Philips</strong> ise ev-ofis konforunu öne çıkarıyor.')
A('Sıralamayı belirleyen şey fiyat etiketi değil, <strong>ihtiyacınızın hangi sütunda durduğu</strong>. '
  'Önce amaç tablosundaki satırınızı bulun, ardından panel ve çözünürlük kararını oradan türetin. '
  'Dizüstü tarafını da güncelliyorsanız <a href="2026da-en-iyi-10-notebook-onerisi.html">2026\'nın '
  'en iyi 10 notebook önerisi</a> ve ekranla birlikte izleme deneyimini düşünüyorsanız '
  '<a href="2026nin-en-iyi-10-televizyonu-oled-mini-led-qled.html">2026\'nın en iyi 10 televizyonu</a> '
  'listelerimiz bir sonraki adımı tamamlıyor.')
A('<p><em>Bu makale TechWave tarafından hazırlanmıştır. Fiyatlar ve stok durumu yayın tarihi '
  'itibarıyla tahminidir; satın almadan önce resmî mağaza sayfalarını kontrol edin.</em></p>')

BODY = "\n".join(B)

HEAD = '''<!DOCTYPE html>
<html lang="tr" data-theme="light">
<head>
    <meta name="google-site-verification" content="-7pHgAzQSH7HXgUgc7cpgCXlwHivhN9X5MWaniE68Go" />
<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; } }
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],a.async=1,a.src=r,a.parentNode.insertBefore(a,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=112858721', 'ym');

    ym(112858721, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/112858721" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="__DESC__">
  <meta name="author" content="TechWave">
  <meta name="robots" content="index, follow">
  <title>__TITLE__ &mdash; TechWave</title>
  <meta property="og:title" content="__TITLE__ &mdash; TechWave">
  <meta property="og:description" content="__DESC__">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:image" content="__HERO__">
  <link rel="canonical" href="https://techwaveblog.site/articles/__SLUG__.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "__TITLE__",
    "author": {"@type": "Person", "name": "TechWave Ekibi"},
    "datePublished": "__DATE_ISO__",
    "description": "__DESC__",
    "publisher": {"@type": "Organization", "name": "TechWave", "url": "https://techwaveblog.site"},
    "mainEntityOfPage": "https://techwaveblog.site/articles/__SLUG__.html",
    "image": "__HERO__"
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "TechWave Ekibi",
    "jobTitle": "Teknoloji ve Yapay Zeka Yazarı",
    "url": "https://techwaveblog.site",
    "sameAs": [],
    "worksFor": {
      "@type": "Organization",
      "name": "TechWave"
    }
  }
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3459052960619900" crossorigin="anonymous"></script>
<!-- Google Translate -->
<meta name="google-translate-customization" content="YOUR-ID">
<div id="google_translate_element"></div>
<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'tr', includedLanguages: 'en,ar,de,es,fr,ru,ja,ko,zh-CN', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, autoDisplay: false}, 'google_translate_element');
}
</script>
<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<style>
.goog-te-gadget {
  font-family: 'Inter', sans-serif !important;
  font-size: 14px !important;
}
.goog-te-gadget-simple {
  border: 1px solid #e0e7ff !important;
  border-radius: 8px !important;
  background: white !important;
  padding: 4px 8px !important;
}
.goog-te-gadget-simple .goog-te-menu-value {
  color: #1e293b !important;
  font-family: 'Inter', sans-serif !important;
}
body {
  position: relative;
}
#google_translate_element {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 9999;
  background: white;
  padding: 8px 12px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
</style>
<!-- /Google Translate -->
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo"><img src="../images/logo.svg" alt="TechWave"></a>
      <button class="mobile-menu-btn" aria-label="Menü">☰</button>
      <nav>
        <a href="../index.html">Ana Sayfa</a>
        <a href="../kategori.html">Kategoriler</a>
        <a href="../iletisim.html">İletişim</a>
        <button class="theme-toggle" aria-label="Tema Değiştir">🌓</button>
      </nav>
    </div>
  </header>
  <article class="article-page">
    <div class="container">
      <div class="article-header">
        <span class="card-tag" data-category="__CAT__">__CAT__</span>
        <h1 class="article-title">__TITLE__</h1>
        <div class="article-meta">
          <span>📅 __DATE_H__</span>
          <span>⏱ __READ__</span>
          <span>👤 Çağlar Şelik</span>
        </div>
      </div>
      <div class="article-hero">
        <img src="__HERO__" alt="__TITLE__" loading="eager">
      </div>
      <div class="article-content">


__BODY__


      </div>
      <div class="article-tags">
        <span class="card-tag" data-category="__CAT__">__CAT__</span>
      </div>
    </div>
    <div class="container">
    <div class="author-box">
      <div class="author-avatar">👤</div>
      <div class="author-info">
        <div class="author-name">Çağlar Şelik</div>
        <p class="author-bio">TechWave'in kurucusu ve editörü. Yapay zeka araçları, yazılım ve siber güvenlik konularını yakından takip ediyor; rehberleri kendi deneyim ve araştırmalarıyla hazırlıyor. <a href="../hakkimizda.html">Hakkında daha fazla bilgi</a></p>
      </div>
    </div>
  </div>

</article>
  <div class="container">
    <div class="newsletter-cta">
      <h3>📬 TechWave Bültenine Katılın</h3>
      <p>Her hafta yapay zeka, yazılım ve teknoloji dünyasından en güncel gelişmeler doğrudan e-posta kutuna gelsin.</p>
      <form class="newsletter-form" onsubmit="event.preventDefault(); alert('Teşekkürler! Bültenimize başarıyla katıldınız.');">
        <input type="email" placeholder="E-posta adresiniz" required>
        <button type="email" placeholder="E-posta adresiniz" required>
        <button type="submit">Katıl</button>
      </form>
    </div>
  </div>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="../index.html" class="logo"><img src="../images/logo.svg" alt="TechWave"></a>
          <p>Teknoloji, yapay zeka ve yazılım dünyasından güncel yazılar ve rehberler. 2026'dan beri aktif.</p>
          <a href="https://x.com/blogTechWave" target="_blank" rel="noopener" style="display:inline-flex; align-items:center; gap:6px; margin-top:12px; font-weight:600; color:#0891b2;"> 🐦 X'te takip et: @blogTechWave</a>
        </div>
        <div>
          <h3 style="font-size:.95rem; margin-bottom:12px;">Sayfalar</h3>
          <ul class="footer-links">
            <li><a href="../index.html">Ana Sayfa</a></li>
            <li><a href="../kategori.html">Kategoriler</a></li>
            <li><a href="../hakkimizda.html">Hakkımızda</a></li>
            <li><a href="../iletisim.html">İletişim</a></li>
          </ul>
        </div>
        <div>
          <h3 style="font-size:.95rem; margin-bottom:12px;">Kategoriler</h3>
          <ul class="footer-links">
            <li><a href="../kategori.html">Yapay Zeka</a></li>
            <li><a href="../kategori.html">Yazılım</a></li>
            <li><a href="../kategori.html">Python</a></li>
            <li><a href="../kategori.html">AI Araçları</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 TechWave. Tüm hakları saklıdır.</p>
      </div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>
'''

HEAD = (HEAD.replace('__DESC__', DESC)
            .replace('__TITLE__', TITLE)
            .replace('__HERO__', px(HERO))
            .replace('__SLUG__', SLUG)
            .replace('__DATE_ISO__', DATE_ISO)
            .replace('__DATE_H__', DATE_HUMAN)
            .replace('__CAT__', CAT)
            .replace('__READ__', READ)
            .replace('__BODY__', BODY))

# --- fix accidental duplicate button line in newsletter form ---
HEAD = HEAD.replace(
    '<input type="email" placeholder="E-posta adresiniz" required>\n        <button type="email" placeholder="E-posta adresiniz" required>\n        <button type="submit">Katıl</button>',
    '<input type="email" placeholder="E-posta adresiniz" required>\n        <button type="submit">Katıl</button>')

art_path = os.path.join(BASE, 'articles', SLUG + '.html')
with io.open(art_path, 'w', encoding='utf-8') as f:
    f.write(HEAD)

# ---------------- word count ----------------
txt = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', HEAD, flags=re.DOTALL | re.IGNORECASE)
m = re.search(r'<div class="article-content"[^>]*>(.*?)\n\s*</div>', HEAD, re.DOTALL)
content = m.group(1) if m else HEAD
content = re.sub(r'<[^>]+>', ' ', content)
content = htmlmod.unescape(content)
words = [w for w in re.split(r'\s+', content) if w]

# ---------------- images used ----------------
imgs = sorted(set(int(x) for x in re.findall(r'images\.pexels\.com/photos/(\d+)/', HEAD)))

# ---------------- index.html card ----------------
idx_path = os.path.join(BASE, 'index.html')
with io.open(idx_path, encoding='utf-8') as f:
    idx = f.read()

EXCERPT = ("2026'nın en iyi 10 monitörü: Samsung Odyssey OLED, LG UltraGear, ASUS ROG Swift, Dell UltraSharp, "
           "BenQ PD3226G, LG UltraWide, AOC, Xiaomi, Philips ve iiyama; OLED/IPS/VA/Mini LED panel rehberi, "
           "amaç tablosu, çözünürlük-yenileme ve boyut-mesafe rehberi ile SSS.")

CARD = '''
        <!-- YENİ MAKALE - Otomatik eklendi -->
        <article class="card" data-category="__CAT__">
          <div class="card-img"><img src="__HERO__" alt="__TITLE__" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag" data-category="__CAT__">__CAT__</span>
            <h2 class="card-title">
              <a href="articles/__SLUG__.html">__TITLE__</a>
            </h2>
            <p class="card-excerpt">__EXCERPT__</p>
            <div class="card-meta">
              <span>📅 __DATE_H__</span>
              <span>⏱ __READ__</span>
            </div>
          </div>
        </article>
'''.replace('__CAT__', CAT).replace('__HERO__', px(HERO)).replace('__TITLE__', TITLE) \
   .replace('__SLUG__', SLUG).replace('__EXCERPT__', EXCERPT) \
   .replace('__DATE_H__', DATE_HUMAN).replace('__READ__', READ)

anchor = '<div class="card-grid">'
if SLUG + '.html' not in idx:
    assert anchor in idx, 'card-grid anchor not found'
    idx = idx.replace(anchor, anchor + CARD, 1)
    with io.open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html: card added')
else:
    print('index.html: card already present')

# ---------------- sitemap.xml ----------------
sm_path = os.path.join(BASE, 'sitemap.xml')
with io.open(sm_path, encoding='utf-8') as f:
    sm = f.read()

url = ('  <url>\n'
       '    <loc>https://techwaveblog.site/articles/__SLUG__.html</loc>\n'
       '    <lastmod>__LASTMOD__</lastmod>\n'
       '    <changefreq>weekly</changefreq>\n'
       '    <priority>0.8</priority>\n'
       '  </url>\n'
       '</urlset>').replace('__SLUG__', SLUG).replace('__LASTMOD__', DATE_ISO)

if SLUG + '.html' not in sm:
    sm = sm.replace('</urlset>', url)
    with io.open(sm_path, 'w', encoding='utf-8') as f:
        f.write(sm)
    print('sitemap.xml: url added')
else:
    print('sitemap.xml: url already present')

print('WORDS=%d' % len(words))
print('IMAGES=%s' % ','.join(str(i) for i in imgs))
print('ARTICLE=%s' % art_path)
