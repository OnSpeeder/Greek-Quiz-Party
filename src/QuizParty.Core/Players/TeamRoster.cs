namespace QuizParty.Core.Players;

public enum TeamId { A = 1, B = 2 }
public sealed record PlayerTeam(PlayerId PlayerId, TeamId TeamId);
public sealed record TeamScore(TeamId TeamId, long Total, IReadOnlyList<PlayerId> Members);

/// <summary>Immutable membership; aggregation/ranking runs on the host.</summary>
public sealed class TeamRoster
{
    private readonly PlayerTeam[] _members;
    public TeamRoster(IEnumerable<PlayerId> players, IEnumerable<PlayerTeam> members)
    {
        ArgumentNullException.ThrowIfNull(players); ArgumentNullException.ThrowIfNull(members);
        var roster = players.ToArray(); _members = members.ToArray();
        if (roster.Length is < 2 or > 8 || roster.Any(p => p.Value == Guid.Empty) || roster.Distinct().Count() != roster.Length ||
            _members.Any(m => m is null || m.TeamId is not (TeamId.A or TeamId.B)) ||
            !_members.Select(m => m.PlayerId.Value).Order().SequenceEqual(roster.Select(p => p.Value).Order()) ||
            _members.Select(m => m.TeamId).Distinct().Count() != 2)
            throw new ArgumentException("Every player must belong to exactly one of two nonempty teams.", nameof(members));
    }
    public TeamId TeamOf(PlayerId player) => _members.Single(m => m.PlayerId == player).TeamId;
    public void ValidateRoster(IEnumerable<PlayerId> players)
    {
        if (!_members.Select(m => m.PlayerId.Value).Order().SequenceEqual(players.Select(p => p.Value).Order()))
            throw new ArgumentException("Team membership differs from the match roster.", nameof(players));
    }
    public IReadOnlyList<PlayerId> PlayersIn(IEnumerable<TeamId> teams)
    {
        var selected = teams.ToHashSet();
        return Array.AsReadOnly(_members.Where(m => selected.Contains(m.TeamId)).Select(m => m.PlayerId).ToArray());
    }
    public IReadOnlyList<TeamScore> Scores(IReadOnlyList<Game.PlayerScore> scores) => Array.AsReadOnly(
        new[] { TeamId.A, TeamId.B }.Select(team => new TeamScore(team,
            _members.Where(m => m.TeamId == team).Aggregate(0L, (total, member) => checked(total + scores.Single(s => s.PlayerId == member.PlayerId).Total)),
            PlayersIn([team]))).ToArray());
}
