function solution(a, b) {
    const ab = Number(String(a) + String(b))
    const tab = Number(a) * Number(b) * 2
    return ab >=tab ? ab : tab
}