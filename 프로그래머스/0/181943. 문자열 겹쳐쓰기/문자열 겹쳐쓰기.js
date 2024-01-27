function solution(my_string, overwrite_string, s) {
    const splittedStr = my_string.split("")
    const splittedOwStr = overwrite_string.split("")
    let ovtNum = 0
    return splittedStr.map((ele, idx)=>idx +1 >s && ovtNum < splittedOwStr.length? splittedOwStr[ovtNum++] : ele).join("")
}