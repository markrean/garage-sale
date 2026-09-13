# גראז׳ סייל — תכולת דירה

עמוד סטטי אחד, בלי בנייה ובלי תלויות. מתארח כמו שהוא ב-GitHub Pages.

## קבצים

| קובץ | מה הוא עושה |
|---|---|
| `index.html` | כל העמוד: תוכן, עיצוב וקוד. 40 הפריטים בשלוש שפות נמצאים במערך `ITEMS` בתחתית הקובץ. |
| `sold.json` | רשימת הפריטים שנמכרו. |
| `images.json` | התמונות של כל פריט. |
| `img/` | קבצי התמונות. |

## לסמן פריט כנמכר

עורכים את `sold.json` ומוסיפים את המזהה של הפריט:

```json
{ "ids": ["sonos", "fridge"] }
```

commit → העמוד מתעדכן תוך פחות מדקה. הפריט מקבל תג "נמכר", הפס שלו הופך לשחור והכרטיס מתעמעם.

## להוסיף תמונות

שמים את הקבצים ב-`img/` ומחברים אותם ב-`images.json`:

```json
{ "sonos": ["img/sonos-1.jpg", "img/sonos-2.jpg", "img/sonos-3.jpg"] }
```

התמונה הראשונה היא זו שמופיעה על הכרטיס; לחיצה פותחת לייטבוקס עם מעבר בין כולן.

המלצות: רוחב 1600px, WebP או JPG באיכות 80, עד ~150KB לתמונה. תמונה ריבועית נראית הכי טוב על הכרטיס.

ל-`img/og.jpg` (1200×630) יש תפקיד מיוחד — היא התמונה שמופיעה בתצוגה המקדימה של הלינק בפייסבוק ובוואטסאפ.

## מזהי הפריטים

`sonos`, `symfonisk`, `lgtv`, `ps5`, `dell`, `lighting`, `nuki`, `aqara`, `philips`, `dishwasher`, `oven`, `fridge`, `kingfridge`, `microwave`, `kitchenaid`, `ninja`, `toasters`, `roborock`, `dyson`, `washer`, `dryer`, `starkvind`, `kivik`, `keter`, `oskarshamn`, `dining`, `pax8`, `pax3`, `brimnes`, `slakt1`, `slakt2`, `alex`, `kallax`, `vihals`, `bergig`, `bissa`, `nysjon`, `palms`, `ficus`, `philodendron`

## פרסום ב-GitHub Pages

Settings → Pages → Source: Deploy from a branch → `main` / `root`.
