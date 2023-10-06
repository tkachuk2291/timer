from timer_writes_logs import TimerWritesLogs


def start_timer() -> None:
    timer_logs = TimerWritesLogs()
    timer_logs.pomodoro_success()
    timer_logs.pomodoro_fail()


start_timer()
