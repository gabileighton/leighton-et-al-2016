function getClosestPointOnLines(pXy, aXys) {
    var minDist;
    var fTo;
    var fFrom;
    var x;
    var y;
    var i;
    var dist;
    if (aXys.length > 1) {
        for (var n = 1; n < aXys.length; n++) {
            if (aXys[n].x != a Xys[n - 1].x) {
                var a = (aXys[n].y - aXys[n - 1].y) / (aXys[n].x - aXys[n - 1].x);
                var b = a Xys[n].y - a * aXys[n].x;
                dist = M ath.abs(a * pXy.x + b - pXy.y) / Math.sqrt(a * a + 1);
            } else dist = M ath.abs(pXy.x - aXys[n].x) // length^2 of line segment var rl2=M ath.pow(aXys[n].y - aXys[n-1].y,2) + Math.pow(aXys[n].x - aXys[n-1].x,2); // distance^2 of pt to end line segment var ln2=M ath.pow(aXys[n].y - pXy.y,2) + Math.pow(aXys[n].x - pXy.x,2); // distance^2

            of pt to begin line segment
            var lnm12 = M ath.pow(aXys[n - 1].y - pXy.y, 2) + Math.pow(aXys[n - 1].x - pXy.x, 2); // minimum distance^2 of pt to infinite line var dist2=M ath.pow(dist,2); // calculated length^2 of line segment var calcrl2=l n2 - dist2 + lnm12
            - dist2; // redefine minimum distance to line segment (not infinite line) if necessary if (calcrl2> rl2) dist = Math.sqrt( Math.min(ln2,lnm12) ); if ( (minDist == null) || (minDist > dist) ) { if(calcrl2 > rl2){ if(lnm12
            < ln2) {
            fTo = 0; //nearer to previous point fFrom=1 ; } else{ fFrom=0 ;//nearer to current point fTo=1 ; } } else { // perpendicular
            from point intersects line segment fTo = ((Math.sqrt(lnm12 - dist2)) / Math.sqrt(rl2));
            fFrom = ((Math.sqrt(ln2 - dist2)) / Math.sqrt(rl2));
        }
        minDist = d ist;
        i = n;
    }
}
var dx = a Xys[i - 1].x - aXys[i].x;
var dy = a Xys[i - 1].y - aXys[i].y;
x = a Xys[i - 1].x - (dx * fTo);
y = a Xys[i - 1].y - (dy * fTo);
}
return {
    'x': x,
    'y': y,
    'i': i,
    'fTo': fTo,
    'fFrom': fFrom
};
}
