function solution(str1, str2) {
    const spStr1 = str1.split("")
    const spStr2 = str2.split("")
    return spStr1.map((ele, idx)=>ele+spStr2[idx]).join("")
}