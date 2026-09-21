#!/usr/bin/env python3
"""Create 2 new articles for TechWave blog."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(BASE, "articles")

# ============================================================
# ARTICLE 1: Yapay Zeka Nedir? 2026'da Bilmeniz Gereken Her Şey
# ============================================================

article1_content = """
        <h2>Yapay Zeka Nedir?</h2>
        <p>Yapay zeka (Artificial Intelligence / AI), insan zekasını taklit eden veya insan benzeri zekâ gerektiren görevleri yerine getirebilen bilgisayar sistemlerinin tümüdür. MACHINE LEARNING, DEEP LEARNING ve NÖRAL AĞLAR gibi alt dalları bulunan yapay zeka, günümüzde hayatımızın hemen her alanında karşımıza çıkmaktadır. 1956 yılında Dartmouth Konferansı'nda约翰·マッカーシー tarafından ilk kez resmi olarak tanımlanan bu kavram, o günden bu yana büyük bir dönüşüm geçirmiştir.</p>
        <p>2026 yılında yapay zeka, artık yalnızca teknoloji şirketlerinin değil, her sektörden işletmenin vazgeçilmez bir parçası haline gelmiştir. Doğal dil işleme (NLP), bilgisayarlı görü (Computer Vision), otonom sistemler ve üretken yapay zeka (Generative AI) alanlarında yaşanan gelişmeler, iş dünyasını ve günlük yaşamımızı köklü biçimde değiştirmektedir.</p>

        <h2>Yapay Zeka Nasıl Çalışır?</h2>
        <h3>Makine Öğrenmesi (Machine Learning)</h3>
        <p>Makine öğrenmesi, bilgisayarların verilerden desen çıkarmasını ve bu desenlere dayanarak tahminler yapmasını sağlayan bir yaklaşımdır. Denetimli öğrenme (Supervised Learning), denetimsiz öğrenme (Unsupervised Learning) ve pekiştirmeli öğrenme (Reinforcement Learning) olmak üzere üç ana kategorisi bulunmaktadır. Örneğin, bir e-posta filtresinin spam iletmeleri tanıması, makine öğrenmesinin en yaygın uygulamalarından biridir.</p>
        <h3>Derin Öğrenme (Deep Learning)</h3>
        <p>Derin öğrenme, yapay sinir ağlarını kullanarak karmaşık verileri işleyen bir makine öğrenmesi dalıdır. Çok katmanlı sinir ağları sayesinde görüntü tanıma, ses işleme ve doğal dil anlama gibi zorlu görevlerde insan düzeyinde başarı sağlamaktadır. ChatGPT, Claude ve Gemini gibi Large Language Modelleri (LLM'ler) de derin öğrenmenin en güncel ve etkileyici uygulamaları arasında yer almaktadır.</p>
        <h3>Nöral Ağlar (Neural Networks)</h3>
        <p>İnsan beyninin sinir yapısından ilham alan nöral ağlar, girdi katmanı, gizli katmanlar ve çıktı katmanından oluşur. Her düğüm (nöron), girdileri alır, bir ağırlıklandırılmış toplama yapar ve bir aktivasyon fonksiyonu uygular. Bu yapı, görüntü tanıma (CNN), sekansanal veri işleme (RNN/LSTM) ve dikkat mekanizmaları (Transformer) gibi farklı mimarilerin temelini oluşturur.</p>

        <h2>Yapay Zeka Türleri</h2>
        <h3>1. Dar Yapay Zeka (Narrow AI / Weak AI)</h3>
        <p>Bu, günümüzde var olan tek yapay zeka türüdür. Belirli bir göreve odaklanmış, o görevde insan düzeyinde veya insan üstünde performans gösterebilen sistemlerdir. Siri, Alexa, Google Asistan, önerilen içerik sistemleri ve otonom araçlar hep dar yapay zeka örnekleridir.</p>
        <h3>2. Genel Yapay Zeka (General AI / Strong AI)</h3>
        <p>İnsan düzeyinde genel zekaya sahip olacak, herhangi bir entelektüel görevi insan gibi yerine getirebilecek yapay zeka türüdür. Henüz gerçekleşmemiştir ancak 2026 yılında各大 teknoloji şirketleri bu hedefe ulaşmak için yoğun çalışmalar yürütmektedir. GPT-5, Gemini Ultra ve Claude 4 gibi modeller bu yönde önemli adımlar temsil etmektedir.</p>
        <h3>3. Süper Yapay Zeka (Super AI)</h3>
        <p>İnsan zekasını tüm alanlarda aşacak, kendi kendine düşünebilen, plan yapabilen ve yaratabilen yapay zeka türüdür. Henüz teorik bir kavramdır ve bilim insanları tarafından hem heyecanla hem de endişeyle tartışılmaktadır. Nick Bostrom ve Stuart Russell gibi isimler, süper yapay zekanın insanlık için hem fırsat hem de varoluşsal risk taşıdığını savunmaktadır.</p>

        <h2>Günlük Hayatta Yapay Zeka Uygulamaları</h2>
        <h3>Sağlık</h3>
        <p>Yapay zeka, tıbbi teşhiste çığır açmaktadır. Radyoloji影像larının analizi, ilaç keşfi, genomik araştırma ve kişiselleştirilmiş tedavi planları AI sayesinde büyük bir hız kazanmıştır. 2026 yılında Việt胜 Hospital'ın AI destekli kanser tarama sistemleri, erken teşhis oranlarını önemli ölçüde artırmıştır.</p>
        <h3>Eğitim</h3>
        <p>Kişiselleştirilmiş öğrenme deneyimleri sunan AI destekli eğitim platformları, her öğrencinin öğrenme hızına ve tarzına uygun içerikler sunmaktadır. Dil öğrenme uygulamalarından online sınavlara kadar eğitim sectoründe yapay zeka devrimi yaşanmaktadır.</p>
        <h3>Finans</h3>
        <p>Algoritmik ticaret, kredi risk analizi, dolandırıcılık tespiti ve kişisel finansal asistanlar yapay zeka sayesinde daha hassas ve hızlı hale gelmiştir. Robo-danışmanlar, bireysel yatırımcıların portföy yönetimini demokratikleştirmektedir.</p>
        <h3>Ulaştırma</h3>
        <p>Otonom araçlar, trafik optimizasyonu, rota planlama ve lojistik yönetimi yapay zeka ile dönüşüm geçirmektedir. Tesla, Waymo ve yerli girişimlerin otonom araç testleri 2026 yılında büyük ilerleme kaydetmiştir.</p>

        <h2>Türkiye'de Yapay Zeka</h2>
        <p>Türkiye, yapay zeka alanında son yıllarda büyük bir atılım içerisindedir. TÜBİTAK'ın AI strateji belgeleri, üniversitelerin araştırma merkezleri ve özel sektörün yatırımları ile Türkiye, bölgesel bir yapay zeka merkezi olma yolunda ilerlemektedir. İstanbul Teknik Üniversitesi, Ortadoğu Teknik Üniversitesi ve Boğaziçi Üniversitesi'nin yapay zeka araştırma laboratuvarları, uluslararası düzeyde önemli çalışmalara imza atmaktadır.</p>
        <p>Türkiye'deki girişim ekosistemi de AI tabanlı çözümler üretmektedir. Sağlık, e-ticaret, tarım ve savunma sanayii gibi alanlarda yerli yapay zeka çözümleri geliştirilmekte ve ihracatı yapılmaktadır. Hükümetin dijital dönüşüm stratejileri ve yapay zeka milli strateji belgesi, bu dönüşüme hız kazandırmaktadır.</p>

        <h2>2026'da Yapay Zekanın Geleceği</h2>
        <p>2026 yılı, yapay zeka için bir dönüm noktası niteliği taşımaktadır. Üretken yapay zeka araçlarının yaygınlaşması, multimodal modellerin gelişmesi ve edge computing ile cihaz düzeyinde yapay zeka uygulamalarının artması beklenmektedir. İşte öne çıkan trendler:</p>
        <ul>
            <li><strong>Multimodal Yapay Zeka:</strong> Metin, görüntü, ses ve videoyu aynı anda işleyebilen modeller (GPT-5, Gemini 2.0)</li>
            <li><strong>AI Ajanları:</strong> Bağımsız karar alabilen ve görevleri otonom olarak tamamlayabilen yapay zeka sistemleri</li>
            <li><strong>Küçültülmüş Modeller:</strong> Mobil cihazlarda ve edge cihazlarda çalışabilen küçük ama güçlü AI modelleri</li>
            <li><strong>Sorumlu Yapay Zeka:</strong> Etik, şeffaflık ve adalet odaklı AI geliştirme yaklaşımları</li>
            <li><strong>AI ve Bilim:</strong> İlaç keşfi, iklim modellemesi ve uzay araştırmalarında yapay zeka kullanımı</li>
        </ul>

        <h2>Riskler ve Etik Endişeler</h2>
        <p>Yapay zekanın hızlı gelişimi beraberinde ciddi riskleri de getirmektedir. Gizlilik ihlalleri, önyargılı algoritmalar, iş gücü kaybı, dezenfomasyon üretimi ve otonom silah sistemleri gibi konular, yapay zeka etiğinin en tartışmalı başlıkları arasında yer almaktadır.</p>
        <p>Avrupa Birliği'nin AI Yasası (AI Act), yapay zeka geliştiricileri için katı düzenlemeler getirmektedir. Türkiye'de de benzer düzenlemelerin hazırlanması süreci devam etmektedir. Responsible AI (Sorumlu Yapay Zeka) yaklaşımı, geliştiricilerin adillik, şeffaflık ve hesap verebilirlik ilkelerini benimsemesini hedeflemektedir.</p>
        <blockquote>"Yapay zeka, insanlığın en büyük güçlerinden biri olabilir; ancak bu gücü doğru kullanmak, en büyük sorumluluğumuzdur." — Tim Cook</blockquote>

        <h2>Sonuç</h2>
        <p>Yapay zeka, 2026 yılında hayatımızın her alanında varlığını hissettiren, dönüşümün ve yeniliğin anahtarı konumundadır. Sağlık, eğitim, finans, ulaşım ve daha birçok sektörde köklü değişikliklere yol açmaktadır. Türkiye'nin bu global dönüşüme ayak uydurması ve yapay zeka alanında yatırım yapması, geleceğin rekabetçi ekonomisinde söz sahibi olabilmesi için hayati önem taşımaktadır.</p>
        <p>Bireyler olarak yapay zeka hakkında bilgi sahibi olmak, bu araçları etkin kullanabilmek ve etik boyutlarını anlamak, geleceğe hazırlanmak adına atılabilecek en önemli adımlardan biridir. TechWave olarak yapay zeka gelişmelerini takip etmeye ve sizleri bilgilendirmeye devam edeceğiz.</p>
        <p><em>Bu makale TechWave tarafından hazırlanmıştır.</em></p>"""

article1 = {
    "title": "Yapay Zeka Nedir? 2026'da Bilmeniz Gereken Her Şey",
    "slug": "yapay-zeka-nedir-2026da-bilmeniz-gereken-her-sey",
    "category": "Yapay Zeka",
    "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
    "meta_description": "Yapay zeka nedir, nasıl çalışır ve 2026 yılında hayatımızı nasıl değiştiriyor? Yapay zeka türleri, uygulamaları, Türkiye'deki durumu ve etik endişeler hakkında kapsamlı rehber.",
    "date": "21 Eylül 2026",
    "date_iso": "2026-09-21",
    "read_time": "7 dk okuma",
    "content": article1_content,
}

# ============================================================
# ARTICLE 2: WordPress mi HTML mi? 2026'da Blog Kurmak İçin En İyi Seçim
# ============================================================

article2_content = """
        <h2>WordPress mi HTML mi? Doğru Seçim Hangisi?</h2>
        <p>Blog kurmak isteyenlerin en çok karşılaştığı karar WordPress mi yoksa saf HTML/CSS ile mi blog yazacağıdır. Her iki yaklaşımın da kendine göre avantajları ve dezavantajları bulunmaktadır. Bu makalede, 2026 yılında hangi seçimin size daha uygun olduğunu kapsamlı bir şekilde ele alacağız.</p>

        <h2>WordPress: Avantajları ve Dezavantajları</h2>
        <h3>WordPress'in Avantajları</h3>
        <p>WordPress, dünya genelinde web sitelerinin yaklaşık %43'ünü power etmektedir. Kolay kurulum, geniş eklenti ekosistemi, binlerce tema seçeneği ve teknik bilgiye ihtiyaç duymadan içerik yönetim imkanı sunması, WordPress'i popüler yapmaktadır. WooCommerce, Elementor, Yoast SEO gibi eklentiler sayesinde e-ticaret sitesinden portfolyoya kadar her türlü web sitesi kurulabilmektedir.</p>
        <p>WordPress'in en büyük avantajlarından biri topluluk desteğidir. Milyonlarca kullanıcı, binlerce geliştirici ve zengin Türkçe kaynak havuzu sayesinde sorun yaşadığınızda hızlıca çözüm bulabilirsiniz. Ayrıca WordPress.com üzerinden ücretsiz hosting imkanı da sunulmaktadır.</p>
        <h3>WordPress'in Dezavantajları</h3>
        <p>WordPress'in dezavantajları da göz ardı edilemez. Güvenlik açıkları en sık karşılaşılan sorunların başında gelmektedir. Eklenti ve tema güncellemelerinin takip edilmesi, PHP tabanlı yapısının getirdiği bazı sınırlamalar, ve çok fazla eklenti kullanılması halinde site hızının düşmesi önemli sorunlardır. Ayrıca WordPress barındırma (hosting) masrafı da dikkate alınmalıdır.</p>

        <h2>HTML/CSS Blog: Avantajları ve Dezavantajları</h2>
        <h3>HTML/CSS'in Avantajları</h3>
        <p>Saf HTML ve CSS ile oluşturulan bloglar, tối hız ve performans sunar. Statik dosyalar olduğu için sunucu yükü minimaldir,/PageSpeed Insights'tan tam puan almak mümkündür. Güvenlik açığı neredeyse yoktur çünkü sunucu tarafı bir dil çalışmaz. Dosya boyutları küçüktür, CDN üzerinden hızla dağıtılabilir. GitHub Pages, Netlify ve Vercel gibi platformlarda ücretsiz olarak barındırılabilir.</p>
        <p>HTML/CSS bloglarSEO açısından da büyük avantaj sağlar. Hızlı yükleme süreleri Google sıralamalarında kritik bir faktördür. Schema.org markup ile zengin sonuçlar elde edilebilir. Daha az bağımlılık, daha az kırılganlık demektir.</p>
        <h3>HTML/CSS'in Dezavantajları</h3>
        <p>HTML/CSS blogların en büyük dezavantajı, içerik yönetimi için teknik bilgi gerektirmesidir. Her yeni yazı için HTML dosyası oluşturmak, test etmek ve yayına almak uzun sürebilir. Yorum sistemi, arama fonksiyonu ve etiket sistemi gibi özellikler için sıfırdan kodlama gerekir. İçerik yönetim sistemi (CMS) bulunmadığı için büyük içerik havuzlarını yönetmek zorlaşır.</p>

        <h2>Karşılaştırma Tablosu</h2>
        <table>
            <thead>
                <tr>
                    <th>Kriter</th>
                    <th>WordPress</th>
                    <th>HTML/CSS</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kurulum Zorluğu</td>
                    <td>Kolay (5 dakika)</td>
                    <td>Orta-Zor</td>
                </tr>
                <tr>
                    <td>Teknik Bilgi Gereksinimi</td>
                    <td>Düşük</td>
                    <td>Yüksek</td>
                </tr>
                <tr>
                    <td>Site Hızı</td>
                    <td>Orta</td>
                    <td>Mükemmel</td>
                </tr>
                <tr>
                    <td>Güvenlik</td>
                    <td>Düşük (saldırganlara açık)</td>
                    <td>Yüksek (statik dosya)</td>
                </tr>
                <tr>
                    <td>SEO Performansı</td>
                    <td>İyi (eklentilerle)</td>
                    <td>Mükemmel (doğal)</td>
                </tr>
                <tr>
                    <td>Host Maliyeti</td>
                    <td>Aylık 10-50 USD</td>
                    <td>Ücretsiz (GitHub Pages)</td>
                </tr>
                <tr>
                    <td>İçerik Yönetimi</td>
                    <td>Kolay (CMS paneli)</td>
                    <td>Zor (dosya düzenleme)</td>
                </tr>
                <tr>
                    <td>Ölçeklenebilirlik</td>
                    <td>Yüksek</td>
                    <td>Düşük</td>
                </tr>
                <tr>
                    <td>Topluluk Desteği</td>
                    <td>Çok geniş</td>
                    <td>Sınırlı</td>
                </tr>
            </tbody>
        </table>

        <h2>Performans Karşılaştırması</h2>
        <p>Site hızı, 2026 yılında Google sıralama faktörleri arasında en kritik unsurlardan biridir. HTML/CSS ile oluşturulan statik bloglar,server tarafı işleme olmadığı için ortalama 100-200ms'de yüklenirken,WordPress siteleri ortalama 1-3 saniye yüklenmektedir. Core Web Vitals (LCP, FID, CLS) metriklerinde HTML/CSS bloglar her zaman üstündür.</p>
        <p>Ancak modern WordPress kurulumlarında LiteSpeed Cache, WP Rocket ve Redis gibi optimizasyon araçları kullanılarak performans önemli ölçüde artırılabilir. Managed WordPress hosting hizmetleri de bu konuda büyük kolaylık sağlamaktadır.</p>

        <h2>SEO Karşılaştırması</h2>
        <p>Her iki platform da SEO açısından güçlüdür; ancak farklı avantajlar sunur. WordPress, Yoast SEO, Rank Math ve All in One SEO Pack gibi eklentiler ile teknik SEO ayarlarını kolayca yapmanıza olanak tanır. Otomatik XML sitemap oluşturma, schema markup ekleme ve sosyal medya meta etiketleri gibi özellikler entegre gelir.</p>
        <p>HTML/CSS bloglarda ise SEO tamamen size bağlıdır. Doğru HTML yapısı, semantic markup, hızlı yükleme süreleri ve schema.org entegrasyonu ile mükemmel SEO sonuçları elde edebilirsiniz; ancak bunu manuel olarak yapmanız gerekir. Avantajı, gereksiz eklenti bağımlılığı olmaması ve saf, temiz bir HTML yapısı elde edebilmenizdir.</p>

        <h2>Maliyet Karşılaştırması</h2>
        <p>WordPress için hosting masrafı aylık ortalama 10-50 USD arasında değişmektedir. Ücretsiz tema ve eklentiler mevcut olsa da, profesyonel bir görünüm için premium tema ve eklenti masrafları da eklenebilir. Domain ücreti her iki platform için de ortaktır.</p>
        <p>HTML/CSS bloglar için GitHub Pages, Netlify veya Vercel gibi platformlarda tamamen ücretsiz hosting imkanı bulunmaktadır. Sadece bir domain name için masraf yapmanız yeterlidir. Uzun vadede HTML/CSS bloglar çok daha ekonomik bir seçenektir.</p>

        <h2>Güvenlik Karşılaştırması</h2>
        <p>Güvenlik, web sitesi sahiplerinin en çok endişelendiği konuların başında gelmektedir. WordPress, açık kaynaklı yapısı nedeniyle sıklıkla güvenlik açıklarına maruz kalmaktadır. Eklenti ve tema kaynaklı güvenlik açıkları, brute force saldırıları ve SQL injection gibi tehditler sürekli gündemdedir.</p>
        <p>HTML/CSS bloglar ise statik dosyalardan oluştuğu için sunucu tarafı bir kod çalıştırmaz ve bu nedenle güvenlik açığı neredeyse yoktur. DDoS saldırılarına karşı koruma dışında özel bir güvenlik önlemi gerekmez. Bu açıdan HTML/CSS, güvenlik bilincine sahip kullanıcılar için çok daha güvenli bir tercihdir.</p>

        <h2>Hangi Durumda Hangisini Tercih Etmelisiniz?</h2>
        <h3>WordPress'i Tercih Etmelisiniz Eğer:</h3>
        <ul>
            <li>Teknik bilgi düzeyiniz düşükse ve hızlıca bir blog kurmak istiyorsanız</li>
            <li>Sık içerik güncelleyecekseniz ve CMS paneline ihtiyaç duyuyorsanız</li>
            <li>E-ticaret, forum veya topluluk gibi gelişmiş özellikler eklemeyi planlıyorsanız</li>
            <li>Geniş bir topluluk desteğine ve zengin kaynaklara erişmek istiyorsanız</li>
            <li>Birden fazla yazar ile içerik üretecekseniz</li>
        </ul>
        <h3>HTML/CSS'i Tercih Etmelisiniz Eğer:</h3>
        <ul>
            <li>Site hızı ve performans sizin için en üst düzeyde önemliyse</li>
            <li>Maksimum güvenlik talep ediyorsanız</li>
            <li>Ücretsiz hosting ile çalışmak istiyorsanız</li>
            <li>Kişisel bir blog veya portfolyo sitesi kuracaksanız</li>
            <li>Uzun vadeli, sürdürülebilir ve düşük maliyetli bir çözüm arıyorsanız</li>
            <li>HTML, CSS ve temel JavaScript bilgisine sahipseniz</li>
        </ul>
        <h3>Hybrid Yaklaşım: Statik Site Oluşturucular</h2>
        <p>2026 yılında popülerleşen bir diğer yaklaşım, Hugo, Jekyll, Eleventy ve Astro gibi statik site oluşturucuları kullanmaktır. Bu araçlar, Markdown ile içerik yazmanızı sağlarken HTML/CSS performansını sunar. Hem WordPress'in içerik yönetim kolaylığını hem de HTML/CSS'in hız ve güvenlik avantajlarını bir arada sunan bu çözüm, birçokdeveloper için ideal orta yol olabilir.</p>

        <h2>Sonuç</h2>
        <p>WordPress ve HTML/CSS arasındaki seçim, tamamen ihtiyaçlarınıza, teknik bilgi düzeyinize ve uzun vadeli planlarınıza bağlıdır. Hızlı ve kolay bir çözüm istiyorsanız WordPress, maksimum performans ve güvenlik istiyorsanız HTML/CSS doğru tercih olacaktır. 2026 yılında statik site oluşturucuların yükselişi ile her iki dünyanın en iyi yönlerini birleştiren hybrid çözümler de giderek daha popüler hale gelmektedir.</p>
        <p>Hangi yolu seçerseniz seçin, kaliteli içerik üretmek ve okuyucularınıza değer sunmak her zaman en önemli faktör olacaktır. TechWave olarak teknoloji blogculuğu hakkında daha fazla rehber ve ipucu paylaşmaya devam edeceğiz.</p>
        <p><em>Bu makale TechWave tarafından hazırlanmıştır.</em></p>"""

article2 = {
    "title": "WordPress mi HTML mi? 2026'da Blog Kurmak İçin En İyi Seçim",
    "slug": "wordpress-mi-html-mi-2026da-blog-kurmak-icin-en-iyi-secim",
    "category": "Yazılım",
    "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1200",
    "meta_description": "WordPress mi HTML mi? 2026'da blog kurmak için hangi platform daha iyi? Performans, SEO, güvenlik ve maliyet karşılaştırması ile kapsamlı rehber.",
    "date": "21 Eylül 2026",
    "date_iso": "2026-09-21",
    "read_time": "6 dk okuma",
    "content": article2_content,
}

# ============================================================
# HTML Template (copy from python-nedir-bilmeniz-gereken-her-sey.html)
# ============================================================

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="tr" data-theme="light">
<head>
    <meta name="google-site-verification" content="-7pHgAzQSH7HXgUgc7cpgCXlwHivhN9X5MWaniE68Go" />
<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){{
        m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {{if (document.scripts[j].src === r) {{ return; }} }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    }})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=112858721', 'ym');

    ym(112858721, 'init', {{ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true}});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/112858721" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_description}">
  <meta name="author" content="TechWave">
  <meta name="robots" content="index, follow">
  <title>{title} — TechWave</title>
  <meta property="og:title" content="{title} — TechWave">
  <meta property="og:description" content="{meta_description}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:image" content="{image_url}">
  <link rel="canonical" href="https://techwaveblog.site/articles/{slug}.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "author": {{"@type": "Person", "name": "TechWave"}},
    "datePublished": "{date_iso}",
    "description": "{meta_description}",
    "publisher": {{"@type": "Organization", "name": "TechWave", "url": "https://techwaveblog.site"}},
    "mainEntityOfPage": "https://techwaveblog.site/articles/{slug}.html",
    "image": "{image_url}"
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3459052960619900" crossorigin="anonymous"></script>
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
        <button class="theme-toggle" aria-label="Tema Değiştir">🌙</button>
      </nav>
    </div>
  </header>
  <article class="article-page">
    <div class="container">
      <div class="article-header">
        <span class="card-tag" data-category="{category}">{category}</span>
        <h1 class="article-title">{title}</h1>
        <div class="article-meta">
          <span>📅 {date}</span>
          <span>⏱️ {read_time}</span>
        </div>
      </div>
      <div class="article-hero">
        <img src="{image_url}" alt="{title}" loading="eager">
      </div>
      <div class="article-content">
        {content}
      </div>
      <div class="article-tags">
        <span class="card-tag" data-category="{category}">{category}</span>
      </div>
    </div>
  </article>
  <div class="container">
    <div class="newsletter-cta">
      <h3>📬 TechWave Bültenine Katılın</h3>
      <p>Her hafta yapay zeka, yazılım ve teknoloji dünyasından en güncel gelişmeler doğrudan e-posta kutuna gelsin.</p>
      <form class="newsletter-form" onsubmit="event.preventDefault(); alert('Teşekkürler! Bültenimize başarıyla katıldınız.');">
        <input type="email" placeholder="E-posta adresiniz" required>
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
</html>'''


def write_file(filepath, content):
    """Write file with utf-8 encoding using Python."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: {filepath}")


def create_article_html(article):
    """Create the full HTML for an article."""
    html = HTML_TEMPLATE.format(
        title=article["title"],
        slug=article["slug"],
        category=article["category"],
        image_url=article["image_url"],
        meta_description=article["meta_description"],
        date=article["date"],
        date_iso=article["date_iso"],
        read_time=article["read_time"],
        content=article["content"],
    )
    filepath = os.path.join(ARTICLES_DIR, f"{article['slug']}.html")
    write_file(filepath, html)
    return filepath


def build_card_html(article, img_url=None):
    """Build the article card HTML for index.html."""
    if img_url is None:
        img_url = article["image_url"]
    return f'''
        <!-- YENİ MAKALE — Otomatik eklendi -->
        <article class="card" data-category="{article['category']}">
          <div class="card-img"><img src="{img_url}" alt="{article['title']}" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag" data-category="{article['category']}">{article['category']}</span>
            <h2 class="card-title">
              <a href="articles/{article['slug']}.html">{article['title']}</a>
            </h2>
            <p class="card-excerpt">{article['meta_description'][:120]}...</p>
            <div class="card-meta">
              <span>📅 {article['date']}</span>
              <span>⏱️ {article['read_time']}</span>
            </div>
          </div>
        </article>
'''


def update_index_html(articles):
    """Prepend new article cards to index.html card-grid section."""
    index_path = os.path.join(BASE, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build card HTML for each new article
    cards = ""
    for a in articles:
        cards += build_card_html(a)

    # Insert after <div class="card-grid">
    marker = '<div class="card-grid">'
    if marker in content:
        content = content.replace(marker, marker + "\n" + cards)
    else:
        print("WARNING: Could not find card-grid marker in index.html")
        return

    write_file(index_path, content)


def update_sitemap(articles):
    """Add new article URLs to sitemap.xml."""
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_urls = ""
    for a in articles:
        new_urls += f'''  <url>
    <loc>https://techwaveblog.site/articles/{a["slug"]}.html</loc>
    <lastmod>2026-09-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''

    # Insert before closing </urlset>
    content = content.replace("</urlset>", new_urls + "</urlset>")
    write_file(sitemap_path, content)


if __name__ == "__main__":
    os.makedirs(ARTICLES_DIR, exist_ok=True)

    print("Creating Article 1: Yapay Zeka Nedir...")
    create_article_html(article1)

    print("Creating Article 2: WordPress mi HTML mi?...")
    create_article_html(article2)

    print("Updating index.html...")
    update_index_html([article1, article2])

    print("Updating sitemap.xml...")
    update_sitemap([article1, article2])

    print("\nAll files created successfully!")
    print("Article 1 URL: https://techwaveblog.site/articles/yapay-zeka-nedir-2026da-bilmeniz-gereken-her-sey.html")
    print("Article 2 URL: https://techwaveblog.site/articles/wordpress-mi-html-mi-2026da-blog-kurmak-icin-en-iyi-secim.html")
