---
layout: page-fullwidth
title: "netto.null Website Vorschlag"
subheadline: "Lets collaborate"
teaser: "Es gibt nicht nut Google Docs"
categories:
    - strategy
comments: false
show_meta: false
author: dneise
---

# Ein Vorschlag für die netto.null Website

Im telegram chat ist vor einiger Zeit vorgeschlagen worden, den web-stack der [Zeitschrift Rebublik](https://www.republik.ch/) auch für die netto.null zu verwenden.
Meines Wissens sind keine Argumente für diese Lösung, aber auch keine dagegen ausgetauscht worden. Aus dem Kontext schien mir jedoch klar zu sein, dass eine simple [wordpress page](https://de-ch.wordpress.org/) nicht gewünscht wird.

Ich habe mich ein wenig mit dem [stack der Republik](https://github.com/orbiting) beschäftigt und habe den Eindruck gewonnen, dass die Lösung recht aufwendig ist. Vermutlich liegt das aber an mangelnder Expertise meinerseits.

Dennoch möchte ich sagen, dass mich eines ihrer Konzepte wirklich sehr interessiert hat.

## Das Republik Kollaboration Konzept

Die Leute dort bei der Republik beschreiben sehr schön, wie sie ich eine [effiziente Kollaboration beim erstellen von Dokumenten][1] (also z.B. Artikeln) vorstellen.
Was sie beschreiben ist nämlich nichts anderes, als das was software EntwicklerInnen schon seit vielen Jahrzehnten tun, um effizient zu kollaborieren. Sie benutzen ein Versionskontrollsystem.

Im Detail wird dort vorgeschlagen [`git`][2] zu benutzen, und zwar unter Benutzung der
weit verbreiteten Plattform [`github`][3].

Ich finde diese Idee super und kann ihre [Gründe hier][1] sehr gut nachvollziehen.

Es ist allerdings sehr viel einfacher eine Website zu erzeugen, und dabei `git` zu benutzen, völlig ohne den stack der Republik zu benutzen. Denn `github` bietet allen Nutzern an ihre Software auf sogenannten [`github-pages`][5] den möglichen Kunden oder users vorzustellen.


## Ein erster Versuch

Ich habe heute eine [Testseite][4] aufgesetzt, um mich einmal selbst damit vertraut zu machen.
Sicher ist da noch nichts perfekt, aber es scheint zu funktionieren.

## Das Problem (?)
Ein "Problem" hingegen ist es, dass [github-pages][5] by-design für jede und jeden frei zugänglich sind, während meines Erachtens ein zentraler Punkt des Republik designs war, dass nur zahlende KundInnen die Artikel zu sehen bekommen.

Sobald menschen in Klassen unterteilt werden (hier zahlen versus nicht-zahlend) schafft man gewisse Herausforderungen. Es ist z.B. notwendig den Zahlenden schnell und reibungslos Zugang zu verschaffen, und nicht Nichtzahlenden verlässlich auszusperren. Es ist daher notwendig sensible Informationen über Zahlende zu speichern (z.B. Kreditkartendaten), wodurch nun die Harausfordeung besteht diese sensiblen Daten hinreichend vor Angriffen zu schützen.

Ich stelle mich auf den Standpunkt, dass dies für die netto.null nicht zielführend ist.
Besser wäre ...

## Kostenlos und frei!

Ich benutze seit vielen Jahren fast ausschliesslich freie und quell offene Software.
Auch ist jede Software die ich jemals geschrieben habe frei und quelloffen, d.h. von jedem Menschen nutzbar und veränderbar.

Nicht nur software, wie das Betriebsystem Linux oder eben `git` werden von Kreativen kostenlos und quelloffen geschaffen und der Menschheit zur Verfügung gestellt, auch andere Kunstschaffende arbeiten so.

Der berühmte Autor Cory Doctorow hat lange Zeit viele seiner Bücher frei zur Verfügung gestellt und einfach darum gebeten, das Buch zu kaufen, wenn es gut war. Strassenmusiker arbeiten nach dem selben Prinzip, die Musik wir zuerst gespielt und genossen und danach findet möglicherweise eine Bezahlung statt. Viele PodcasterInnen veröffentlichen ihre Werke frei zugänglich, bieten aber die Möglichkeit zu spenden an. Professionelle streamer (z.B. auf twitch) bieten Unterhaltung an, und leben von den Spenden.

Warum sollte also die elektronische Ausgabe der netto.null nicht frei und offen zur Verfügung gestellt werden?


## Reichweite

Des weiteren bin ich Ansicht, dass es wundervoll ist, wenn ein Artikel aus der netto.null in den sozialen Netzwerken geteilt werden kann und damit eine Reichweite erhält, von der wir mit der print version nur träumen können. Wann immer jedoch ein Artikel geteilt wird, der sich hinter einer [pay-wall][6] verbirgt, teile zumindest ich diesen nicht weiter, sondern such eine öffentliche Version, welche die selben Informationen enthält.

## Wie geht das hier nun?

Das zeige ich vielleicht am besten in einem [Video](https://youtu.be/WKDhipBzKVk)


[1]: https://github.com/orbiting/docs/blob/dbbd0dc5a26d9cf501c1c57e2bed143f3d3e21f6/concept/cms/plan.md#collaborating-on-documents
[2]: https://de.wikipedia.org/wiki/Git
[3]: https://github.com/
[4]: https://dominikneise.github.io
[5]: https://pages.github.com/
[6]: https://de.wikipedia.org/wiki/Paywall


### All Header-Styles
{: .t60 }

{% include list-posts tag='header' %}
