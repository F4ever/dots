    let type = "WebGL"
    if(!PIXI.utils.isWebGLSupported()){
      type = "canvas"
    }

    PIXI.utils.sayHello(type)

    let points = [];
    let distances = [];
    let map;
    const mapSize = 512;

    const app = new PIXI.Application({width: mapSize, height: mapSize});
    const container = new PIXI.Container();

    document.body.appendChild(app.view);
    app.stage.addChild(container);

    let colors = ["0xBDD393","0x00B917","0x9E008E","0x001544","0xC28C9F","0xFF74A3","0x01D0FF","0x004754","0xE56FFE","0x788231","0x0E4CA1","0x91D0CB","0xBE9970","0x968AE8","0xBB8800","0x43002C","0xDEFF74","0x00FFC6","0xFFE502","0x620E00","0x008F9C","0x98FF52","0x7544B1","0xB500FF","0x00FF78","0xFF6E41","0x005F39","0x6B6882","0x5FAD4E","0xA75740","0xA5FFD2","0xFFB167","0x009BFF","0xE85EBE"];

    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function getRandomTriangleCoords() {
        let coords = [];

        coords[0] = 0; //x1
        coords[1] = getRandomInt(mapSize / 16, mapSize - mapSize / 16); // y1

        coords[2] = getRandomInt(mapSize / 16, mapSize - mapSize / 16); //x2
        coords[3] = 0; // y2

        coords[4] = getRandomInt((mapSize * 3) / 4, mapSize); //x3
        coords[5] = getRandomInt((mapSize * 3) / 4, mapSize); // y3

        return coords;
    }

    function clearContainer() {
        container.removeChildren();
    }

    function startNewGame() {
        clearContainer();
        points = [];

        setTriangleMap(getRandomTriangleCoords());
    }

    function setTriangleMap(coords) {
        map = new PIXI.Graphics();
        map.beginFill(0x66FF33);
        map.drawPolygon(coords);
        map.endFill();

        map.x = 0;
        map.y = 0;

        map.interactive = true;

        map.on('pointerdown', onClickMap);

        container.addChild(map);
    }

    function onClickMap(event) {
      addPoint(event.data.global.x, event.data.global.y);
    }

    function addPoint(x, y) {
        let circle = new PIXI.Graphics();
        circle.beginFill(colors[points.length]);
        circle.drawCircle(0, 0, 10);
        circle.endFill();
        circle.x = x;
        circle.y = y;

        let circleIndex = new PIXI.Text(''+(points.length + 1));
        circleIndex.x = x;
        circleIndex.y = y;

        container.addChild(circle);
        container.addChild(circleIndex);

        points.push({x: x, y: y});
    }

    function finishGame() {

        let maxDist = 0;
        let maxIndex = 0;

        for (i = 0; i < points.length; i++) {
            distances[i] = 9999999;
            for (j = 0; j < points.length; j++) {
                if (i == j) continue;

                x1 = points[i].x;
                y1 = points[i].y;
                x2 = points[j].x;
                y2 = points[j].y;

                distances[i] = Math.min(distances[i], Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2,2)));
            }

            if (distances[i] > maxDist) {
                  maxDist = distances[i];
                  maxIndex = i;
            }
        }

        console.log(distances);
        alert("WIN " + (maxIndex + 1));

    }