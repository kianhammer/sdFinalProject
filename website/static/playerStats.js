function populateStatsTableHeader(statCategories) {
  var tableHeaderRow = document.getElementById("statsHeaderRow");
  for (var i=0; i<statCategories.length; i++) {
    var th = document.createElement("th");
    th.innerHTML = statCategories[i];
    th.setAttribute("class", "clickable");
    th.setAttribute('onclick', "sortTable(" + (i+1) + ")");
    tableHeaderRow.appendChild(th);
  }
}

function createStatsTable(playerStats) {
  var tableBody = document.getElementById("statsTableBody");
  let rowIndex = 0;
  for (const [player, stats] of Object.entries(playerStats)) {
    let row = tableBody.insertRow(rowIndex++);
    for(var i = 0; i < stats.length; i++) {
        var cell = row.insertCell(i);
        cell.innerHTML = stats[i]
    }
  }
}

/**
 * sorting table by header click 
 * example from: https://www.w3schools.com/howto/howto_js_sort_table.asp
 * @param columnIndex the column index to sort by
 */
function sortTable(columnIndex) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("statsTableBody");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "desc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 0; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[columnIndex];
      y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "desc") {
        dir = "asc";
        switching = true;
      }
    }
  }
  updateSortedColumnArrow(columnIndex);
  highlight_column(columnIndex);
}

function updateSortedColumnArrow(columnIndex) {
  var columnHeaders = document.getElementById("statsHeaderRow").getElementsByTagName("TH");
  for (var i = 1; i < columnHeaders.length; i++) {
    header = columnHeaders[i];
    if (i == columnIndex) {
      if (header.classList.contains("arrow-down")) {
        header.classList.remove("arrow-down");
        header.classList.add("arrow-up");
      } else {
        header.classList.remove("arrow-up");
        header.classList.add("arrow-down");
      }
    } else {
      header.classList.remove("arrow-up");
      header.classList.remove("arrow-down");
    }
  }
}

function highlight_column(columnIndex) {
  var tableBody = document.getElementById("statsTableBody");
  var tds = tableBody.querySelectorAll("td");

  for (var i = 0; i < tds.length; i++) {
    var cell = tds[i];
    console.log("i = " + i + ", cell value =" + cell.innerHTML);
    // cell.onclick = function() {
    //   const columns = document.querySelectorAll(`td:nth-child(${columnIndex})`);
    //   columns.forEach(col => {
    //     if (col.classList.contains('selected'))
    //       col.classList.remove('selected');
    //     else
    //       col.classList.add('selected');
    //   });
    // }
  }
}