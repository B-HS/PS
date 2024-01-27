function solution(a, b) {
    const ab = String(a) + String(b)
    const ba = String(b) + String(a)
    return Number(ab) > Number(ba) ? Number(ab) : Number(ba)
}