#!/usr/bin/env python3
"""Rebuild Lektion 8 courseware with 100% faithful text reproduction from textbook."""

import os, re

SRC = '/home/gem/workspace/agent/workspace-main/projects/lektion7-interactive/lektion8-latest.html'
OUT = '/home/gem/workspace/agent/workspace-main/projects/lektion7-interactive/index.html'

with open(SRC) as f:
    h = f.read()

# ============================================================
# 1. Title and header replacements
# ============================================================
for old, new in [
    ('Lektion 7 · Start in die Zukunft! · 交互式课件','Lektion 8 · Was will ich werden? · 交互式课件'),
    ('语法·zu不定式','语法·并列连词'),
    ('🚀 Start in die Zukunft!','💼 Was will ich werden?'),
    ('📖 Lektion 7 <span>Start in die Zukunft!</span>','📖 Lektion 8 <span>Was will ich werden?</span>'),
]:
    if old in h: h = h.replace(old, new)

# ============================================================
# 2. HOME section
# ============================================================
hs = h.find('<section id="home"')
he = h.find('</section>', hs) + len('</section>')
h = h.replace(h[hs:he], '''<section id="home" class="active">
    <div class="hero">
      <h1>💼 Was will ich werden?</h1>
      <div class="sub">新经典德语 · 第二册 · Lektion 8</div>
      <div class="meta">职业选择 · 男女差异 · Erika的故事 · 语法:并列连词</div>
    </div>

    <div class="home-grid">
      <div class="text-card" style="cursor:pointer" onclick="switchSection('text')">
        <h3>📚 课文讲解</h3>
        <p style="font-size:13px;color:var(--text-light)">
          T1 Berufswahlverhalten + Studienwahl · T2 Lieber Werkstatt statt Schreibtisch
        </p>
      </div>
      <div class="text-card" style="cursor:pointer" onclick="switchSection('vocab')">
        <h3>📝 重点词汇</h3>
        <p style="font-size:13px;color:var(--text-light)">
          Beruf & Studium · 职业选择词汇 · 性格特质 · 点击翻转记忆
        </p>
      </div>
      <div class="text-card" style="cursor:pointer" onclick="switchSection('grammar')">
        <h3>🔤 语法 · 并列连词</h3>
        <p style="font-size:13px;color:var(--text-light)">
          zwar…aber · nicht nur…sondern auch · sowohl…als auch
        </p>
      </div>
      <div class="text-card" style="cursor:pointer" onclick="switchSection('exercise')">
        <h3>✏️ 练习</h3>
        <p style="font-size:13px;color:var(--text-light)">
          选择题 · 语法填空 · 句子改写
        </p>
      </div>
    </div>

    <div class="info-box">
      <span class="label">🎯 学习目标</span><br>
      <ul style="margin-top:6px;padding-left:18px">
        <li>了解德国男女职业/专业选择的数据差异</li>
        <li>了解女性打破传统选择非典型职业（电工）的真实故事</li>
        <li>完整掌握 Berufswahlverhalten/Studienwahl 相关词汇</li>
        <li>熟练运用并列连词 <strong>zwar…aber</strong> / <strong>nicht nur…sondern auch</strong> / <strong>sowohl…als auch</strong></li>
        <li>能用德语描述统计数据与表达职业选择</li>
      </ul>
    </div>

    <div class="info-box" style="margin-top:16px">
      <span class="label">📖 主课文</span><br>
      <ul style="margin-top:6px;padding-left:18px">
        <li><strong>T1</strong> — Berufswahlverhalten + Studienwahl（男女职业/专业选择统计）</li>
        <li><strong>T2</strong> — Lieber Werkstatt statt Schreibtisch（Erika：年轻女性成为电工的故事）</li>
      </ul>
    </div>
  </section>''')

# ============================================================
# 3. TEXT section — 100% faithful reproduction
# ============================================================
ts = h.find('<section id="text"')
te = h.find('</section>', ts) + len('</section>')
h = h.replace(h[ts:te], '''<section id="text">

    <h2 class="section-title"><span class="num">1</span> T1 · Berufswahlverhalten · 职业选择行为</h2>
    <p style="margin-bottom:12px;font-size:14px;color:var(--text-light)">
      德国男女职业选择的数据分析。点击<span style="color:#c0392b;font-weight:600">红色标注的词汇</span>查看中文释义和例句。
    </p>

    <div class="text-card">
      <h3>Berufswahlverhalten — 职业选择行为</h3>
      <div class="de">
        <p>Das <span class="vocab-word" onclick="showVocab(&apos;das Berufswahlverhalten&apos;,&apos;职业选择行为&apos;,&apos;die Art und Weise, wie man einen Beruf waehlt. 例：Das Berufswahlverhalten von Frauen und Maennern hat sich wenig veraendert.&apos;)">Berufswahlverhalten</span> von Frauen und Maennern hat sich wenig veraendert – das zeigt der Blick auf die <span class="vocab-word" onclick="showVocab(&apos;die Ausbildungsstelle&apos;,&apos;培训岗位&apos;,&apos;der Platz in einem Ausbildungsbetrieb. 例：Das zeigt der Blick auf die Ausbildungsstellen.&apos;)">Ausbildungsstellen</span>. Frauen und Maenner <span class="vocab-word" onclick="showVocab(&apos;sich entscheiden&apos;,&apos;决定&apos;,&apos;eine Wahl treffen. 例：Sie entscheiden sich fuer bestimmte Berufe.&apos;)">entscheiden</span> sich nach wie vor fuer ganz bestimmte Berufe. Heute <span class="vocab-word" onclick="showVocab(&apos;einem Beruf nachgehen&apos;,&apos;从事职业&apos;,&apos;einen Beruf ausueben. 例：Heute gehen mehr Frauen einem Beruf nach als frueher.&apos;)">gehen</span> in Deutschland deutlich mehr Frauen einem Beruf nach als vor einigen Jahrzehnten. Dennoch sind Frauen in manchen <span class="vocab-word" onclick="showVocab(&apos;die Branche&apos;,&apos;行业&apos;,&apos;ein bestimmter Wirtschaftsbereich. 例：In manchen Branchen sind Frauen kaum vertreten.&apos;)">Branchen</span> noch immer kaum vertreten.</p>
        <p style="margin-top:6px">Im vergangenen Jahr <span class="vocab-word" onclick="showVocab(&apos;gehoeren zu&apos;,&apos;属于&apos;,&apos;Teil von etwas sein. 例：Diese Berufe gehoerten zu den beliebtesten.&apos;)">gehoerten</span> die Kauffrau fuer Bueromanagement, die medizinische und die zahnmedizinische <span class="vocab-word" onclick="showVocab(&apos;der/die Fachangestellte&apos;,&apos;专业人员(职员)&apos;,&apos;eine qualifizierte Angestellte in einem Fachbereich. 例：Sie ist medizinische Fachangestellte.&apos;)">Fachangestellte</span> zu den beliebtesten <span class="vocab-word" onclick="showVocab(&apos;der Ausbildungsberuf&apos;,&apos;培训职业&apos;,&apos;ein Beruf, den man in einer Ausbildung lernt. 例：Zu den beliebtesten Ausbildungsberufen gehoert der Kfz-Mechatroniker.&apos;)">Ausbildungsberufen</span> von Frauen. Das ist im <span class="vocab-word" onclick="showVocab(&apos;der Vergleich&apos;,&apos;比较&apos;,&apos;das Vergleichen von Dingen. 例：Im Vergleich zu den Vorjahren ist das unveraendert.&apos;)">Vergleich</span> zu den Vorjahren unveraendert geblieben. Maenner waehlen <span class="vocab-word" onclick="showVocab(&apos;dagegen&apos;,&apos;相反&apos;,&apos;im Gegensatz dazu. 例：Maenner waehlen dagegen technische Berufe.&apos;)">dagegen</span> am haeufigsten die Ausbildung zum Kfz-Mechatroniker, <span class="vocab-word" onclick="showVocab(&apos;der Fachinformatiker&apos;,&apos;IT专家&apos;,&apos;eine IT-Fachkraft. 例：Viele Maenner werden Fachinformatiker.&apos;)">Fachinformatiker</span> und <span class="vocab-word" onclick="showVocab(&apos;der/die Elektroniker/in&apos;,&apos;电子技术员&apos;,&apos;eine Fachkraft fuer elektronische Systeme. 例；Er macht eine Ausbildung zum Elektroniker.&apos;)">Elektroniker</span>. Unter den Top-5-Ausbildungsberufen waren nur die Kauffrau / der Kaufmann und die <span class="vocab-word" onclick="showVocab(&apos;der Verkaeufer/die Verkaeuferin&apos;,&apos;售货员&apos;,&apos;jemand, der Waren verkauft. 例：Der Verkaeufer im Einzelhandel ist sehr beliebt.&apos;)">Verkaeuferin / der Verkaeufer</span> im <span class="vocab-word" onclick="showVocab(&apos;der Einzelhandel&apos;,&apos;零售业&apos;,&apos;der Verkauf von Waren an Endkunden. 例：Sie arbeitet im Einzelhandel.&apos;)">Einzelhandel</span> bei beiden <span class="vocab-word" onclick="showVocab(&apos;das Geschlecht&apos;,&apos;性别&apos;,&apos;ob mannlich oder weiblich. 例：Bei beiden Geschlechtern ist der Beruf beliebt.&apos;)">Geschlechtern</span> fast gleich beliebt. <span class="vocab-word" onclick="showVocab(&apos;waehrend&apos;,&apos;而、当&apos;,&apos;im Gegensatz dazu. 例：Waehrend in Bauberufen wenige Frauen sind, sind sie im Gesundheitswesen stark vertreten.&apos;)">Waehrend</span> in einigen der Bau- und Metallberufe deutlich weniger als 10 Prozent der <span class="vocab-word" onclick="showVocab(&apos;der/die Beschaeftigte&apos;,&apos;雇员、从业者&apos;,&apos;eine Person, die in einem Betrieb arbeitet. 例：Weniger als 10 Prozent der Beschaeftigten waren Frauen.&apos;)">Beschaeftigten</span> Frauen waren, <span class="vocab-word" onclick="showVocab(&apos;betragen&apos;,&apos;总计为&apos;,&apos;eine bestimmte Menge haben. 例：Ihr Anteil betrug mehr als 80 Prozent.&apos;)">betrug</span> ihr <span class="vocab-word" onclick="showVocab(&apos;der Anteil&apos;,&apos;比例&apos;,&apos;der prozentuale Teil. 例：Ihr Anteil betrug mehr als 80 Prozent.&apos;)">Anteil</span> vor allem in den Berufen des Erziehungs- und Gesundheitswesens mehr als 80 Prozent.</p>
      </div>
      <div class="highlight-box">Berufswahlverhalten: Frauen→Buero/Medizin dominieren, Maenner→Technik/Handwerk. Nur Kaufmann/Kauffrau und Verkaeufer bei beiden Geschlechtern gleich beliebt.</div>
    </div>

    <div class="text-card">
      <h3>Studienwahl — 大学专业选择</h3>
      <div class="de">
        <p>Heute entscheiden sich mehr Frauen fuer eine akademische <span class="vocab-word" onclick="showVocab(&apos;die Laufbahn&apos;,&apos;职业生涯&apos;,&apos;der berufliche Werdegang. 例：Sie entscheidet sich fuer eine akademische Laufbahn.&apos;)">Laufbahn</span>. Trotzdem zeigen sich bei der <span class="vocab-word" onclick="showVocab(&apos;die Studienwahl&apos;,&apos;大学专业选择&apos;,&apos;die Wahl des Studienfachs. 例：Bei der Studienwahl zeigen sich deutliche Unterschiede.&apos;)">Studienwahl</span> noch immer deutliche Unterschiede: <span class="vocab-word" onclick="showVocab(&apos;zwar … aber&apos;,&apos;虽然…但是&apos;,&apos;zwei gegensaetzliche Aussagen verbinden. 例：Zwar liegt BWL auf Platz eins, aber danach zeigen sich Unterschiede.&apos;)">Zwar</span> liegt <span class="vocab-word" onclick="showVocab(&apos;die Betriebswirtschaftslehre (BWL)&apos;,&apos;企业经济学&apos;,&apos;das Studium der Wirtschaftsfuehrung. 例：BWL liegt bei den Studienanfaengern auf Platz eins.&apos;)">Betriebswirtschaftslehre (BWL)</span> bei den <span class="vocab-word" onclick="showVocab(&apos;der/die Studienanfaenger/in&apos;,&apos;大学新生&apos;,&apos;jemand, der ein Studium beginnt. 例：Bei den Studienanfaengern beider Geschlechter ist BWL am beliebtesten.&apos;)">Studienanfaengern</span> beider Geschlechter auf Platz eins, danach <span class="vocab-word" onclick="showVocab(&apos;dominieren&apos;,&apos;占主导&apos;,&apos;am haeufgsten sein. 例：Bei Maennern dominieren technische Faecher.&apos;)">dominieren</span> bei den Maennern aber <span class="vocab-word" onclick="showVocab(&apos;technisch&apos;,&apos;技术的&apos;,&apos;die Technik betreffend. 例：Technische Faecher sind bei Maennern beliebt.&apos;)">technische</span> und <span class="vocab-word" onclick="showVocab(&apos;naturwissenschaftlich&apos;,&apos;自然科学的&apos;,&apos;die Naturwissenschaft betreffend. 例：Naturwissenschaftliche Faecher wie Physik sind gefragt.&apos;)">naturwissenschaftliche</span> <span class="vocab-word" onclick="showVocab(&apos;das Fach&apos;,&apos;学科、专业&apos;,&apos;ein Studienfach. 例：Informatik ist ein technisches Fach.&apos;)">Faecher</span> wie <span class="vocab-word" onclick="showVocab(&apos;die Informatik&apos;,&apos;计算机科学&apos;,&apos;die Wissenschaft der Computer. 例；Informatik ist bei Maennern sehr beliebt.&apos;)">Informatik</span> und <span class="vocab-word" onclick="showVocab(&apos;der Maschinenbau&apos;,&apos;机械工程&apos;,&apos;das Studium des Baus von Maschinen. 例：Maschinenbau ist ein typisches Mannerfach.&apos;)">Maschinenbau</span>. Bei den Frauen sind nach BWL vor allem <span class="vocab-word" onclick="showVocab(&apos;die Rechtswissenschaft&apos;,&apos;法学&apos;,&apos;das Studium des Rechts. 例：Rechtswissenschaften sind bei Frauen beliebt.&apos;)">Rechtswissenschaften</span>, <span class="vocab-word" onclick="showVocab(&apos;die Psychologie&apos;,&apos;心理学&apos;,&apos;die Wissenschaft der Psyche. 例：Psychologie studieren viele Frauen.&apos;)">Psychologie</span> sowie <span class="vocab-word" onclick="showVocab(&apos;die Erziehungswissenschaft&apos;,&apos;教育科学&apos;,&apos;die Wissenschaft der Erziehung. 例：Erziehungswissenschaften sind ein beliebtes Studienfach.&apos;)">Erziehungswissenschaften</span> beliebt.</p>
        <p style="margin-top:6px">Insgesamt <span class="vocab-word" onclick="showVocab(&apos;sich unterscheiden&apos;,&apos;区别于&apos;,&apos;anders sein. 例：Frauen und Maenner unterscheiden sich in ihrer Berufswahl.&apos;)">unterscheiden</span> sich Frauen und Maenner in ihrer Berufswahl demnach noch immer stark voneinander. Daran ist nichts <span class="vocab-word" onclick="showVocab(&apos;auszusetzen haben an&apos;,&apos;批评、挑剔&apos;,&apos;etwas zu kritisieren haben. 例：Daran ist nichts auszusetzen.&apos;)">auszusetzen</span>, wenn die Wahl den jeweiligen <span class="vocab-word" onclick="showVocab(&apos;die Vorliebe&apos;,&apos;偏好&apos;,&apos;besondere Neigung. 例：Die Wahl entspricht den Vorlieben.&apos;)">Vorlieben</span> <span class="vocab-word" onclick="showVocab(&apos;entsprechen&apos;,&apos;符合、对应&apos;,&apos;zu etwas passen. 例：Die Wahl entspricht den Vorlieben.&apos;)">entspricht</span>. Dennoch gibt es gute <span class="vocab-word" onclick="showVocab(&apos;der Grund&apos;,&apos;原因&apos;,&apos;die Ursache. 例：Es gibt gute Gruende fuer diese Entscheidung.&apos;)">Gruende</span> dafuer, junge Menschen zu <span class="vocab-word" onclick="showVocab(&apos;ermoetigen&apos;,&apos;鼓励&apos;,&apos;Mut machen. 例：Man sollte Jugendliche ermoetigen, neue Wege zu gehen.&apos;)">ermoetigen</span>, die traditionellen <span class="vocab-word" onclick="showVocab(&apos;das Rollenmuster&apos;,&apos;角色模式&apos;,&apos;typische Verhaltensweisen fuer Maenner/Frauen in der Gesellschaft. 例：Traditionelle Rollenmuster sollten aufgebrochen werden.&apos;)">Rollenmuster</span> zu verlassen und sich von <span class="vocab-word" onclick="showVocab(&apos;stereotyp&apos;,&apos;刻板的&apos;,&apos;klischeehaft, immer gleich. 例：Stereotype Vorstellungen ueber Berufe gibt es leider noch.&apos;)">stereotypen</span> <span class="vocab-word" onclick="showVocab(&apos;die Vorstellung&apos;,&apos;观念、想象&apos;,&apos;die Idee, die man von etwas hat. 例：Stereotype Vorstellungen sollten ueberwunden werden.&apos;)">Vorstellungen</span> zu loesen.</p>
      </div>
      <div class="highlight-box">Studienwahl: BWL Platz 1 bei beiden. Danach Maenner→Informatik/Maschinenbau, Frauen→Jura/Psychologie/Paedagogik.</div>
    </div>

    <h2 class="section-title" style="margin-top:40px"><span class="num">2</span> T2 · Lieber Werkstatt statt Schreibtisch · Erika</h2>
    <p style="margin-bottom:12px;font-size:14px;color:var(--text-light)">
      一位年轻女性选择成为电工的真实故事。点击红色词汇查看释义。
    </p>

    <div class="text-card">
      <h3>Erika — „Lieber Werkstatt statt Schreibtisch"</h3>
      <div class="de">
        <p><span class="vocab-word" onclick="showVocab(&apos;zunaechst&apos;,&apos;起初、首先&apos;,&apos;am Anfang, zuerst. 例：Zunaechst besuchte sie ein Gymnasium.&apos;)">Zunaechst</span> besuchte Erika ein <span class="vocab-word" onclick="showVocab(&apos;das Gymnasium&apos;,&apos;文理中学&apos;,&apos;die Schulform, die zum Abitur fuehrt. 例：Auf dem Gymnasium macht man das Abitur.&apos;)">Gymnasium</span>. <span class="vocab-word" onclick="showVocab(&apos;jedoch&apos;,&apos;然而&apos;,&apos;aber, trotzdem. 例：Jedoch stellte sie fest, dass ...&apos;)">Jedoch</span> <span class="vocab-word" onclick="showVocab(&apos;feststellen&apos;,&apos;发现、确认&apos;,&apos;etwas bemerken oder erkennen. 例：Sie stellte fest, dass ihr die Werkstatt besser gefaellt.&apos;)">stellte</span> sie fest, dass sie den Nachmittag in der <span class="vocab-word" onclick="showVocab(&apos;die Werkstatt&apos;,&apos;车间、工坊&apos;,&apos;der Arbeitsraum, in dem repariert oder gebaut wird. 例：Sie half in der Werkstatt ihres Vaters.&apos;)">Elektro-Werkstatt</span> ihres Vaters verbrachte, als nur am <span class="vocab-word" onclick="showVocab(&apos;der Schreibtisch&apos;,&apos;办公桌&apos;,&apos;der Tisch, an dem man schreibt und arbeitet. 例：Sie sass lieber in der Werkstatt als am Schreibtisch.&apos;)">Schreibtisch</span> zu sitzen. Dadurch wurde ihr klar: „Ich muss nicht studieren wie meine Freundinnen." Sie entschied sich daher fuer die <span class="vocab-word" onclick="showVocab(&apos;die Ausbildung&apos;,&apos;职业培训&apos;,&apos;die berufliche Bildung in einem Betrieb. 例：Sie machte eine Ausbildung zur Elektronikerin.&apos;)">Ausbildung</span> zur <span class="vocab-word" onclick="showVocab(&apos;der/die Elektroniker/in&apos;,&apos;电子技术员&apos;,&apos;eine Fachkraft fuer elektronische Systeme. 例：Sie absolviert eine Ausbildung zur Elektronikerin.&apos;)">Elektronikerin</span> – aus dem Traum wurde Realitaet. Nun <span class="vocab-word" onclick="showVocab(&apos;betreuen&apos;,&apos;照顾、服务&apos;,&apos;sich um jemanden kuemmern. 例：Sie betreut Kundinnen und Kunden.&apos;)">betreut</span> sie <span class="vocab-word" onclick="showVocab(&apos;der Kunde/die Kundin&apos;,&apos;客户&apos;,&apos;jemand, der eine Dienstleistung kauft. 例：Die Kundin ist mit der Arbeit zufrieden.&apos;)">Kundinnen und Kunden</span> und plant die <span class="vocab-word" onclick="showVocab(&apos;die Beleuchtung&apos;,&apos;照明&apos;,&apos;das Licht in einem Gebaeude. 例：Sie plant die Beleuchtung in Gebaeuden.&apos;)">Beleuchtung</span> in Gebaeuden.</p>
        <p style="margin-top:6px">In ihrer Arbeit kommt es <span class="vocab-word" onclick="showVocab(&apos;darauf ankommen&apos;,&apos;关键取决于&apos;,&apos;wichtig sein fuer etwas. 例：Es kommt darauf an, die Systeme richtig zu gestalten.&apos;)">darauf an</span>, <span class="vocab-word" onclick="showVocab(&apos;sogenannt&apos;,&apos;所谓的&apos;,&apos;wie man etwas nennt. 例：Sie baut sogenannte Smart-Home-Systeme.&apos;)">sogenannte</span> Smart-Home-Systeme fuer die nachhaltige <span class="vocab-word" onclick="showVocab(&apos;die Energieversorgung&apos;,&apos;能源供应&apos;,&apos;die Bereitstellung von Energie. 例：Nachhaltige Energieversorgung ist wichtig fuer den Klimaschutz.&apos;)">Energieversorgung</span> und den <span class="vocab-word" onclick="showVocab(&apos;der Klimaschutz&apos;,&apos;气候保护&apos;,&apos;der Schutz des Klimas. 例：Smart-Home-Systeme helfen beim Klimaschutz.&apos;)">Klimaschutz</span> <span class="vocab-word" onclick="showVocab(&apos;mitgestalten&apos;,&apos;共同设计、参与塑造&apos;,&apos;bei der Gestaltung mitwirken. 例：Sie gestaltet die Systeme mit.&apos;)">mitzugestalten</span>. Dabei hat Erika auch ihre persoenlichen <span class="vocab-word" onclick="showVocab(&apos;die Staerke&apos;,&apos;优势、长处&apos;,&apos;eine positive Eigenschaft oder Faehigkeit. 例：Ihre persoenlichen Staerken hat sie weiterentwickelt.&apos;)">Staerken</span> weiterentwickelt. „Ich bin <span class="vocab-word" onclick="showVocab(&apos;durchsetzungsfaehig&apos;,&apos;有决断力的&apos;,&apos;faehig, eigene Ideen und Ziele zu verwirklichen. 例：Sie ist durchsetzungsfaehiger geworden.&apos;)">durchsetzungsfaehiger</span> geworden, weil ich meistens als einzige Frau mit Maennern <span class="vocab-word" onclick="showVocab(&apos;zusammenarbeiten&apos;,&apos;合作&apos;,&apos;mit anderen gemeinsam arbeiten. 例：Sie arbeitet mit Maennern zusammen.&apos;)">zusammenarbeite</span>." Sie lachte, als sie sagte: „Ich mache das gerne, es ist ein sehr angenehmes Arbeiten. Meine maennlichen Kollegen sprechen Probleme immer direkt an. Das finde ich gut." Sie <span class="vocab-word" onclick="showVocab(&apos;sich freuen&apos;,&apos;感到高兴&apos;,&apos;froh ueber etwas sein. 例：Sie freut sich, wenn Maedchen ihren Traum verwirklichen.&apos;)">freut</span> sich, wenn Maedchen den <span class="vocab-word" onclick="showVocab(&apos;der Mut&apos;,&apos;勇气&apos;,&apos;die Tapferkeit, etwas zu tun. 例：Sie hat den Mut, ihren eigenen Weg zu gehen.&apos;)">Mut</span> haben, ihrem eigenen <span class="vocab-word" onclick="showVocab(&apos;der Berufswunsch&apos;,&apos;职业愿望&apos;,&apos;der Wunsch, einen bestimmten Beruf auszuueben. 例：Sie folgte ihrem Berufswunsch.&apos;)">Berufswunsch</span> zu folgen.</p>
      </div>
      <div class="highlight-box">Erika: besuchte Gymnasium→half lieber in der Werkstatt→Ausbildung zur Elektronikerin→betreut Kunden, plant Beleuchtung, baut Smart-Home-Systeme. „Ich bin durchsetzungsfaehiger geworden."</div>
    </div>

    </section>''')

# ============================================================
# 4. GRAMMAR section
# ============================================================
gs = h.find('<section id="grammar"')
ge = h.find('</section>', gs) + len('</section>')
h = h.replace(h[gs:ge], '''  <section id="grammar">
    <h2 class="section-title"><span class="num">1</span> 语法 · 并列连词</h2>

    <div class="grammar-block">
      <h3>1. zwar … aber (虽然…但是)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>连接两个对立的陈述。zwar 不占位，aber 占位。<br>
        <code>zwar + Satz, <strong>aber</strong> + Satz</code>
      </div>
      <div class="grammar-example">
        <span class="de">Brieffreundschaften sind <strong>zwar</strong> fast immer E-Mail-Kontakte, <strong>aber</strong> manche moechten mit ihren Brieffreunden lieber per Post kommunizieren.</span>
        <span class="zh">笔友关系虽然几乎都是邮件联系，但有些人更喜欢通过信件交流。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Zwar</strong> liegt BWL bei den Studienanfaengern beider Geschlechter auf Platz eins, <strong>aber</strong> danach zeigen sich deutliche Unterschiede.</span>
        <span class="zh">虽然BWL在男女新生中都排第一，但此后显示出明显差异。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Zwar</strong> gehen heute mehr Frauen einem Beruf nach, <strong>aber</strong> in manchen Branchen sind sie kaum vertreten.</span>
        <span class="zh">虽然今天更多女性从事职业，但在某些行业她们几乎不被代表。</span>
      </div>
    </div>

    <div class="grammar-block">
      <h3>2. nicht nur … sondern auch (不仅…而且)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>强调两个并列信息都成立。<br>
        <code><strong>nicht nur</strong> + A, <strong>sondern auch</strong> + B</code>
      </div>
      <div class="grammar-example">
        <span class="de">Zu viel Fernsehen schadet <strong>nicht nur</strong> der Gesundheit, <strong>sondern</strong> macht <strong>auch</strong> einen dumm.</span>
        <span class="zh">看电视太多不仅损害健康，还会让人变笨。</span>
      </div>
      <div class="grammar-example">
        <span class="de">Durchs Praktikum gewinnt man <strong>nicht nur</strong> Arbeitserfahrungen, <strong>sondern</strong> lernt <strong>auch</strong> neue Freunde kennen.</span>
        <span class="zh">通过实习不仅获得工作经验，还能结识新朋友。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Nicht nur</strong> in China, <strong>sondern auch</strong> in Europa ist es unhoeflich, unpuenktlich zu sein.</span>
        <span class="zh">不仅在中国，在欧洲不守时也是不礼貌的。</span>
      </div>
    </div>

    <div class="grammar-block">
      <h3>3. sowohl … als auch (既…又)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>表示两者都成立，相当于"und".<br>
        <code><strong>sowohl</strong> + A <strong>als auch</strong> + B</code>
      </div>
      <div class="grammar-example">
        <span class="de">Xu Meng stoert <strong>sowohl</strong> die Unpuenktlichkeit <strong>als auch</strong> die Unzuverlaessigkeit von Lukas.</span>
        <span class="zh">Xu Meng对Lukas的不守时和不靠谱都感到困扰。</span>
      </div>
      <div class="grammar-example">
        <span class="de">Unter den Top-5-Ausbildungsberufen waren <strong>sowohl</strong> die Kauffrau / der Kaufmann <strong>als auch</strong> der Verkaeufer im Einzelhandel beliebt.</span>
        <span class="zh">前五名职业培训中，女/男商人和零售员都受欢迎。</span>
      </div>
    </div>

    <h3 style="margin-top:32px;color:var(--primary);">三组连词对比</h3>
    <table class="comp-table" style="margin-top:12px;">
      <thead><tr><th>连词</th><th>含义</th><th>语序</th><th>例句</th></tr></thead>
      <tbody>
        <tr><td><strong>zwar … aber</strong></td><td>虽然…但是</td><td>zwar 不占位, aber 占位</td><td class="de">Er ist zwar muede, aber er arbeitet weiter.</td></tr>
        <tr><td><strong>nicht nur … sondern auch</strong></td><td>不仅…而且</td><td>nicht nur 不占位, sondern 占位</td><td class="de">Sie kann nicht nur Deutsch, sondern auch Chinesisch.</td></tr>
        <tr><td><strong>sowohl … als auch</strong></td><td>既…又</td><td>不占位</td><td class="de">Er spricht sowohl Deutsch als auch Englisch.</td></tr>
      </tbody>
    </table>

  </section>''')

# ============================================================
# 5. EXERCISE section
# ============================================================
es = h.find('<section id="exercise"')
ee = h.find('</section>', es) + len('</section>')
h = h.replace(h[es:ee], '''  <section id="exercise">
    <h2 class="section-title"><span class="num">1</span> 练习 · Uebungen</h2>

    <div class="quiz-card"><div class="q-text">1. Welche Berufe sind bei Frauen am beliebtesten?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,1,0)">A. Kfz-Mechatroniker, Fachinformatiker</div>
        <div class="opt" onclick="checkQuiz(this,1,1)">B. Kauffrau fuer Bueromanagement, med. Fachangestellte</div>
        <div class="opt" onclick="checkQuiz(this,1,2)">C. Elektroniker, Metalltechniker</div>
        <div class="opt" onclick="checkQuiz(this,1,3)">D. Bauer, Gaertner</div>
      </div>
      <div class="q-answer">答案：B</div>
    </div>

    <div class="quiz-card"><div class="q-text">2. Welches Fach liegt bei Studienanfaengern beider Geschlechter auf Platz eins?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,2,0)">A. Informatik</div>
        <div class="opt" onclick="checkQuiz(this,2,1)">B. Betriebswirtschaftslehre (BWL)</div>
        <div class="opt" onclick="checkQuiz(this,2,2)">C. Maschinenbau</div>
        <div class="opt" onclick="checkQuiz(this,2,3)">D. Psychologie</div>
      </div>
      <div class="q-answer">答案：B</div>
    </div>

    <div class="quiz-card"><div class="q-text">3. Was hat Erika nach dem Gymnasium gemacht?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,3,0)">A. Sie hat studiert.</div>
        <div class="opt" onclick="checkQuiz(this,3,1)">B. Sie hat eine Ausbildung zur Elektronikerin gemacht.</div>
        <div class="opt" onclick="checkQuiz(this,3,2)">C. Sie hat im Buero gearbeitet.</div>
        <div class="opt" onclick="checkQuiz(this,3,3)">D. Sie ist ins Ausland gegangen.</div>
      </div>
      <div class="q-answer">答案：B</div>
    </div>

    <div class="quiz-card"><div class="q-text">4. Erika ist durchsetzungsfaehiger geworden, ______________.</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,4,0)">A. weil sie viel gelernt hat</div>
        <div class="opt" onclick="checkQuiz(this,4,1)">B. weil sie meistens als einzige Frau mit Maennern zusammenarbeitet</div>
        <div class="opt" onclick="checkQuiz(this,4,2)">C. weil sie eine neue Stelle bekommen hat</div>
        <div class="opt" onclick="checkQuiz(this,4,3)">D. weil sie eine Pruefung bestanden hat</div>
      </div>
      <div class="q-answer">答案：B</div>
    </div>

    <div class="quiz-card"><div class="q-text">5. Welche Konjunktion verbindet zwei gegensaetzliche Informationen?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,5,0)">A. nicht nur … sondern auch</div>
        <div class="opt" onclick="checkQuiz(this,5,1)">B. zwar … aber</div>
        <div class="opt" onclick="checkQuiz(this,5,2)">C. sowohl … als auch</div>
        <div class="opt" onclick="checkQuiz(this,5,3)">D. und</div>
      </div>
      <div class="q-answer">答案：B</div>
    </div>

    <div class="quiz-card"><div class="q-text">6. "________ in China ________ in Europa ist es unhoeflich, unpuenktlich zu sein."</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,6,0)">A. Zwar … aber</div>
        <div class="opt" onclick="checkQuiz(this,6,1)">B. Nicht nur … sondern auch</div>
        <div class="opt" onclick="checkQuiz(this,6,2)">C. Sowohl … als auch</div>
        <div class="opt" onclick="checkQuiz(this,6,3)">D. Weder … noch</div>
      </div>
      <div class="q-answer">答案：C</div>
    </div>

  </section>''')

# ============================================================
# 6. Labels and person tabs
# ============================================================
for old, new in [
    ('重点词汇 · Wortschatz', '重点词汇 · Beruf & Studium'),
    ('T1 词汇 · 课文一', 'T1 词汇 · Berufswahl'),
    ('T2 词汇 · 课文二', 'T2 词汇 · Erika'),
    ('学校类型词汇', 'Berufs-Tabellen'),
    ('学校类型', 'Berufsfelder'),
    ("switchPerson('tobias')", "switchPerson('berufswahl')"),
    ("switchPerson('melisa')", "switchPerson('erika')"),
    ("switchPerson('ingrid')", "switchPerson('zusatz')"),
    ("switchPerson('schule')", "switchPerson('tabellen')"),
    ('id="p-tobias"', 'id="p-berufswahl"'),
    ('id="p-melisa"', 'id="p-erika"'),
    ('id="p-ingrid"', 'id="p-zusatz"'),
    ('id="p-schule"', 'id="p-tabellen"'),
    ('Tobias · 综合中学', 'T1 · Berufswahlverhalten'),
    ('Melisa · 实科中学', 'T2 · Werkstatt statt Schreibtisch'),
    ('Ingrid · 文理中学', 'Simon (Zusatztext)'),
    ("id === 'tobias' ? 'Tobias' :", "id === 'berufswahl' ? 'Berufswahl' :"),
    ("id === 'melisa' ? 'Melisa' : id === 'ingrid' ? 'Ingrid' : '学校'", "id === 'erika' ? 'Erika' : id === 'zusatz' ? 'Zusatz' : 'Tabellen'"),
    ('onclick="switchPerson(\'tobias\')"', 'onclick="switchPerson(\'berufswahl\')"'),
    ('onclick="switchPerson(\'melisa\')"', 'onclick="switchPerson(\'erika\')"'),
    ('onclick="switchPerson(\'ingrid\')"', 'onclick="switchPerson(\'zusatz\')"'),
    ('onclick="switchPerson(\'schule\')"', 'onclick="switchPerson(\'tabellen\')"'),
]:
    if old in h: h = h.replace(old, new)

# ============================================================
# 7. VocabData - complete word list
# ============================================================
vd = h.find('const vocabData')
vd_end = h.find('};', vd) + 2
h = h.replace(h[vd:vd_end], '''const vocabData = {
  'T1': [
    { word: 'das Berufswahlverhalten', zh: '职业选择行为', pos: 'n.', example: 'Das Berufswahlverhalten von Frauen und Maennern hat sich wenig veraendert.', exampleZh: '男女的职业选择行为几乎没变。' },
    { word: 'die Ausbildungsstelle', zh: '培训岗位', pos: 'f.', example: 'Das zeigt der Blick auf die Ausbildungsstellen.', exampleZh: '看培训岗位数据就能看出来。' },
    { word: 'sich entscheiden', zh: '决定', pos: 'v.', example: 'Sie entscheiden sich fuer bestimmte Berufe.', exampleZh: '她们选择特定的职业。' },
    { word: 'einem Beruf nachgehen', zh: '从事职业', pos: 'phrase', example: 'Heute gehen mehr Frauen einem Beruf nach.', exampleZh: '今天更多女性从事职业。' },
    { word: 'die Branche', zh: '行业', pos: 'f.', example: 'In manchen Branchen sind Frauen kaum vertreten.', exampleZh: '在某些行业女性几乎不参与。' },
    { word: 'gehoeren zu', zh: '属于', pos: 'v.', example: 'Diese Berufe gehoerten zu den beliebtesten.', exampleZh: '这些职业属于最受欢迎的。' },
    { word: 'der/die Fachangestellte', zh: '专业人员(职员)', pos: 'n.', example: 'Die medizinische Fachangestellte hilft beim Arzt.', exampleZh: '医疗助理在诊所帮助医生。' },
    { word: 'der Ausbildungsberuf', zh: '培训职业', pos: 'm.', example: 'Der Kfz-Mechatroniker ist ein beliebter Ausbildungsberuf.', exampleZh: '汽车机电技工是受欢迎的培训职业。' },
    { word: 'der Vergleich', zh: '比较', pos: 'm.', example: 'Im Vergleich zu den Vorjahren ist das unveraendert.', exampleZh: '与前几年相比，这没有变化。' },
    { word: 'dagegen', zh: '相反', pos: 'adv.', example: 'Maenner waehlen dagegen technische Berufe.', exampleZh: '男性则相反，选择技术职业。' },
    { word: 'der Fachinformatiker', zh: 'IT专家', pos: 'm.', example: 'Viele Maenner werden Fachinformatiker.', exampleZh: '很多男性成为IT专家。' },
    { word: 'der Einzelhandel', zh: '零售业', pos: 'm.', example: 'Der Verkaeufer im Einzelhandel ist ein beliebter Beruf.', exampleZh: '零售业售货员是受欢迎的职业。' },
    { word: 'das Geschlecht', zh: '性别', pos: 'n.', example: 'Bei beiden Geschlechtern ist der Beruf beliebt.', exampleZh: '这个职业在两性中都受欢迎。' },
    { word: 'waehrend', zh: '而、在…期间', pos: 'konj.', example: 'Waehrend Frauen im Gesundheitswesen stark sind, sind sie in Bauberufen selten.', exampleZh: '女性在医疗行业占比高，而在建筑行业占比低。' },
    { word: 'der/die Beschaeftigte', zh: '雇员', pos: 'n.', example: 'Weniger als 10% der Beschaeftigten waren Frauen.', exampleZh: '不到10%的雇员是女性。' },
    { word: 'betragen', zh: '总计为', pos: 'v.', example: 'Ihr Anteil betrug mehr als 80 Prozent.', exampleZh: '她们的比例超过80%。' },
    { word: 'der Anteil', zh: '比例', pos: 'm.', example: 'Ihr Anteil in technischen Berufen ist niedrig.', exampleZh: '她们在技术职业中的比例很低。' },
    { word: 'die Laufbahn', zh: '职业生涯', pos: 'f.', example: 'Sie entscheidet sich fuer eine akademische Laufbahn.', exampleZh: '她选择了学术生涯。' },
    { word: 'die Studienwahl', zh: '大学专业选择', pos: 'f.', example: 'Bei der Studienwahl zeigen sich deutliche Unterschiede.', exampleZh: '在专业选择上显示出明显差异。' },
    { word: 'die Betriebswirtschaftslehre', zh: '企业经济学', pos: 'f.', example: 'BWL liegt bei den Studienanfaengern auf Platz eins.', exampleZh: '企业经济学在新生中最受欢迎。' },
    { word: 'der/die Studienanfaenger/in', zh: '大学新生', pos: 'n.', example: 'Bei den Studienanfaengern beider Geschlechter ist BWL beliebt.', exampleZh: '在男女新生中BWL都受欢迎。' },
    { word: 'dominieren', zh: '占主导', pos: 'v.', example: 'Bei Maennern dominieren technische Faecher.', exampleZh: '男性以技术专业为主导。' },
    { word: 'die Informatik', zh: '计算机科学', pos: 'f.', example: 'Informatik ist bei Maennern sehr beliebt.', exampleZh: '计算机科学在男性中很受欢迎。' },
    { word: 'der Maschinenbau', zh: '机械工程', pos: 'm.', example: 'Maschinenbau ist ein klassisches Mannerfach.', exampleZh: '机械工程是典型的男性专业。' },
    { word: 'die Rechtswissenschaft', zh: '法学', pos: 'f.', example: 'Rechtswissenschaften sind bei Frauen beliebt.', exampleZh: '法学在女性中受欢迎。' },
    { word: 'die Psychologie', zh: '心理学', pos: 'f.', example: 'Psychologie studieren viele Frauen.', exampleZh: '很多女性学习心理学。' },
    { word: 'die Erziehungswissenschaft', zh: '教育科学', pos: 'f.', example: 'Erziehungswissenschaften sind ein beliebtes Studienfach.', exampleZh: '教育科学是受欢迎的专业。' },
    { word: 'sich unterscheiden', zh: '区别于', pos: 'v.', example: 'Frauen und Maenner unterscheiden sich in der Berufswahl.', exampleZh: '男女在职业选择上有区别。' },
    { word: 'die Vorliebe', zh: '偏好', pos: 'f.', example: 'Die Wahl entspricht den persoenlichen Vorlieben.', exampleZh: '选择符合个人偏好。' },
    { word: 'ermoetigen', zh: '鼓励', pos: 'v.', example: 'Junge Menschen sollten ermoetigt werden.', exampleZh: '年轻人应该被鼓励。' },
    { word: 'das Rollenmuster', zh: '角色模式', pos: 'n.', example: 'Traditionelle Rollenmuster sollten aufgebrochen werden.', exampleZh: '传统的角色模式应该被打破。' },
  ],
  'T2': [
    { word: 'zunaechst', zh: '起初', pos: 'adv.', example: 'Zunaechst besuchte Erika ein Gymnasium.', exampleZh: '起初Erika上文理中学。' },
    { word: 'das Gymnasium', zh: '文理中学', pos: 'n.', example: 'Auf dem Gymnasium macht man das Abitur.', exampleZh: '在文理中学参加高考。' },
    { word: 'jedoch', zh: '然而', pos: 'konj.', example: 'Jedoch stellte sie fest, dass ihr die Werkstatt besser gefaellt.', exampleZh: '然而她发现她更喜欢车间。' },
    { word: 'feststellen', zh: '发现、确认', pos: 'v.', example: 'Sie stellte fest, dass sie nicht studieren musste.', exampleZh: '她发现自己不必上大学。' },
    { word: 'die Werkstatt', zh: '车间', pos: 'f.', example: 'Sie half in der Elektro-Werkstatt ihres Vaters.', exampleZh: '她在父亲的电气车间帮忙。' },
    { word: 'der Schreibtisch', zh: '办公桌', pos: 'm.', example: 'Sie sass lieber in der Werkstatt als am Schreibtisch.', exampleZh: '她喜欢在车间胜过在办公桌前。' },
    { word: 'die Ausbildung', zh: '职业培训', pos: 'f.', example: 'Sie macht eine Ausbildung zur Elektronikerin.', exampleZh: '她接受电子技术员培训。' },
    { word: 'die Elektronikerin', zh: '电子技术员(女)', pos: 'f.', example: 'Die Ausbildung zur Elektronikerin war ihr Traum.', exampleZh: '成为电子技术员是她的梦想。' },
    { word: 'betreuen', zh: '照顾、服务', pos: 'v.', example: 'Sie betreut Kundinnen und Kunden.', exampleZh: '她照顾客户。' },
    { word: 'der Kunde / die Kundin', zh: '客户', pos: 'm./f.', example: 'Die Kunden sind mit ihrer Arbeit zufrieden.', exampleZh: '客户对她的工作满意。' },
    { word: 'die Beleuchtung', zh: '照明', pos: 'f.', example: 'Sie plant die Beleuchtung in Gebaeuden.', exampleZh: '她规划建筑物的照明。' },
    { word: 'darauf ankommen', zh: '关键在于', pos: 'phrase', example: 'Es kommt darauf an, die Systeme richtig zu gestalten.', exampleZh: '关键在于正确设计系统。' },
    { word: 'sogenannt', zh: '所谓的', pos: 'adj.', example: 'Sie baut sogenannte Smart-Home-Systeme.', exampleZh: '她构建所谓的智能家居系统。' },
    { word: 'die Energieversorgung', zh: '能源供应', pos: 'f.', example: 'Nachhaltige Energieversorgung ist wichtig.', exampleZh: '可持续能源供应很重要。' },
    { word: 'der Klimaschutz', zh: '气候保护', pos: 'm.', example: 'Smart-Home-Systeme helfen beim Klimaschutz.', exampleZh: '智能家居系统有助于气候保护。' },
    { word: 'mitgestalten', zh: '共同设计', pos: 'v.', example: 'Sie gestaltet die Systeme mit.', exampleZh: '她参与设计这些系统。' },
    { word: 'die Staerke', zh: '优势、长处', pos: 'f.', example: 'Sie hat ihre persoenlichen Staerken weiterentwickelt.', exampleZh: '她进一步发展了个人优势。' },
    { word: 'durchsetzungsfaehig', zh: '有决断力的', pos: 'adj.', example: 'Sie ist durchsetzungsfaehiger geworden.', exampleZh: '她变得更有决断力了。' },
    { word: 'zusammenarbeiten', zh: '合作', pos: 'v.', example: 'Sie arbeitet mit Maennern zusammen.', exampleZh: '她和男性一起工作。' },
    { word: 'der Mut', zh: '勇气', pos: 'm.', example: 'Sie hat den Mut, ihren eigenen Weg zu gehen.', exampleZh: '她有勇气走自己的路。' },
    { word: 'der Berufswunsch', zh: '职业愿望', pos: 'm.', example: 'Sie folgte ihrem Berufswunsch.', exampleZh: '她追随了自己的职业愿望。' },
  ]
};''')

# ============================================================
# 8. Verify and write
# ============================================================
print('=== VERIFICATION ===')
for w in ['Berufswahlverhalten','Studienwahl','Werkstatt','Erika','Elektronikerin','Energieversorgung','Klimaschutz','durchsetzungsfaehiger','Rollenmuster','stereotype']:
    print('  {}: {}'.format(w, w in h))
for w in ['Tobias','Melisa','Niklas','Ingrid']:
    if w in h: print('  L7 REMAINING: {}'.format(w))
print('  Sections: {} opens, {} closes'.format(h.count('<section id='), h.count('</section>')))
print('  Vocab-words: {}'.format(h.count('vocab-word')))
print('  Size: {:.0f} KB'.format(len(h)/1024))

with open(OUT, 'w') as f:
    f.write(h)
print('Written!')
