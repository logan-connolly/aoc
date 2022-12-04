package util

// Intersect takes two sets and returns a set with the
// shared items.
func Intersect[T comparable](s1, s2 map[T]bool) map[T]bool {
	if len(s2) < len(s1) {
		s1, s2 = s2, s1
	}
	setMap := make(map[T]bool)
	for key := range s1 {
		_, ok := s2[key]
		if ok {
			setMap[key] = true
		}
	}
	return setMap
}

// Intersect takes two sets and returns a set with the
// shared items.
func Union[T comparable](s1, s2 map[T]bool) map[T]bool {
	setMap := make(map[T]bool)
	for key := range s1 {
		setMap[key] = true
	}
	for key := range s2 {
		setMap[key] = true
	}
	return setMap
}
