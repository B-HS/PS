function solution(participant, completion) {
    const participantCount = {};
    participant.map(name => participantCount[name] = (participantCount[name] || 0) + 1);
    completion.map(name => participantCount[name] -= 1);
    return Object.keys(participantCount).find(name => participantCount[name] > 0);
}