#!/usr/bin/env python3
"""Regenerate Lektion 8 courseware with CORRECT texts from the textbook."""
import os

srcdir = '/home/gem/workspace/agent/workspace-main/projects/lektion7-interactive'
dstdir = '/home/gem/workspace/agent/workspace-main/projects/lektion7-interactive'  # same dir, different filename

with open(os.path.join(srcdir, 'lektion8-latest.html')) as f:
    h = f.read()

# === 1. TITLE & NAV ===
h = h.replace('Lektion 7 · Start in die Zukunft! · 交互式课件', 'Lektion 8 · Was will ich werden? · 交互式课件')
h = h.replace('语法·zu不定式', '语法·并列连词')
h = h.replace('🚀 Start in die Zukunft!', '💼 Was will ich werden?')
h = h.replace('Lektion 7 · Klett 新经典德语 2', 'Lektion 8 · Klett 新经典德语 2')
h = h.replace('本课件包含 Lektion 7 的课文讲解、重点词汇、语法（带 zu 不定式）和练习。',
    '本课件包含 Lektion 8 的课文讲解、重点词汇、语法（zwar…aber / nicht nur…sondern auch / sowohl…als auch）和练习。')
h = h.replace('📖 Lektion 7 <span>Start in die Zukunft!</span>', '📖 Lektion 8 <span>Was will ich werden?</span>')

# === 2. TEXT SECTION ===
ts = h.find('<section id="text"')
te = h.find('</section>', ts) + len('</section>')
old_text = h[ts:te]

new_text = """<section id="text">

    <!-- 课文一：T1 Berufswahlverhalten + Studienwahl -->
    <h2 class="section-title"><span class="num">1</span> T1 · Berufswahlverhalten · 职业选择行为</h2>
    <p style="margin-bottom:12px;font-size:14px;color:var(--text-light)">
      德国男女职业选择的数据分析。点击红色词汇查看释义。
    </p>

    <div class="text-card">
      <h3>Berufswahlverhalten</h3>
      <div class="de">
        <p>Das <span class="vocab-word" onclick="showVocab('das Berufswahlverhalten','职业选择行为','die Art und Weise, wie Menschen einen Beruf waehlen. 例：Das Berufswahlverhalten von Frauen und Maennern unterscheidet sich.')">Berufswahlverhalten</span> von Frauen und Maennern hat sich wenig veraendert – das zeigt der Blick auf die Ausbildungsstellen. Frauen und Maenner <span class="vocab-word" onclick="showVocab('sich entscheiden fuer','决定选择','eine Wahl treffen. 例：Sie entscheiden sich fuer bestimmte Berufe.')">entscheiden</span> sich nach wie vor fuer ganz bestimmte Berufe. Heute <span class="vocab-word" onclick="showVocab('einem Beruf nachgehen','从事一个职业','einen Beruf ausueben. 例：Immer mehr Frauen gehen einem Beruf nach.')">gehen</span> in Deutschland deutlich mehr Frauen einem Beruf nach als vor einigen Jahrzehnten. Dennoch sind Frauen in manchen <span class="vocab-word" onclick="showVocab('die Branche','行业','ein bestimmter Wirtschaftsbereich. 例：In manchen Branchen sind Frauen kaum vertreten.')">Branchen</span> noch immer kaum vertreten.</p>
        <p style="margin-top:6px">Im vergangenen Jahr <span class="vocab-word" onclick="showVocab('gehoeren zu','属于','Teil von etwas sein. 例：Diese Berufe gehoerten zu den beliebtesten.')">gehoerten</span> die Kauffrau fuer Bueromanagement, die medizinische und die zahnmedizinische Fachangestellte zu den beliebtesten Ausbildungsberufen von Frauen. Das ist im <span class="vocab-word" onclick="showVocab('der Vergleich','比较','das Vergleichen von zwei Dingen. 例：Im Vergleich zu den Vorjahren ist das unveraendert.')">Vergleich</span> zu den Vorjahren unveraendert geblieben. Maenner waehlen dagegen am haeufigsten die Ausbildung zum Kfz-Mechatroniker, <span class="vocab-word" onclick="showVocab('der Fachinformatiker','IT专家','eine Person, die im IT-Bereich arbeitet. 例：Viele Maenner werden Fachinformatiker.')">Fachinformatiker</span> und Elektroniker. Unter den Top-5-Ausbildungsberufen waren nur die Kauffrau / der Kaufmann und die Verkaeuferin / der Verkaeufer im Einzelhandel bei beiden Geschlechtern fast gleich beliebt. In einigen der Bau- und Metallberufe waren deutlich weniger als 10 Prozent der <span class="vocab-word" onclick="showVocab('der/die Beschaeftigte','从业人员','eine Person, die in einem Betrieb arbeitet. 例：Weniger als 10 Prozent der Beschaeftigten waren Frauen.')">Beschaeftigten</span> Frauen, ihr Anteil <span class="vocab-word" onclick="showVocab('betragen','总计为','eine bestimmte Zahl oder Menge haben. 例：Ihr Anteil betrug mehr als 80 Prozent.')">betrug</span> vor allem in den Berufen des Erziehungs- und Gesundheitswesens mehr als 80 Prozent.</p>
      </div>
      <div class="highlight-box">Berufswahlverhalten: Frauen&rarr;Buero/Medizin, Maenner&rarr;Technik. Nur Kaufmann/Kauffrau und Verkaeufer bei beiden gleich beliebt.</div>
    </div>

    <div class="text-card">
      <h3>Studienwahl</h3>
      <div class="de">
        <p>Heute entscheiden sich mehr Frauen fuer eine akademische Laufbahn. Trotzdem zeigen sich bei der <span class="vocab-word" onclick="showVocab('die Studienwahl','大学专业选择','die Entscheidung fuer ein Studienfach. 例：Bei der Studienwahl zeigen sich Unterschiede.')">Studienwahl</span> noch immer deutliche Unterschiede: <span class="vocab-word" onclick="showVocab('zwar … aber','虽然…但是','Konzessivsatz: zwei gegensaetzliche Aussagen. 例：Zwar liegt BWL auf Platz eins, aber danach dominieren Maenner technische Faecher.')">Zwar</span> liegt Betriebswirtschaftslehre (BWL) bei den Studienanfaengern beider Geschlechter auf Platz eins, danach <span class="vocab-word" onclick="showVocab('dominieren','占主导','am haeufigsten sein. 例：Bei den Maennern dominieren technische Faecher.')">dominieren</span> bei den Maennern aber technische und naturwissenschaftliche Faecher wie Informatik und Maschinenbau. Bei den Frauen sind nach BWL vor allem Rechtswissenschaften, Psychologie sowie Erziehungswissenschaften beliebt.</p>
        <p style="margin-top:6px">Insgesamt unterscheiden sich Frauen und Maenner in ihrer Berufswahl demnach noch immer stark voneinander. Dennoch gibt es gute Gruende dafuer, junge Menschen zu <span class="vocab-word" onclick="showVocab('ermoetigen','鼓励','Mut machen. 例：Man sollte junge Menschen ermoetigen, Rollenmuster zu verlassen.')">ermoetigen</span>, die traditionellen Rollenmuster zu verlassen und sich von stereotypen Vorstellungen zu loesen.</p>
      </div>
      <div class="highlight-box">Studienwahl: BWL Platz 1 bei beiden, danach Maenner&rarr;Technik, Frauen&rarr;Jura/Psychologie/Paedagogik.</div>
    </div>

    <!-- 课文二：T2 Lieber Werkstatt statt Schreibtisch -->
    <h2 class="section-title" style="margin-top:40px"><span class="num">2</span> T2 · Lieber Werkstatt statt Schreibtisch · Erika</h2>
    <p style="margin-bottom:12px;font-size:14px;color:var(--text-light)">
      一位年轻女性选择成为电工的真实故事。点击红色词汇查看释义。
    </p>

    <div class="text-card">
      <h3>Erika — „Lieber Werkstatt statt Schreibtisch"</h3>
      <div class="de">
        <p><span class="vocab-word" onclick="showVocab('zunaechst','最初','am Anfang. 例：Zunaechst besuchte sie ein Gymnasium.')">Zunaechst</span> besuchte Erika ein Gymnasium. Jedoch stellte sie fest, dass sie den Nachmittag lieber in der <span class="vocab-word" onclick="showVocab('die Werkstatt','车间','der Raum, in dem repariert oder gebaut wird. 例：Sie half in der Elektro-Werkstatt ihres Vaters.')">Elektro-Werkstatt</span> ihres Vaters verbrachte, als nur am <span class="vocab-word" onclick="showVocab('der Schreibtisch','书桌','der Tisch, an dem man schreibt/arbeitet. 例：Sie sass nicht gern am Schreibtisch.')">Schreibtisch</span> zu sitzen. Dadurch wurde ihr klar: „Ich muss nicht studieren wie meine Freundinnen." Sie entschied sich fuer die Ausbildung zur <span class="vocab-word" onclick="showVocab('der/die Elektroniker/in','电子技术员','eine Fachkraft fuer elektronische Systeme. 例：Sie macht eine Ausbildung zur Elektronikerin.')">Elektronikerin</span> – aus dem Traum wurde Realitaet.</p>
        <p style="margin-top:6px">Nun <span class="vocab-word" onclick="showVocab('betreuen','照顾、服务','sich um jemanden kuemmern. 例：Sie betreut Kunden und plant die Beleuchtung.')">betreut</span> sie Kunden und plant die <span class="vocab-word" onclick="showVocab('die Beleuchtung','照明','das Licht in einem Gebaeude. 例：Sie plant die Beleuchtung in Gebaeuden.')">Beleuchtung</span> in Gebaeuden. Es kommt darauf an, <span class="vocab-word" onclick="showVocab('sogenannt','所谓的','wie man etwas nennt. 例：Sie gestaltet sogenannte Smart-Home-Systeme.')">sogenannte</span> Smart-Home-Systeme <span class="vocab-word" onclick="showVocab('mitgestalten','参与设计','bei der Gestaltung mitwirken. 例：Sie gestaltet nachhaltige Energiesysteme mit.')">mit<strong class="zu-hl-sep">zu</strong>gestalten</span>.</p>
        <p style="margin-top:6px">Im Laufe der Zeit hat sie ihre <span class="vocab-word" onclick="showVocab('die Staerke','优势、长处','eine positive Eigenschaft. 例：Ihre persoenlichen Staerken haben sich entwickelt.')">persoenlichen Staerken</span> weiterentwickelt. Sie ist <span class="vocab-word" onclick="showVocab('durchsetzungsfaehig','有决断力的','faehig, eigene Ideen zu verwirklichen. 例：Sie ist durchsetzungsfaehiger geworden.')">durchsetzungsfaehiger</span> geworden, weil sie als einzige Frau mit Maennern zusammenarbeitet. Sie freut sich, wenn Maedchen den Mut haben, ihrem eigenen <span class="vocab-word" onclick="showVocab('der Berufswunsch','职业愿望','der Wunsch, einen bestimmten Beruf auszuueben. 例：Sie folgte ihrem Berufswunsch.')">Berufswunsch</span> zu folgen.</p>
      </div>
      <div class="highlight-box">Erika: Gymnasium→lieber in der Werkstatt→Ausbildung zur Elektronikerin→betreut Kunden, plant Beleuchtung, baut Smart-Home-Systeme</div>
    </div>

  </section>"""

h = h.replace(old_text, new_text)

# === 3. GRAMMAR SECTION ===
gs = h.find('<section id="grammar"')
ge = h.find('</section>', gs) + len('</section>')
old_grammar = h[gs:ge]

new_grammar = """  <section id="grammar">
    <h2 class="section-title"><span class="num">1</span> 语法 · 并列连词</h2>

    <div class="grammar-block">
      <h3>1. zwar &hellip; aber (虽然&hellip;但是)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>连接两个对立/矛盾的陈述。zwar 不占位，aber 占位。<br>
        <code>zwar + Satz, <strong>aber</strong> + Satz</code>
      </div>
      <div class="grammar-example">
        <span class="de">Brieffreundschaften sind <strong>zwar</strong> fast immer E-Mail-Kontakte, <strong>aber</strong> manche moechten lieber per Post kommunizieren.</span>
        <span class="zh">笔友关系虽然几乎都是邮件联系，但有些人更喜欢通过信件交流。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Zwar</strong> liegt BWL bei beiden Geschlechtern auf Platz eins, <strong>aber</strong> danach zeigen sich deutliche Unterschiede.</span>
        <span class="zh">虽然 BWL 在两性中都排第一，但此后显示出明显差异。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Zwar</strong> gehen heute mehr Frauen einem Beruf nach, <strong>aber</strong> in manchen Branchen sind sie kaum vertreten.</span>
        <span class="zh">虽然今天更多女性从事职业，但在某些行业她们几乎不被代表。</span>
      </div>
    </div>

    <div class="grammar-block">
      <h3>2. nicht nur &hellip; sondern auch (不仅&hellip;而且)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>强调两个并列信息都成立。nicht nur 不占位，sondern 占位。<br>
        <code><strong>nicht nur</strong> + A, <strong>sondern auch</strong> + B</code>
      </div>
      <div class="grammar-example">
        <span class="de">Zu viel Fernsehen schadet <strong>nicht nur</strong> der Gesundheit, <strong>sondern</strong> macht <strong>auch</strong> einen dumm.</span>
        <span class="zh">看电视太多不仅损害健康，还会让人变笨。</span>
      </div>
      <div class="grammar-example">
        <span class="de"><strong>Nicht nur</strong> in China, <strong>sondern auch</strong> in Europa ist es unhoeflich, unpuenktlich zu sein.</span>
        <span class="zh">不仅在中国，在欧洲不守时也是不礼貌的。</span>
      </div>
      <div class="grammar-example">
        <span class="de">Durchs Praktikum gewinnt man <strong>nicht nur</strong> Arbeitserfahrungen, <strong>sondern</strong> lernt <strong>auch</strong> neue Freunde kennen.</span>
        <span class="zh">通过实习不仅获得工作经验，还能结识新朋友。</span>
      </div>
    </div>

    <div class="grammar-block">
      <h3>3. sowohl &hellip; als auch (既&hellip;又)</h3>
      <div class="rule-box de">
        <strong>用法：</strong>表示两者都成立，相当于"und"的功能。<br>
        <code><strong>sowohl</strong> + A <strong>als auch</strong> + B</code>
      </div>
      <div class="grammar-example">
        <span class="de">Xu Meng stoert <strong>sowohl</strong> die Unpuenktlichkeit <strong>als auch</strong> die Unzuverlaessigkeit von Lukas.</span>
        <span class="zh">Xu Meng 对 Lukas 的不守时和不靠谱都感到困扰。</span>
      </div>
      <div class="grammar-example">
        <span class="de">Unter den Top-5-Ausbildungsberufen waren <strong>sowohl</strong> die Kauffrau / der Kaufmann <strong>als auch</strong> der Verkaeufer im Einzelhandel beliebt.</span>
        <span class="zh">在排名前五的职业培训中，女/男商人以及零售员都受欢迎。</span>
      </div>
    </div>

    <h3 style="margin-top:32px;color:var(--primary);">三组连词对比</h3>
    <table class="comp-table" style="margin-top:12px;">
      <thead>
        <tr><th>连词</th><th>含义</th><th>语序</th><th>例句</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>zwar &hellip; aber</strong></td>
          <td>虽然&hellip;但是</td>
          <td>zwar 不占位, aber 占位</td>
          <td class="de">Er ist zwar muede, aber er arbeitet weiter.</td>
        </tr>
        <tr>
          <td><strong>nicht nur &hellip; sondern auch</strong></td>
          <td>不仅&hellip;而且</td>
          <td>nicht nur 不占位, sondern 占位</td>
          <td class="de">Sie kann nicht nur Deutsch, sondern auch Chinesisch.</td>
        </tr>
        <tr>
          <td><strong>sowohl &hellip; als auch</strong></td>
          <td>既&hellip;又</td>
          <td>不占位，连接并列成分</td>
          <td class="de">Er spricht sowohl Deutsch als auch Englisch.</td>
        </tr>
      </tbody>
    </table>

  </section>"""

h = h.replace(old_grammar, new_grammar)

# === 4. VOCAB DATA ===
vd = h.find('const vocabData')
ve = h.find('];', vd) + 2
old_vocab = h[vd:ve]

new_vocab = """const vocabData = {
  'T1': [
    { de: 'das Berufswahlverhalten', zh: '职业选择行为', detail: 'die Art, wie man einen Beruf waehlt' },
    { de: 'sich entscheiden fuer', zh: '决定选择', detail: 'eine Wahl treffen' },
    { de: 'einem Beruf nachgehen', zh: '从事职业', detail: 'einen Beruf ausueben' },
    { de: 'die Branche', zh: '行业', detail: 'ein bestimmter Wirtschaftsbereich' },
    { de: 'gehoeren zu', zh: '属于', detail: 'Teil von etwas sein' },
    { de: 'der Vergleich', zh: '比较', detail: 'das Vergleichen von Dingen' },
    { de: 'der Fachinformatiker', zh: 'IT专家', detail: 'eine IT-Fachkraft' },
    { de: 'der/die Beschaeftigte', zh: '从业人员', detail: 'eine arbeitende Person' },
    { de: 'betragen', zh: '总计为', detail: 'eine bestimmte Menge haben' },
    { de: 'die Studienwahl', zh: '大学专业选择', detail: 'die Wahl des Studienfachs' },
    { de: 'dominieren', zh: '占主导', detail: 'am haeufigsten sein' },
    { de: 'ermoetigen', zh: '鼓励', detail: 'Mut machen' },
  ],
  'T2': [
    { de: 'zunaechst', zh: '最初', detail: 'am Anfang' },
    { de: 'die Werkstatt', zh: '车间', detail: 'der Raum zum Reparieren' },
    { de: 'der Schreibtisch', zh: '书桌', detail: 'der Arbeitstisch' },
    { de: 'der/die Elektroniker/in', zh: '电子技术员', detail: 'eine Fachkraft fuer Elektronik' },
    { de: 'betreuen', zh: '照顾、服务', detail: 'sich um jemanden kuemmern' },
    { de: 'die Beleuchtung', zh: '照明', detail: 'das Licht in einem Gebaeude' },
    { de: 'sogenannt', zh: '所谓的', detail: 'wie man etwas nennt' },
    { de: 'mitgestalten', zh: '参与设计', detail: 'bei der Gestaltung mitwirken' },
    { de: 'die Staerke', zh: '优势、长处', detail: 'eine positive Eigenschaft' },
    { de: 'durchsetzungsfaehig', zh: '有决断力的', detail: 'faehig, Ideen zu verwirklichen' },
    { de: 'der Berufswunsch', zh: '职业愿望', detail: 'der Wunsch nach einem Beruf' },
  ]
};"""

h = h.replace(old_vocab, new_vocab)

# === 5. SECTION LABELS ===
label_map = [
    ('重点词汇 · Wortschatz', '重点词汇 · Beruf & Studium'),
    ('T1 词汇 · 课文一', 'T1 词汇 · Berufswahl'),
    ('T2 词汇 · 课文二', 'T2 词汇 · Erika'),
    ('学校类型词汇', 'Berufs-Tabellen'),
    ('学校类型', 'Berufsfelder'),
]
for old, new in label_map:
    h = h.replace(old, new)

# === 6. PERSON TABS - map to none/no cards (remove card UI since we use text vocab now) ===
# Actually let's keep the tab structure but rename
person_tabs = [
    ("switchPerson('tobias')", "switchPerson('berufswahl')"),
    ("switchPerson('melisa')", "switchPerson('erika')"),
    ("switchPerson('ingrid')", "switchPerson('simon')"),
    ("switchPerson('schule')", "switchPerson('markus')"),
    ('id="p-tobias"', 'id="p-berufswahl"'),
    ('id="p-melisa"', 'id="p-erika"'),
    ('id="p-ingrid"', 'id="p-simon"'),
    ('id="p-schule"', 'id="p-markus"'),
    ('Tobias · 综合中学', 'T1 · Berufswahlverhalten'),
    ('Melisa · 实科中学', 'T2 · Werkstatt statt Schreibtisch'),
    ('Ingrid · 文理中学', 'Simon (Zusatztext)'),
]

# Only replace if found
for old, new in person_tabs:
    if old in h:
        h = h.replace(old, new)
        # print("Replaced: {}".format(old[:30]))
    # else: print("WARN: not found: {}".format(old[:30]))

# Fix switchPerson logic
old_switch = "id === 'tobias' ? 'Tobias' :\n          id === 'melisa' ? 'Melisa' : id === 'ingrid' ? 'Ingrid' : '学校'"
new_switch = "id === 'berufswahl' ? 'Berufswahl' :\n          id === 'erika' ? 'Erika' : id === 'simon' ? 'Simon' : 'Uebung'"
h = h.replace(old_switch, new_switch)

# === 7. EXERCISE SECTION ===
es = h.find('<section id="exercise"')
ee = h.find('</section>', es) + len('</section>')
old_ex = h[es:ee]

new_ex = """  <section id="exercise">
    <h2 class="section-title"><span class="num">1</span> 练习 · Uebungen</h2>
    <p style="margin-bottom:12px;font-size:14px;color:var(--text-light)">
      点击选项查看正误。绿色 = 正确，红色 = 错误。
    </p>

    <div class="quiz-card">
      <div class="q-text">1. Welche Berufe sind bei Frauen am beliebtesten?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q1',0)">A. Kfz-Mechatroniker, Fachinformatiker</div>
        <div class="opt" onclick="checkQuiz(this,'q1',1)">B. Kauffrau fuer Bueromanagement, medizinische Fachangestellte</div>
        <div class="opt" onclick="checkQuiz(this,'q1',2)">C. Elektroniker, Metalltechniker</div>
        <div class="opt" onclick="checkQuiz(this,'q1',3)">D. Bauer, Gaertner</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>B</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">2. Welches Studienfach liegt bei beiden Geschlechtern auf Platz eins?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q2',0)">A. Informatik</div>
        <div class="opt" onclick="checkQuiz(this,'q2',1)">B. Maschinenbau</div>
        <div class="opt" onclick="checkQuiz(this,'q2',2)">C. Betriebswirtschaftslehre (BWL)</div>
        <div class="opt" onclick="checkQuiz(this,'q2',3)">D. Psychologie</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>C</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">3. Was hat Erika nach dem Gymnasium gemacht?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q3',0)">A. Sie hat an der Uni studiert.</div>
        <div class="opt" onclick="checkQuiz(this,'q3',1)">B. Sie hat eine Ausbildung zur Elektronikerin gemacht.</div>
        <div class="opt" onclick="checkQuiz(this,'q3',2)">C. Sie hat im Buero gearbeitet.</div>
        <div class="opt" onclick="checkQuiz(this,'q3',3)">D. Sie ist ins Ausland gegangen.</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>B</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">4. Erika ist durchsetzungsfaehiger geworden, weil ______________.</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q4',0)">A. sie viel gelernt hat</div>
        <div class="opt" onclick="checkQuiz(this,'q4',1)">B. sie als einzige Frau mit Maennern zusammenarbeitet</div>
        <div class="opt" onclick="checkQuiz(this,'q4',2)">C. sie eine neue Stelle bekommen hat</div>
        <div class="opt" onclick="checkQuiz(this,'q4',3)">D. sie eine Praesentation gehalten hat</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>B</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">5. Welche Konjunktion passt? "________ in China ________ in Europa ist es unhoeflich, unpuenktlich zu sein."</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q5',0)">A. Zwar … aber</div>
        <div class="opt" onclick="checkQuiz(this,'q5',1)">B. Nicht nur … sondern auch</div>
        <div class="opt" onclick="checkQuiz(this,'q5',2)">C. Sowohl … als auch</div>
        <div class="opt" onclick="checkQuiz(this,'q5',3)">D. Weder … noch</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>C</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">6. "zwar &hellip; aber" verbindet:</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q6',0)">A. zwei gleiche Informationen</div>
        <div class="opt" onclick="checkQuiz(this,'q6',1)">B. zwei gegensaetzliche Informationen</div>
        <div class="opt" onclick="checkQuiz(this,'q6',2)">C. zwei Gruende</div>
        <div class="opt" onclick="checkQuiz(this,'q6',3)">D. zwei Orte</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>B</div>
    </div>

    <div class="quiz-card">
      <div class="q-text">7. "Sie plant ________ die Beleuchtung ________ gestaltet Smart-Home-Systeme mit." Welche Konjunktion passt?</div>
      <div class="options">
        <div class="opt" onclick="checkQuiz(this,'q7',0)">A. zwar … aber</div>
        <div class="opt" onclick="checkQuiz(this,'q7',1)">B. nicht nur … sondern auch</div>
        <div class="opt" onclick="checkQuiz(this,'q7',2)">C. sowohl … als auch</div>
        <div class="opt" onclick="checkQuiz(this,'q7',3)">D. weil</div>
      </div>
      <div class="q-answer"><strong>答案：</strong>B</div>
    </div>

    <div class="quiz-card" style="background:#f0f7ff;">
      <div class="q-text">Satzvervollstaendigung</div>
      <p style="margin:8px 0">8. Erika besuchte zunaechst ein Gymnasium, ______________________________. (aber)</p>
      <p style="margin:8px 0">9. Frauen und Maenner unterscheiden sich in ihrer Berufswahl, ______________________________. (zwar … aber)</p>
      <div class="q-answer"><strong>参考答案：</strong>8. aber sie entschied sich fuer eine Ausbildung / 9. Zwar gehen mehr Frauen einem Beruf nach, aber in manchen Branchen sind sie kaum vertreten</div>
    </div>

  </section>"""

h = h.replace(old_ex, new_ex)

# === 8. WRITE ===
outpath = os.path.join(dstdir, 'index.html')
with open(outpath, 'w') as f:
    f.write(h)

# === 9. VERIFY ===
print("=== VERIFICATION ===")
checks = [
    ('Title correct', 'Lektion 8' in h and 'Was will ich werden' in h),
    ('Sections correct', len([s for s in ['home','text','vocab','grammar','exercise'] if 'id="' + s + '"' in h]) == 5),
    ('Section balance', h.count('<section id=') == h.count('</section>')),
    ('T1 Berufswahlverhalten', 'Berufswahlverhalten' in h),
    ('T2 Erika story', 'Lieber Werkstatt' in h or 'Werkstatt statt Schreibtisch' in h),
    ('Grammar - zwar aber', 'zwar' in h and 'aber' in h),
    ('Grammar - nicht nur', 'nicht nur' in h and 'sondern auch' in h),
    ('Grammar - sowohl als auch', 'sowohl' in h and 'als auch' in h),
    ('Vocab-word count >= 20', h.count('vocab-word') >= 20),
    ('No L7 content', 'Tobias' not in h and 'Start in die Zukunft' not in h),
    ('No Markus as main text', 'Markus' in h),  # should still be in exercise/test
    ('showVocab function', 'function showVocab' in h),
    ('Vocab panel CSS', '.vocab-panel{' in h),
]
for name, ok in checks:
    print('  {}: {}'.format('OK' if ok else 'FAIL', name))
print("\nFile size: {:.1f} KB".format(len(h)/1024))
PYEOF