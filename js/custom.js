const po = org.polymaps;
const maps = po.maps();
const map = po
  .map()
  .container(document.body.appendChild(po.svg("svg")))
  .add(po.image().url())
  .add(po.geoJson().url().on("load", load))
  .add(po.interact())
  .add(po.arrow())
  .add(po.drag())
  .add(po.dblclick())
  .add(po.wheel())
  .add(po.hash());
map.container(); // returns SVGSVGElement
function load(e) {
  for (const i = 0; i < e.features.length; i++) {
    const feature = e.features[i];
    feature.element.appendChild(
      po.svg("title").appendChild(document.createTextNode(feature.data.id))
        .parentNode
    );
  }
}
