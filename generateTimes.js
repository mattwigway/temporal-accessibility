var csv = require('csv');
var opening_hours = require('opening_hours');
var fs = require('fs');


// There are 24 * 7 = 168 hours in a week, we want five minutes after the hour
// on every one of them

// TODO: time zones
// This is a Sunday at 00:05.
var date = new Date('12 May 2013 00:05:00');
var eateries = fs.readFileSync(__dirname+'/eateries.csv')

for (var i = 0; i < 168; i++) {

    (function () {
        var numOpen = 0;

        // make a cloned local copy
        var theDate = new Date(date);

        console.log('iteration ' + i + ': ' + theDate);

        var day = (['0Su', '1Mo', '2Tu', '3We', '4Th', '5Fr', '6Sa'])[theDate.getDay()] +  '_' +
            (theDate.getHours() < 10 ? '0' + theDate.getHours() : theDate.getHours()) + ':' +
            (theDate.getMinutes() < 10 ? '0' + theDate.getMinutes() : theDate.getMinutes());

        // heavily based on the example
        csv()
            .from.string(eateries)
            .to.path(__dirname + '/eateries_' + i + '_' + day + '.csv')
            .transform(function (row) {
                if (row[0] == 'Latitude') {
                    // this is the header
                    row.push('Open');
                    return row;
                }

                var oh = new opening_hours(row[3]);

//                console.log(row[3])

          //          console.log(row[2] + ' is open at ' + day)

                row.push(oh.getState(theDate) ? '1' : '0')

                row.push(''  + theDate);

                return row;
            });

    })();


    // bump the date one hour, using JS's cool wraparound
    date.setHours(date.getHours() + 1);
}