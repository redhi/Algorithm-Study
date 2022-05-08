var list = [
    {"gidx":"1", "gdate":"2016-09-27", "lid":"2",  }
    ,{"gidx":"4", "gdate":"2016-09-27", "lid":"2",  }
    ,{"gidx":"2", "gdate":"2016-09-27", "lid":"2",  }
    ,{"gidx":"5", "gdate":"2016-09-27", "lid":"3",  }
    ,{"gidx":"3", "gdate":"2016-09-26", "lid":"3",  }
]
 
 
sorted_list = list.sort(function(a, b) {
 
 
 var o1 = b['gdate']
  var o2 = a['gdate']
  var p1 = a['gidx']
  var p2 = b['gidx']
 
  if (o1 < o2) return -1;
  if (o1 > o2) return 1;
  if (p1 < p2) return -1;
  if (p1 > p2) return 1;
  return 0;
});
 
console.log(sorted_list);