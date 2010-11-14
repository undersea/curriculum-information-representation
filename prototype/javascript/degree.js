var degreeReq = {
  binfsci: [[/158\d{3}/i, /159\d{3}/i, /160\d{3}/i, /161\d{3}/i, /(119177)|(192102)/i],{comp_sci:[/159101/i,/159102/i,/((1592\d{2}).*){4}/i, /((1593\d{2}).*){4}/i]}]
};

var initDegree = function  (degree,container,width,height) {
  var paper = Raphael(container, width, height);
  
};


var getRequiredDegreePapers =function(degree) {
  return degreeReq[degree][0];
};


var getRequiredMajorDegreePapers = function(degree,major) {
  return degreeReq[degree][1][major];
}


var getPrerequisites = function(paper) {
  return [];
};


var getNextPossible = function (paper) {
  return [];
};