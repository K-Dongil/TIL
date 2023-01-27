function solution(n, losts, reserves) {
  let answer = n;
  losts.sort()
  reserves.sort()
  
  for (lost of losts){
      if (reserves.includes(lost)){
          reserves = reserves.filter((element) => element !== lost);
          losts = losts.filter((element) => element !== lost);
      }
  }
  
  for (reserve of reserves){
      if (losts.includes(reserve-1)){
          losts.shift(reserve-1);
          continue;
      }else if (losts.includes(reserve+1)){
          losts.shift(reserve+1);
      }
  }
  
  return answer - losts.length;
}