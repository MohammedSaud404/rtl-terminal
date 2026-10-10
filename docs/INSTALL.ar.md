<div dir="rtl">

# دليل التثبيت

[English](INSTALL.md) · [العودة إلى الصفحة الرئيسية](../README.ar.md)

## المتطلبات

- **Claude Code بالإصدار 2.1.294 أو أحدث.** تحقّق من إصدارك بالأمر `claude --version`، وحدّثه بالأمر `claude update`.
- **طرفية يرتّب فيها Claude Code النص العربي بنفسه**، للحصول على الترتيب الكامل: Windows Terminal، أو conhost (نافذة موجّه الأوامر وPowerShell التقليدية)، أو الطرفية المدمجة في VS Code على Windows أو macOS أو Linux. أما في الطرفيات الأخرى فتتنحّى الإضافة؛ راجع [أين تعمل؟](../README.ar.md#أين-تعمل).

## التثبيت من داخل Claude Code

١. نفّذ الأمر:

</div>

```
/plugin install rtl-terminal --marketplace MohammedSaud404/rtl-terminal
```

<div dir="rtl">

٢. يسألك Claude Code إن كنت تريد إضافة الـ marketplace باسم `github:MohammedSaud404/rtl-terminal`. أجب بـ `y`.

٣. اختر النطاق:
- **User** (موصى به): لك أنت، في كل المشاريع.
- **Project**: يُسجَّل في ملف `.claude/settings.json` الخاص بالمشروع، لمشاركته مع فريقك.
- **Local**: لك أنت، في هذا المشروع فقط.

٤. يؤكد Claude Code أن rtl-terminal ثُبّتت وأصبحت فعّالة. تعمل فورًا، وفي كل جلسة جديدة.

## التثبيت من سطر الأوامر

بأمر واحد:

</div>

```
claude plugin install rtl-terminal --marketplace MohammedSaud404/rtl-terminal --scope user
```

<div dir="rtl">

أو على خطوتين:

</div>

```
claude plugin marketplace add MohammedSaud404/rtl-terminal
claude plugin install rtl-terminal@rtl-terminal --scope user
```

<div dir="rtl">

تحمّل الجلسات الجديدة الإضافة تلقائيًا. أما الجلسة المفتوحة أثناء التثبيت فتحتاج إلى الأمر `/reload-plugins`.

## التأكد من أنها تعمل

- اسأل Claude أي سؤال بالعربية أو العبرية أو الفارسية أو الأردية. يجب أن يظهر الرد على اليمين، مع النقاط والأرقام على اليمين.
- نفّذ الأمر `/rtl mode`. في الطرفيات المدعومة يجيبك بأن Claude Code يرتّب الأسطر هنا وأن الإضافة تتولّى ترتيبها.

## التحديث

</div>

```
claude plugin marketplace update rtl-terminal
claude plugin update rtl-terminal@rtl-terminal
```

<div dir="rtl">

ثم أعد تشغيل Claude Code، أو نفّذ الأمر `/reload-plugins`.

## الإيقاف أو الإزالة

لإيقاف الترتيب مؤقتًا نفّذ `/rtl off`، ولإعادته نفّذ `/rtl on`.

لإزالة الإضافة:

</div>

```
claude plugin uninstall rtl-terminal@rtl-terminal
claude plugin marketplace remove rtl-terminal
```

<div dir="rtl">

## حل المشكلات

**ما زالت الردود على اليسار.**
نفّذ `/rtl mode`. إذا أجاب بأن الطرفية هي التي ترتّب الأسطر، فأنت في طرفية تتنحّى فيها الإضافة عن قصد؛ راجع [أين تعمل؟](../README.ar.md#أين-تعمل). وإذا كنت متأكدًا أن Claude Code يرتّب النص في طرفيتك، فنفّذ `/rtl mode claude`. وتأكد أيضًا أن الترتيب مفعّل بالأمر `/rtl on`.

**لم يتغيّر شيء بعد التثبيت.**
الجلسة التي كانت مفتوحة أثناء التثبيت تحتاج إلى `/reload-plugins`، أو إلى إعادة التشغيل.

**لا يظهر إصلاح من إصدار أحدث.**
نفّذ `claude plugin list`. إذا ظهرت rtl-terminal أكثر من مرة، كأن يضمّ برنامج تثبيت نسخته الخاصة منها، فإن Claude Code لا يشغّل إلا النسخة التي ثُبّتت قبل غيرها. احتفظ بالنسخة `rtl-terminal@rtl-terminal`، وأزِل البقية بالأمر `claude plugin uninstall` متبوعًا بأسمائها (مثلًا `claude plugin uninstall rtl-terminal@launchpad-plugins`)، ثم أعد تشغيل Claude Code.

**لم يُعثر على الـ marketplace أو الإضافة.**
تأكّد من كتابة `MohammedSaud404/rtl-terminal` بشكل صحيح، ثم نفّذ `claude plugin marketplace update rtl-terminal`.

**النص المنسوخ يظهر مبعثرًا.**
استخدم أمر `/copy` في Claude Code: فهو ينسخ النص الأصلي للرد بترتيب القراءة. أما التحديد بالماوس فينسخ الشاشة، والشاشة تحمل النص بترتيب العرض.

**مشكلة أخرى.**
[افتح بلاغًا](https://github.com/MohammedSaud404/rtl-terminal/issues) مع لقطة شاشة، واسم طرفيتك، ونتيجة الأمر `claude --version`.

</div>
